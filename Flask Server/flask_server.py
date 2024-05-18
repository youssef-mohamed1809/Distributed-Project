### FORWARD TO LOADBALANCER ###
URL ="http://ec2-13-51-163-255.eu-north-1.compute.amazonaws.com:5000/receive_data"
PATH = "files/"
import requests
from flask import Flask, render_template, request, send_file, jsonify
from flask_cors import CORS
import json
import boto3
import os
import threading
from io import BytesIO
import zipfile


AWS_ACCESS_KEY_ID = os.environ.get("AWS_ACCESS_KEY")
AWS_SECRET_ACCESS_KEY = os.environ.get("AWS_SECRET_ACCESS_KEY")
BUCKET_NAME = "dist-img-proc"
REGION_NAME = "eu-north-1"
app = Flask(__name__)
CORS(app)

@app.route('/', methods=['GET'])
def hello():
        return "Hello from the server!"


## Receive data from web browser
@app.route('/upload', methods=['POST'])
def upload():
        userid = request.form['userid']
        print("User ID: ", userid)
        option = request.form['option']
        files = request.files.getlist('files[]')
        file_paths = []
        for i in range(len(files)):
                files[i].save(PATH + str(i) + ".jpg")
                file_paths.append(PATH + str(i) + ".jpg")        
        t1 = threading.Thread(target = forward_to_lb, args=(option, file_paths, userid,))
        t1.start()
        return f"Image Successfully uploaded"

@app.route('/download', methods=['GET'])
def download():
        user_id = request.args.get('id')
        s3 = boto3.client('s3', aws_access_key_id=AWS_ACCESS_KEY_ID,
                aws_secret_access_key = AWS_SECRET_ACCESS_KEY,
                region_name=REGION_NAME)
        response = s3.list_objects_v2(Bucket=BUCKET_NAME, Prefix=f"{user_id}/")
        count = 0
        for res in response["Contents"]:
                if count == 0:
                        count += 1
                        continue
                s3.download_file(BUCKET_NAME, res['Key'], f"./results/{count}.jpg")
                count+=1
                print(res['Key'])
        zip_buffer = zip_folder("./results")
        return send_file(
                zip_buffer,
                as_attachment=True,
                download_name='processed_images.zip',
                mimetype='application/zip'
        )
        # return send_file("ProcessedImages/newImg.jpg", as_attachment = True)

def zip_folder(folder_path):
    zip_buffer = BytesIO()
    
    # Create a new zip file in the memory buffer
    with zipfile.ZipFile(zip_buffer, 'w', zipfile.ZIP_DEFLATED) as zip_file:
        # Traverse the directory and add files to the zip file
        for root, dirs, files in os.walk(folder_path):
            for file in files:
                file_path = os.path.join(root, file)
                arcname = os.path.relpath(file_path, start=folder_path)
                zip_file.write(file_path, arcname)
    
    # Set the buffer's position to the beginning
    zip_buffer.seek(0)
    
    return zip_buffer

def forward_to_lb(option, file_paths, userid):      
        files = []
        data = {
                "option": option,
                "userid": userid
        }
        for i in range(len(file_paths)):
                files.append((f'{i}', open(file_paths[i], 'rb')))
        response = requests.post(URL, files=files, data=data)
        print(response)

if __name__ == '__main__':
        app.run(host='0.0.0.0', port=5000)
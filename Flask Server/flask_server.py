### FORWARD TO LOADBALANCER ###
URL ="http://127.0.0.1:5001/receive_data"
PATH = r"C:\Users\youss\Documents\Projects\Distributed Project\Flask Server\files\\"
import requests
from flask import Flask, render_template, request, send_file, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/', methods=['GET'])
def hello():
        return "Hello from the server!"


## Receive data from web browser
@app.route('/upload', methods=['POST'])
def upload():
        option = request.form['option']
        files = request.files.getlist('files[]')
        file_paths = []
        for i in range(len(files)):
                files[i].save(PATH + str(i))
                file_paths.append(PATH + str(i))        
        forward_to_lb(option, file_paths)
        return f"Image Successfully uploaded"

@app.route('/download', methods=['GET'])
def download():
        pass
        # return send_file("ProcessedImages/newImg.jpg", as_attachment = True)

def forward_to_lb(option, file_paths):      
        files = []
        for i in range(len(file_paths)):
                files.append((f'{i}', open(file_paths[i], 'rb')))
        response = requests.post(URL, files=files)
        print(response)

if __name__ == '__main__':
        app.run(host='0.0.0.0', port=5000)
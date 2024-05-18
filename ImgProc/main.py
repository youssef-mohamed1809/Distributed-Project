from flask import Flask, request
from flask_cors import CORS
import os
import boto3


WORKERS = [
   {
      "name": "worker1",
      "ip": "51.20.51.151"
   },
   {
      "name": "worker2",
      "ip": "16.170.218.108"
   },
   {
      "name": "worker3",
      "ip": "13.60.31.52"
   }
] 


AWS_ACCESS_KEY_ID = os.environ.get("AWS_ACCESS_KEY")
AWS_SECRET_ACCESS_KEY = os.environ.get("AWS_SECRET_ACCESS_KEY")
NUMOFPROCESSES = 5
PATH = r"uploaded/"
BUCKET_NAME = "dist-img-proc"
REGION_NAME = "eu-north-1"
app = Flask(__name__)
CORS(app)

# FLASK SERVER
@app.route("/receive_data", methods = ['POST'])
def receive_data():
      option = request.form['option']
      userid = request.form['userid']
      # print(userid)
      num_of_files = 0
      for file in request.files.items():
         num_of_files += 1
         file[1].save(PATH + f"{file[0]}.jpg")
      process_images(num_of_files, option)
      

      ####CODE OF S3####
      
      save_to_s3(userid)
      
      ##################  
      return "Done"


def save_to_s3(userid):
   s3 = boto3.client('s3', aws_access_key_id=AWS_ACCESS_KEY_ID,
                     aws_secret_access_key = AWS_SECRET_ACCESS_KEY,
                     region_name=REGION_NAME)
   folder_name = f"{userid}/"
   s3.put_object(Bucket=BUCKET_NAME, Key=(folder_name))
   image_folder = "./processed"
   for filename in os.listdir(image_folder):
      if filename.endswith('.jpg') or filename.endswith('.png'):  # Filter only image files
        file_path = os.path.join(image_folder, filename)
        s3.upload_file(file_path, BUCKET_NAME, folder_name + filename)
      #   print(f'Uploaded {filename} to {folder_name} in {bucket_name}')


def check_available_workers():
   alive_workers = []
   for worker in WORKERS:
      stream = os.popen(f"ping -c 4 {worker['ip']}")
      output = stream.read()
      if "0 received" in output:
         alive_workers.append(worker['name'])
   return alive_workers

def process_images(num_of_files, option):
   if num_of_files == 1:
      
      alive_workers = check_available_workers()
      s = "master,"
      for w in alive_workers:
         s += alive_workers
         s += ","
      command = f"mpiexec -n {len(alive_workers) + 1} -host {s} python mpi.py {option} {num_of_files}"
      output_stream = os.popen(command)
      output = output_stream.read()
      output_stream.close()
      # print(output) 
   else:
      alive_workers = check_available_workers()
      s = "master,"
      for w in alive_workers:
         s += alive_workers
         s += ","
      command = f"mpiexec -n {len(alive_workers) + 1} -host {s} python mpi.py {option} {num_of_files}"
      output_stream = os.popen(command)
      output = output_stream.read()
      output_stream.close()
      # print(output)
      

if __name__ == "__main__":
   app.run(host='0.0.0.0', port=5001)
from flask import Flask, request
from flask_cors import CORS
import os


NUMOFPROCESSES = 5
PATH = r"uploaded/"

app = Flask(__name__)
CORS(app)

# FLASK SERVER
@app.route("/receive_data", methods = ['POST'])
def receive_data():
      option = request.form['option']
      userid = request.form['userid']
      print(userid)
      num_of_files = 0
      for file in request.files.items():
         num_of_files += 1
         file[1].save(PATH + f"{file[0]}.jpg")
      process_images(num_of_files, option)
      
      
      ####CODE OF S3####
      
      
      
      ##################  
      return "Done"


def save_to_s3():
   pass

def process_images(num_of_files, option):
   if num_of_files == 1:
      command = f"mpiexec -n {num_of_files} python mpi.py 1IMG {option} {num_of_files}"
      output_stream = os.popen(command)
      output = output_stream.read()
      output_stream.close()
      print(output) 
   else:
      command = f"mpiexec -n {num_of_files} python mpi.py MULTIIMG {option} {num_of_files}"
      output_stream = os.popen(command)
      output = output_stream.read()
      output_stream.close()
      print(output)
      

if __name__ == "__main__":
   app.run(host='0.0.0.0', port=5001)
from flask import Flask, request
from flask_cors import CORS
import os

NUMOFPROCESSES = 5
PATH = r"C:\Users\youss\Desktop\Dist Project\ImgProc\uploaded\\"

app = Flask(__name__)
CORS(app)

# FLASK SERVER
@app.route("/receive_data", methods = ['POST'])
def receive_data():
      option = request.form['option']
      num_of_files = 0
      for file in request.files.items():
         num_of_files += 1
         file[1].save(PATH + f"{file[0]}.jpg")
      process_images(num_of_files, option)   
      return "Done"

def process_images(num_of_files, option):
   if num_of_files == 1:
      command = f"mpiexec -n {NUMOFPROCESSES} python mpi.py 1IMG {option}"
      output_stream = os.popen(command)
      output = output_stream.read()
      output_stream.close()
      print(output) 
   else:
      command = f"mpiexec -n {NUMOFPROCESSES} python mpi.py MULTIIMG {option}"
      output_stream = os.popen(command)
      output = output_stream.read()
      output_stream.close()
      print(output)
      

if __name__ == "__main__":
   app.run(host='0.0.0.0', port=5001)
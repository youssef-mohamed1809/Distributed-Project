from flask import Flask, request
from flask_cors import CORS
import os

PATH = r"C:\Users\youss\Documents\Projects\Distributed Project\ImgProc\processed\\"

app = Flask(__name__)
CORS(app)

# FLASK SERVER
@app.route("/receive_data", methods = ['POST'])
def receive_data():
      num_of_files = 0
      for file in request.files.items():
         num_of_files += 1
         file[1].save(PATH + f"{file[0]}.jpg")
      process_images(num_of_files)
      
      
      
      return "Done"

def process_images(num_of_files):
   ############
# RUNNING A PYTHON FILE WITHIN A PYTHON FILE AND GETTING ITS OUTPUT(WHAT IS IN THE CONSOLE)
############


   # Define the command you want to run
   command = "mpiexec -n 4 python mpi.py"

   # Run the command and capture its output
   output_stream = os.popen(command)

   # Read the output
   output = output_stream.read()

   # Close the output stream
   output_stream.close()

   # Print the output
   print(output)

   ############

if __name__ == "__main__":
   app.run(host='0.0.0.0', port=5001)
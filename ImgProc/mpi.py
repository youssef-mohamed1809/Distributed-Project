from mpi4py import MPI
import img_processing
import cv2
import numpy as np

comm = MPI.COMM_WORLD
size = comm.Get_size()
rank = comm.Get_rank()

def mpi_code():
   print("Rank: ", str(rank))
   
   # myimg = cv2.imread("cat.jpeg")
   # height = myimg.shape[0]
   # width = myimg.shape[1]
   # midx = width // 2
   # midy = height // 2
   
   # q1 = myimg[0:midy, 0:midx]
   # q2 = myimg[0:midy, midx:width]
   # q3 = myimg[midy:height, 0:midx]
   # q4 = myimg[midy:height, midx:width]


   # data = []


   # if rank == 0:
   #    data.append(q1)
   #    data.append(q2)
   #    data.append(q3)
   #    data.append(q4)
   # else:
   #    data = None
      
   # data = comm.scatter(data, root=0)

   # gray_part = img_processing.grayscale(data)

   # newData = comm.gather(gray_part ,root = 0)
   # if rank == 0:
   #    combined_image = np.concatenate((newData[0], newData[2]))
   #    comb2 = np.concatenate((newData[1], newData[3]))
   #    comb = np.hstack((combined_image, comb2))    
   #    cv2.imwrite("output.jpg", comb)
      
   MPI.Finalize()





mpi_code()





#############
# RUNNING A PYTHON FILE WITHIN A PYTHON FILE AND GETTING ITS OUTPUT(WHAT IS IN THE CONSOLE)
#############

# import os

# # Define the command you want to run
# command = "python testbardo.py"

# # Run the command and capture its output
# output_stream = os.popen(command)

# # Read the output
# output = output_stream.read()

# # Close the output stream
# output_stream.close()

# # Print the output
# print(output)

#############
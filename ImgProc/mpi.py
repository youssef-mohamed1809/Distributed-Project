from mpi4py import MPI
import img_processing
import cv2
import numpy as np
import sys

NUMOFPROCESSES = 5

def divide_image_horizontal(image, n):
    height, width = image.shape[:2]
    part_height = height // n
    parts = []
    for i in range(n):
        start_y = i * part_height
        end_y = start_y + part_height
        parts.append(image[start_y:end_y, :])
    return parts


if __name__ == "__main__":
   comm = MPI.COMM_WORLD
   size = comm.Get_size()
   rank = comm.Get_rank()
   option = sys.argv[2]
   multiple_images = sys.argv[1]
   
   if multiple_images == "1IMG":   
      if rank == 0:

         print(multiple_images) 
         ### Single Image
         myimage = cv2.imread("uploaded/0.jpg")
         parts = divide_image_horizontal(myimage, size)
      else:
         parts = None
      data = comm.scatter(parts, root=0)
      if option == "blurring":
         out = img_processing.blur(data)
         
      elif option == "sharpen":
         out = img_processing.sharpen(data)
      elif option == "color_inversion":
         out = img_processing.invert_color(data)
      elif option == "edge_detection":
         out = img_processing.detect_edge(data)
      elif option == "shrink":
         out = img_processing.shrink(data)
      elif option == "enlarge":
         out = img_processing.enlarge(data)
      elif option == "gray_scale":
         out = img_processing.grayscale(data) 
      
      newData = comm.gather(out, root=0)
      
      if rank == 0:
         combined_image = cv2.vconcat(newData)
         cv2.imwrite("processed/suii.jpg", combined_image) 
   elif multiple_images == "MULTIIMG":
      pass
     
   MPI.Finalize()





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
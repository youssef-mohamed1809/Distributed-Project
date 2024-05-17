from mpi4py import MPI
import img_processing
import cv2
import numpy as np
import sys

def process_img(img, option):
    if option == "blurring":
        out = img_processing.blur(img)
    elif option == "sharpen":
        out = img_processing.sharpen(img)
    elif option == "color_inversion":
        out = img_processing.invert_color(img)
    elif option == "edge_detection":
        out = img_processing.detect_edge(img)
    elif option == "shrink":
        out = img_processing.shrink(img)
    elif option == "enlarge":
        out = img_processing.enlarge(img)
    elif option == "gray_scale":
        out = img_processing.grayscale(img)
    elif option == "hist_equalize":
        out = img_processing.histEqualize(img)
    else:
        out = None
    return out 
    

def divide_image_horizontal(image, n):
    height, width = image.shape[:2]
    part_height = height // n
    parts = []
    for i in range(n):
        start_y = i * part_height
        end_y = start_y + part_height
        parts.append(image[start_y:end_y, :])
    return parts

def process_one_image(option):
    if rank == 0:
        img = cv2.imread("uploaded/0.jpg")
        parts = divide_image_horizontal(img, size)
    else:
        parts = None
    data = comm.scatter(parts, root=0)
    
    out = process_img(option, data)
    
    newData = comm.gather(out, root=0)

    if rank == 0:
        combined_image = cv2.vconcat(newData)
        cv2.imwrite("processed/suii.jpg", combined_image)

def process_multiple_images(option):
    
    images = []
    
    for i in range(num_of_images):
        images.append(cv2.imread(f"uploaded/{i}.png"))
    
    images_per_process = num_of_images // size
    extra_images = num_of_images % size

    start_index = rank * images_per_process + min(rank, extra_images)
    end_index = start_index + images_per_process + (1 if rank < extra_images else 0)

    subset_images = images[start_index:end_index]

    processed_images = [process_img(img, option) for img in subset_images]

    all_processed_images = comm.gather(processed_images, root=0)

    if rank == 0:
        all_processed_images = [img for sublist in all_processed_images for img in sublist]
        for i in range(len(all_processed_images)):
            cv2.imwrite(f"processed/{i}.jpg", all_processed_images[i])

comm = MPI.COMM_WORLD
size = comm.Get_size()
rank = comm.Get_rank()

option = sys.argv[1]   
num_of_images = int(sys.argv[2])

if num_of_images == 1:
    process_one_image(option)
else:
    process_multiple_images(option)


MPI.Finalize()
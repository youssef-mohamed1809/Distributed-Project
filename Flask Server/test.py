import cv2


img1 = cv2.imread(r"C:\Users\youss\Documents\Spring 2024\Distributed Computing\Test Images\cat.jpeg")
img2  = cv2.imread(r"C:\Users\youss\Documents\Spring 2024\Distributed Computing\Test Images\cat.jpeg")

if img1 == img2:
    print("Equal masalan aw ay 7aga")
else:
    print("Not equal masalan aw ay 7aga")
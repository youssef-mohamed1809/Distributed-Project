import cv2
import numpy as np

def grayscale(img):
        # img = cv2.imread(path)
        gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        # cv2.imwrite("ProcessedImages\gray.jpg", gray_img)
        return gray_img

def blur(path):
        img = cv2.imread(path)
        blurred = cv2.GaussianBlur(img, (5, 5), 0)
        # cv2.imwrite("ProcessedImages\gray.jpg", blurred)

def detect_edge(path):
        img = cv2.imread(path)
        edges = cv2.Canny(img, 100, 200)
        # cv2.imwrite("ProcessedImages\gray.jpg", edges)

def invert_color(path):
        img = cv2.imread(path)
        inverted = cv2.bitwise_not(img)
        # cv2.imwrite("ProcessedImages\gray.jpg", inverted)

def shrink(path):
        img = cv2.imread(path)
        img= img.astype(np.uint8)
        img_small = cv2.resize(img, (img.shape[1]//2, img.shape[0]//2))  
        # cv2.imwrite("ProcessedImages\gray.jpg", img_small)

def enlarge(path):
        img = cv2.imread(path)
        img= img.astype(np.uint8)
        img_large = cv2.resize(img, (img.shape[1]*2, img.shape[0]*2))  
        # cv2.imwrite("ProcessedImages\gray.jpg", img_large)

def sharpen(path):
        image = cv2.imread(path)
        kernel = np.array([
                [-1,-1,-1], 
                [-1, 9,-1],
                [-1,-1,-1]
                ])

        sharpened = cv2.filter2D(image, -1, kernel) 
        # cv2.imwrite("ProcessedImages\gray.jpg", sharpened)
        #Nognog w Seif Were Here Nihahahahaha
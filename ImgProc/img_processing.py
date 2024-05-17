import cv2
import numpy as np

def histEqualize(img):
        bordered_img = cv2.equalizeHist(img) 
        return bordered_img

def grayscale(img):
        gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        return gray_img

def blur(img):
        blurred = cv2.GaussianBlur(img, (5, 5), 0)
        return blurred

def detect_edge(img):
        edges = cv2.Canny(img, 100, 200)
        return edges

def invert_color(img):
        inverted = cv2.bitwise_not(img)
        return inverted

def shrink(img):
        img_small = cv2.resize(img, (img.shape[1]//2, img.shape[0]//2))  
        return img_small

def enlarge(img):
        img_large = cv2.resize(img, (img.shape[1]*2, img.shape[0]*2))  
        return img_large

def sharpen(img):
        kernel = np.array([
                [-1,-1,-1], 
                [-1, 9,-1],
                [-1,-1,-1]
                ])

        sharpened = cv2.filter2D(img, -1, kernel) 
        return sharpened
        #Nognog w Seif Were Here Nihahahahaha
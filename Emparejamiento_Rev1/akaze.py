import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt
from menu_emparejamiento import *

def akaze(detector,emparejador):
    
    if opcion == 'd':
        img1= cv.imread('graf1.png',cv.IMREAD_GRAYSCALE)          # queryImage
        img2 = cv.imread('graf3.png',cv.IMREAD_GRAYSCALE) # trainImage
    if opcion == 'n':
        img1= cv.imread(nombre1,cv.IMREAD_GRAYSCALE)          # queryImage
        img2 = cv.imread(nombre2,cv.IMREAD_GRAYSCALE) # trainImage
        
    # Initiate ORB detector
    akaze=cv.AKAZE_create()
    # find the keypoints and descriptors with AKAZE
    kp1, des1 = akaze.detectAndCompute(img1,None)
    kp2, des2 = akaze.detectAndCompute(img2,None)
    
    menu_emparejamiento(emparejador,kp1,des1,kp2,des2,img1,img2)
    
if __name__ == "__main__":
    akaze(detector,emparejador)

    
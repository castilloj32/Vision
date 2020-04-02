import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt
from menu_emparejamiento import *


def brief(detector,emparejador):
    
    if opcion == 'd':
        img1= cv.imread('graf1.png',cv.IMREAD_GRAYSCALE)          # queryImage
        img2 = cv.imread('graf3.png',cv.IMREAD_GRAYSCALE) # trainImage
    if opcion == 'n':
        img1= cv.imread(nombre1,cv.IMREAD_GRAYSCALE)          # queryImage
        img2 = cv.imread(nombre2,cv.IMREAD_GRAYSCALE) # trainImages
    
    # Initiate FAST detector
    star = cv.xfeatures2d.StarDetector_create()
    
    # Initiate ORB detector
    brief = cv.xfeatures2d.BriefDescriptorExtractor_create()
    # find the keypoints and descriptors with ORB
    kpa = star.detect(img1,None)
    kp1, des1 = brief.compute(img1,kpa)
    
    kpb = star.detect(img2,None)
    kp2, des2 = brief.compute(img1,kpb)
    
    menu_emparejamiento(emparejador,kp1,des1,kp2,des2,img1,img2)    
    
if __name__ == "__main__":
    brief(detector,emparejador)

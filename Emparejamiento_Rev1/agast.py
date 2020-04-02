import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt
from menu_emparejamiento import *


def agast(detector,emparejador):
    
    if opcion == 'd':
        img1= cv.imread('graf1.png',cv.IMREAD_GRAYSCALE)          # queryImage
        img2 = cv.imread('graf3.png',cv.IMREAD_GRAYSCALE) # trainImage
    if opcion == 'n':
        img1= cv.imread(nombre1,cv.IMREAD_GRAYSCALE)          # queryImage
        img2 = cv.imread(nombre2,cv.IMREAD_GRAYSCALE) # trainImage
        
    # Initiate SIFT detector
    agast = cv.AgastFeatureDetector_create()
    brief = cv.xfeatures2d.BriefDescriptorExtractor_create()
    # find the keypoints and descriptors with SIFT
    kpa= agast.detect(img1,None)
    kp1,des1=brief.compute(img1,kpa)
    
    kpb= agast.detect(img2,None)
    kp2,des2=brief.compute(img2,kpb)
    
    menu_emparejamiento(emparejador,kp1,des1,kp2,des2,img1,img2)
    
if __name__ == "__main__":
    agast(detector,emparejador)

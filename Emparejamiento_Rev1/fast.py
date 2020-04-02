import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt
from menu_emparejamiento import *

def fast(detector,emparejador):
    
    if opcion == 'd':
        img1= cv.imread('graf1.png',cv.IMREAD_GRAYSCALE)          # queryImage
        img2 = cv.imread('graf3.png',cv.IMREAD_GRAYSCALE) # trainImage
    if opcion == 'n':
        img1= cv.imread(nombre1,cv.IMREAD_GRAYSCALE)          # queryImage
        img2 = cv.imread(nombre2,cv.IMREAD_GRAYSCALE) # trainImage
    
    fast= cv.FastFeatureDetector_create()
    # Initiate BRIEF extractor
    brief = cv.xfeatures2d.BriefDescriptorExtractor_create()
    
    kpa= fast.detect(img1,None)
    kp1,des1=brief.compute(img1,kpa)
    
    kpb= fast.detect(img1,None)
    kp2,des2=brief.compute(img2,kpb)
    
    menu_emparejamiento(emparejador,kp1,des1,kp2,des2,img1,img2)

if __name__ == "__main__":
    fast(detector,emparejador)
    
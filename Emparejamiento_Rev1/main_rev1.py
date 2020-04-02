import numpy as np

from sift import *
from agast import *
from akaze import *
from brief import *
from brisk import *
from kaze import *
from orb import *
from surf import *
from gftt import *
from fast import *

from menu_emparejamiento import *
relacion_det_empa=np.array([[11,11,11,11,11,11,11,11,11,11],[12,12,12,12,12,12,12,13,13,13]])
#a=[[11,11,11,11,11,11,11,11,11,11],[12,12,12,12,12,12,12,13,13,13]]
#print([row[detector - 1] for row in a])

print("****************************************************************************")
print("******Deteccion, descripcion y Emparejamiento de Rasgos en OpenCV***********")
print("****************************************************************************")
print("Seleccione un metodo de Deteccion")

print("1-Good Features to Track")
print("2-FAST")
print("3-BRIEF")
print("4-ORB")
print("5-AGAST")
print("6-AKAZE")
print("7-BRISK")
print("8-KAZE")
print("9-SIFT")
print("10-SURF")
detector = int(input("Detector:__"))
print("Seleccione un metodo de emparejamiento")
print("11-Brute-force")
print("12-Flann")
emparejador = int(input("Emparejador:__"))



if emparejador == 11:
    print("Detector:Brute-force")
    
if emparejador == 12:
    
    print("Detector:Brute-force")
    
if emparejador == 13:
    #if detector in a in a:
    print("Detector:Brute-force")   


if detector == 1 :
    print("Detector:Good Features to Track")
    if emparejador in relacion_det_empa[:,(detector-1)]:
    #if emparejador in [row[detector - 1] for row in a]:
        gftt(detector,emparejador)
if detector == 2:
    print("Detector:FAST")
    if emparejador in relacion_det_empa[:,(detector-1)]:
        fast(detector,emparejador)
if detector == 3:
    print("Detector:BRIEF")
    if emparejador in relacion_det_empa[:,(detector-1)]:    
        brief(detector,emparejador)
if detector == 4:
    print("Detector:ORB")
    if emparejador in relacion_det_empa[:,(detector-1)]:    
        orb(detector,emparejador)
if detector == 5:
    print("Detector:AGAST")
    if emparejador in relacion_det_empa[:,(detector-1)]:    
        agast(detector,emparejador)
if detector == 6:
    print("Detector:AKAZE")
    if emparejador in relacion_det_empa[:,(detector-1)]:    
        akaze(detector,emparejador)
if detector == 7:
    print("Detector:BRISK")
    if emparejador in relacion_det_empa[:,(detector-1)]:
        brisk(detector,emparejador)
if detector == 8:
    print("Detector:KAZE")
    if emparejador in relacion_det_empa[:,(detector-1)]:
        kaze(detector,emparejador)
if detector == 9:
    print("Detector:SIFT")
    if emparejador in relacion_det_empa[:,(detector-1)]:
        sift(detector,emparejador)
if detector == 10:
    print("Detector:SURF")
    if emparejador in relacion_det_empa[:,(detector-1)]:    
        surf(detector,emparejador)
    

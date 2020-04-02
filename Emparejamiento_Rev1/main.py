import tkinter as tk
from tkinter import filedialog
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


root=tk.Tk()
root.withdraw()

print("****************************************************************************")
print("******Deteccion, descripcion y Emparejamiento de Rasgos en OpenCV***********")
print("****************************************************************************")

print("Ingrese las imagenes a analizar, seleccione una opcion:")
print("Opcion 1: Imagenes preestablecidas  presione --> 'd'")
print("Opcion 2: Ingresar el nombre de ambas imagenes de prueba --> 'n'")
opcion=input("Ingrese una opcion:__")
if opcion == 'd':
    print("Selecciono usar imagenes preestablecidas \n")
    nombre1=''
    nombre2=''
if opcion == 'n':
    input("Seleccione archivo 1 --> Presione una tecla para continuar......")
    nombre1=filedialog.askopenfilename()
    input("Seleccione archivo 2 --> Presione una tecla para continuar......")
    nombre2=filedialog.askopenfilename()
    print(nombre1,nombre2)
print("Seleccione un metodo de Deteccion de Rasgos")
print("1-Good Features to Track     2-FAST      3-BRIEF     4-ORB       5-AGAST")
print("6-AKAZE                      7-BRISK     8-KAZE      9-SIFT      10-SURF")
detector = int(input("Detector:__"))

print("Seleccione un metodo de emparejamiento")
print("11-Brute-force               12-Flann")
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
    gftt(detector,emparejador,opcion,nombre1,nombre2)
if detector == 2:
    print("Detector:FAST")
    fast(detector,emparejador,nombre1,nombre2)
if detector == 3:
    print("Detector:BRIEF")
    brief(detector,emparejador,nombre1,nombre2)
if detector == 4:
    print("Detector:ORB")
    orb(detector,emparejador,nombre1,nombre2)
if detector == 5:
    print("Detector:AGAST")
    agast(detector,emparejador,nombre1,nombre2)
if detector == 6:
    print("Detector:AKAZE")
    akaze(detector,emparejador,nombre1,nombre2)
if detector == 7:
    print("Detector:BRISK")
    brisk(detector,emparejador,nombre1,nombre2)
if detector == 8:
    print("Detector:KAZE")
    kaze(detector,13,nombre1,nombre2)
if detector == 9:
    print("Detector:SIFT")
    sift(detector,13,nombre1,nombre2)
if detector == 10:
    print("Detector:SRF")    
    surf(detector,13,nombre1,nombre2)


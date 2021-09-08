import cv2
import math
from sklearn import neighbors
import os
import os.path
import pickle
from PIL import Image, ImageDraw
import cvlib as cv

dir="vae"
dest="vae_proper"
n=0
for fol in os.listdir(dir):
    path=os.path.join(dir,fol)
    img=cv2.imread(path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    for i in range(0,16):
        if(n%16==0):
            temp=gray[69:164,73:168]
            
        elif(n%16==1):
            temp=gray[69:164,190:285]
            
        elif(n%16==2):
            temp=gray[69:164,306:401]
            
        elif(n%16==3):
            temp=gray[69:164,423:518]
            
        elif(n%16==4):
            temp=gray[183:277,73:168]
            
        elif(n%16==5):
            temp=gray[183:277,190:285]
            
        elif(n%16==6):
            temp=gray[183:277,306:401]
            
        elif(n%16==7):
            temp=gray[183:277,423:518]
            
        elif(n%16==8):
            temp=gray[296:391,73:168]
           
        elif(n%16==9):
            temp=gray[296:391,190:285]
           
        elif(n%16==10):
            temp=gray[296:391,306:401]
           
        elif(n%16==11):
           temp=gray[296:391,423:518]
           
        elif(n%16==12):
            temp=gray[409:504,73:168]
           
        elif(n%16==13):
            temp=gray[409:504,190:285]
           
        elif(n%16==14):
            temp=gray[409:504,306:401]
           
        elif(n%16==15):
            temp=gray[409:504,423:518]
            
        cv2.imwrite(os.path.join(dest,str(n)+".jpeg"),temp)
        n=n+1

print(n)
    

# -*- coding: utf-8 -*-
import cv2
import matplotlib.pyplot as plt
import numpy as np
import random

def main():
    
    img_path="/home/atif/spyder_project/youtube_ashwin_tutorial/leon.jpg"
    
    img=cv2.imread(img_path,1)
    img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    
    rows,columns,channels=img.shape
    
    
    p=0.05
    
    output= np.zeros(img.shape,np.uint8)
    
    for i in range(rows):
        for j in range(columns):
            r=random.random()
            if r<p/2:
                output[i][j]=[0,0,0]
            elif r<p:
                output[i][j]=[255,255,255]
            else:
                output[i][j]=img[i][j]
                
    
    
    plt.imshow(output)
    plt.title('original image')
    plt.show()
    
main()

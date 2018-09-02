# -*- coding: utf-8 -*-

import cv2
import matplotlib.pyplot as plt
import numpy as np
import random

def main():
    
    img_path="/home/atif/spyder_project/youtube_ashwin_tutorial/leon.jpg"
    
    img=cv2.imread(img_path,1)
    img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    
    noisy= np.zeros(img.shape, np.uint8)
    
    p=0.2
    
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            r=random.random()
            if r<p/2:
                noisy[i][j]=[0,0,0]
            elif r<p:
                noisy[i][j]=[255,255,255]
            else:
                noisy[i][j]=img[i][j]
                
    denoised=cv2.medianBlur(noisy,3)
    
    output=[img,noisy,denoised]
    titles=['original img','noisy image','denoised by median filter']
    
    '''while(True):
        
        cv2.imshow('original image',img)
        cv2.imshow('noisy',noisy)
        cv2.imshow('denoised by median filter',denoised)
        
        cv2.waitKey(0)
        
        if cv2.waitKey(1)==27:
            break'''
    
    for i in range(3):
        plt.subplot(3,1,i+1)
        plt.imshow(output[i])
        plt.title(titles[i])
        plt.xticks([0,20,100])
        plt.yticks([0,20,100])
    plt.show()
    #cv2.destroyAllWindows()
    
main()
    
    
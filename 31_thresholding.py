# -*- coding: utf-8 -*-
import cv2
import matplotlib.pyplot as plt

def main():
    
    img_path="/home/atif/spyder_project/youtube_ashwin_tutorial/leon.jpg"
    
    img2=cv2.imread(img_path,1)
    
    img1=cv2.cvtColor(img2,cv2.COLOR_BGR2RGB)
    
    th=0
    max_val=255
    
    
    ret,o1=cv2.threshold(img1,th,max_val, cv2.THRESH_BINARY)
    ret,o2=cv2.threshold(img1,th,max_val, cv2.THRESH_BINARY_INV)
    ret,o3=cv2.threshold(img1,th,max_val, cv2.THRESH_TOZERO)
    ret,o4=cv2.threshold(img1,th,max_val, cv2.THRESH_TOZERO_INV)
    ret,o5=cv2.threshold(img1,th,max_val, cv2.THRESH_TRUNC)


    output=[img1,o1,o2,o3,o4,o5]
    
    titles=['original','binary','binary_inv','to zero','to zero inv','trunc']
    
    for i in range(6):
        plt.subplot(2,3,i+1)
        plt.imshow(output[i])
        
        
        plt.title(titles[i])
        
        
        
    plt.show()
    
main()
        
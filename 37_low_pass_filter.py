# -*- coding: utf-8 -*-
import cv2
import matplotlib.pyplot as plt

def main():
    
    img_path="/home/atif/spyder_project/youtube_ashwin_tutorial/leon.jpg"
    
    img=cv2.imread(img_path,1)
    img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    
    box=cv2.boxFilter(img,-1,(50,50))
    
    blur=cv2.blur(img,(20,20))
    
    gaussian=cv2.GaussianBlur(img,(35,35),0)
    
    titles=['original image','box','blur','gaussian blur']
    
    output=[img,box,blur,gaussian]
    
    for i in range(4):
        plt.subplot(2,2,i+1)
        plt.imshow(output[i])
        plt.title(titles[i])
        plt.xticks([])
        plt.yticks([])
    plt.show()
    
main()

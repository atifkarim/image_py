# -*- coding: utf-8 -*-
import cv2
import matplotlib.pyplot as plt

def main():
    
    img_path="/home/atif/spyder_project/youtube_ashwin_tutorial/leon.jpg"
    
    img=cv2.imread(img_path,1)
    img1=cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    
    r,g,b=cv2.split(img1)
    
    titles=["original image","red","green","blue"]
    
    images=[cv2.merge((r,g,b)),r,g,b]
    
    plt.subplot(2,2,1)
    plt.imshow(images[0])
    plt.title(titles[0])
    
    plt.subplot(2,2,2)
    plt.imshow(images[1], cmap='Reds')
    plt.title(titles[1])
    
    plt.subplot(2,2,3)
    plt.imshow(images[2],cmap='Greens')
    plt.title(titles[2])
    
    plt.subplot(2,2,4)
    plt.imshow(images[3],cmap='Blues')
    plt.title(titles[3])
    
    plt.show()
    
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
main()




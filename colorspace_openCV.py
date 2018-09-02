# -*- coding: utf-8 -*-
import cv2
import matplotlib.pyplot as plt

def main():
    
    image="/home/atif/spyder_project/youtube_ashwin_tutorial/leon.jpg"
    img=cv2.imread(image,1)
    
    img=cv2.cvtColor(img, cv2.COLOR_BGR2RGB)  #if you remove this line then o/p will be RGB
    
    plt.imshow(img)
    plt.show()
    
main()
# -*- coding: utf-8 -*-
import cv2
import numpy as np
import matplotlib.pyplot as plt

def main():
    
    img_path="/home/atif/spyder_project/youtube_ashwin_tutorial/leon.jpg"
    
    img=cv2.imread(img_path,1)
    img1=cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    
    rows,columns,channels=img1.shape
    
    point1=np.float32([[100,100],[400,100],[800,500]])
    point2=np.float32([[150,850],[700,300],[200,400]])
    
    A=cv2.getAffineTransform(point1, point2)
    print(A)
    
    output=cv2.warpAffine(img1,A,(columns,rows))
    
    plt.imshow(output)
    plt.title('transform')
    plt.show()
    
main()
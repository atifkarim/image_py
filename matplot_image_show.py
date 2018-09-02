# -*- coding: utf-8 -*-
import cv2
import matplotlib.pyplot as plt

def main():
    
    image1= "/home/atif/spyder_project/youtube_ashwin_tutorial/leon.jpg"
    img=cv2.imread(image1,1)
    
    img=cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    
    plt.imshow(img, cmap='gray')
    plt.title('Gray map')
    plt.xticks([])
    plt.yticks([0,40])
    plt.show()

    
    plt.imshow(img,cmap='Spectral')
    plt.show()
    
    '''cv2.imshow('Leon',img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()'''
        #c = cv2.waitKey(27)
        #if c == 27:
         #   cv2.DestroyAllWindows("Test")
          #  break
main()
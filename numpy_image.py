# -*- coding: utf-8 -*-

import cv2
import numpy as np

def main():
    
       # top left is the origin in image processing (0,0)
    img1=np.zeros((512,512,3),np.uint8)
    cv2.line(img1,(0,115),(215,58),(255,122,231),15)
     #attributes are img=where you are going to draw
     #then x, y coordinate
     #then color BGR
     #then thickness of the line
    '''cv2.rectangle(img1,(115,115),(215,58),(0,122,231),15)
    cv2.circle(img1,(300,300),55,(0,0,255),-1) #here -1 to fill the circle
    
    
    points = np.array([[910, 641], [206, 632], [696, 488], [458, 485]])
# points.dtype => 'int64'
    cv2.polylines(img1, np.int32([points]), 1, (255,255,255))
    
    text1="testing my text"
    cv2.putText(img1,text1,(200,200),cv2.FONT_HERSHEY_COMPLEX,5,(0,0,200),5)'''
    
    while(True):
        cv2.imshow("leon",img1)
        
        if cv2.waitKey(1)==27:
            break
        
    
    #cv2.imshow("leon",img1)
    #cv2.imwrite(outpath,img)
    #cv2.waitKey(0)
    cv2.destroyAllWindows()
    
if __name__=="__main__":
    main()

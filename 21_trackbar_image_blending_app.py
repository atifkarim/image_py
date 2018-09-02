# -*- coding: utf-8 -*-
import cv2

def emptyfunction():
    pass

def main():
    
    path="/home/atif/spyder_project/youtube_ashwin_tutorial"
    
    #img1_path="/home/atif/spyder_project/youtube_ashwin_tutorial/leon.jpg"
    #img2_path="/home/atif/spyder_project/youtube_ashwin_tutorial/cat.jpg"
    
    img1_path=path+"/leon.jpg"
    img2_path=path+"/cat.jpg"
    
    
    img1=cv2.imread(img1_path,1)
    img2=cv2.imread(img2_path,1)
    
    #cv2.imshow('1',img1)
    #cv2.waitKey(0)
    
    output=cv2.addWeighted(img1,0.5,img2,0.5,0)
    windowname='transition window'
    cv2.namedWindow(windowname)
    
    cv2.createTrackbar('Alpha',windowname,0,10,emptyfunction)
    
    while(True):
        
        cv2.imshow(windowname,output)
        
        if cv2.waitKey(1)==27:
            break
        
        alpha=cv2.getTrackbarPos('Alpha',windowname)/10
        beta=1-alpha
        
        output = cv2.addWeighted(img1,alpha,img2,beta,0)
        
        print(alpha,beta)
        
    cv2.destroyAllWindows()
    
main()

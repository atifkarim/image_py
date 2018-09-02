# -*- coding: utf-8 -*-
import cv2

def main():
    
    #imagepath="/home/atif/spyder_project/youtube_ashwin_tutorial/leon.jpg"
    img=cv2.imread("/home/atif/spyder_project/youtube_ashwin_tutorial/leon.jpg",-1)
    
    outpath = "/home/atif/spyder_project/youtube_ashwin_tutorial/write image/1.png"
    
    cv2.imshow("leon",img)
    cv2.imwrite(outpath,img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
#if __name__=="__main__":
main()
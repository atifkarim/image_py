# -*- coding: utf-8 -*-

import cv2

def main():
    
    #imagepath="/home/atif/spyder_project/youtube_ashwin_tutorial/leon.jpg"
    img=cv2.imread("/home/atif/spyder_project/youtube_ashwin_tutorial/leon.jpg",0)#change 1 to 0 
                                                                                    #to see the info about grayscale image
    
    #outpath = "/home/atif/spyder_project/youtube_ashwin_tutorial/write image/1.png"
    print(img)
    print('the type is:',type(img))
    print(img.dtype)
    print(img.shape)   #gives resolution. the third position gives channel number
    print(img.ndim) #gives dimension
    print(img.size)
    '''cv2.imshow("leon",img)
    cv2.imwrite(outpath,img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()'''
    
if __name__=="__main__":
    main()
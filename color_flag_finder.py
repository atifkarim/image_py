# -*- coding: utf-8 -*-
import cv2

def main():
    j=0
    for filename in dir(cv2):
        if filename.startswith('COLOR_'):
            print(filename)
            j=j+1
    print('total '+ str((j+1))+' color flag')
    
main()

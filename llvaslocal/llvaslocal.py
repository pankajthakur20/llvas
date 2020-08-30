#!/bin/python
import cv2
import glob
import os
import sys
import time

#n=int(input("Enter no. of images to capture : "))
#s=int(input("Sleep Time : "))
n=5
s=2
path='~/llvaslocal/attendance/'
ext='.jpg'
i=1
while i <= n:
    time.sleep(s)
    filename = time.strftime("%Y%m%d%H%M%S")
    r='rgb'
    fullpath="%s%s%s%s" %(path,filename,r,ext)
    #for laptop webcam
    webcam = cv2.VideoCapture(0, cv2.CAP_V4L)
    #for IP camera
    #webcam = cv2.VideoCapture("rtsp://username:password@camera-ip-address:port)

    ret, frame = webcam.read()
    #print(ret)
    cv2.imwrite(fullpath, img=frame)
    print(i,filename +r +ext)
    img = cv2.imread(fullpath)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    r='gray'
    fullpath="%s%s%s%s" %(path,filename,r,ext)
    cv2.imwrite(fullpath, gray)
    webcam.release()
    print(" ",filename +r +ext)
    i=i+1

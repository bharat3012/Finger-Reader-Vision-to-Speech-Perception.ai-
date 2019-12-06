#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 21 23:41:29 2018

@author: bharat
"""

import cv2
import os
import numpy as np
import matplotlib.pyplot as plt
#from pyimagesearch import imutils
import imutils
import csv

def sort_contours(cnts, method="left-to-right"):
	# initialize the reverse flag and sort index
	reverse = False
	i = 0
 
	# handle if we need to sort in reverse
	if method == "right-to-left" or method == "bottom-to-top":
		reverse = True
 
	# handle if we are sorting against the y-coordinate rather than
	# the x-coordinate of the bounding box
	if method == "top-to-bottom" or method == "bottom-to-top":
		i = 1
 
	# construct the list of bounding boxes and sort them from top to
	# bottom
	boundingBoxes = [cv2.boundingRect(c) for c in cnts]
	(cnts, boundingBoxes) = zip(*sorted(zip(cnts, boundingBoxes),
		key=lambda b:b[1][i], reverse=reverse))
 
	# return the list of sorted contours and bounding boxes
	return (cnts, boundingBoxes)
def adapt(image_path):
    path = 'crop'
    path2 ='adapt'
    im_path = os.path.join(path,image_path)
    out_path = os.path.join(path2, image_path)
    img1 = cv2.imread(im_path)
    img2 = cv2.medianBlur(img1, 5)
    img = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
    
    #ret,th1 = cv2.threshold(img,127,255,cv2.THRESH_BINARY)
    th2 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,75,10)
    #th3 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,11,2)
    th4 = cv2.bitwise_not(th2)
    
    cv2.imwrite(out_path,th4)
    #cv2.imwrite('adtm.jpg',th2)
    #cv2.imwrite('adtg.jpg',th3)
    #cv2.imwrite('otsu.jpg',th1)
    
    
    
    img3 =cv2.imread(out_path)
    _,contours, hierarchy = cv2.findContours(th4,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    
    contours = sorted(contours, key=cv2.contourArea, reverse=True)[:len(contours)]
    (contours, boundingBoxes) = sort_contours(contours, method=True)
    
    
    l = []
    
    for cnt in contours:
        x,y,w,h = cv2.boundingRect(cnt)
        #bound the images
        cv2.rectangle(img3,(x,y),(x+w,y+h),(255,0,255),3)
        cv2.circle(img3,(x+5,y+h),3,(255,255,0),-1)
        a =[y,x,w,h]
        b = [y+h,x]
        l.append(a)
        
    l = sorted(l, key=lambda tup: (tup[0],tup[1]))
    #j = 4
    #cv2.line(img3, l[j], l[j+1], (255, 255, 0), 5)
    #cv2.line(img3, l[j+1], l[j+2], (255, 255, 0), 5)
    
    i=0
    for cnt in contours:
        x,y,w,h = cv2.boundingRect(cnt)
        #following if statement is to ignore the noises and save the images which are of normal size(character)
        #In order to write more general code, than specifying the dimensions as 100,
        # number of characters should be divided by word dimension
        if w>100 and h>100:
            #save individual images
            cv2.imwrite(str(i)+".jpg",th4[y:y+h,x:x+w])
            i=i+1
    #cv2.namedWindow('BindingBox', cv2.WINDOW_NORMAL)
            
    img4 = cv2.bitwise_not(img3)        
    cv2.imwrite('out2.jpg',img4)


#        
#X_mid = np.size(img4,1)
#Y_mid = np.size(img4,0)    
#d=0
#
#
#def distance(a,b):
#    d = np.sqrt((a-X_mid)**2+(b-Y_mid)**2)
#    return d


        
        
        
        
    
        
        
        
        












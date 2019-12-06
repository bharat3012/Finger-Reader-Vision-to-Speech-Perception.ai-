# -*- coding: utf-8 -*-
"""
Created on Fri Dec 21 17:37:14 2018

@author: Dheeraj Varma
"""

import cv2
import numpy as np
import os
#import otsu
def drawcursor(img, image, image_path):
    path3 = 'cursor'
    path4 = 'tipcursor'
    path5 = 'crop'
    out1 = os.path.join(path3,image_path)
    out2 = os.path.join(path4,image_path)
    out3 = os.path.join(path5,image_path)
    B = cv2.imread(image)
    A = cv2.cvtColor(B, cv2.COLOR_BGR2GRAY)

   
    A = A.astype(float)
    
    I=[]
    SUM=0
    mid_col=[]
    J=0
    
    
    for i in range(0,np.size(A,1)):
        for j in range(0,np.size(A,0)):
            SUM = SUM + A[j,i]
        if (SUM>250*255):                            #todo
            I.append(i)
        SUM = 0
            
    i_max = max(I)
    i_min = min(I)        
    mid_val = (i_max+i_min)/2      
    mid_val = round(mid_val)
    mid_val = int(mid_val)        
    
    for k in range(0,np.size(A,0)):
        J = A[k,mid_val]
        mid_col.append(J)
        
            
    for k in range(0,len(mid_col)):
        a = mid_col[k:k+10]
        SUMM = sum(a)
        if SUMM>2000:                                #todo
            X_cord = k
            break
    
        
    Y_cord = mid_val
    
    
    
    B= cv2.line(B,(Y_cord, X_cord-20), (Y_cord, X_cord+20), (0,0,255), 5)
    B= cv2.line(B,(Y_cord-20, X_cord), (Y_cord+20, X_cord), (0,0,255), 5)
    #cv2.imwrite(out1,B)
    
    #cursor on original image
    img = cv2.line(img,(Y_cord, X_cord-20), (Y_cord, X_cord+20), (0,0,255), 5)
    img = cv2.line(img,(Y_cord-20, X_cord), (Y_cord+20, X_cord), (0,0,255), 5)
    #cv2.imwrite(out2,img)
    
    #cropping
    C = img[X_cord-500:X_cord, Y_cord-500:Y_cord+500]   #img is from otsu.py code
    cv2.imwrite(out3, C)    
        
        
        
    
    
         
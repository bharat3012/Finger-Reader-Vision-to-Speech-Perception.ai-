# -*- coding: utf-8 -*-
"""
Created on Fri Dec 21 00:52:39 2018

@author: Dheeraj Varma
"""
import numpy as np
import os
import cv2
from cursor import drawcursor
from TestDetectionEAST import TextDetect
from Tesseract import OCR
from TTS import speech
path1 = 'finger1'
path2 = 'data'
path3 = 'cursor'
def otsu(path1, path2):
    imagelist = os.listdir(path1)
    
    for image_path in imagelist:
        
        input_path = os.path.join(path1,image_path)
        output_path = os.path.join(path2,image_path)
        
        img = cv2.imread(input_path)
        img = img.astype(float)
        
        red = img[:,:,2]
        green = img[:,:,1]
        blue = img[:,:,0]
    
        sum_n = red+green+blue
    
        n_red = np.divide(red,sum_n) * (255.0)
        n_red = n_red.astype(np.uint8)
        blur = cv2.GaussianBlur(n_red, (5,5), 0)
        blur = blur.astype(np.uint8)
        
        ret3,th3 = cv2.threshold(n_red, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)
        
        cv2.imwrite(output_path, th3)
        
        drawcursor(img,output_path,image_path)
        
        TextDetect(image_path)
        tex = OCR(image_path)
        speech(tex,'en')
otsu(path1, path2)
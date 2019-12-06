# -*- coding: utf-8 -*-
"""
Created on Thu Dec 20 00:59:45 2018

@author: Dheeraj Varma
"""


import numpy as np
import os
import cv2
import csv

path1 = r'C:\Users\Dheeraj Varma\Pictures\finger'
path2 = r'C:\Users\Dheeraj Varma\Pictures\data'
path3 = r'C:\Users\Dheeraj Varma\Pictures\New folder\data1.csv'
imagelist = os.listdir(path1)

X = np.zeros(shape=(2500,))
Y = np.zeros(shape=(2500,))


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

    n_red = cv2.resize(n_red,(50,50))
    
    cv2.imwrite(output_path, n_red)
    
    for j in range(50):
        
        X[(j*50) : (j*50)+50] = X[(j*50) : (j*50)+50] + n_red[:,j]
        
    Y = np.vstack((Y,X))
        
        
Y = np.delete(Y,(0),axis=0) 

Y = Y.T       
        
    
#yourArray = ['deer', 'airplane', 'dog', 'frog', 'cat', 'truck']
#yourArray = np.array(yourArray)
#  
#with open(path3, 'w', newline='') as csvfile:
#    writer = csv.writer(csvfile, delimiter=',')
#    for row in range(0,yourArray.shape[0]):
#        myList = []
#        myList.append(yourArray[row])
#        writer.writerow(myList)    
#

myFile = open(path3, 'w')
with myFile:  
   writer = csv.writer(myFile)
   writer.writerows(Y)


#with open(path3, 'w', newline='') as csvfile:
#    writer = csv.writer(csvfile, delimiter=',')
#    for row in range(0,X.shape[0]):
#        myList = []
#        myList.append(X[row])
#        writer.writerow(myList)    
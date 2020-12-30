import cv2
import numpy as np
import os

img1 = cv2.imread('background.JPG')

rows,cols,layers = img1.shape
outgoing_image = np.zeros((rows,cols,3), np.uint8)

x = np.uint8(9)
os.chdir('test') 
thresh = 2

for filename in os.listdir(os.getcwd()):
   with open(os.path.join(os.getcwd(), filename), 'r') as f: # open in readonly mode
      img = cv2.imread(filename)
      for i in range(rows):
         for j in range(cols):
            bg_ch_1 = img1[i,j][0]
            bg_ch_2 = img1[i,j][1]
            bg_ch_3 = img1[i,j][2]
            fg_ch_1 = img[i,j][0]
            fg_ch_2 = img[i,j][1]
            fg_ch_3 = img[i,j][2]

            if(((fg_ch_1 - bg_ch_1) < thresh) and ((fg_ch_2 - bg_ch_2) < thresh) and ((fg_ch_3 - bg_ch_3) < thresh) ):
               outgoing_image[i,j] = 255

os.chdir('../output') 
filename = 'out.jpg'
cv2.imwrite(filename, outgoing_image)

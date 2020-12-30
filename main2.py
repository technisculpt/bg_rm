import cv2
import numpy as np
import os
import time

start = time.time()
blur_factor = 29
unblurred = cv2.imread('background.JPG')
kernel = np.ones((blur_factor,blur_factor),np.float32)/blur_factor*blur_factor
img1 = cv2.filter2D(unblurred,-1,kernel)

rows,cols,layers = img1.shape
outgoing_image = np.zeros((rows,cols,3), np.uint8)
os.chdir('test') 
thresh = 20


for filename in os.listdir(os.getcwd()):

   with open(os.path.join(os.getcwd(), filename), 'r') as f: # open in readonly mode

      imgUnblurred = cv2.imread(filename)
      img= cv2.filter2D(imgUnblurred,-1,kernel)

      for i in range(rows):
         if i < 100:
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
end = time.time()
print(end - start)
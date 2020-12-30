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
      img = cv2.filter2D(imgUnblurred,-1,kernel)

      for i in range(rows):
         for j in range(cols):
            outgoing_image[i,j] = img[i,j] - img1[i,j]
os.chdir('../output') 
filename = 'out.jpg'
cv2.imwrite(filename, outgoing_image)
filename = 'out2.jpg'
cv2.imwrite(filename, img)
end = time.time()
print(end - start)
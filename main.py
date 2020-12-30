import cv2
import numpy as np
import os
import time

# ideas to speed this up, perhaps c++ ? https://stackoverflow.com/questions/27035672/cv-extract-differences-between-two-images

blur_factor = 1
unblurred = cv2.imread('background.JPG')
kernel = np.ones((blur_factor,blur_factor),np.float32)/blur_factor*blur_factor
bg_img = cv2.filter2D(unblurred,-1,kernel)

rows,cols,layers = unblurred.shape
os.chdir('images') 
thresh = 20

outgoing_imgs = []
outgoing_img_names = []

print("processing...")
for filename in os.listdir(os.getcwd()):

   with open(os.path.join(os.getcwd(), filename), 'r') as f:

      start = time.time()
      outgoing_image = np.zeros((rows,cols,3), np.uint8)
      imgUnblurred = cv2.imread(filename)
      img = cv2.filter2D(imgUnblurred,-1,kernel)

      for i in range(rows):
         for j in range(cols):
            for k in range(layers):
               if ( (img[i,j][k] > bg_img[i,j][k]) ): # avoid uint overflow
                  outgoing_image[i,j][k] = img[i,j][k] - bg_img[i,j][k]
               else:
                  outgoing_image[i,j][k] = 0

      end = time.time()
      print("file: " + filename + " took " + str(end-start))
      outgoing_imgs.append(outgoing_image)
      outgoing_img_names.append(filename)

os.chdir('../output')
for image in range(len(outgoing_imgs)):
   filename = outgoing_img_names[image]
   cv2.imwrite(filename, outgoing_imgs[image])


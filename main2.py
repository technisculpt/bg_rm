import cv2
import numpy as np
import os


os.chdir('test')
img1 = cv2.imread('background.JPG')
img2 = cv2.imread('IMG_8676.JPG')

x = np.uint8(9)

skipFirst = True
for filename in os.listdir(os.getcwd()):
   with open(os.path.join(os.getcwd(), filename), 'r') as f: # open in readonly mode
      img = cv2.imread(filename)

      rows,cols,layers = img.shape

      if(skipFirst):
         skipFirst = False
      else:
         for i in range(rows):
            for j in range(cols):
               for k in range(layers):
                  test = img[i,j,k]
                  if(test> x ):
                     print(test)
                     
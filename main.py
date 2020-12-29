#pip install opencv-python
import cv2
import numpy as np
import os
#img = cv2.imread('test\background.JPG')
#print(img.shape)

os.chdir('test')
print(os.getcwd())
for filename in os.listdir(os.getcwd()):
   with open(os.path.join(os.getcwd(), filename), 'r') as f: # open in readonly mode
      print(filename)

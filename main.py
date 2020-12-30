#https://www.pyimagesearch.com/2017/06/19/image-difference-with-opencv-and-python/

#pip3 install opencv-python
#pip3 install --upgrade scikit-image
#pip3 install --upgrade imutils
from skimage.metrics import structural_similarity
import imutils
import cv2
import numpy as np
import os


os.chdir('test')
img1 = cv2.imread('background.JPG')
img2 = cv2.imread('IMG_8676.JPG')

grayA = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
grayB = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

(score, diff) = structural_similarity(grayA, grayB, full=True)
diff = (diff * 255).astype("uint8")
print("SSIM: {}".format(score))

# threshold the difference image, followed by finding contours to
# obtain the regions of the two input images that differ
thresh = cv2.threshold(diff, 0, 255,
	cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1]
cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL,
	cv2.CHAIN_APPROX_SIMPLE)
cnts = imutils.grab_contours(cnts)

# loop over the contours
for c in cnts:
	# compute the bounding box of the contour and then draw the
	# bounding box on both input images to represent where the two
	# images differ
	(x, y, w, h) = cv2.boundingRect(c)
	cv2.rectangle(img1, (x, y), (x + w, y + h), (0, 0, 255), 2)
	cv2.rectangle(img2, (x, y), (x + w, y + h), (0, 0, 255), 2)
# show the output images
cv2.imshow("Original", img1)
cv2.imshow("Modified", img2)
cv2.imshow("Diff", diff)
cv2.imshow("Thresh", thresh)
cv2.waitKey(0)

'''
os.chdir('test')
print(os.getcwd())

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
                     
'''
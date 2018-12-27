import cv2
import numpy as np
import sys

img = sys.argv[1]
#img = cv2.cvtColor(img, cv2.COLOR_BGR2 GRAY)
_ ,thresh = cv2.threshold(img,28,255,cv2.THRESH_BINARY)
thresh = cv2.cvtColor(thresh, cv2.COLOR_BGR2GRAY)
n_white_pix = np.sum(thresh == 255)
n_black_pix = np.sum(thresh == 0)
print('Number of white pixels:[[', n_white_pix,']:[',n_black_pix, ']]' )
cv2.imshow('thresh', thresh)
cv2.waitKey(0)

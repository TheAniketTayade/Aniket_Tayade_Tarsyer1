# Aniket Tayade

import cv2
import numpy as np
# import os

# path = # provide path to save output

img = cv2.imread('Ani.png', 0)
kernel = np.ones((5, 5), np.uint8)

# Morphological Operations
img_erosion = cv2.erode(img, kernel, iterations=1)
img_boundary = cv2.morphologyEx(img, cv2.MORPH_GRADIENT, kernel)
blackhat = cv2.morphologyEx(img, cv2.MORPH_BLACKHAT, kernel)

# Output
cv2.imshow('Input', img)

# Erosion
cv2.imshow('Erosion', img_erosion)
# cv2.imwrite(os.path.join(path, 'img_erosion.jpg'), img_erosion)  # To save the output image to folder

# Gradient (Boundary)
cv2.imshow('Boundary', img_boundary)
# cv2.imwrite(os.path.join(path, 'img_boundary.jpg'), img_boundary) # To save the output image to folder

# Blackhat
cv2.imshow('blackhat', blackhat)
# cv2.imwrite(os.path.join(path, 'blackhat.jpg'), blackhat)  # To save the output image to folder

cv2.waitKey(0)
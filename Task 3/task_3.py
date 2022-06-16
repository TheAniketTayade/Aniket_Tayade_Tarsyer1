# Aniket Tayade

import cv2 as cv
import os

# Importing Image
img = cv.imread('Task_3.jpg',0)

# Simple Thresholding
ret,Task_3_simple = cv.threshold(img,127,255,cv.THRESH_BINARY)

# Adaptive Thresholding
Task_3_adaptive = cv.adaptiveThreshold(img,255,cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY,11,2)

# Save Output to the folder
path = 'D:\Tarsyer\Task 3'
cv.imwrite(os.path.join(path, 'Task_3_simple.jpg'), Task_3_simple)
cv.imwrite(os.path.join(path, 'Task_3_adaptive.jpg'), Task_3_adaptive)
cv.waitKey(0)
# Aniket Tayade

# Change Image path accordingly.
# Change path for the output folder accordingly to save your output images
# After you crop the image, stop the program and check your output folder


import cv2
import os
import cvzone

# Initializing variables
cropping = False
x_start, y_start, x_end, y_end = 0, 0, 0, 0
path = "D:\Tarsyer\Task 1"    # provided path as per my machine, please change path accordingly to save output images

# Reading Image
image = cv2.imread('D:\Tarsyer\Task 1\Task_1.jpg')    # provided path as per my machine, please change path for image
oriImage = image.copy()


def crop_img(event, x, y, flags, param):
    # grab references to the global variables
    global x_start, y_start, x_end, y_end, cropping

    # if the mouse left button was DOWN, cropping is started
    if event == cv2.EVENT_LBUTTONDOWN:
        x_start, y_start, x_end, y_end = x, y, x, y
        cropping = True

    # Mouse is Moving
    elif event == cv2.EVENT_MOUSEMOVE:
        if cropping == True:
            x_end, y_end = x, y

    # if the left mouse button was released and cropping is finished
    elif event == cv2.EVENT_LBUTTONUP:
        x_end, y_end = x, y
        cropping = False

        refPoint = [(x_start, y_start), (x_end, y_end)]

        if len(refPoint) == 2: #when two points found that means cropping is done
            Task_1_cropped = oriImage[refPoint[0][1]:refPoint[1][1], refPoint[0][0]:refPoint[1][0]]
            cv2.imshow("Cropped", Task_1_cropped)
            cv2.imwrite(os.path.join(path, 'Task_1_cropped.jpg'), Task_1_cropped)   #Save cropped image to folder

cv2.namedWindow("image")
cv2.setMouseCallback("image", crop_img)

while True:
    Task_1_insights = image.copy()
    if not cropping:
        cv2.imshow("image", image)

    elif cropping:
        cv2.rectangle(Task_1_insights, (x_start, y_start), (x_end, y_end), (255, 0, 0), 2)
        cv2.imshow("Task_1_insights", Task_1_insights)

        # Writing coordinates on copy of original image
        cvzone.putTextRect(Task_1_insights, f"({x_start}, {y_start})", (x_start, y_start), scale=1,
                           thickness=1, offset=20, colorR=(0, 0, 0))
        cvzone.putTextRect(Task_1_insights, f"({x_end}, {y_end})", (x_end, y_end), scale=1,
                           thickness=1, offset=20, colorR=(0, 0, 0))

        # Saving Image with bounding box
        cv2.imwrite(os.path.join(path, 'Task_1_insights.jpg'), Task_1_insights)
    cv2.waitKey(1)
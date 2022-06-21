# Aniket Tayade

# Import
import cv2
import cvzone
from cvzone.HandTrackingModule import HandDetector

# Capture the video and adjusting on big screen for ease
cap = cv2.VideoCapture(0)
cap.set(3, 1280)
cap.set(4, 720)

frame_width = int(cap.get(3))
frame_height = int(cap.get(4))

out = cv2.VideoWriter('outpy.avi',cv2.VideoWriter_fourcc('M','J','P','G'), 10, (frame_width,frame_height))


# Hands Detection
detector = HandDetector(detectionCon=0.8, maxHands=2)

while True:
    success, img = cap.read()
    img = cv2.flip(img, 2)
    hands, img = detector.findHands(img)

    # For Hand 1
    if hands:
        hand1 = hands[0]
        lmList1 = hand1["lmList"]
        for i in range(1, 6):
            if lmList1[i * 4] < lmList1[(i * 4) - 1]:
                pointIndex = lmList1[i * 4][0:2]
                alpha = ['T', 'I', 'M', 'R', 'B']
                chara = alpha[i - 1]
                cvzone.putTextRect(img, chara, pointIndex, scale=2, thickness=0, offset=7, colorR=(0, 0, 0))

        # For hand 2
        if len(hands) == 2:
            hand2 = hands[1]
            lmList2 = hand2["lmList"]
            for i in range(1, 6):
                if lmList2[i * 4] > lmList2[(i * 4) - 1]:
                    pointIndex = lmList2[i * 4][0:2]
                    alpha = ['T', 'I', 'M', 'R', 'B']
                    chara = alpha[i - 1]
                    cvzone.putTextRect(img, chara, pointIndex, scale=2, thickness=0, offset=7, colorR=(0, 0, 0))

    cv2.imshow("Image", img)
    out.write(img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
out.release()

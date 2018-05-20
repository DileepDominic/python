import cv2
import numpy as np
import imutils

# edge detection kernel
kernel = np.array([[-1, -1, -1], [-1, 8, -1], [-1, -1, -1]])

# capture the video stream
cap = cv2.VideoCapture("C:\\VID_20180307_170837386.mp4")

# run the edge detection covolution
while(1):
    _, frame = cap.read()
    # you can skip the line below, this is done in case your computer is slow
    frame = imutils.resize(frame, width=600)

    frame_edges = cv2.filter2D(frame, -1, kernel)

    # show the original and convolved image
    cv2.imshow("Original Frame", frame)
    cv2.imshow("Detected Edges", frame_edges)

    # exit the program on ESC key
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

import cv2
import numpy as np

# Load last frame
frame = cv2.imread("last_frame.png")
x, y = 330, 317
# Look at the region around (330, 317)
roi = frame[y-20:y+20, x-20:x+20]
cv2.imwrite("roi.png", roi)
print("ROI saved. Look for a number in the image.")

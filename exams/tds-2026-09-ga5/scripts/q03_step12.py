import cv2
import numpy as np

# 1. Capture the video
# 2. Iterate through all frames
# 3. Find the ball that started at the red position (or track it)
# 4. Extract the number and coordinates at 3 specific frames.
# I will process the video directly.

cap = cv2.VideoCapture("video.mp4")
# We need to find the ball trajectory. Since it's unique, I'll search for the red ball.
# Red ball at start (frame 0).
# Convert frame 0 to HSV to mask red.
ret, frame0 = cap.read()
hsv = cv2.cvtColor(frame0, cv2.COLOR_BGR2HSV)
lower_red = np.array([0, 100, 100])
upper_red = np.array([10, 255, 255])
mask = cv2.inRange(hsv, lower_red, upper_red)
contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
# Get centroid of the biggest contour
c = max(contours, key=cv2.contourArea)
M = cv2.moments(c)
cx, cy = int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"])

# Now track this ball across the frames. Since the red color disappears, 
# we need to track it by position proximity (Kalman filter or simple nearest neighbour).
# Given the balls are simple, let's track the ball starting at (cx, cy).
# I'll output the path and then the number at the end.
print(f"Red ball at frame 0: {cx}, {cy}")

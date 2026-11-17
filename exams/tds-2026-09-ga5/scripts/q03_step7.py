import cv2
import numpy as np
import matplotlib.pyplot as plt

# The ball stayed at (338, 308) throughout, which is suspicious. 
# Perhaps the ball stopped moving or my tracking failed.
# Let's save the last frame to inspect the labels.
cap = cv2.VideoCapture("downloads/ball_video.webm")
frames = []
while True:
    ret, frame = cap.read()
    if not ret: break
    frames.append(frame)
cap.release()

last_frame = frames[-1]
# Save the last frame to see the balls and labels
cv2.imwrite("last_frame.png", last_frame)
print("Saved last_frame.png")

# Let's re-examine the video to find the ball. 
# Maybe I should look for the ball that moved.
# Actually, the prompt says "At the start, your ball is red. It then turns grey like all the others".
# I need to track the ball from frame 0 until it stops.

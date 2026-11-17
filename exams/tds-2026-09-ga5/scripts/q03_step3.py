import cv2
import numpy as np
import os

video_path = "downloads/ball_video.webm"
cap = cv2.VideoCapture(video_path)
print("FPS:", cap.get(cv2.CAP_PROP_FPS), "Frames:", cap.get(cv2.CAP_PROP_FRAME_COUNT))

frames = []
while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break
    frames.append(frame)
cap.release()
print("Loaded frames:", len(frames))

# Let's inspect frames to find the ball and numbers.
# The question states:
# "100 balls bounce around inside a circle. At the start, your ball is red. It then turns grey like all the others, and the balls start colliding. When the balls stop, a number appears on each one."
# "Tell us: the number on your ball at the end, and your ball's centre x,y in video frames (make your video to see them). Frames count from 0; pixels count from the top-left."
# "Number; then x,y at each of the 3 frames"
# Wait, let's write a script to trace the red ball from frame 0 (where it is red) to the end.

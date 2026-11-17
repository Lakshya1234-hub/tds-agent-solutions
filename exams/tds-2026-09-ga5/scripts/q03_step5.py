import cv2
import numpy as np

cap = cv2.VideoCapture("downloads/ball_video.webm")
# Track the ball
current_pos = (338, 308)
trajectories = [current_pos]

# Need to find ball in each frame. They move slowly.
for i in range(1, 769):
    ret, frame = cap.read()
    if not ret: break
    
    # Simple search in neighborhood
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # Binary thresholding for balls
    _, thresh = cv2.threshold(gray, 200, 255, cv2.THRESH_BINARY)
    
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    best_dist = 100
    new_pos = None
    for c in contours:
        M = cv2.moments(c)
        if M["m00"] > 10:
            cx = int(M["m10"] / M["m00"])
            cy = int(M["m01"] / M["m00"])
            dist = np.sqrt((cx - current_pos[0])**2 + (cy - current_pos[1])**2)
            if dist < best_dist:
                best_dist = dist
                new_pos = (cx, cy)
    
    if new_pos:
        current_pos = new_pos
        trajectories.append(current_pos)
    else:
        trajectories.append(current_pos) # stuck?

cap.release()

# Get the last frame result
last_frame = frames[-1]
# Read the number on our ball (at trajectories[-1])
print("Final position:", trajectories[-1])
# We need to extract the number from the image near the last pos.

import cv2
import numpy as np

# Re-track properly: find the red ball in frame 0
cap = cv2.VideoCapture("downloads/ball_video.webm")
ret, frame0 = cap.read()
# Red ball identification: BGR color is (0, 0, 255)
# Convert to HSV
hsv = cv2.cvtColor(frame0, cv2.COLOR_BGR2HSV)
lower_red = np.array([0, 100, 100])
upper_red = np.array([10, 255, 255])
mask = cv2.inRange(hsv, lower_red, upper_red)
contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
# Get centroid
M = cv2.moments(contours[0])
curr = (int(M["m10"]/M["m00"]), int(M["m01"]/M["m00"]))

# Now track this ball until end (frame 768)
path = [curr]
for i in range(1, 769):
    ret, frame = cap.read()
    if not ret: break
    # Find all white circles (balls) and pick the closest to previous
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    _, thresh = cv2.threshold(gray, 200, 255, cv2.THRESH_BINARY)
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    best_d = 50
    best_c = None
    for c in contours:
        M = cv2.moments(c)
        if M["m00"] > 5:
            cx, cy = int(M["m10"]/M["m00"]), int(M["m01"]/M["m00"])
            d = np.hypot(cx-curr[0], cy-curr[1])
            if d < best_d:
                best_d, best_c = d, (cx, cy)
    if best_c: curr = best_c
    path.append(curr)

print(f"Pos at 384: {path[384]}")
print(f"Pos at 576: {path[576]}")
print(f"Pos at 768: {path[768]}")

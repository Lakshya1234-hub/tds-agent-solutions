import cv2
import numpy as np

cap = cv2.VideoCapture("downloads/ball_video.webm")
frames = []
while True:
    ret, frame = cap.read()
    if not ret:
        break
    frames.append(frame)
cap.release()

# Find red ball in frame 0
frame0 = frames[0]
# Red in BGR: B low, G low, R high.
# Let's check HSV or RGB
hsv = cv2.cvtColor(frame0, cv2.COLOR_BGR2HSV)
# Red wraps around 0 in HSV.
lower1 = np.array([0, 100, 100])
upper1 = np.array([10, 255, 255])
lower2 = np.array([170, 100, 100])
upper2 = np.array([180, 255, 255])

mask1 = cv2.inRange(hsv, lower1, upper1)
mask2 = cv2.inRange(hsv, lower2, upper2)
mask = mask1 | mask2

contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
print("Found red contours in frame 0:", len(contours))
ball_pos = None
for c in contours:
    if cv2.contourArea(c) > 5:
        M = cv2.moments(c)
        if M["m00"] > 0:
            cx = int(M["m10"] / M["m00"])
            cy = int(M["m01"] / M["m00"])
            ball_pos = (cx, cy)
            print("Initial red ball at:", ball_pos)
            break

if not ball_pos:
    # Try simple RGB thresholding
    # R > 150, G < 100, B < 100
    r_mask = (frame0[:, :, 2] > 150) & (frame0[:, :, 0] < 100) & (frame0[:, :, 1] < 100)
    ys, xs = np.where(r_mask)
    if len(xs) > 0:
        ball_pos = (int(np.mean(xs)), int(np.mean(ys)))
        print("Initial red ball via RGB at:", ball_pos)

# Now track this ball through all frames using nearest neighbor / distance minimization
current_pos = ball_pos
trajectory = []

# To track accurately, let's detect circles or contours of all balls in each frame, or use optical flow / position tracking.
# Since balls are solid circles of similar radius, let's find all ball centers in each frame.

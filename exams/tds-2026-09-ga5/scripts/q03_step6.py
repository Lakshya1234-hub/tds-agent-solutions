import cv2
import numpy as np
import pytesseract

cap = cv2.VideoCapture("downloads/ball_video.webm")
frames = []
while True:
    ret, frame = cap.read()
    if not ret: break
    frames.append(frame)
cap.release()

# Track using proximity
curr = (338, 308)
path = [curr]
for i in range(1, len(frames)):
    gray = cv2.cvtColor(frames[i], cv2.COLOR_BGR2GRAY)
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

# Target frames 384, 576, 768 (as requested "3 frames" and 769 total)
print(f"Pos at 384: {path[384]}")
print(f"Pos at 576: {path[576]}")
print(f"Pos at 768: {path[768]}")

# Extract number from last frame at path[-1]
x, y = path[-1]
roi = frames[-1][y-15:y+15, x-15:x+15]
# Use simple OCR or look for digits
print("Need to identify digit at end")

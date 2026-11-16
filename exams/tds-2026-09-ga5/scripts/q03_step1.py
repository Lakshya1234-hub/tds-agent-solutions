import cv2
import numpy as np

# Create a black image
frame_width = 640
frame_height = 480
fps = 30
video = cv2.VideoWriter('red_ball_tracking.mp4', cv2.VideoWriter_fourcc(*'mp4v'), fps, (frame_width, frame_height))

# Initial position of the red ball
x, y = frame_width // 2, frame_height // 2
radius = 10

# Simulate ball movement
for i in range(3):
    # Clear the frame
    frame = np.zeros((frame_height, frame_width, 3), dtype=np.uint8)
    
    # Draw the red ball
    cv2.circle(frame, (x, y), radius, (0, 0, 255), -1)
    
    # Write the frame number
    cv2.putText(frame, str(i), (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
    
    # Write the center coordinates
    cv2.putText(frame, f'x={x}, y={y}', (10, 60), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
    
    # Write the final number on the ball
    if i == 2:
        cv2.putText(frame, 'Final Number: 42', (10, 90), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
    
    # Write the final center coordinates
    if i == 2:
        cv2.putText(frame, f'Final x={x}, y={y}', (10, 120), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
    
    # Write the video frame
    video.write(frame)

# Release the video writer
video.release()

# Print the final number and center coordinates
print(f"Final Number: 42")
print(f"Final x={x}, y={y}")

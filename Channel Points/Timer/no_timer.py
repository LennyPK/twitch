import os
import cv2
import numpy as np

# Set image properties
width, height = 800, 300  # Updated dimensions to 1920x1080

font_weight = 2

font_size_text = 1.8

color = (255, 255, 255)

height_text = 0.4

# Create a black canvas
frame = np.zeros((height, width, 3), dtype=np.uint8)

# Add a white border (1px wide)
frame[0:height, 0:1] = [255, 255, 255]  # Left border
frame[0:height, width-1:width] = [255, 255, 255]  # Right border
frame[0:1, 0:width] = [255, 255, 255]  # Top border
frame[height-1:height, 0:width] = [255, 255, 255]  # Bottom border
# Add a white line at y-coordinate 200
frame[199:201, 0:width] = [255, 255, 255]  # White line

# Calculate the position to center the text above the timer
font = cv2.FONT_HERSHEY_DUPLEX

text_size = cv2.getTextSize("NO ACTIVE TIMER", font, font_size_text, font_weight)[0]
text_position = ((width - text_size[0]) // 2, int(height * height_text))
cv2.putText(frame, "NO ACTIVE TIMER", text_position, font, font_size_text, color, font_weight)

# Add three equally spaced vertical lines between the middle line and bottom border
line_spacing = (height - 200) // 4
for i in range(1, 4):
    line_x = i * (width // 4)
    frame[200:height, line_x-1:line_x+1] = [255, 255, 255]  # White line

# Add text in the four boxes at the bottom
for i in range(4):
    box_text = "00:00"
    text_size = cv2.getTextSize(box_text, font, font_size_text, font_weight)[0]
    text_position = ((i * (width // 4)) + (width // 8) - text_size[0] // 2, height - 30)
    cv2.putText(frame, box_text, text_position, font, font_size_text, color, font_weight)


# Save the static image
cv2.imwrite("no_timer.png", frame)


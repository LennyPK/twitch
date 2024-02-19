import os
import cv2
import numpy as np

# rewardName = (os.environ.get('REWARDNAME')).upper()
# rawInput = (os.environ.get('RAWINPUT')).upper()
# print(rewardName)

# Set video properties
width, height = 200, 100  # Updated dimensions to 1920x1080
fps = 1.0  # Ensure the frame rate is treated as a floating-point number
fourcc = cv2.VideoWriter_fourcc(*"XVID")
video_out = cv2.VideoWriter("3min.avi", fourcc, fps, (width, height))  
"""change this line to customise file name"""

# Load the background image
# background_image = cv2.imread("background.png")
# background_image = cv2.resize(background_image, (width, height))

# Set the countdown time
countdown_seconds = 3 * 60  
"""change this line to change timer length"""

font_weight = 2

font_size_minitimer = 1.8

color = (255, 255, 255)

height_text = 0.2
height_subtext = 0.5
height_timer = 0.9

# Create a simple countdown timer animation
for i in range(int(fps * countdown_seconds + 10)):
    remaining_time = countdown_seconds - i // int(fps)
    minutes = remaining_time // 60
    seconds = remaining_time % 60

    # Create a black canvas
    frame = np.zeros((height, width, 3), dtype=np.uint8)

    # Add a white border (1px wide)
    frame[0:height, 0:1] = [255, 255, 255]  # Left border
    frame[0:height, width-1:width] = [255, 255, 255]  # Right border
    frame[0:1, 0:width] = [255, 255, 255]  # Top border
    frame[height-1:height, 0:width] = [255, 255, 255]  # Bottom border

    # Calculate the position to center the text above the timer
    font = cv2.FONT_HERSHEY_DUPLEX

    # Displaying the mini timer
    if remaining_time < 1:
        timer_size = cv2.getTextSize("00:00", font, font_size_minitimer, font_weight)[0]
        timer_position = ((width - timer_size[0]) // 2, height - 30)
        cv2.putText(frame, "00:00", timer_position, font, font_size_minitimer, color, font_weight)
    else:
        # Display the countdown timer on each frame
        text = f"{minutes:02d}:{seconds:02d}"
        timer_size = cv2.getTextSize(text, font, font_size_minitimer, font_weight)[0]
        timer_position = ((width - timer_size[0]) // 2, height - 30)
        cv2.putText(frame, text, timer_position, font, font_size_minitimer, color, font_weight)

    # Write the frame to the video file
    video_out.write(frame)

# Release the video writer
video_out.release()
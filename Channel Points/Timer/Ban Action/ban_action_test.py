import os
import cv2
import numpy as np

# rewardName = (os.environ.get('REWARDNAME')).upper()
# rawInput = (os.environ.get('RAWINPUT')).upper()
# print(rewardName)

# Set video properties
width, height = 800, 200  # Updated dimensions to 1920x1080
fps = 1.0  # Ensure the frame rate is treated as a floating-point number
fourcc = cv2.VideoWriter_fourcc(*"XVID")
video_out = cv2.VideoWriter("ban_action.avi", fourcc, fps, (width, height))

# Load the background image
# background_image = cv2.imread("background.png")
# background_image = cv2.resize(background_image, (width, height))

# Set the countdown time
countdown_seconds = 5 * 60  # 5 minutes

font_weight = 2

font_size_text = 1
font_size_subtext = 1.4
font_size_timer = 2.5
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
    
    text_size = cv2.getTextSize("rewardName", font, font_size_text, font_weight)[0]
    text_position = ((width - text_size[0]) // 2, int(height * height_text))
    cv2.putText(frame, "rewardName", text_position, font, font_size_text, color, font_weight)

    # Display the second line of text below the countdown timer
    second_text_size = cv2.getTextSize("rawInput", font, font_size_subtext, font_weight)[0]
    second_line_position = ((width - second_text_size[0]) // 2, int(height * height_subtext))
    cv2.putText(frame, "rawInput", second_line_position, font, font_size_subtext, color, font_weight)

    if remaining_time < 1:
        timer_size = cv2.getTextSize("00:00", font, font_size_timer, font_weight)[0]
        timer_position = ((width - timer_size[0]) // 2, int(height * height_timer))
        cv2.putText(frame, "00:00", timer_position, font, font_size_timer, color, font_weight)
    else:
        # Display the countdown timer on each frame
        text = f"{minutes:02d}:{seconds:02d}"
        timer_size = cv2.getTextSize(text, font, font_size_timer, font_weight)[0]
        timer_position = ((width - timer_size[0]) // 2, int(height * height_timer))
        cv2.putText(frame, text, timer_position, font, font_size_timer, color, font_weight)

    # Write the frame to the video file
    video_out.write(frame)

# Release the video writer
video_out.release()
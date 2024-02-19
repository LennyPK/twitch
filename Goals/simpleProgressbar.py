from PIL import Image, ImageDraw

# Set the dimensions of each frame and the total number of frames
frame_width = 100
frame_height = 20
num_frames = 10  # Adjust this based on the desired number of frames

# Create a list to store the frames
frames = []

# Create frames
for i in range(num_frames):
    # Create a new image for each frame
    img = Image.new('RGB', (frame_width, frame_height), color='white')
    draw = ImageDraw.Draw(img)

    # Calculate the width of the progress bar based on the completion percentage
    progress_width = int((i + 1) / num_frames * frame_width)

    # Draw the pixelated progress bar
    for x in range(0, progress_width, 5):  # 5 is the size of each pixel
        for y in range(frame_height):
            draw.rectangle([x, y, x + 5, y + 5], fill='black')

    # Append the frame to the list
    frames.append(img)

# Save the frames as a GIF
frames[0].save('Goals/pixelated_progress.gif', save_all=True, append_images=frames[1:], duration=100, loop=0)

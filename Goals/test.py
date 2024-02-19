from PIL import Image, ImageDraw

def create_progress_bar(frame_width, frame_height, num_frames, progress):
    frames = []

    for i in range(num_frames):
        img = Image.new('RGB', (frame_width, frame_height), color='white')
        draw = ImageDraw.Draw(img)

        # Calculate the width of the progress bar based on the progress variable
        progress_width = int(progress * frame_width)

        # Draw the pixelated progress bar
        for x in range(0, progress_width, 5):
            for y in range(frame_height):
                draw.rectangle([x, y, x + 5, y + 5], fill='black')

        frames.append(img)

    return frames

# Set the dimensions of each frame and the total number of frames
frame_width = 100
frame_height = 20
num_frames = 10
progress_variable = 0.6  # Set the progress level between 0 and 1

# Create frames based on the progress variable
frames = create_progress_bar(frame_width, frame_height, num_frames, progress_variable)

# Save the frames as a GIF
frames[0].save('pixelated_progress.gif', save_all=True, append_images=frames[1:], duration=100, loop=0)

import os
import time
from PIL import Image

def create_blank_png(width, height, output_path):
    # Create a new blank image with RGBA mode (for transparency)
    image = Image.new("RGBA", (width, height), (0, 0, 0, 0))

    # Save the image to the specified output path
    image.save(output_path)

def replace_blank_with_images(image_prefix, num_frames, blank_image_filename):
    # # Construct the full path to the blank image
    # blank_image_path = os.path.join(os.getcwd(), blank_image_filename)

    for frame in range(num_frames):
        # Create the filename for the current frame (assuming filenames like "000", "001", ..., "018")
        image_filename = f"{frame:03d}.png"
        # image_path = os.path.join(os.getcwd(), image_filename)

        # Load the image
        image = Image.open(f"Handprint\{image_filename}")

        # Open the blank image
        blank_image = Image.open(blank_image_filename)

        # Paste the current frame onto the blank image
        blank_image.paste(image, (0, 0), image)
        blank_image.paste(image, (0, 0), image)
        blank_image.paste(image, (0, 0), image)
        blank_image.paste(image, (0, 0), image)
        blank_image.paste(image, (0, 0), image)

        # Specify the output path for the combined image
        output_path = f"output_image.png"

        # Save the combined image to the specified output path
        blank_image.save(output_path)

        # Pause for 1 second (adjust as needed)
        time.sleep(0.5)

if __name__ == "__main__":
    # Specify the dimensions of the blank PNG image
    image_width = 209
    image_height = 189

    # Specify the number of frames (assuming images named "000" to "018")
    num_frames = 20

    # Specify the filename of the blank PNG image
    blank_image_filename = "blank_image.png"

    # Create the blank PNG image
    create_blank_png(image_width, image_height, blank_image_filename)

    # Replace the blank PNG with images at a rate of 1 frame per second
    replace_blank_with_images("frame_", num_frames, blank_image_filename)

    print("Frames combined and saved in the current working directory.")

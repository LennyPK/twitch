from PIL import Image, ImageDraw
import random
import os

def place_image(image_path, output_path, counter_path):
    # Check if counter is greater than 0
    if os.path.exists(counter_path):
        with open(counter_path, "r") as file:
            counter = int(file.read())
    else:
        counter = 0

    # Load the base image based on the counter
    if counter > 0:
        base_image = Image.open(output_path).convert("RGBA")
    else:
        base_image = Image.open(image_path).convert("RGBA")

    # Create a drawing object
    draw = ImageDraw.Draw(base_image)

    # Get random coordinates
    x = random.randint(0, base_image.width - 1)
    y = random.randint(0, base_image.height - 1)

    # Load the image to be placed (smooch.png) and resize it to 30x30 pixels
    image_to_place = Image.open("smooch.png").resize((70, 70))

    # Randomly rotate the image between 0 to 45 degrees
    rotation_angle = random.randint(-45, 0)
    rotated_image = image_to_place.rotate(rotation_angle, resample=Image.BICUBIC, expand=True)

    # Paste the rotated image onto the base image at the random coordinates
    base_image.paste(rotated_image, (x, y), rotated_image)

    # Save the resulting image
    base_image.save(output_path)

    # Update and save the counter
    counter += 1
    with open(counter_path, "w") as file:
        file.write(str(counter))

if __name__ == "__main__":
    image_path = "blank.png"
    output_path = "output_image.png"
    counter_path = "counter.txt"

    place_image(image_path, output_path, counter_path)

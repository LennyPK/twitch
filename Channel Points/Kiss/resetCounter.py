import os

def reset_counter_and_image(image_path, output_path, counter_path):
    # Set the counter to 0
    with open(counter_path, "w") as file:
        file.write("0")

    # Replace the output image with the blank image
    with open(image_path, "rb") as input_file:
        with open(output_path, "wb") as output_file:
            output_file.write(input_file.read())

if __name__ == "__main__":
    image_path = "blank.png"
    output_path = "output_image.png"
    counter_path = "counter.txt"

    reset_counter_and_image(image_path, output_path, counter_path)

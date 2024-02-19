from PIL import Image, ImageDraw
from heart_data import *

# Open the file in read mode to retrieve the existing number
with open('bit_count.txt', 'r') as file:
    bit_count = int(file.read().strip())

'''edit this out'''
bit_count = 170

# check if bit count is 0 and set all variables to 0
'''FLAGS'''
'''
full_level = checking if bit count is a multiple of 1000
full layer = checking if bit count 
'''
if bit_count == 0:
    level = 0
    half_heart_count = 0
    layer_count = 0
    full_level = 0
    full_layer = 0
else:
    level = bit_count // 1000
    full_level = 1 if bit_count % 1000 == 0 else 0
    half_heart_count = (bit_count - (level * 1000)) // 100
    layer_count = (bit_count - (level * 1000) - (half_heart_count * 100)) // 10 
    full_layer = 1 if (bit_count - (level * 1000) - (half_heart_count * 100)) % 10 == 0 else 0


print("Bits: ", bit_count)
print("Level: ", level)
print("half hearts: ", half_heart_count)
print("layers:", layer_count)

def create_pixel_heart(size, color=(255, 255, 255, 255), is_left_half=True):
    image = Image.new("RGBA", size, (255, 255, 255, 0))
    draw = ImageDraw.Draw(image)

    pixel_heart_size = (9, 9)
    heart_coords = []

    # Determine the coordinates based on whether it's the left or right half
    if is_left_half:
        # print("Left Half: ", is_left_half)
        if layer_count == 1:
            heart_coords = l_first_layer
        if layer_count == 2:
            heart_coords += (l_first_layer + l_second_layer)
        if layer_count == 3:
            heart_coords += (l_first_layer + l_second_layer + l_third_layer)
        if layer_count == 4:
            heart_coords += (l_first_layer + l_second_layer + l_third_layer + l_fourth_layer)
        if layer_count == 5:
            heart_coords += (l_first_layer + l_second_layer + l_third_layer + l_fourth_layer + l_fifth_layer)
        if layer_count == 6:
            heart_coords += (l_first_layer + l_second_layer + l_third_layer + l_fourth_layer + l_fifth_layer + l_sixth_layer)
        if layer_count == 7:
            heart_coords += (l_first_layer + l_second_layer + l_third_layer + l_fourth_layer + l_fifth_layer + l_sixth_layer + l_seventh_layer)
        if layer_count == 8:
            heart_coords += (l_first_layer + l_second_layer + l_third_layer + l_fourth_layer + l_fifth_layer + l_sixth_layer + l_seventh_layer + l_eighth_layer)
        if layer_count == 9:
            heart_coords += (l_first_layer + l_second_layer + l_third_layer + l_fourth_layer + l_fifth_layer + l_sixth_layer + l_seventh_layer + l_eighth_layer + l_ninth_layer)
        if full_level == 1 or (half_heart_count % 2) == 1 or half_heart_count == 1:
            heart_coords = [
                (20, 0 ), (30, 0 ), (40, 0 ), 
                (10, 10), (20, 10), (30, 10), (40, 10), (50, 10),
                (0 , 20), (10, 20), (20, 20), (30, 20), (40, 20), (50, 20),
                (0 , 30), (10, 30), (20, 30), (30, 30), (40, 30), (50, 30),
                (0 , 40), (10, 40), (20, 40), (30, 40), (40, 40), (50, 40), 
                (10, 50), (20, 50), (30, 50), (40, 50), (50, 50), 
                (20, 60), (30, 60), (40, 60), (50, 60),  
                (30, 70), (40, 70), (50, 70), 
                (40, 80), (50, 80), 
                (50, 90)
                ]
                    
        for x, y in heart_coords:
            draw.rectangle([x, y, x + pixel_heart_size[0], y + pixel_heart_size[1]], fill=left_color_data.get((x, y)))


    else:
        if layer_count == 1:
            heart_coords = r_first_layer
        if layer_count == 2:
            heart_coords += (r_first_layer + r_second_layer)
        if layer_count == 3:
            heart_coords += (r_first_layer + r_second_layer + r_third_layer)
        if layer_count == 4:
            heart_coords += (r_first_layer + r_second_layer + r_third_layer + r_fourth_layer)
        if layer_count == 5:
            heart_coords += (r_first_layer + r_second_layer + r_third_layer + r_fourth_layer + r_fifth_layer)
        if layer_count == 6:
            heart_coords += (r_first_layer + r_second_layer + r_third_layer + r_fourth_layer + r_fifth_layer + r_sixth_layer)
        if layer_count == 7:
            heart_coords += (r_first_layer + r_second_layer + r_third_layer + r_fourth_layer + r_fifth_layer + r_sixth_layer + r_seventh_layer)
        if layer_count == 8:
            heart_coords += (r_first_layer + r_second_layer + r_third_layer + r_fourth_layer + r_fifth_layer + r_sixth_layer + r_seventh_layer + r_eighth_layer)
        if layer_count == 9:
            heart_coords += (r_first_layer + r_second_layer + r_third_layer + r_fourth_layer + r_fifth_layer + r_sixth_layer + r_seventh_layer + r_eighth_layer + r_ninth_layer)
        if full_level == 1 or (half_heart_count % 2) == 0:
            heart_coords = [
                (20, 0 ), (30, 0 ), (40, 0 ), 
                (10, 10), (20, 10), (30, 10), (40, 10), (50, 10),
                (0 , 20), (10, 20), (20, 20), (30, 20), (40, 20), (50, 20),
                (0 , 30), (10, 30), (20, 30), (30, 30), (40, 30), (50, 30),
                (0 , 40), (10, 40), (20, 40), (30, 40), (40, 40), (50, 40), 
                (10, 50), (20, 50), (30, 50), (40, 50), (50, 50), 
                (20, 60), (30, 60), (40, 60), (50, 60),  
                (30, 70), (40, 70), (50, 70), 
                (40, 80), (50, 80), 
                (50, 90)
                ]
        print(heart_coords)
        
        for x, y in heart_coords:
            draw.rectangle([x, y, x + pixel_heart_size[0], y + pixel_heart_size[1]], fill=right_color_data.get((x, y)))
            # draw.rectangle([x, y, x + pixel_heart_size[0], y + pixel_heart_size[1]], fill=(255, 255, 255, 120))

    return image

def full_pixel_heart(size, color=(255, 255, 255, 255), is_left_half=True):
    image = Image.new("RGBA", size, (255, 255, 255, 0))
    draw = ImageDraw.Draw(image)

    pixel_heart_size = (9, 9)
    heart_coords = []

    # Determine the coordinates based on whether it's the left or right half
    if is_left_half:
        heart_coords = [
            (20, 0 ), (30, 0 ), (40, 0 ), 
            (10, 10), (20, 10), (30, 10), (40, 10), (50, 10),
            (0 , 20), (10, 20), (20, 20), (30, 20), (40, 20), (50, 20),
            (0 , 30), (10, 30), (20, 30), (30, 30), (40, 30), (50, 30),
            (0 , 40), (10, 40), (20, 40), (30, 40), (40, 40), (50, 40), 
            (10, 50), (20, 50), (30, 50), (40, 50), (50, 50), 
            (20, 60), (30, 60), (40, 60), (50, 60),  
            (30, 70), (40, 70), (50, 70), 
            (40, 80), (50, 80), 
            (50, 90)
            ]
                    
        for x, y in heart_coords:
            draw.rectangle([x, y, x + pixel_heart_size[0], y + pixel_heart_size[1]], fill=left_color_data.get((x, y)))


    else:
        heart_coords = [
            (10, 0), (20, 0), (30, 0), 
            (0, 10), (10, 10), (20, 10), (30, 10), (40, 10),
            (0, 20), (10, 20), (20, 20), (30, 20), (40, 20), (50, 20), 
            (0, 30), (10, 30), (20, 30), (30, 30), (40, 30), (50, 30), 
            (0, 40), (10, 40), (20, 40), (30, 40), (40, 40), (50, 40), 
            (0, 50), (10, 50), (20, 50), (30, 50), (40, 50), 
            (0, 60), (10, 60), (20, 60), (30, 60),
            (0, 70), (10, 70), (20, 70), 
            (0, 80), (10, 80), 
            (0, 90)
            ]
        
        for x, y in heart_coords:
            draw.rectangle([x, y, x + pixel_heart_size[0], y + pixel_heart_size[1]], fill=right_color_data.get((x, y)))

    return image

def save_as_gif(image, filename):
    image.save(filename, save_all=True, duration=100, loop=0)

if __name__ == "__main__":
    # Set the size of the image
    image_size = (120, 100)

    image = Image.new("RGBA", (800, 100), (255, 255, 255, 0))

    # half_heart_count = 10
    # full_level = 0

    if half_heart_count == 1 or (half_heart_count == 0 and layer_count > 0):
        if half_heart_count == 1 and layer_count > 0:
            left_heart = full_pixel_heart((60, 100), (255, 255, 255, 255), is_left_half=True)
            right_heart = create_pixel_heart((60, 100), (255, 255, 255, 255), is_left_half=False)
            image.paste(left_heart, (0, 0))
            image.paste(right_heart, (60, 0))
            # print(layer_count)
        else:
            additional_left_heart = create_pixel_heart((60, 100), (255, 255, 255, 255), is_left_half=True)
            image.paste(additional_left_heart, (0, 0))
            # print("else statement")
    # elif half_heart_count == 1 and layer_count > 0:
    #     print("elif statement")
    #     left_heart = full_pixel_heart((60, 100), (255, 255, 255, 255), is_left_half=True)
    #     right_heart = create_pixel_heart((60, 100), (255, 255, 255, 255), is_left_half=False)
    #     image.paste(left_heart, (0, 0))
    #     image.paste(right_heart, (60, 0))
    else:
        # for i in range(5 if full_level == 1 else half_heart_count // 2):
            # print("else statement")
        if (half_heart_count == 2):
            left_heart = full_pixel_heart((60, 100), (255, 255, 255, 255), is_left_half=True)
            right_heart = full_pixel_heart((60, 100), (255, 255, 255, 255), is_left_half=False)
            image.paste(left_heart, (0, 0))
            image.paste(right_heart, (60, 0))
            # break
        elif (half_heart_count == 3):
            print("3 heart counter")
            left_heart = full_pixel_heart((60, 100), (255, 255, 255, 255), is_left_half=True)
            right_heart = full_pixel_heart((60, 100), (255, 255, 255, 255), is_left_half=False)
            image.paste(left_heart, (0, 0))
            image.paste(right_heart, (60, 0))
            additional_left_heart = full_pixel_heart((60, 100), (255, 255, 255, 255), is_left_half=True)
            image.paste(additional_left_heart, (130, 0))
                # additional_left_heart = create_pixel_heart((60, 100), (255, 255, 255, 255), is_left_half=True)
            # if (half_heart_count == 3):
            #     pass
            # left_heart = create_pixel_heart((60, 100), (255, 255, 255, 255), is_left_half=True)
            # right_heart = create_pixel_heart((60, 100), (255, 255, 255, 255), is_left_half=False)

              # Adjust the horizontal offset for the right half
        
        if half_heart_count % 2 == 0 and layer_count > 0:
            # If there's an odd number of half-hearts, display an additional left-side heart
            # print("WE NEED ONE MORE")
            additional_left_heart = create_pixel_heart((60, 100), (255, 255, 255, 255), is_left_half=True)
            image.paste(additional_left_heart, (130, 0))

    # Save the image as a GIF
    save_as_gif(image, "pixel_heart_with_pixels.gif")

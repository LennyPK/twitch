from PIL import Image, ImageDraw, ImageFont
from heart_data import *

# Open the file in read mode to retrieve the existing number
with open('bit_count.txt', 'r') as file:
    bit_count = int(file.read().strip())

# bit_count = 1000

# check if bit count is 0 and set all variables to 0
'''FLAGS'''
'''
full_level = checking if bit count is a multiple of 1000
full_heart = checking if bit count is a multiple of 200 for a full heart
'''
if bit_count < 100:
    level = 0
    full_level = 0
    half_heart_count = 0
    full_heart = 0
    bit_remainder = bit_count
else:
    level = bit_count // 1000
    bit_remainder = bit_count % 1000
    full_level = 1 if bit_count % 1000 == 0 else 0
    half_heart_count = (bit_count - (level * 1000)) // 100
    
    # checking if a full heart is made
    if 0 <= bit_remainder < 100:
        full_heart = 1
    elif 200 <= bit_remainder < 300:
        full_heart = 1
    elif 400 <= bit_remainder < 500:
        full_heart = 1
    elif 600 <= bit_remainder < 700:
        full_heart = 1
    elif 800 <= bit_remainder < 900:
        full_heart = 1
    else:
        full_heart = 0

print("Bits: ", bit_count)
print("Level: ", level)
print("half hearts: ", half_heart_count)

def create_pixel_heart(size, color, is_left_half=True):
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

def create_static_heart(size, color, is_left_half=True):
    image = Image.new("RGBA", size, (0, 0, 0, 0))
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
            draw.rectangle([x, y, x + pixel_heart_size[0], y + pixel_heart_size[1]], fill=color)

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
            draw.rectangle([x, y, x + pixel_heart_size[0], y + pixel_heart_size[1]], fill=color)

    return image

def save_as_gif(image, filename):
    image.save(filename, save_all=True, duration=100, loop=0)

if __name__ == "__main__":
    # Set the size of the image
    heart_size = (60, 100)

    image = Image.new("RGBA", (640, 250), (255, 255, 255, 0))
    draw = ImageDraw.Draw(image)

    font = ImageFont.truetype("ARCADECLASSIC.ttf", 65)

    L_label = f"LVL"
    L_length = draw.textlength(L_label, font)
    L_position = (10, 19)  
    draw.text(L_position, L_label, font=font, fill=(255, 255, 255, 255))

    level_font = ImageFont.truetype("ARCADECLASSIC.ttf", 90)
    level_num = "0" + str(level) if level < 10 else str(level)
    level_length = draw.textlength(level_num, font)
    level_position = (110, 0) 
    draw.text(level_position, level_num, font=level_font, fill=(255, 255, 255, 255))

    counter_label = f"{bit_count if bit_remainder == 0 else bit_remainder}"
    counter_length = draw.textlength(counter_label, font)
    counter_position = (image.width - counter_length, 19)  
    draw.text(counter_position, counter_label, font=font, fill=(255, 255, 255, 255))

    goal_name = "CHEER METER"
    goal_name_length = draw.textlength(goal_name, font)
    goal_name_position = ((image.width - goal_name_length) // 2, 200)
    draw.text(goal_name_position, goal_name, font=font, fill=(255, 255, 255, 255))

    for i in range(5):
        left_heart = create_static_heart(heart_size, (0, 0, 0, 200), is_left_half=True)
        right_heart = create_static_heart(heart_size, (0, 0, 0, 200), is_left_half=False)

        left_heart_resized = left_heart.resize((48, 80))
        right_heart_resized = right_heart.resize((48, 80))

        image.paste(left_heart_resized, ((i * 130) + 12, 105), mask=left_heart_resized)
        image.paste(right_heart_resized, ((i * 130) + 60, 105), mask=right_heart_resized)

    frames = []
    for frame_num in range(30):
        frame = image.copy()
        frame_draw = ImageDraw.Draw(frame)

        if half_heart_count > 1:
            for i in range(5 if full_level == 1 else half_heart_count // 2):
                left_heart = create_pixel_heart(heart_size, (255, 255, 255, 255), is_left_half=True)
                right_heart = create_pixel_heart(heart_size, (255, 255, 255, 255), is_left_half=False)

                # if full_heart == 1:
                if (0 <= frame_num < 15):
                    left_heart_resized = left_heart.resize((48, 80))
                    right_heart_resized = right_heart.resize((48, 80))

                    frame.paste(left_heart_resized, ((i * 130) + 12, 105))
                    frame.paste(right_heart_resized, ((i * 130) + 60, 105))
                elif 15 <= frame_num < 30:
                    frame.paste(left_heart, (i * 130, 95))
                    frame.paste(right_heart, ((i * 130) + 60, 95))
                # else:
                #     left_heart_resized = left_heart.resize((48, 80))
                #     right_heart_resized = right_heart.resize((48, 80))
                #     frame.paste(left_heart_resized, ((i * 130) + 12, 105))
                #     frame.paste(right_heart_resized, ((i * 130) + 60, 105))

            if half_heart_count % 2 == 1:
                # If there's an odd number of half-hearts, display an additional left-side heart
                additional_left_heart = create_pixel_heart(heart_size, (255, 255, 255, 255), is_left_half=True)
                add_left_heart_resized = additional_left_heart.resize((48, 80))
                frame.paste(add_left_heart_resized, ((i * 130) + 12 + 130, 105))
        elif bit_count < 100:
            pass
        else:
                if full_level == 1 or bit_remainder < 100:
                    for i in range(5):
                        left_heart = create_pixel_heart(heart_size, (255, 255, 255, 255), is_left_half=True)
                        right_heart = create_pixel_heart(heart_size, (255, 255, 255, 255), is_left_half=False)

                        if (0 <= frame_num < 15):
                            left_heart_resized = left_heart.resize((48, 80))
                            right_heart_resized = right_heart.resize((48, 80))

                            frame.paste(left_heart_resized, ((i * 130) + 12, 105))
                            frame.paste(right_heart_resized, ((i * 130) + 60, 105))
                        elif 15 <= frame_num < 30:
                            frame.paste(left_heart, (i * 130, 95))
                            frame.paste(right_heart, ((i * 130) + 60, 95))
                else:
                    left_heart = create_pixel_heart((60, 100), (255, 255, 255, 255), is_left_half=True)
                    left_heart_resized = left_heart.resize((48, 80))
                    frame.paste(left_heart_resized, (12, 105))

        frames.append(frame)


    # Save the image as a GIF
    frames[0].save("bit_meter.gif", save_all=True, append_images=frames[1:], duration=100, loop=0)

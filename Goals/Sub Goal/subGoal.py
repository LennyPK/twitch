import os
from PIL import Image, ImageDraw, ImageFont

sub_count = os.environ.get('SUBCOUNT')

progress = int(sub_count) % 10 * 2
if int(sub_count) % 10 == 0:
    progress = 20
else:
    progress = int(sub_count) % 10 * 2

# Set image properties
box_size = 20
num_boxes = 20
spacer_size = 6
padding = 10
border_size_outer = 4

# Calculate total height including spaces and padding
total_height = num_boxes * box_size + (num_boxes - 1) * spacer_size + 2 * padding
total_width = box_size + 4 * padding

# Create a new GIF image with a white background
image = Image.new("RGBA", (total_width + 50, total_height + 100), color=(255, 255, 255, 0))
draw = ImageDraw.Draw(image)

# Draw the outer white border
draw.line([(58, 0), (total_width + 40, 0)], fill="white", width=border_size_outer)  # Top
draw.line([(total_width + 46, 8), (total_width + 46, total_height - 8)], fill="white", width=border_size_outer)  # Right
draw.line([(58, total_height-2), (total_width + 40, total_height-2)], fill="white", width=border_size_outer)  # Bottom
draw.line([(50, 8), (50, total_height - 8)], fill="white", width=border_size_outer)  # Left


# Create frames for loading animation
frames = []
for frame_num in range(30):
    frame = image.copy()
    frame_draw = ImageDraw.Draw(frame)

    for i in range(num_boxes):
        if int(sub_count) > 0:
            if i == progress - 1:
                if frame_num >= 0 and frame_num <= 14:
                    color = (255, 255, 255, 0)
                elif frame_num >= 15 and frame_num <= 29:
                    color = (255, 255, 255, 255)
            elif i > progress - 1:
                color = (255, 255, 255, 0)
            else:
                color = (255, 255, 255, 255)

            box_y = total_height - (i + 1) * (box_size + spacer_size) - border_size_outer
            box_rect = [padding + 50,  
                        box_y,
                        total_width - 1 - padding + 48,  
                        box_y + box_size - 1]
            
            if i == progress - 1:
                top_box_y = box_y
                top_box_x = padding + 50

            frame_draw.rectangle(box_rect, fill=color)
        else:
            pass

    # Add LVL # text
    font = ImageFont.truetype("ARCADECLASSIC.ttf", 30)
    L_label = f"L"
    L_length = frame_draw.textlength(L_label, font)
    L_position = ((total_width - L_length) // 2 + 33, total_height)  
    frame_draw.text(L_position, L_label, font=font, fill=(255, 255, 255, 255))

    V_label = f"V"
    V_length = frame_draw.textlength(V_label, font)
    V_position = ((total_width - V_length) // 2 + 30, total_height + 20)  
    frame_draw.text(V_position, V_label, font=font, fill=(255, 255, 255, 255))

    L2_label = f"L"
    L2_length = frame_draw.textlength(L2_label, font)
    L2_position = ((total_width - L2_length) // 2 + 33, total_height + 40)  
    frame_draw.text(L2_position, L2_label, font=font, fill=(255, 255, 255, 255))

    level_font = ImageFont.truetype("ARCADECLASSIC.ttf", 60)
    level_num = f"{int(sub_count)//10}"
    level_length = frame_draw.textlength(level_num, font)
    level_position = ((total_width - level_length) // 2 + 55, total_height + 5)  
    frame_draw.text(level_position, level_num, font=level_font, fill=(255, 255, 255, 255))

    label_font = ImageFont.truetype("ARCADECLASSIC.ttf", 35)
    zero_label = "0"
    zero_length = frame_draw.textlength(zero_label, font)
    zero_position = (27, total_height - 37)  
    frame_draw.text(zero_position, zero_label, font=label_font, fill=(255, 255, 255, 255))

    ten_label = "10"
    ten_length = frame_draw.textlength(ten_label, font)
    ten_position = (8, 0)  
    frame_draw.text(ten_position, ten_label, font=label_font, fill=(255, 255, 255, 255))

    # Current sub number
    if int(sub_count) % 10 != 0:
        label_font = ImageFont.truetype("ARCADECLASSIC.ttf", 35)
        curr_prog = f"{int(sub_count) % 10}"
        curr_prog_length = frame_draw.textlength(curr_prog, label_font)
        curr_prog_position = (top_box_x + 10, top_box_y - 2*box_size + padding)  
        frame_draw.text(curr_prog_position, curr_prog, font=label_font, fill=(255, 255, 255, 255))

    goal_name = "SUB METER"
    goal_name_length = frame_draw.textlength(goal_name, font)
    goal_name_position = (0, total_height // 2)
    name_height = int((total_height - goal_name_length) // 2) - 20

    # frame_draw.text(goal_name_position, goal_name, font=label_font, fill=(255, 255, 255, 255))
    # Create a transparent image to draw the rotated text
    rotated_image = Image.new("RGBA", (200, 200), (0, 0, 0, 0))
    rotated_draw = ImageDraw.Draw(rotated_image)

    # Rotate the text and draw it on the new image
    rotated_draw.text((20, 15), goal_name, font=label_font, fill=(255, 255, 255, 255))
    rotated_image = rotated_image.rotate(90, expand=True)

    # Paste the rotated text onto the original image
    frame.paste(rotated_image, (0, name_height), rotated_image)

    frames.append(frame)

# Save the GIF
frames[0].save("sub_goal.gif", save_all=True, append_images=frames[1:], duration=100, loop=0)

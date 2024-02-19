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
total_width = num_boxes * box_size + (num_boxes - 1) * spacer_size + 2 * padding
total_height = box_size + 4 * padding

# Create a new GIF image with a white background
image = Image.new("RGBA", (total_width + 80, total_height + 100), color=(255, 255, 255, 0))
draw = ImageDraw.Draw(image)

# Draw the outer white border
draw.line([(38, 90), (total_width + 20, 90)], fill="white", width=border_size_outer)  # Top
draw.line([(total_width + 26, 8+90), (total_width + 26, total_height - 8+90)], fill="white", width=border_size_outer)  # Right
draw.line([(38, total_height-2+90), (total_width + 20, total_height-2+90)], fill="white", width=border_size_outer)  # Bottom
draw.line([(30, 8+90), (30, total_height - 8+90)], fill="white", width=border_size_outer)  # Left

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

            box_x = i * (box_size + spacer_size) + border_size_outer
            box_rect = [box_x + 35,
                        padding + 90,
                        box_x + box_size - 1 + 35,
                        total_height - padding + 90]
            
            if i == progress - 1:
                top_box_x = box_x + 35 + box_size
                top_box_y = padding + 90

            frame_draw.rectangle(box_rect, fill=color)
        else:
            pass

    # Add LVL # text
    font = ImageFont.truetype("ARCADECLASSIC.ttf", 35)
    L_label = f"LVL"
    L_length = frame_draw.textlength(L_label, font)
    L_position = ((total_width - L_length) - 20, 55)  
    frame_draw.text(L_position, L_label, font=font, fill=(255, 255, 255, 255))

    level_font = ImageFont.truetype("ARCADECLASSIC.ttf", 60)
    level_num = f"{int(sub_count)//10}"
    level_length = frame_draw.textlength(level_num, font)
    level_position = ((total_width - level_length), 37)  
    frame_draw.text(level_position, level_num, font=level_font, fill=(255, 255, 255, 255))

    zero_label = "0"
    zero_length = frame_draw.textlength(zero_label, font)
    zero_position = (5, (2*border_size_outer+box_size)//2 + 90)  
    frame_draw.text(zero_position, zero_label, font=font, fill=(255, 255, 255, 255))

    ten_label = "10"
    ten_length = frame_draw.textlength(ten_label, font)
    ten_position = (total_width + 35, (2*border_size_outer+box_size)//2 + 90) 
    frame_draw.text(ten_position, ten_label, font=font, fill=(255, 255, 255, 255))

    # Current sub number
    if int(sub_count) % 10 != 0:
        curr_prog = f"{int(sub_count) % 10}"
        curr_prog_length = frame_draw.textlength(curr_prog, font)
        curr_prog_position = (top_box_x + 10, top_box_y)  
        frame_draw.text(curr_prog_position, curr_prog, font=font, fill=(255, 255, 255, 255))

    goal_name = "SUB METER"
    goal_name_length = frame_draw.textlength(goal_name, font)
    goal_name_position = (30, 55)
    frame_draw.text(goal_name_position, goal_name, font=font, fill=(255, 255, 255, 255))

    frames.append(frame)

# Save the GIF
frames[0].save("sub_goal_horizontal.gif", save_all=True, append_images=frames[1:], duration=100, loop=0)

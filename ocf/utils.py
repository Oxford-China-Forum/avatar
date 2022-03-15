import uuid
import random
import textwrap
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

from ocf.constants import AVATAR_OUTPUT_MAX_SIZE, AVATAR_OUTPUT_DIR, TICKET_BASE_IMAGE, TICKET_OUTPUT_DIR, IMAGE_OUTPUT_QUALITY, TICKET_MAJORS, TICKET_COLLEGES, TICKET_OCCUPATION, TICKET_LOCATIONS, TICKET_TOPICS, TICKET_TEXT


def superimpose_images(base_path: str, overlay_path: str) -> Path:
    base_im = Image.open(base_path)
    overlay_im = Image.open(overlay_path)

    # Calculate new size and position to paste the image
    sidelength = min(max(base_im.size), AVATAR_OUTPUT_MAX_SIZE)
    base_new_size = [sidelength, sidelength]
    if base_im.size[0] > base_im.size[1]:
        base_new_size[1] = round(base_im.size[1] * (sidelength / base_im.size[0]))
    elif base_im.size[0] < base_im.size[1]:
        base_new_size[0] = round(base_im.size[0] * (sidelength / base_im.size[1]))
    paste_pos = ((sidelength - base_new_size[0]) // 2, (sidelength - base_new_size[1]) // 2)

    # Resize the images
    base_im = base_im.resize(base_new_size, Image.ANTIALIAS)
    overlay_im = overlay_im.resize((sidelength, sidelength), Image.ANTIALIAS)
    
    bg_im = Image.new('RGB', (sidelength, sidelength), (255, 255, 255))
    bg_im.paste(base_im, paste_pos)
    bg_im.paste(overlay_im, (0, 0), overlay_im)
    filename = f'{uuid.uuid1()}.jpg'
    bg_im.save((AVATAR_OUTPUT_DIR / filename).as_posix(), 'jpeg', quality=IMAGE_OUTPUT_QUALITY, progressive=True)

    return filename


def generate_ticket(name, ticket_id):
    major = random.choice(TICKET_MAJORS)
    college = random.choice(TICKET_COLLEGES)
    occupation = random.choice(TICKET_OCCUPATION)
    location = random.choice(TICKET_LOCATIONS)
    topic = random.choice(TICKET_TOPICS)
    
    ticket_im = Image.open(TICKET_BASE_IMAGE.as_posix())
    body_font = ImageFont.truetype(font='assets/FZFWZhuZiAYuanJWD.TTF', size=28)
    title_font = ImageFont.truetype(font='assets/FZFWZhuZiAYuanJWB.TTF', size=52)
    draw = ImageDraw.Draw(im=ticket_im)

    # Draw ticket ID and name
    draw.text((80, 780), text=ticket_id, font=title_font, fill='black')
    draw.text((390, 780), text=name, font=title_font, fill='black')

    # Draw body text
    margin = 80
    x_offset = margin
    y_offset = 896
    width = 690
    line_height = body_font.getsize('H')[1] * 1.35
    avoid_head_chars = ('。', '，', '”', ' ')
    
    curr_len = 0
    for snippet in TICKET_TEXT:
        line = snippet['text'].format(major=major, occupation=occupation, location=location, topic=topic, **college)
        for char in line:
            char_len = body_font.getlength(char)
            if char == '\n' or (curr_len + char_len > width and char not in avoid_head_chars):
                # Simulate line break
                if x_offset == margin: # double line break
                    y_offset += line_height * 0.6
                else:
                    x_offset = margin
                    y_offset += line_height
                    curr_len = 0
            if char != '\n':
                # Draw single character
                draw.text((x_offset, y_offset), text=char, font=body_font, fill=snippet['color'])
                x_offset += char_len
                curr_len += char_len

    # Save the image
    filename = f'{uuid.uuid1()}.jpg'
    ticket_im.save((TICKET_OUTPUT_DIR / filename).as_posix(), 'jpeg', quality=IMAGE_OUTPUT_QUALITY, progressive=True)

    return filename


def generate_ticket_old(name, ticket_id):
    major = random.choice(TICKET_MAJORS)
    college = random.choice(TICKET_COLLEGES)
    occupation = random.choice(TICKET_OCCUPATION)
    location = random.choice(TICKET_LOCATIONS)
    topic = random.choice(TICKET_TOPICS)
    random_text = TICKET_TEXT.format(major=major, occupation=occupation, location=location, topic=topic, **college)
    
    ticket_im = Image.open(TICKET_BASE_IMAGE.as_posix())
    body_font = ImageFont.truetype(font='assets/FZFWZhuZiAYuanJWD.TTF', size=32)
    title_font = ImageFont.truetype(font='assets/FZFWZhuZiAYuanJWB.TTF', size=58)
    draw = ImageDraw.Draw(im=ticket_im)

    margin = 50
    offset = 539
    width = 2800
    # for line in textwrap.wrap(random_text, width=width):
    #     draw.text((margin, offset), text=line, font=body_font, fill='black')
    #     offset += body_font.getsize(line)[1] * 1.4
    draw.multiline_text((margin, offset), text=random_text, font=body_font, fill='black', spacing=12)
    
    draw.text((50, 416), text=name, font=title_font, fill='black')
    draw.text((500, 416), text=ticket_id, font=title_font, fill='black')
    
    filename = f'{uuid.uuid1()}.jpg'
    ticket_im.save((TICKET_OUTPUT_DIR / filename).as_posix(), 'jpeg', quality=IMAGE_OUTPUT_QUALITY, progressive=True)

    return filename


def generate_ticket_old_old(name, ticket_id):
    ticket_im = Image.open(TICKET_BASE_IMAGE.as_posix())
    font = ImageFont.truetype(font='assets/FZFWZhuZiAYuanJWB.TTF', size=58)
    draw = ImageDraw.Draw(im=ticket_im)
    draw.text(xy=(100, 1086), text=name, font=font, fill='black')
    draw.text(xy=(100, 1235), text=ticket_id, font=font, fill='black')
    filename = f'{uuid.uuid1()}.jpg'
    ticket_im.save((TICKET_OUTPUT_DIR / filename).as_posix(), 'jpeg', quality=IMAGE_OUTPUT_QUALITY, progressive=True)

    return filename

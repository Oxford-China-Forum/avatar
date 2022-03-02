from tkinter.tix import IMAGE
import uuid
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

from ocf.constants import AVATAR_OUTPUT_MAX_SIZE, AVATAR_OUTPUT_DIR, TICKET_BASE_IMAGE, TICKET_OUTPUT_DIR, IMAGE_OUTPUT_QUALITY


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
    ticket_im = Image.open(TICKET_BASE_IMAGE.as_posix())
    font = ImageFont.truetype(font='assets/FZFWZhuZiAYuanJWB.TTF', size=58)
    draw = ImageDraw.Draw(im=ticket_im)
    draw.text(xy=(100, 1086), text=name, font=font, fill='black')
    draw.text(xy=(100, 1235), text=ticket_id, font=font, fill='black')
    filename = f'{uuid.uuid1()}.jpg'
    ticket_im.save((TICKET_OUTPUT_DIR / filename).as_posix(), 'jpeg', quality=IMAGE_OUTPUT_QUALITY, progressive=True)

    return filename

from pathlib import Path

IMAGE_OUTPUT_QUALITY = 90

OUTPUT_DIR = Path('ocf/static/')

AVATAR_OUTPUT_MAX_SIZE = 1200
AVATAR_OUTPUT_DIR = OUTPUT_DIR / 'avatars/'
AVATAR_ALLOWED_FORMATS = ('jpg', 'jpeg', 'png', 'gif')
AVATAR_OVERLAY_IMAGE = Path('assets/overlay.png')

TICKET_OUTPUT_DIR = OUTPUT_DIR / 'tickets/'
TICKET_BASE_IMAGE = Path('assets/ticket.png')
TICKET_ID_DIGITS = 7

# Create necessary directories
AVATAR_OUTPUT_DIR.mkdir(exist_ok=True, parents=True)
TICKET_OUTPUT_DIR.mkdir(exist_ok=True, parents=True)

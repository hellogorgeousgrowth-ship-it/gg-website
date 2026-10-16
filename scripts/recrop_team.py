import os
from PIL import Image

CANVA_DIR = r"c:\Users\Rapto\.gemini\antigravity-ide\scratch\gg-website\Gorgeous Growth"
SITE_IMG_DIR = r"c:\Users\Rapto\.gemini\antigravity-ide\scratch\gg-website\images\site_images"
CANVA_ASSETS_DIR = r"c:\Users\Rapto\.gemini\antigravity-ide\scratch\gg-website\images\canva_assets"

im = Image.open(os.path.join(CANVA_DIR, "ABOUT.png"))

# Coordinates for the 4 team photos in ABOUT.png (1366 x 13660):
# In ABOUT.png:
# Member 1 (Nico): x: 108 to 468, y: 4620 to 5060
# Member 2 (Sonal): x: 108 to 468, y: 5210 to 5650
# Member 3 (Mary): x: 108 to 468, y: 5800 to 6240
# Member 4 (Lisa): x: 108 to 468, y: 6390 to 6830

crops = [
    ("team-nicole-silva.jpg", (108, 4620, 468, 5060)),
    ("team-sonal-matta.jpg", (108, 5210, 468, 5650)),
    ("team-mary-scott.jpg", (108, 5800, 468, 6240)),
    ("team-lisa-tshuma.jpg", (108, 6390, 468, 6830)),
]

for name, box in crops:
    c = im.crop(box)
    c.save(os.path.join(CANVA_ASSETS_DIR, name), quality=95)
    print(f"Saved to canva_assets: {name} ({c.size})")

print("Team photos extracted!")

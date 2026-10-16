import os
from PIL import Image

CANVA_DIR = r"c:\Users\Rapto\.gemini\antigravity-ide\scratch\gg-website\Gorgeous Growth"
MEMBERS_DIR = r"c:\Users\Rapto\.gemini\antigravity-ide\scratch\gg-website\images\canva_assets\members"

im = Image.open(os.path.join(CANVA_DIR, "NETWORK.png"))
w, h = im.size
print("NETWORK size:", w, h)

# Let's inspect the exact card boxes:
# In NETWORK.png (1366 x 8195):
# Card width is about 236px, card height is about 485px (photo ~395px, label ~90px)
# 5 columns:
# c0: 45 to 282
# c1: 300 to 537
# c2: 556 to 793
# c3: 812 to 1049
# c4: 1068 to 1305

# 4 rows:
# r0: 2980 to 3465 (photo: 2980 to 3375)
# r1: 3505 to 3990 (photo: 3505 to 3900)
# r2: 4030 to 4515 (photo: 4030 to 4425)
# r3: 4555 to 5040 (photo: 4555 to 4950)

# Let's crop the FULL card (including the photo and label directly) or crop the photo portion only:
# Let's crop the exact photo portion:

col_coords = [
    (45, 282),
    (300, 537),
    (556, 793),
    (812, 1049),
    (1068, 1305)
]

row_photo_coords = [
    (2980, 3375),
    (3505, 3900),
    (4030, 4425),
    (4555, 4950)
]

members_grid = [
    [
        {"id": "olivia-gonzalez", "name": "Olivia Gonzalez", "tag": "Sales Consultant"},
        {"id": "plina", "name": "Sarah & Natalie", "tag": "PLINA"},
        {"id": "autumn-hxze", "name": "Autumn Hxze", "tag": "AutumnHxzePhoto"},
        {"id": "alejandra-llines", "name": "Alejandra Llines", "tag": "Social Media Manager"},
        {"id": "shanjali-arul", "name": "Shanjali Arul", "tag": "Chi Meadow Collective"},
    ],
    [
        {"id": "thomas-kneifel", "name": "Thomas Kneifel", "tag": "Thomas K Jewlery"},
        {"id": "hannah-andrews", "name": "Hannah Andrews", "tag": "HXAPhotography"},
        {"id": "sanya-gujral", "name": "Sanya Gujral", "tag": "UGC & Media Manager"},
        {"id": "ava-doherty", "name": "Ava Doherty", "tag": "Creative Assistant"},
        {"id": "taryn-hamel", "name": "Taryn Hamel", "tag": "Admin Assistant"},
    ],
    [
        {"id": "luis-chang", "name": "Luis Chang", "tag": "Luis' Funnel Design"},
        {"id": "sanjana-senthilkumar", "name": "Sanjana Senthilkumar", "tag": "Travel UGC Creator"},
        {"id": "erin-lindsay", "name": "Erin Lindsay", "tag": "Penchant Boutique"},
        {"id": "diya-sonani", "name": "Diya Sonani", "tag": "Idyia Studios"},
        {"id": "aiah-elessawy", "name": "Aiah Elessawy", "tag": "Hyde & Heal Studio"},
    ],
    [
        {"id": "monique-moguel", "name": "Monique Moguel", "tag": "TruVigil"},
        {"id": "nico-silva", "name": "Nico Silva", "tag": "Analytics Consultant"},
        {"id": "sonal-matta", "name": "Sonal Matta", "tag": "Financial Consultant"},
        {"id": "alexis-vasquez", "name": "Alexis Vasquez", "tag": "Studio Lex Chicago"},
        {"id": "joel-moore", "name": "Joel Moore", "tag": "Emi's Playhouse"},
    ]
]

for r_idx, row in enumerate(members_grid):
    y1, y2 = row_photo_coords[r_idx]
    for c_idx, m in enumerate(row):
        x1, x2 = col_coords[c_idx]
        cropped = im.crop((x1, y1, x2, y2))
        fname = f"{m['id']}.jpg"
        cropped.save(os.path.join(MEMBERS_DIR, fname), quality=95)
        print(f"Saved: {fname} ({cropped.size})")

print("Cropped with perfect precision!")

import os
from PIL import Image, ImageDraw, ImageFont

OUT_DIR = r"c:\Users\Rapto\.gemini\antigravity-ide\scratch\gg-website\images\player_cards"
os.makedirs(OUT_DIR, exist_ok=True)

FONTS_DIR = os.path.join(os.environ.get('WINDIR', 'C:\\Windows'), 'Fonts')
font_bold_large = ImageFont.truetype(os.path.join(FONTS_DIR, 'arialbd.ttf'), 54)
font_title = ImageFont.truetype(os.path.join(FONTS_DIR, 'georgiab.ttf'), 20)
font_sub = ImageFont.truetype(os.path.join(FONTS_DIR, 'arialbd.ttf'), 13)
font_small = ImageFont.truetype(os.path.join(FONTS_DIR, 'arial.ttf'), 12)
font_brand = ImageFont.truetype(os.path.join(FONTS_DIR, 'georgiab.ttf'), 14)

CARDS = [
    {"letter": "A", "code": "card-a", "name": "Olivia Gonzalez", "role": "Sales Consultant"},
    {"letter": "B", "code": "card-b", "name": "Sarah & Natalie", "role": "PLINA Wellness"},
    {"letter": "C", "code": "card-c", "name": "Autumn Hxze", "role": "AutumnHxzePhoto"},
    {"letter": "D", "code": "card-d", "name": "Alejandra Llines", "role": "Social Media Manager"},
    {"letter": "E", "code": "card-e", "name": "Shanjali Arul", "role": "Chi Meadow Collective"},
    {"letter": "F", "code": "card-f", "name": "Thomas Kneifel", "role": "Thomas K Jewlery"},
    {"letter": "G", "code": "card-g", "name": "Hannah Andrews", "role": "HXAPhotography"},
    {"letter": "H", "code": "card-h", "name": "Sanya Gujral", "role": "UGC & Media Manager"},
    {"letter": "I", "code": "card-i", "name": "Ava Doherty", "role": "Creative Assistant"},
    {"letter": "J", "code": "card-j", "name": "Taryn Hamel", "role": "Admin Assistant"},
    {"letter": "K", "code": "card-k", "name": "Luis Chang", "role": "Luis' Funnel Design"},
    {"letter": "L", "code": "card-l", "name": "Sanjana Senthilkumar", "role": "Travel UGC Creator"},
    {"letter": "M", "code": "card-m", "name": "Erin Lindsay", "role": "Penchant Boutique"},
    {"letter": "N", "code": "card-n", "name": "Diya Sonani", "role": "IdYia Studios"},
    {"letter": "O", "code": "card-o", "name": "Aiah Elessawy", "role": "Hyde & Heal Studio"},
    {"letter": "P", "code": "card-p", "name": "Monique Moguel", "role": "TruVigil Solutions"},
    {"letter": "Q", "code": "card-q", "name": "Nico Silva", "role": "Analytics Consultant"},
    {"letter": "R", "code": "card-r", "name": "Sonal Matta", "role": "Financial Consultant"},
    {"letter": "S", "code": "card-s", "name": "Alexis Vasquez", "role": "Studio Lex Chicago"},
    {"letter": "T", "code": "card-t", "name": "Joel Moore", "role": "Emi's Playhouse"},
    {"letter": "U", "code": "card-u", "name": "SoulTree", "role": "Film Production Space"},
    {"letter": "V", "code": "card-v", "name": "Kris O", "role": "Creative Entrepreneur"},
    {"letter": "W", "code": "card-w", "name": "Lei PJ (@relei_doe)", "role": "Flight Attendant & Creator"}
]

def hex_to_rgb(hex_str):
    hex_str = hex_str.lstrip('#')
    return tuple(int(hex_str[i:i+2], 16) for i in (0, 2, 4))

w, h = 400, 500

for c in CARDS:
    im = Image.new("RGB", (w, h), hex_to_rgb("#1B2E20"))
    draw = ImageDraw.Draw(im)

    # Double Gold Border
    draw.rectangle([10, 10, w - 11, h - 11], outline=hex_to_rgb("#D4AF37"), width=2)
    draw.rectangle([16, 16, w - 17, h - 17], outline=hex_to_rgb("#D4AF37"), width=1)

    center_x = w // 2

    # Top Brand Header
    draw.text((center_x, 40), "GORGEOUS GROWTH", fill=hex_to_rgb("#D4AF37"), font=font_brand, anchor="mm")
    draw.text((center_x, 60), "COMMUNITY MEMBER PLACEHOLDER", fill=hex_to_rgb("#FDFBF7"), font=font_sub, anchor="mm")

    # Center Badge Frame for Huge Card Letter
    bx1, by1 = 35, 95
    bx2, by2 = 365, 385
    draw.rectangle([bx1, by1, bx2, by2], fill=hex_to_rgb("#233D2A"), outline=hex_to_rgb("#D4AF37"), width=2)

    # Big Prominent Card Letter Box
    lx1, ly1 = 70, 115
    lx2, ly2 = 330, 215
    draw.rectangle([lx1, ly1, lx2, ly2], fill=hex_to_rgb("#BA552A"), outline=hex_to_rgb("#D4AF37"), width=2)
    draw.text((center_x, 165), f"CARD {c['letter']}", fill=hex_to_rgb("#FFFFFF"), font=font_bold_large, anchor="mm")
    
    # Member Name
    draw.text((center_x, 248), c["name"], fill=hex_to_rgb("#FDFBF7"), font=font_title, anchor="mm")
    
    # Member Role
    draw.text((center_x, 280), c["role"].upper(), fill=hex_to_rgb("#D4AF37"), font=font_sub, anchor="mm")

    # Replacement Dimensions & File Instructions Box
    draw.rectangle([50, 315, 350, 365], fill=hex_to_rgb("#1B2E20"), outline=hex_to_rgb("#D4AF37"), width=1)
    draw.text((center_x, 330), "REPLACE WITH (400 x 500 px):", fill=hex_to_rgb("#D4AF37"), font=font_sub, anchor="mm")
    draw.text((center_x, 348), f"images/player_cards/{c['code']}.png", fill=hex_to_rgb("#FDFBF7"), font=font_small, anchor="mm")

    # Footer note
    draw.text((center_x, 435), "Drop photo with matching filename into repo", fill=hex_to_rgb("#D4AF37"), font=font_small, anchor="mm")

    out_path = os.path.join(OUT_DIR, f"{c['code']}.png")
    im.save(out_path, quality=95)
    print(f"Generated {c['code']}.png with large letter font")

print(f"All 20 placeholder images generated with large letter font in {OUT_DIR}!")

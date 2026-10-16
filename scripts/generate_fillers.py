import os
from PIL import Image, ImageDraw, ImageFont

OUT_DIR = r"c:\Users\Rapto\.gemini\antigravity-ide\scratch\gg-website\images\site_images"
os.makedirs(OUT_DIR, exist_ok=True)

# Define all image slots
IMAGE_SLOTS = [
    # HOME
    {"code": "image-a", "label": "IMAGE A", "desc": "Home Hero Photo Divider (1366x700)", "w": 1366, "h": 700, "bg": "#0F1B03", "fg": "#FFF7EC", "accent": "#D4AF37"},
    {"code": "image-b", "label": "IMAGE B", "desc": "Method: Knowledge Photo (310x330)", "w": 310, "h": 330, "bg": "#FFF7EC", "fg": "#0F1B03", "accent": "#A8451B"},
    {"code": "image-c", "label": "IMAGE C", "desc": "Method: Toolkits Photo (310x330)", "w": 310, "h": 330, "bg": "#FFF7EC", "fg": "#0F1B03", "accent": "#A8451B"},
    {"code": "image-d", "label": "IMAGE D", "desc": "Method: Network Photo (310x330)", "w": 310, "h": 330, "bg": "#FFF7EC", "fg": "#0F1B03", "accent": "#A8451B"},
    {"code": "image-e", "label": "IMAGE E", "desc": "Home Team Meeting Divider (1366x350)", "w": 1366, "h": 350, "bg": "#0F1B03", "fg": "#FFF7EC", "accent": "#D4AF37"},
    {"code": "image-f", "label": "IMAGE F", "desc": "Internship Phone Mockup (355x700)", "w": 355, "h": 700, "bg": "#BA552A", "fg": "#FFF7EC", "accent": "#FFF7EC"},
    {"code": "image-g", "label": "IMAGE G", "desc": "Strategy Split: Woman in Red Blouse (666x750)", "w": 666, "h": 750, "bg": "#0F1B03", "fg": "#FFF7EC", "accent": "#D4AF37"},
    {"code": "image-h", "label": "IMAGE H", "desc": "Tools Split: Monitor Mockup (700x850)", "w": 700, "h": 850, "bg": "#0F1B03", "fg": "#FFF7EC", "accent": "#D4AF37"},
    {"code": "image-i", "label": "IMAGE I", "desc": "Growing: Internship Applications (305x320)", "w": 305, "h": 320, "bg": "#FFF7EC", "fg": "#0F1B03", "accent": "#A8451B"},
    {"code": "image-j", "label": "IMAGE J", "desc": "Growing: Builder's Dinner Chicago (305x320)", "w": 305, "h": 320, "bg": "#FFF7EC", "fg": "#0F1B03", "accent": "#A8451B"},
    {"code": "image-k", "label": "IMAGE K", "desc": "Growing: Online Afterhours Session (305x320)", "w": 305, "h": 320, "bg": "#FFF7EC", "fg": "#0F1B03", "accent": "#A8451B"},
    {"code": "image-l", "label": "IMAGE L", "desc": "Growing: New Gorgeous Merch (305x320)", "w": 305, "h": 320, "bg": "#FFF7EC", "fg": "#0F1B03", "accent": "#A8451B"},
    {"code": "image-m", "label": "IMAGE M", "desc": "Instagram 10-Post Feed (1200x550)", "w": 1200, "h": 550, "bg": "#0F1B03", "fg": "#FFF7EC", "accent": "#D4AF37"},

    # ABOUT
    {"code": "image-n", "label": "IMAGE N", "desc": "About: Workshop Divider (1366x700)", "w": 1366, "h": 700, "bg": "#0F1B03", "fg": "#FFF7EC", "accent": "#D4AF37"},
    {"code": "image-o", "label": "IMAGE O", "desc": "About: Our Mission Side Photo (546x920)", "w": 546, "h": 920, "bg": "#BA552A", "fg": "#FFF7EC", "accent": "#FFF7EC"},
    {"code": "image-p", "label": "IMAGE P", "desc": "About: Foundational Roots Photo (420x900)", "w": 420, "h": 900, "bg": "#0F1B03", "fg": "#FFF7EC", "accent": "#D4AF37"},
    {"code": "image-q", "label": "IMAGE Q", "desc": "Founder Portrait: Shay Gorgie (570x1150)", "w": 570, "h": 1150, "bg": "#FFF7EC", "fg": "#0F1B03", "accent": "#A8451B"},
    {"code": "image-r", "label": "IMAGE R", "desc": "Team: Nicole Silva Portrait (375x470)", "w": 375, "h": 470, "bg": "#FFF7EC", "fg": "#0F1B03", "accent": "#A8451B"},
    {"code": "image-s", "label": "IMAGE S", "desc": "Team: Sonal Matta Portrait (375x450)", "w": 375, "h": 450, "bg": "#FFF7EC", "fg": "#0F1B03", "accent": "#A8451B"},
    {"code": "image-t", "label": "IMAGE T", "desc": "Team: Mary Scott Portrait (375x460)", "w": 375, "h": 460, "bg": "#FFF7EC", "fg": "#0F1B03", "accent": "#A8451B"},
    {"code": "image-u", "label": "IMAGE U", "desc": "Team: Lisa Tshuma Portrait (375x450)", "w": 375, "h": 450, "bg": "#FFF7EC", "fg": "#0F1B03", "accent": "#A8451B"},
    {"code": "image-v", "label": "IMAGE V", "desc": "About: Story 4-Photo Quad Strip (1366x300)", "w": 1366, "h": 300, "bg": "#0F1B03", "fg": "#FFF7EC", "accent": "#D4AF37"},
    {"code": "image-w", "label": "IMAGE W", "desc": "Client Logo: Chi Meadow Collective (380x200)", "w": 380, "h": 200, "bg": "#FFF7EC", "fg": "#0F1B03", "accent": "#A8451B"},
    {"code": "image-x", "label": "IMAGE X", "desc": "Client Logo: PLINA (400x200)", "w": 400, "h": 200, "bg": "#FFF7EC", "fg": "#0F1B03", "accent": "#A8451B"},
    {"code": "image-y", "label": "IMAGE Y", "desc": "Client Photo: Travel Content Creator (410x200)", "w": 410, "h": 200, "bg": "#FFF7EC", "fg": "#0F1B03", "accent": "#A8451B"},

    # KNOWLEDGE
    {"code": "image-z", "label": "IMAGE Z", "desc": "Knowledge Hero Workspace Banner (1366x700)", "w": 1366, "h": 700, "bg": "#0F1B03", "fg": "#FFF7EC", "accent": "#D4AF37"},
    {"code": "image-aa", "label": "IMAGE AA", "desc": "Event Planning: Crowd Photo (670x700)", "w": 670, "h": 700, "bg": "#FFF7EC", "fg": "#0F1B03", "accent": "#A8451B"},
    {"code": "image-ab", "label": "IMAGE AB", "desc": "Event Planning: Polaroid Stationery (635x450)", "w": 635, "h": 450, "bg": "#FFF7EC", "fg": "#0F1B03", "accent": "#A8451B"},
    {"code": "image-ac", "label": "IMAGE AC", "desc": "Event Planning: 8-Grid Photo Collage (1366x800)", "w": 1366, "h": 800, "bg": "#FFF7EC", "fg": "#0F1B03", "accent": "#A8451B"},
    {"code": "image-ad", "label": "IMAGE AD", "desc": "Growth Report Mockup 1 (390x750)", "w": 390, "h": 750, "bg": "#BA552A", "fg": "#FFF7EC", "accent": "#FFF7EC"},
    {"code": "image-ae", "label": "IMAGE AE", "desc": "Growth Report Mockup 2 (395x750)", "w": 395, "h": 750, "bg": "#BA552A", "fg": "#FFF7EC", "accent": "#FFF7EC"},
    {"code": "image-af", "label": "IMAGE AF", "desc": "Growth Report Mockup 3 (395x750)", "w": 395, "h": 750, "bg": "#BA552A", "fg": "#FFF7EC", "accent": "#FFF7EC"},
    {"code": "image-ag", "label": "IMAGE AG", "desc": "Creative House: Model Photo (635x750)", "w": 635, "h": 750, "bg": "#0F1B03", "fg": "#FFF7EC", "accent": "#D4AF37"},
    {"code": "image-ah", "label": "IMAGE AH", "desc": "Creative Story Mockup 1 (230x430)", "w": 230, "h": 430, "bg": "#0F1B03", "fg": "#FFF7EC", "accent": "#D4AF37"},
    {"code": "image-ai", "label": "IMAGE AI", "desc": "Creative Story Mockup 2 (230x430)", "w": 230, "h": 430, "bg": "#0F1B03", "fg": "#FFF7EC", "accent": "#D4AF37"},
    {"code": "image-aj", "label": "IMAGE AJ", "desc": "Creative Story Mockup 3 (230x430)", "w": 230, "h": 430, "bg": "#0F1B03", "fg": "#FFF7EC", "accent": "#D4AF37"},
    {"code": "image-ak", "label": "IMAGE AK", "desc": "Creative Story Mockup 4 (230x430)", "w": 230, "h": 430, "bg": "#0F1B03", "fg": "#FFF7EC", "accent": "#D4AF37"},
    {"code": "image-al", "label": "IMAGE AL", "desc": "Creative Story Mockup 5 (230x430)", "w": 230, "h": 430, "bg": "#0F1B03", "fg": "#FFF7EC", "accent": "#D4AF37"},

    # NETWORK
    {"code": "image-am", "label": "IMAGE AM", "desc": "Network Hero Banner (1366x700)", "w": 1366, "h": 700, "bg": "#0F1B03", "fg": "#FFF7EC", "accent": "#D4AF37"},
    {"code": "image-an", "label": "IMAGE AN", "desc": "Member 1: Olivia Gonzalez (237x395)", "w": 237, "h": 395, "bg": "#FFF7EC", "fg": "#0F1B03", "accent": "#A8451B"},
    {"code": "image-ao", "label": "IMAGE AO", "desc": "Member 2: Sarah & Natalie (237x395)", "w": 237, "h": 395, "bg": "#FFF7EC", "fg": "#0F1B03", "accent": "#A8451B"},
    {"code": "image-ap", "label": "IMAGE AP", "desc": "Member 3: Autumn Hxze (237x395)", "w": 237, "h": 395, "bg": "#FFF7EC", "fg": "#0F1B03", "accent": "#A8451B"},
    {"code": "image-aq", "label": "IMAGE AQ", "desc": "Member 4: Alejandra Llines (237x395)", "w": 237, "h": 395, "bg": "#FFF7EC", "fg": "#0F1B03", "accent": "#A8451B"},
    {"code": "image-ar", "label": "IMAGE AR", "desc": "Member 5: Shanjali Arul (237x395)", "w": 237, "h": 395, "bg": "#FFF7EC", "fg": "#0F1B03", "accent": "#A8451B"},
    {"code": "image-as", "label": "IMAGE AS", "desc": "Member 6: Thomas Kneifel (237x395)", "w": 237, "h": 395, "bg": "#FFF7EC", "fg": "#0F1B03", "accent": "#A8451B"},
    {"code": "image-at", "label": "IMAGE AT", "desc": "Member 7: Hannah Andrews (237x395)", "w": 237, "h": 395, "bg": "#FFF7EC", "fg": "#0F1B03", "accent": "#A8451B"},
    {"code": "image-au", "label": "IMAGE AU", "desc": "Member 8: Sanya Gujral (237x395)", "w": 237, "h": 395, "bg": "#FFF7EC", "fg": "#0F1B03", "accent": "#A8451B"},
    {"code": "image-av", "label": "IMAGE AV", "desc": "Member 9: Ava Doherty (237x395)", "w": 237, "h": 395, "bg": "#FFF7EC", "fg": "#0F1B03", "accent": "#A8451B"},
    {"code": "image-aw", "label": "IMAGE AW", "desc": "Member 10: Taryn Hamel (237x395)", "w": 237, "h": 395, "bg": "#FFF7EC", "fg": "#0F1B03", "accent": "#A8451B"},
    {"code": "image-ax", "label": "IMAGE AX", "desc": "Member 11: Luis Chang (237x395)", "w": 237, "h": 395, "bg": "#FFF7EC", "fg": "#0F1B03", "accent": "#A8451B"},
    {"code": "image-ay", "label": "IMAGE AY", "desc": "Member 12: Sanjana Senthilkumar (237x395)", "w": 237, "h": 395, "bg": "#FFF7EC", "fg": "#0F1B03", "accent": "#A8451B"},
    {"code": "image-az", "label": "IMAGE AZ", "desc": "Member 13: Erin Lindsay (237x395)", "w": 237, "h": 395, "bg": "#FFF7EC", "fg": "#0F1B03", "accent": "#A8451B"},
    {"code": "image-ba", "label": "IMAGE BA", "desc": "Member 14: Diya Sonani (237x395)", "w": 237, "h": 395, "bg": "#FFF7EC", "fg": "#0F1B03", "accent": "#A8451B"},
    {"code": "image-bb", "label": "IMAGE BB", "desc": "Member 15: Aiah Elessawy (237x395)", "w": 237, "h": 395, "bg": "#FFF7EC", "fg": "#0F1B03", "accent": "#A8451B"},
    {"code": "image-bc", "label": "IMAGE BC", "desc": "Member 16: Monique Moguel (237x395)", "w": 237, "h": 395, "bg": "#FFF7EC", "fg": "#0F1B03", "accent": "#A8451B"},
    {"code": "image-bd", "label": "IMAGE BD", "desc": "Member 17: Nico Silva (237x395)", "w": 237, "h": 395, "bg": "#FFF7EC", "fg": "#0F1B03", "accent": "#A8451B"},
    {"code": "image-be", "label": "IMAGE BE", "desc": "Member 18: Sonal Matta (237x395)", "w": 237, "h": 395, "bg": "#FFF7EC", "fg": "#0F1B03", "accent": "#A8451B"},
    {"code": "image-bf", "label": "IMAGE BF", "desc": "Member 19: Alexis Vasquez (237x395)", "w": 237, "h": 395, "bg": "#FFF7EC", "fg": "#0F1B03", "accent": "#A8451B"},
    {"code": "image-bg", "label": "IMAGE BG", "desc": "Member 20: Joel Moore (237x395)", "w": 237, "h": 395, "bg": "#FFF7EC", "fg": "#0F1B03", "accent": "#A8451B"},
    {"code": "image-bh", "label": "IMAGE BH", "desc": "Network Join Team Portrait (686x800)", "w": 686, "h": 800, "bg": "#0F1B03", "fg": "#FFF7EC", "accent": "#D4AF37"},
    {"code": "image-bi", "label": "IMAGE BI", "desc": "Green Hoodie Merch Showcase (700x800)", "w": 700, "h": 800, "bg": "#FFF7EC", "fg": "#0F1B03", "accent": "#A8451B"},
    {"code": "image-bj", "label": "IMAGE BJ", "desc": "Merchandise 6-Detail Strip (1366x250)", "w": 1366, "h": 250, "bg": "#FFF7EC", "fg": "#0F1B03", "accent": "#A8451B"},

    # TOOLKITS
    {"code": "image-bk", "label": "IMAGE BK", "desc": "Toolkits Hero Banner (1366x700)", "w": 1366, "h": 700, "bg": "#0F1B03", "fg": "#FFF7EC", "accent": "#D4AF37"},
    {"code": "image-bl", "label": "IMAGE BL", "desc": "Toolkit Box: Growth Shop (370x550)", "w": 370, "h": 550, "bg": "#FFF7EC", "fg": "#0F1B03", "accent": "#A8451B"},
    {"code": "image-bm", "label": "IMAGE BM", "desc": "Toolkit Box: Templates (370x550)", "w": 370, "h": 550, "bg": "#FFF7EC", "fg": "#0F1B03", "accent": "#A8451B"},
    {"code": "image-bn", "label": "IMAGE BN", "desc": "Toolkit Box: Planners (370x550)", "w": 370, "h": 550, "bg": "#FFF7EC", "fg": "#0F1B03", "accent": "#A8451B"},
    {"code": "image-bo", "label": "IMAGE BO", "desc": "Product 1: Monthly Content Calendar (410x370)", "w": 410, "h": 370, "bg": "#0F1B03", "fg": "#FFF7EC", "accent": "#D4AF37"},
    {"code": "image-bp", "label": "IMAGE BP", "desc": "Product 2: Ultimate Team Hub Tracker (410x370)", "w": 410, "h": 370, "bg": "#0F1B03", "fg": "#FFF7EC", "accent": "#D4AF37"},
    {"code": "image-bq", "label": "IMAGE BQ", "desc": "Product 3: Live Canva 101 Course (410x370)", "w": 410, "h": 370, "bg": "#0F1B03", "fg": "#FFF7EC", "accent": "#D4AF37"},
    {"code": "image-br", "label": "IMAGE BR", "desc": "Product 4: Live Business Ethics (410x370)", "w": 410, "h": 370, "bg": "#0F1B03", "fg": "#FFF7EC", "accent": "#D4AF37"},
    {"code": "image-bs", "label": "IMAGE BS", "desc": "Product 5: Personal vs Professional (410x370)", "w": 410, "h": 370, "bg": "#0F1B03", "fg": "#FFF7EC", "accent": "#D4AF37"},
    {"code": "image-bt", "label": "IMAGE BT", "desc": "Product 6: Event Planning Hub Template (410x370)", "w": 410, "h": 370, "bg": "#0F1B03", "fg": "#FFF7EC", "accent": "#D4AF37"},
    {"code": "image-bu", "label": "IMAGE BU", "desc": "Embroidered Hoodie Merch Banner (1366x750)", "w": 1366, "h": 750, "bg": "#0F1B03", "fg": "#FFF7EC", "accent": "#D4AF37"},

    # CONTACT & CAREERS
    {"code": "image-bv", "label": "IMAGE BV", "desc": "Stay Connected 5-Women Photo (600x1100)", "w": 600, "h": 1100, "bg": "#0F1B03", "fg": "#FFF7EC", "accent": "#D4AF37"},
    {"code": "image-bw", "label": "IMAGE BW", "desc": "Careers Hero Banner (1366x700)", "w": 1366, "h": 700, "bg": "#0F1B03", "fg": "#FFF7EC", "accent": "#D4AF37"},
    {"code": "image-bx", "label": "IMAGE BX", "desc": "Careers Culture & Team Workspace (1366x450)", "w": 1366, "h": 450, "bg": "#BA552A", "fg": "#FFF7EC", "accent": "#FFF7EC"},
]

def hex_to_rgb(hex_str):
    hex_str = hex_str.lstrip('#')
    return tuple(int(hex_str[i:i+2], 16) for i in (0, 2, 4))

for item in IMAGE_SLOTS:
    w, h = item["w"], item["h"]
    im = Image.new("RGB", (w, h), hex_to_rgb(item["bg"]))
    draw = ImageDraw.Draw(im)

    # Double border
    draw.rectangle([12, 12, w - 13, h - 13], outline=hex_to_rgb(item["accent"]), width=2)
    draw.rectangle([18, 18, w - 19, h - 19], outline=hex_to_rgb(item["accent"]), width=1)

    # Text rendering (simple fallback fonts or default)
    # Draw primary label: "IMAGE A"
    label = item["label"]
    desc = item["desc"]

    # Calculate positioning
    center_x, center_y = w // 2, h // 2
    
    # We draw geometric badge in center
    badge_w = min(w - 60, max(200, len(desc) * 10))
    badge_h = 90
    bx1 = center_x - badge_w // 2
    by1 = center_y - badge_h // 2
    bx2 = center_x + badge_w // 2
    by2 = center_y + badge_h // 2
    
    draw.rectangle([bx1, by1, bx2, by2], fill=hex_to_rgb(item["bg"]), outline=hex_to_rgb(item["accent"]), width=2)
    
    # Text lines
    draw.text((center_x, center_y - 20), label, fill=hex_to_rgb(item["accent"]), anchor="mm")
    draw.text((center_x, center_y + 15), desc, fill=hex_to_rgb(item["fg"]), anchor="mm")

    fname = f"{item['code']}.png"
    out_path = os.path.join(OUT_DIR, fname)
    im.save(out_path, quality=95)
    print(f"Generated {fname} ({w}x{h})")

print(f"Successfully generated all {len(IMAGE_SLOTS)} placeholder images in {OUT_DIR}!")

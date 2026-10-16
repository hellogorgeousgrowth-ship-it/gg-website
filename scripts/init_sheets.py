import urllib.request
import json
import time

URL = "https://script.google.com/macros/s/AKfycbx1zBAhnFAphb2CzlgjybvALriovJ2XW9nXRQoq5wfoiNOQq8H-_kjhE7YgQ1dp3rTt/exec"

MEMBERS = [
    {"name": "Olivia Gonzalez", "role": "Sales Consultant", "url": "https://hellogorgeousgrowth-ship-it.github.io/gg-website/members/member-olivia-gonzalez.html"},
    {"name": "Sarah & Natalie", "role": "PLINA — Digital Women's Wellness Community", "url": "https://hellogorgeousgrowth-ship-it.github.io/gg-website/members/member-plina.html"},
    {"name": "Autumn Hxze", "role": "AutumnHxzePhoto — Photographer & Videographer", "url": "https://hellogorgeousgrowth-ship-it.github.io/gg-website/members/member-autumn-hxze.html"},
    {"name": "Alejandra Llines", "role": "Social Media Manager", "url": "https://hellogorgeousgrowth-ship-it.github.io/gg-website/members/member-alejandra-llines.html"},
    {"name": "Shanjali Arul", "role": "Chi Meadow Collective", "url": "https://hellogorgeousgrowth-ship-it.github.io/gg-website/members/member-shanjali-arul.html"},
    {"name": "Thomas Kneifel", "role": "Thomas K Jewlery — Private Jeweler & Podcast Host", "url": "https://hellogorgeousgrowth-ship-it.github.io/gg-website/members/member-thomas-kneifel.html"},
    {"name": "Hannah Andrews", "role": "HXAPhotography — Ohio-Based Photographer", "url": "https://hellogorgeousgrowth-ship-it.github.io/gg-website/members/member-hannah-andrews.html"},
    {"name": "Sanya Gujral", "role": "UGC & Media Manager", "url": "https://hellogorgeousgrowth-ship-it.github.io/gg-website/members/member-sanya-gujral.html"},
    {"name": "Ava Doherty", "role": "Creative Assistant & Event Production", "url": "https://hellogorgeousgrowth-ship-it.github.io/gg-website/members/member-ava-doherty.html"},
    {"name": "Taryn Hamel", "role": "Admin Assistant & Operations", "url": "https://hellogorgeousgrowth-ship-it.github.io/gg-website/members/member-taryn-hamel.html"},
    {"name": "Luis Chang", "role": "Luis' Funnel Design — Web & Funnel Designer", "url": "https://hellogorgeousgrowth-ship-it.github.io/gg-website/members/member-luis-chang.html"},
    {"name": "Sanjana Senthilkumar", "role": "Travel UGC Creator", "url": "https://hellogorgeousgrowth-ship-it.github.io/gg-website/members/member-sanjana-senthilkumar.html"},
    {"name": "Erin Lindsay", "role": "Penchant Boutique", "url": "https://hellogorgeousgrowth-ship-it.github.io/gg-website/members/member-erin-lindsay.html"},
    {"name": "Diya Sonani", "role": "IdYia Studios — Creative Studio & Content Creator", "url": "https://hellogorgeousgrowth-ship-it.github.io/gg-website/members/member-diya-sonani.html"},
    {"name": "Aiah Elessawy", "role": "Hyde & Heal Studio — Yoga Studio & Classes", "url": "https://hellogorgeousgrowth-ship-it.github.io/gg-website/members/member-aiah-elessawy.html"},
    {"name": "Monique Moguel", "role": "TruVigil — TruVigil Solutions", "url": "https://hellogorgeousgrowth-ship-it.github.io/gg-website/members/member-monique-moguel.html"},
    {"name": "Nico Silva", "role": "Analytics Consultant & Data Specialist", "url": "https://hellogorgeousgrowth-ship-it.github.io/gg-website/members/member-nico-silva.html"},
    {"name": "Sonal Matta", "role": "Financial Consultant", "url": "https://hellogorgeousgrowth-ship-it.github.io/gg-website/members/member-sonal-matta.html"},
    {"name": "Alexis Vasquez", "role": "Studio Lex Chicago — Rentable Studio & Photographer", "url": "https://hellogorgeousgrowth-ship-it.github.io/gg-website/members/member-alexis-vasquez.html"},
    {"name": "Joel Moore", "role": "Emi's Playhouse", "url": "https://hellogorgeousgrowth-ship-it.github.io/gg-website/members/member-joel-moore.html"},
    {"name": "SoulTree", "role": "SoulTree AV — Film Production Space & XR Stage", "url": "https://hellogorgeousgrowth-ship-it.github.io/gg-website/members/member-soultree.html"},
    {"name": "Kris O", "role": "United Airlines Employee & Creative Entrepreneur (Chicago Film Club)", "url": "https://hellogorgeousgrowth-ship-it.github.io/gg-website/members/member-kris-o.html"},
    {"name": "Lei PJ (@relei_doe)", "role": "Flight Attendant & Lifestyle Creator", "url": "https://hellogorgeousgrowth-ship-it.github.io/gg-website/members/member-lei-pj.html"}
]

for m in MEMBERS:
    payload = {
        "timestamp": "2026-08-25T11:00:00Z",
        "page_url": m["url"],
        "target_member": m["name"],
        "target_member_role": m["role"],
        "first_name": "—",
        "last_name": "—",
        "business_name": "—",
        "email": "—",
        "phone": "—",
        "comm_preference": "—",
        "titles": "—",
        "work_date": "—",
        "work_time": "—",
        "budget": "—",
        "membership_interest": "—",
        "additional_notes": "Initial System Setup"
    }
    data = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(URL, data=data, headers={"Content-Type": "application/json"})
    try:
        with urllib.request.urlopen(req) as resp:
            print(f"Created tab for {m['name']}: {resp.read().decode('utf-8')}")
    except Exception as e:
        print(f"Error on {m['name']}: {e}")
    time.sleep(0.4)

print("All 20 member tabs initialized successfully!")

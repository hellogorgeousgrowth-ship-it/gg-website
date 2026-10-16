# Gorgeous Growth Group — Website Replica (Rough Draft)

> **Status Notice:** This repository is the rough draft of the Gorgeous Growth website replica. While core layouts, responsive styling, interactive transitions, and page structures are implemented across all 7 pages, ongoing visual polishes and fine-tuning edits are still underway.

---

## 📋 Google Sheets Job Application Sync

* **Career & Internship Applications Portal (`careers.html`)**:
  * Set up by default to stream candidates into the official Gorgeous Growth Google Sheet:
    **[Gorgeous Growth Applications Spreadsheet](https://docs.google.com/spreadsheets/d/1aXdGgefLs7a7S8GDhsCFqYxnkTgOer9IuW9HAqjFr6g/edit?usp=sharing)**
  * Captures all candidate fields: Timestamp, Position, Full Name, Email, Phone, Location, University, Major, Graduation Date, GPA, Weekly Availability, LinkedIn URL, Portfolio URL, Resume Link, "Why Gorgeous Growth?", "Proud Project", and Work Authorization Certification.
* **Contact Us Form (`contact.html`)**:
  * *Note:* Contact inquiry messages are currently not synced to the spreadsheet. Only job/internship applications on `careers.html` route into the spreadsheet webhook.

---

## 🖼️ Image Replacement Guide (For Shay)

All imagery across the website uses structured placeholders so you can drop your real photos in seamlessly without touching any HTML code:

1. **Locate the Images Folder**:
   * Navigate to `images/site_images/` in this project.
2. **Identify Your Desired Image Slot**:
   * Every image on the website is labeled sequentially (`IMAGE A` through `IMAGE BX`).
   * Each placeholder graphic has a visible label and exact pixel dimensions guide (`e.g., 1200 x 800 (3:2)`) embedded right on the graphic so you can size and crop your photos to fit.
   * Refer to **[`IMAGE_MAP.md`](IMAGE_MAP.md)** for a complete cheat sheet detailing every image letter, its location, and its page.
3. **Replace the Image**:
   * When you have the photo you want to use, **rename your photo file to match the exact placeholder filename** (e.g. `image-a.png`, `image-r.png`, `image-an.png`).
   * Drop your renamed photo into `images/site_images/` (overwriting the placeholder).
   * Refresh your browser, and your real photo will instantly display in the correct position!

---

## 📂 Site Structure & Pages

| Page | File | Description |
| :--- | :--- | :--- |
| **Home** | `index.html` | Brand statement, The Gorgie Method, What's Growing Now ribbons, Instagram & Footer |
| **About Us** | `about.html` | Agency Story, Shay Gorgie Founder spotlight, Meet the Team (editorial bio cards) |
| **Consulting** | `consulting.html` | Strategic Support Pillars, A La Carte Services, Discovery Call booking |
| **Membership** | `network.html` | 20 Individual Member Directory cards, Community Perks, Application form |
| **Growth Shop** | `growth-shop.html` | Editorial Toolkits, Merch Showcase, Book of the Month, Checkout CTAs |
| **Contact** | `contact.html` | General inquiries, Discovery Call scheduler, Social links |
| **Careers** | `careers.html` | Active Fall/Winter Internship roles & Live Greenhouse-style Application Portal |

---

## 🚀 Deployment & Local Preview

* **Local Preview**: Open any `.html` file directly in your browser, or run a lightweight local web server (e.g., `npx serve .` or VS Code Live Server).
* **Live Deployment**: This static site is 100% portable and can be deployed anywhere (GitHub Pages, Vercel, Netlify, Cloudflare Pages, Canva, AWS S3, or custom hosting) with zero server configuration required.

---
*Built by Raptor.*

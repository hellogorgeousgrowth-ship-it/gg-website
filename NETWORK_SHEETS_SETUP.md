# Google Apps Script Setup & Multi-Tab Deployment Guide (NETWORK_SHEETS_SETUP.md)

This setup allows **1 single Google Spreadsheet** to automatically manage all 20 community members with their own individual tab, their live GitHub page URL pinned at the top, and all Question & Answer submissions logged cleanly.

---

## 🌟 How It Works
- When a client submits a form on `https://hellogorgeousgrowth-ship-it.github.io/gg-website/members/member-olivia-gonzalez.html`, the script automatically finds or creates the **Olivia Gonzalez** tab in your spreadsheet.
- The top of each tab features:
  - **Row 1**: Member Name & Specialty Title
  - **Row 2**: Direct clickable GitHub Page URL (`https://hellogorgeousgrowth-ship-it.github.io/gg-website/members/...`)
  - **Row 4**: Question Header Row
  - **Row 5+**: Every incoming submission with timestamps and full answers.

---

## 📋 Step 1: Create Your Google Spreadsheet

1. Open [Google Sheets](https://sheets.new) and create a new spreadsheet.
2. Name it: **`Gorgeous Growth — Network Matchmaking Hub`**

---

## ⚡ Step 2: Paste the Apps Script `Code.gs`

1. In your Google Sheet top menu, click: **Extensions &rarr; Apps Script**.
2. Delete everything in the editor and paste the code below:

```javascript
/**
 * Gorgeous Growth Group - Community Network Matchmaking Handler
 * Logs to individual member tabs & sends email alerts to multiple inboxes.
 */

// 📬 Notification recipients:
const NOTIFICATION_EMAILS = "hello@gorgeousgrowth.org, hellogorgeousgrowth@gmail.com";

const MEMBER_PAGES = {
  "Olivia Gonzalez": "https://hellogorgeousgrowth-ship-it.github.io/gg-website/members/member-olivia-gonzalez.html",
  "Sarah & Natalie": "https://hellogorgeousgrowth-ship-it.github.io/gg-website/members/member-plina.html",
  "Autumn Hxze": "https://hellogorgeousgrowth-ship-it.github.io/gg-website/members/member-autumn-hxze.html",
  "Alejandra Llines": "https://hellogorgeousgrowth-ship-it.github.io/gg-website/members/member-alejandra-llines.html",
  "Shanjali Arul": "https://hellogorgeousgrowth-ship-it.github.io/gg-website/members/member-shanjali-arul.html",
  "Thomas Kneifel": "https://hellogorgeousgrowth-ship-it.github.io/gg-website/members/member-thomas-kneifel.html",
  "Hannah Andrews": "https://hellogorgeousgrowth-ship-it.github.io/gg-website/members/member-hannah-andrews.html",
  "Sanya Gujral": "https://hellogorgeousgrowth-ship-it.github.io/gg-website/members/member-sanya-gujral.html",
  "Ava Doherty": "https://hellogorgeousgrowth-ship-it.github.io/gg-website/members/member-ava-doherty.html",
  "Taryn Hamel": "https://hellogorgeousgrowth-ship-it.github.io/gg-website/members/member-taryn-hamel.html",
  "Luis Chang": "https://hellogorgeousgrowth-ship-it.github.io/gg-website/members/member-luis-chang.html",
  "Sanjana Senthilkumar": "https://hellogorgeousgrowth-ship-it.github.io/gg-website/members/member-sanjana-senthilkumar.html",
  "Erin Lindsay": "https://hellogorgeousgrowth-ship-it.github.io/gg-website/members/member-erin-lindsay.html",
  "Diya Sonani": "https://hellogorgeousgrowth-ship-it.github.io/gg-website/members/member-diya-sonani.html",
  "Aiah Elessawy": "https://hellogorgeousgrowth-ship-it.github.io/gg-website/members/member-aiah-elessawy.html",
  "Monique Moguel": "https://hellogorgeousgrowth-ship-it.github.io/gg-website/members/member-monique-moguel.html",
  "Nico Silva": "https://hellogorgeousgrowth-ship-it.github.io/gg-website/members/member-nico-silva.html",
  "Sonal Matta": "https://hellogorgeousgrowth-ship-it.github.io/gg-website/members/member-sonal-matta.html",
  "Alexis Vasquez": "https://hellogorgeousgrowth-ship-it.github.io/gg-website/members/member-alexis-vasquez.html",
  "Joel Moore": "https://hellogorgeousgrowth-ship-it.github.io/gg-website/members/member-joel-moore.html",
  "SoulTree": "https://hellogorgeousgrowth-ship-it.github.io/gg-website/members/member-soultree.html",
  "Kris O": "https://hellogorgeousgrowth-ship-it.github.io/gg-website/members/member-kris-o.html",
  "Lei PJ (@relei_doe)": "https://hellogorgeousgrowth-ship-it.github.io/gg-website/members/member-lei-pj.html"
};

const QUESTIONS_HEADER = [
  "Submission Timestamp",
  "Q1: First Name",
  "Q2: Last Name",
  "Q3: Business / Preferred Name",
  "Q4: Email Address",
  "Q5: Phone Number",
  "Q6: Preferred Communication Method",
  "Q7: Titles / Roles",
  "Q8: Preferred Introduction Date",
  "Q9: Preferred Introduction Time",
  "Q10: Proposed Project Budget",
  "Q11: Network Membership Interest",
  "Q12: Additional Notes / Questions"
];

function doPost(e) {
  try {
    const ss = SpreadsheetApp.getActiveSpreadsheet();
    const data = JSON.parse(e.postData.contents);
    
    const memberName = data.target_member || "General Network";
    const memberRole = data.target_member_role || "";
    const pageUrl = data.page_url || MEMBER_PAGES[memberName] || "https://hellogorgeousgrowth-ship-it.github.io/gg-website/network.html";
    
    // Find or create sheet for this specific member
    let sheet = ss.getSheetByName(memberName);
    if (!sheet) {
      sheet = setupMemberSheet(ss, memberName, memberRole, pageUrl);
    }
    
    // Append the Q&A submission row
    sheet.appendRow([
      data.timestamp || new Date().toISOString(),
      data.first_name || '',
      data.last_name || '',
      data.business_name || '',
      data.email || '',
      data.phone || '',
      data.comm_preference || '',
      data.titles || '',
      data.work_date || '',
      data.work_time || '',
      data.budget || '',
      data.membership_interest || '',
      data.additional_notes || ''
    ]);
    
    // 📧 Send Instant Email Alert to both inboxes
    if (NOTIFICATION_EMAILS && data.first_name && data.first_name !== "—") {
      const subject = `✨ New Collaboration Request for ${memberName} (${data.first_name} ${data.last_name})`;
      const body = `Hi Gorgeous Growth Team,

A new collaboration request has been submitted on the website!

🤝 TARGET COLLABORATOR:
• Member: ${memberName}
• Role / Specialty: ${memberRole}
• Member Page: ${pageUrl}

👤 CLIENT INFORMATION:
• Name: ${data.first_name} ${data.last_name}
• Business / Preferred Name: ${data.business_name || 'N/A'}
• Email: ${data.email}
• Phone: ${data.phone || 'N/A'}
• Preferred Contact Method: ${data.comm_preference || 'Email'}
• Client Title(s): ${data.titles || 'N/A'}

📅 PROJECT & SCHEDULING DETAILS:
• Preferred Date: ${data.work_date || 'Flexible'}
• Preferred Time: ${data.work_time || 'Flexible'}
• Proposed Budget: ${data.budget || 'Not specified'}
• Interested in GG Membership: ${data.membership_interest || 'N/A'}

📝 NOTES / SCOPE:
${data.additional_notes || 'None provided'}

---
View all inquiries in your spreadsheet:
${ss.getUrl()}
`;
      MailApp.sendEmail(NOTIFICATION_EMAILS, subject, body);
    }
    
    return ContentService.createTextOutput(JSON.stringify({ result: "success" }))
      .setMimeType(ContentService.MimeType.JSON);
  } catch (error) {
    return ContentService.createTextOutput(JSON.stringify({ result: "error", error: error.toString() }))
      .setMimeType(ContentService.MimeType.JSON);
  }
}

/**
 * Creates and formats a member's individual tab with top banner, live page link, and Q&A headers.
 */
function setupMemberSheet(ss, memberName, memberRole, pageUrl) {
  let sheet = ss.insertSheet(memberName);
  
  // Row 1: Profile Title
  sheet.getRange("A1").setValue("✨ GORGEOUS GROWTH COMMUNITY MEMBER: " + memberName.toUpperCase() + (memberRole ? " (" + memberRole + ")" : ""));
  sheet.getRange("A1:M1").merge();
  sheet.getRange("A1").setBackground("#1B2E20").setFontColor("#FDFBF7").setFontWeight("bold").setFontSize(12);
  
  // Row 2: Live GitHub Page Link
  sheet.getRange("A2").setValue("🔗 Live Application Page: " + pageUrl);
  sheet.getRange("A2:M2").merge();
  sheet.getRange("A2").setBackground("#E88A45").setFontColor("#FFFFFF").setFontWeight("bold").setFontSize(10);
  
  // Row 3: Empty Separator
  sheet.getRange("A3:M3").setBackground("#FAF8F5");
  
  // Row 4: Questions Header
  sheet.getRange(4, 1, 1, QUESTIONS_HEADER.length).setValues([QUESTIONS_HEADER]);
  sheet.getRange("A4:M4").setBackground("#2D4A33").setFontColor("#D4AF37").setFontWeight("bold");
  
  // Auto-fit column widths
  sheet.setFrozenRows(4);
  return sheet;
}

/**
 * OPTIONAL: Run this function once inside Apps Script to pre-create all 20 member tabs instantly!
 */
function initializeAllMemberSheets() {
  const ss = SpreadsheetApp.getActiveSpreadsheet();
  for (const [name, url] of Object.entries(MEMBER_PAGES)) {
    if (!ss.getSheetByName(name)) {
      setupMemberSheet(ss, name, "", url);
    }
  }
}
```

---

## 🚀 Step 3: Deployment Walkthrough

1. In the Apps Script editor toolbar, click the **💾 Save** icon.
2. *(Optional)* In the dropdown next to "Debug", select **`initializeAllMemberSheets`** and click **Run** to pre-create all 20 tabs with their GitHub links immediately!
3. Click the blue **Deploy** button (top right) &rarr; **New deployment**.
4. Click the gear icon ⚙️ next to "Select type" &rarr; choose **Web app**.
5. Set the fields:
   - **Description**: `GG Network Matchmaking Webhook`
   - **Execute as**: `Me (your email)`
   - **Who has access**: **`Anyone`** *(⚠️ Critical: Must be set to Anyone)*
6. Click **Deploy**.
7. If prompted for permissions:
   - Click **Authorize access** &rarr; Choose your Google account &rarr; Click **Advanced** &rarr; Click **Go to Untitled project (unsafe)** &rarr; Click **Allow**.
8. Copy the **Web app URL** (`https://script.google.com/macros/s/AKfy.../exec`).

---

## 🔗 Step 4: Link Webhook URL in Code

Because all 20 member pages use the shared [`js/member-form.js`](file:///c:/Users/Rapto/.gemini/antigravity-ide/scratch/gg-website/js/member-form.js), you can either:
- Set `window.MEMBER_WEBHOOK_URL` in each file or centrally in `js/member-form.js` line 11!
- Drop the webhook URL here in chat and I'll plug it in across all pages instantly!

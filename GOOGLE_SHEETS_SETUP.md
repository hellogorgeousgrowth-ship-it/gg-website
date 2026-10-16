# How to Connect the Careers Job Portal to a Google Sheet (GOOGLE_SHEETS_SETUP.md)

This step-by-step guide walks you through connecting your **Job Application Portal** (`careers.html`) directly to a Google Sheet using a free, built-in Google Apps Script webhook (takes 2 minutes, 100% free, no third-party services needed).

---

## 📋 Step 1: Create Your Google Sheet

1. Go to [Google Sheets](https://sheets.new) and create a new spreadsheet named:
   **`Gorgeous Growth — Job Applications`**
2. In Row 1 (the header row), add the following column titles across columns A through P:
   - **Column A**: `Timestamp`
   - **Column B**: `Position`
   - **Column C**: `Full Name`
   - **Column D**: `Email`
   - **Column E**: `Phone`
   - **Column F**: `Location`
   - **Column G**: `University`
   - **Column H**: `Major`
   - **Column I**: `Graduation Date`
   - **Column J**: `GPA`
   - **Column K**: `Weekly Hours`
   - **Column L**: `LinkedIn URL`
   - **Column M**: `Portfolio URL`
   - **Column N**: `Resume Link`
   - **Column O**: `Why Gorgeous Growth`
   - **Column P**: `Proud Project`

---

## ⚡ Step 2: Add Google Apps Script

1. In your Google Sheet, click on the top menu: **Extensions** &rarr; **Apps Script**.
2. Delete whatever code is in the editor and paste this exact script:

```javascript
// 📬 Notification recipients (both emails receive instant alerts):
const NOTIFICATION_EMAILS = "hello@gorgeousgrowth.org, hellogorgeousgrowth@gmail.com";

function doPost(e) {
  try {
    var sheet = SpreadsheetApp.getActiveSpreadsheet().getActiveSheet();
    var data = JSON.parse(e.postData.contents);
    
    sheet.appendRow([
      data.timestamp || new Date(),
      data.position || '',
      data.full_name || '',
      data.email || '',
      data.phone || '',
      data.location || '',
      data.university || '',
      data.major || '',
      data.graduation_date || '',
      data.gpa || '',
      data.weekly_hours || '',
      data.linkedin_url || '',
      data.portfolio_url || '',
      data.resume_link || '',
      data.why_gorgeous_growth || '',
      data.proud_project || ''
    ]);
    
    // 📧 Send Instant Email Alert to both inboxes
    if (NOTIFICATION_EMAILS && data.full_name) {
      const subject = `💼 New Job Application: ${data.position} - ${data.full_name}`;
      const body = `Hi Gorgeous Growth Hiring Team,

A new application has been submitted on the Careers portal!

📋 POSITION:
${data.position}

👤 APPLICANT DETAILS:
• Full Name: ${data.full_name}
• Email: ${data.email}
• Phone: ${data.phone}
• Location: ${data.location}
• University / Major: ${data.university} (${data.major})
• Graduation Date / GPA: ${data.graduation_date} | GPA: ${data.gpa || 'N/A'}
• Availability: ${data.weekly_hours}

🔗 LINKS:
• Resume / CV: ${data.resume_link}
• LinkedIn: ${data.linkedin_url || 'None'}
• Portfolio: ${data.portfolio_url || 'None'}

💭 WHY GORGEOUS GROWTH:
${data.why_gorgeous_growth}

🌟 PROUD PROJECT / ACCOMPLISHMENT:
${data.proud_project}

---
View spreadsheet:
${SpreadsheetApp.getActiveSpreadsheet().getUrl()}
`;
      MailApp.sendEmail(NOTIFICATION_EMAILS, subject, body);
    }
    
    return ContentService.createTextOutput(JSON.stringify({ 'result': 'success' }))
      .setMimeType(ContentService.MimeType.JSON);
  } catch (error) {
    return ContentService.createTextOutput(JSON.stringify({ 'result': 'error', 'error': error.toString() }))
      .setMimeType(ContentService.MimeType.JSON);
  }
}
```

---

## 🚀 Step 3: Deploy as Web App

1. In Apps Script, click the blue **Deploy** button (top right) &rarr; **New deployment**.
2. Click the gear icon next to "Select type" and choose **Web app**.
3. Fill in the deployment details:
   - **Description**: `Job Application Webhook`
   - **Execute as**: `Me (your email)`
   - **Who has access**: **`Anyone`** *(Important: Must be set to Anyone so the website form can send submissions)*
4. Click **Deploy**.
5. If asked, click **Authorize access**, choose your Google account, click **Advanced** &rarr; **Go to Untitled project (unsafe)** &rarr; **Allow**.
6. Copy the **Web App URL** (it looks like `https://script.google.com/macros/s/AKfycbx.../exec`).

---

## 🔗 Step 4: Paste Web App URL in Code

Open **`js/careers.js`** in the project and paste your URL into the top line:

```javascript
const GOOGLE_SHEETS_WEBHOOK_URL = "https://script.google.com/macros/s/YOUR_DEPLOYED_ID/exec";
```

That's it! Every time someone submits an application on `careers.html`, a new row is instantly added to your Google Sheet!

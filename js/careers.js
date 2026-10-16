// careers.js - Job Application submission handler with Google Sheets Webhook integration

// DEVELOPER CONFIGURATION:
// To connect to your Google Sheet, follow the steps in GOOGLE_SHEETS_SETUP.md
// and paste your Google Apps Script Webhook URL below:
const GOOGLE_SHEETS_WEBHOOK_URL = "https://script.google.com/macros/s/AKfycbwRta3XvCHDIu2HG-RvGIN7iJ49BcvwxmW6snPfmGiMS9bN5Vzg7I6bY4FAboYNuYXTTg/exec";

document.addEventListener('DOMContentLoaded', () => {
  const appForm = document.getElementById('job-application-form');
  const statusMsg = document.getElementById('app-status-message');
  const submitBtn = document.getElementById('submit-app-btn');

  if (!appForm) return;

  appForm.addEventListener('submit', async (e) => {
    e.preventDefault();

    // Gather form data
    const formData = new FormData(appForm);
    const data = {
      timestamp: new Date().toISOString(),
      position: formData.get('position') || '',
      full_name: formData.get('full_name') || '',
      email: formData.get('email') || '',
      phone: formData.get('phone') || '',
      location: formData.get('location') || '',
      university: formData.get('university') || '',
      major: formData.get('major') || '',
      graduation_date: formData.get('graduation_date') || '',
      gpa: formData.get('gpa') || 'N/A',
      weekly_hours: formData.get('weekly_hours') || '',
      linkedin_url: formData.get('linkedin_url') || '',
      portfolio_url: formData.get('portfolio_url') || '',
      resume_link: formData.get('resume_link') || '',
      why_gorgeous_growth: formData.get('why_gorgeous_growth') || '',
      proud_project: formData.get('proud_project') || ''
    };

    // Validate work authorization checkbox
    const workAuth = appForm.querySelector('input[name="work_authorization"]');
    if (!workAuth || !workAuth.checked) {
      statusMsg.style.display = 'block';
      statusMsg.style.backgroundColor = '#fce8e6';
      statusMsg.style.color = '#c5221f';
      statusMsg.style.border = '1px solid #fad2cf';
      statusMsg.innerHTML = '<strong>Action Required</strong>: You must certify that you are authorized to work in the United States before submitting.';
      workAuth.focus();
      return;
    }

    // UI Loading state
    submitBtn.disabled = true;
    submitBtn.textContent = 'Submitting Application...';
    statusMsg.style.display = 'none';

    try {
      if (GOOGLE_SHEETS_WEBHOOK_URL && GOOGLE_SHEETS_WEBHOOK_URL.trim() !== "") {
        // Send data to Google Sheets Apps Script Webhook
        const response = await fetch(GOOGLE_SHEETS_WEBHOOK_URL, {
          method: 'POST',
          mode: 'no-cors', // standard for Google Apps Script redirects
          headers: {
            'Content-Type': 'application/json',
          },
          body: JSON.stringify(data)
        });

        statusMsg.style.display = 'block';
        statusMsg.style.backgroundColor = '#e6f4ea';
        statusMsg.style.color = '#137333';
        statusMsg.style.border = '1px solid #ceead6';
        statusMsg.innerHTML = `<strong>Application Submitted Successfully!</strong><br />Thank you, ${data.full_name}. Your application for <em>${data.position}</em> has been securely logged. Our hiring team will be in touch!`;
        appForm.reset();
      } else {
        // Fallback demo mode when Google Sheets Webhook URL hasn't been added yet
        console.log('Application Data Logged (Google Sheet Webhook not yet configured):', data);
        
        statusMsg.style.display = 'block';
        statusMsg.style.backgroundColor = '#e6f4ea';
        statusMsg.style.color = '#137333';
        statusMsg.style.border = '1px solid #ceead6';
        statusMsg.innerHTML = `<strong>Application Recorded!</strong><br />Thank you, ${data.full_name}. Your application for <em>${data.position}</em> has been submitted.<br /><small style="color: #666;">(Note: Set up GOOGLE_SHEETS_WEBHOOK_URL in <code>js/careers.js</code> to stream directly into your live Google Sheet. See <code>GOOGLE_SHEETS_SETUP.md</code>)</small>`;
        appForm.reset();
      }
    } catch (err) {
      console.error('Submission error:', err);
      statusMsg.style.display = 'block';
      statusMsg.style.backgroundColor = '#fce8e6';
      statusMsg.style.color = '#c5221f';
      statusMsg.style.border = '1px solid #fad2cf';
      statusMsg.innerHTML = `<strong>Submission error</strong>: Please try again or email your resume directly to <a href="mailto:hello@gorgeousgrowth.org">hello@gorgeousgrowth.org</a>.`;
    } finally {
      submitBtn.disabled = false;
      submitBtn.textContent = 'Submit Application';
    }
  });
});

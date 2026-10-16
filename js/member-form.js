// member-form.js - Handles community member matchmaking form submissions with Google Sheets Webhook

// CENTRAL DEVELOPER CONFIGURATION:
// Paste your multi-tab Google Apps Script Webhook URL here to connect all 20 member pages at once:
const DEFAULT_MEMBER_WEBHOOK_URL = "https://script.google.com/macros/s/AKfycbx1zBAhnFAphb2CzlgjybvALriovJ2XW9nXRQoq5wfoiNOQq8H-_kjhE7YgQ1dp3rTt/exec";

document.addEventListener('DOMContentLoaded', () => {
  const matchForm = document.getElementById('member-match-form');
  const statusMsg = document.getElementById('match-status-message');
  const submitBtn = document.getElementById('submit-match-btn');

  if (!matchForm) return;

  // Retrieve page-specific webhook URL or fallback to central webhook
  const webhookUrl = window.MEMBER_WEBHOOK_URL || matchForm.getAttribute('data-webhook-url') || DEFAULT_MEMBER_WEBHOOK_URL || "";

  matchForm.addEventListener('submit', async (e) => {
    e.preventDefault();

    const formData = new FormData(matchForm);

    // Collect all checked titles
    const titlesSelected = [];
    matchForm.querySelectorAll('input[name="titles"]:checked').forEach(cb => {
      titlesSelected.push(cb.value);
    });
    const otherTitle = formData.get('title_other') ? `Other: ${formData.get('title_other')}` : '';
    if (otherTitle) titlesSelected.push(otherTitle);

    // Communication method
    let commMethod = formData.get('comm_method') || '';
    if (commMethod === 'Other' && formData.get('comm_method_other')) {
      commMethod = `Other: ${formData.get('comm_method_other')}`;
    }

    const payload = {
      timestamp: new Date().toISOString(),
      page_url: window.location.href,
      target_member: formData.get('target_member') || 'Community Member',
      target_member_role: formData.get('target_member_role') || '',
      email: (formData.get('email') || '').trim(),
      first_name: (formData.get('first_name') || '').trim(),
      last_name: (formData.get('last_name') || '').trim(),
      business_name: (formData.get('business_name') || '').trim(),
      phone: (formData.get('phone') || '').trim(),
      comm_preference: commMethod,
      titles: titlesSelected.join(', '),
      work_date: formData.get('work_date') || '',
      work_time: formData.get('work_time') || '',
      budget: (formData.get('budget') || '').trim(),
      membership_interest: formData.get('membership_interest') || 'Not specified',
      additional_notes: (formData.get('additional_notes') || '').trim()
    };

    // UI Loading state
    if (submitBtn) {
      submitBtn.disabled = true;
      submitBtn.textContent = 'Submitting Request...';
    }
    if (statusMsg) {
      statusMsg.style.display = 'none';
    }

    try {
      if (webhookUrl && webhookUrl.trim() !== "") {
        await fetch(webhookUrl, {
          method: 'POST',
          mode: 'no-cors',
          headers: {
            'Content-Type': 'application/json',
          },
          body: JSON.stringify(payload)
        });

        showStatus('success', `<strong>Request Sent Successfully!</strong><br />Thank you, ${payload.first_name}! Your collaboration request with <strong>${payload.target_member}</strong> has been received. Our team will review the details and connect with you shortly via ${payload.comm_preference || 'email'}.`);
        matchForm.reset();
      } else {
        // Fallback demo mode when webhook has not yet been linked
        console.log('Matchmaking Submission Data Logged (Webhook not configured yet):', payload);

        showStatus('success', `<strong>Request Recorded!</strong><br />Thank you, ${payload.first_name}! Your request to match with <strong>${payload.target_member}</strong> has been logged.<br /><small style="color: #666; display: inline-block; margin-top: 0.5rem;">(Note: Set <code>window.MEMBER_WEBHOOK_URL</code> at the bottom of this page to stream submissions directly into this member's Google Sheet. See <code>NETWORK_SHEETS_SETUP.md</code>)</small>`);
        matchForm.reset();
      }
    } catch (err) {
      console.error('Matchmaking submission error:', err);
      showStatus('error', `<strong>Submission error:</strong> We encountered an issue sending your request. Please try again or email us directly at <a href="mailto:hello@gorgeousgrowth.org" style="color: inherit; text-decoration: underline;">hello@gorgeousgrowth.org</a>.`);
    } finally {
      if (submitBtn) {
        submitBtn.disabled = false;
        submitBtn.textContent = 'Submit Collaboration Request';
      }
    }
  });

  function showStatus(type, html) {
    if (!statusMsg) return;
    statusMsg.style.display = 'block';
    if (type === 'success') {
      statusMsg.style.backgroundColor = '#e6f4ea';
      statusMsg.style.color = '#137333';
      statusMsg.style.border = '1px solid #ceead6';
    } else {
      statusMsg.style.backgroundColor = '#fce8e6';
      statusMsg.style.color = '#c5221f';
      statusMsg.style.border = '1px solid #fad2cf';
    }
    statusMsg.innerHTML = html;
    statusMsg.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
  }
});

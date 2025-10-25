# Streamlit Web App Deployment Guide

**Complete step-by-step instructions to deploy your Notion Exporter web app**

This guide will help you deploy the Notion Exporter as a web application that your team can access via a URL. The entire process takes about 30-45 minutes and is completely free.

---

## Prerequisites

Before you begin, make sure you have:

- ✅ **GitHub account** (free) - Sign up at https://github.com if needed
- ✅ **Notion API key** - You already have this from the CLI setup
- ✅ **Git installed** on your computer (check by running `git --version` in terminal)
- ✅ **This project folder** with all the code

---

## Part 1: Push Code to GitHub (10 minutes)

### Step 1: Create a GitHub Repository

1. Go to https://github.com
2. Click the **"+"** button (top right) → **"New repository"**
3. Fill in:
   - **Repository name**: `notion-externship-exporter`
   - **Description**: "Web app to export Notion externships for GPT training"
   - **Visibility**: Choose **Public** (required for free Streamlit hosting)
   - **DO NOT** check "Add a README file"
4. Click **"Create repository"**

You'll see a page with instructions - keep this tab open.

### Step 2: Initialize Git in Your Project (If Not Already)

Open your terminal/command prompt and navigate to the project:

```bash
cd c:\Users\rodol\extern-ai-automation\notion-export-tool
```

Check if Git is already initialized:

```bash
git status
```

**If you see** `fatal: not a git repository`:
```bash
git init
git add .
git commit -m "Initial commit: Notion exporter with Streamlit web interface"
```

**If you see** `On branch main` or similar:
```bash
git add .
git commit -m "Add Streamlit web interface"
```

### Step 3: Connect to GitHub and Push

Copy these commands from the GitHub page you opened earlier, or use these (replace `YOUR-USERNAME`):

```bash
git remote add origin https://github.com/YOUR-USERNAME/notion-externship-exporter.git
git branch -M main
git push -u origin main
```

**If prompted for credentials:**
- **Username**: Your GitHub username
- **Password**: You'll need a **Personal Access Token** (not your GitHub password)
  - Go to https://github.com/settings/tokens
  - Click "Generate new token (classic)"
  - Give it a name, check "repo" scope, click "Generate token"
  - Copy the token and use it as your password

**Success check:** Refresh your GitHub repository page - you should see all your files!

---

## Part 2: Deploy to Streamlit Cloud (15 minutes)

### Step 1: Sign Up for Streamlit Cloud

1. Go to https://share.streamlit.io
2. Click **"Sign up"** or **"Continue with GitHub"**
3. Choose **"Sign in with GitHub"**
4. Click **"Authorize streamlit"** to connect your GitHub account

### Step 2: Deploy Your App

1. In Streamlit Cloud, click **"New app"** (or "Create app")

2. Fill in the deployment form:
   - **Repository**: Select `YOUR-USERNAME/notion-externship-exporter`
   - **Branch**: `main`
   - **Main file path**: `streamlit_app.py`
   - **App URL** (optional): Choose a custom URL like `extern-exporter` (or leave default)

3. Click **"Advanced settings"** (before deploying)

4. In the "Secrets" section, paste this (replace with your actual Notion API key):

```toml
NOTION_API_KEY = "secret_your_actual_notion_api_key_here"
```

**Important:**
- Use the format exactly as shown above
- Replace `secret_your_actual_notion_api_key_here` with your real API key
- Keep the quotes around the key

5. Click **"Save"**

6. Click **"Deploy!"**

### Step 3: Wait for Deployment

You'll see a log screen showing:
- "Preparing system..."
- "Installing dependencies..."
- "Building app..."

This takes 2-5 minutes. Don't close the page!

**When you see:** "Your app is live!" with a green checkmark - you're done!

### Step 4: Get Your App URL

Your app URL will be something like:
```
https://extern-exporter.streamlit.app
```

Or:
```
https://YOUR-USERNAME-notion-externship-exporter.streamlit.app
```

**Copy this URL** - you'll share it with your team!

---

## Part 3: Add Your Logo (Optional, 5 minutes)

To add the Extern.com logo to the web interface:

### Step 1: Prepare Logo

1. Save your logo as `extern-logo.png`
2. Place it in the `assets/` folder of your project

### Step 2: Push to GitHub

```bash
cd c:\Users\rodol\extern-ai-automation\notion-export-tool
git add assets/extern-logo.png
git commit -m "Add Extern logo to web interface"
git push
```

### Step 3: Automatic Redeployment

Streamlit Cloud automatically detects the change and redeploys within 1-2 minutes. Just refresh your app URL!

See [assets/logo-instructions.md](assets/logo-instructions.md) for detailed logo setup.

---

## Part 4: Test Your Deployment (5 minutes)

### Test with a Real Externship

1. Visit your app URL
2. Paste a Notion externship URL you have access to
3. Click "Export Externship"
4. Verify it processes successfully
5. Download the file
6. Check the file looks correct (open it in a text editor)

### Test Error Handling

1. Try an invalid URL (should show error message)
2. Try a Notion page you don't have access to (should show helpful error)
3. Verify error messages are user-friendly

### Test on Mobile

Visit the app URL on your phone to ensure it works on mobile devices.

---

## Sharing with Your Team

Once deployed successfully:

### Create a Simple Announcement

**Slack/Email template:**

```
🎉 New Tool Alert: Notion Externship Exporter

We now have a web tool to export Notion externships for GPT training!

🔗 Access here: https://your-app-url.streamlit.app

How to use:
1. Open the link above
2. Paste your Notion externship URL
3. Click "Export"
4. Download the file
5. Upload to your OpenAI custom GPT

Full guide: [attach TEAM-GUIDE.md]

Questions? Reach out to [your name] or post in #team-channel
```

### Onboarding

- Share the `TEAM-GUIDE.md` file with your team
- Do a quick 5-minute demo on a team call
- Make sure everyone knows to message you if they hit issues

---

## Updating Your App

When you need to make changes to the web app:

### For Code Changes:

```bash
cd c:\Users\rodol\extern-ai-automation\notion-export-tool

# Make your changes to files
# (edit streamlit_app.py, config.py, etc.)

# Commit and push
git add .
git commit -m "Description of your changes"
git push
```

Streamlit Cloud automatically redeploys within 1-2 minutes!

### For Configuration Changes:

To update the Notion API key or other secrets:

1. Go to https://share.streamlit.io
2. Click on your app
3. Click **"⋮"** menu → **"Settings"**
4. Go to **"Secrets"** tab
5. Edit your secrets
6. Click **"Save"**
7. App will automatically redeploy

---

## Troubleshooting

### Issue: "git command not found"

**Solution:**
- Install Git from https://git-scm.com/downloads
- Restart your terminal after installation
- Try `git --version` again

### Issue: "Permission denied" when pushing to GitHub

**Solution:**
- Make sure you're using a GitHub Personal Access Token, not your password
- Generate one at https://github.com/settings/tokens
- Select "repo" scope when creating the token

### Issue: Streamlit app shows "Configuration Error"

**Solution:**
- Check that you added NOTION_API_KEY to Streamlit secrets
- Verify the format: `NOTION_API_KEY = "your_key_here"`
- Make sure quotes are included
- No extra spaces or characters

### Issue: "Cannot access this Notion page" error

**Solution:**
- This is expected - users need to ensure their Notion integration has access to the pages they want to export
- Your team needs to add the integration to each externship page (covered in TEAM-GUIDE.md)

### Issue: App is slow or timing out

**Solution:**
- Free Streamlit Cloud can be slow for very large externships (100+ pages)
- Contact Streamlit support or consider upgrading to Streamlit Cloud Teams ($20/month)
- For now, the free tier should handle your use case fine

### Issue: Changes not showing after push

**Solution:**
- Check the GitHub repository - did your changes push successfully?
- In Streamlit Cloud, go to your app → "⋮" → "Reboot app"
- Hard refresh your browser: Ctrl+Shift+R (Windows) or Cmd+Shift+R (Mac)

### Issue: Can't find my app in Streamlit Cloud

**Solution:**
- Go to https://share.streamlit.io
- Sign in with the same GitHub account you used to deploy
- You should see your app in the dashboard

---

## Cost & Limits

### Free Tier (What You're Using):

**Streamlit Community Cloud - FREE Forever:**
- ✅ 1 private app OR unlimited public apps
- ✅ 1 GB RAM
- ✅ 1 CPU core
- ✅ Perfect for your 10-12 users
- ✅ Auto-updates from GitHub
- ✅ No credit card required

**Limits you might hit:**
- None for your use case! 10-12 weekly users won't come close to limits

### If You Need to Upgrade (Unlikely):

**Streamlit Cloud Teams - $20/month:**
- Multiple private apps
- 2 GB RAM
- Faster performance
- Password protection
- Custom domains

**When to upgrade:**
- Your team grows significantly (50+ users)
- You need private/password-protected apps
- You need better performance for very large externships

For now, **stick with the free tier** - it's more than enough!

---

## Security Best Practices

### What's Secure:

✅ **Notion API key** is stored as an encrypted secret in Streamlit Cloud
✅ **Not visible** in your code or GitHub repository
✅ **Not accessible** to users of the web app

### What's Public:

⚠️ **Your code** is on GitHub (public repository required for free Streamlit)
⚠️ **Anyone with the URL** can access the web app

### To Improve Security (Optional):

1. **Add password protection:**
   - Upgrade to Streamlit Cloud Teams
   - Enable authentication in settings

2. **Restrict access:**
   - Only share URL with your team
   - URL is hard to guess (not indexed by Google)

3. **Monitor usage:**
   - Check Streamlit Cloud dashboard for analytics
   - See how many people are using the app

For most cases, the default security is fine - users still need valid Notion integration access to export pages.

---

## Maintenance

### Weekly: None Required

The app runs itself. Streamlit handles:
- Server updates
- Security patches
- Uptime monitoring
- Automatic redeployment on code changes

### Monthly: Quick Check

- Verify the app still works (test an export)
- Check for any Streamlit Cloud emails about issues
- Review usage if available in dashboard

### When Notion Updates:

If Notion API changes:
- Check `notion-client` library for updates
- Update `requirements.txt` if needed
- Push changes to GitHub (auto-redeploys)

---

## Getting Help

**Streamlit Issues:**
- Documentation: https://docs.streamlit.io
- Community forum: https://discuss.streamlit.io
- GitHub issues: https://github.com/streamlit/streamlit/issues

**GitHub Issues:**
- GitHub Help: https://docs.github.com
- Git tutorial: https://try.github.io

**Notion API Issues:**
- Notion developers: https://developers.notion.com

**General Problems:**
- Check the troubleshooting section above
- Review error messages carefully
- Search for the error on Google or Stack Overflow

---

## Success Checklist

Before sharing with your team, verify:

- [ ] App deployed successfully to Streamlit Cloud
- [ ] App URL is accessible
- [ ] Notion API key is configured in secrets
- [ ] Test export works with a real externship
- [ ] Error messages are user-friendly
- [ ] (Optional) Logo is displayed
- [ ] TEAM-GUIDE.md is ready to share
- [ ] You know how to update the app (push to GitHub)

**Once all checked: You're ready to roll out to your team!**

---

## Quick Reference Commands

**For future updates:**

```bash
# Navigate to project
cd c:\Users\rodol\extern-ai-automation\notion-export-tool

# Pull latest changes (if working on multiple computers)
git pull

# Make changes, then commit
git add .
git commit -m "Your change description"
git push

# Streamlit auto-redeploys in 1-2 minutes!
```

---

**Congratulations!** Your Notion Exporter is now live as a web app. Share the URL with your team and enjoy the time savings!

Need help? Review this guide or reach out to the Streamlit community.

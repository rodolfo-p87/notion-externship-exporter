# Team Guide: Notion Externship Exporter

**Quick reference for Program Managers and Teaching Assistants**

This simple web tool lets you export Notion externship content and convert it into files you can upload to OpenAI custom GPTs - no technical skills required!

---

## Access the Tool

**Web App URL:** [Your team lead will provide this]

Example: `https://extern-exporter.streamlit.app`

Bookmark this link for easy access!

---

## How to Export an Externship (3 Simple Steps)

### Step 1: Get Your Notion Page URL

1. Open the externship page in Notion
2. Click the **Share** button (top right)
3. Click **Copy link**

**OR** just copy the URL from your browser's address bar.

### Step 2: Use the Exporter

1. Visit the web app URL (from your bookmark)
2. Paste the Notion URL into the input field
3. (Optional) Enter a custom name if you want to override the Notion page title
4. Click **"Export Externship"**

### Step 3: Download the File

1. Wait while the tool fetches all pages (30-60 seconds for a full externship)
2. You'll see progress updates as it works
3. When complete, click the **Download** button
4. Save the `.md` file to your computer

**That's it!** You now have a GPT-ready knowledge base file.

---

## What to Do with the Downloaded File

The file you downloaded is ready to upload to OpenAI for custom GPT training.

### Upload to OpenAI:

1. Go to https://chat.openai.com/gpts/editor
2. Create a new GPT or edit an existing one
3. Scroll to the **"Knowledge"** section
4. Click **"Upload files"**
5. Select the file you just downloaded
6. Your GPT now has access to the complete externship content!

See your team's GPT configuration guide for more details on setting up custom GPTs.

---

## Before Your First Export: Give Integration Access

**IMPORTANT:** Before you can export an externship, you need to give the Notion integration access to the page.

### One-Time Setup Per Externship:

1. Open the externship page in Notion
2. Click the **"..."** menu (top right of the page)
3. Scroll down and click **"Add connections"**
4. Look for **"Extern GPT Exporter"** (or whatever your integration is named)
5. Click to select it
6. Click **"Confirm"**

**You only need to do this once per externship page!** The integration will then have access to that page and all its sub-pages.

**If you don't do this:** The exporter will show an error saying it can't access the page.

---

## Understanding the Process

When you click "Export Externship", the tool:

1. **Connects** to Notion using the API
2. **Fetches** the main page and discovers all sub-pages
3. **Extracts** content from all projects, steps, and sub-steps
4. **Consolidates** everything into one well-formatted markdown file
5. **Generates** a downloadable file optimized for GPT training

For a typical externship (5 projects, ~90 pages), this takes **30-90 seconds**.

---

## What Gets Exported?

**Included:**
- All text content from every page
- All projects, steps, and sub-steps
- Headings, lists, and formatting
- Code blocks and quotes
- The complete curriculum structure

**Not Included:**
- Images (GPT knowledge files don't support images well)
- Embedded videos
- Comments
- Page history or versions

The exported file is **pure text/markdown** - perfect for GPT training!

---

## Common Questions

### How long does an export take?

- **Small externship** (20-30 pages): 10-20 seconds
- **Medium externship** (50-70 pages): 30-45 seconds
- **Large externship** (100+ pages): 60-90 seconds

You'll see real-time progress, so you know it's working!

### Can multiple people use this at once?

Yes! The tool can handle multiple simultaneous users. However, if you notice it's slow, wait a minute and try again.

### Do I need to install anything?

Nope! It's a web app - just visit the URL in any browser. Works on:
- Windows, Mac, Linux
- Chrome, Firefox, Safari, Edge
- Desktop and mobile devices

### Will this work on my phone?

Yes! The interface is mobile-responsive. However, for the best experience, use a desktop or laptop.

### Can I export the same externship multiple times?

Absolutely! If you update the Notion content, just re-export to get the latest version. Each export creates a new file with today's date in the filename.

---

## Troubleshooting

### Error: "Cannot access this Notion page"

**Problem:** The Notion integration doesn't have access to the page.

**Solution:**
1. Go to the Notion page
2. Click "..." menu → "Add connections"
3. Add the "Extern GPT Exporter" integration
4. Try exporting again

### Error: "Please enter a Notion URL"

**Problem:** The URL field is empty or invalid.

**Solution:**
- Make sure you pasted the full URL
- URL should start with `https://www.notion.so/`
- Check there are no extra spaces before/after the URL

### Error: "Configuration Error"

**Problem:** The Notion API key isn't set up correctly (technical issue).

**Solution:**
- This is a setup problem, not your fault!
- Contact your team lead or technical support
- They need to check the Streamlit Cloud secrets configuration

### Export is taking forever (5+ minutes)

**Problem:** Very large externship or slow connection.

**Solution:**
- Wait a bit longer - some externships with 150+ pages can take 2-3 minutes
- If it's been over 5 minutes, refresh the page and try again
- If it keeps happening, contact your team lead

### Downloaded file looks weird or empty

**Problem:** Export might have failed partway through.

**Solution:**
- Try exporting again
- Check your internet connection
- Make sure the Notion page actually has content

### "This app is not working" or blank page

**Problem:** Streamlit Cloud might be down or restarting.

**Solution:**
- Wait 2-3 minutes and refresh the page
- Clear your browser cache (Ctrl+Shift+Delete)
- Try a different browser
- If it persists, contact your team lead

---

## Tips for Success

### 1. Use Descriptive Custom Names

When exporting, use clear names like:
- "Marketing Externship Q1 2025"
- "Beats by Dre Data Analytics Fall 2024"
- "Product Management Bootcamp Nov 2024"

This makes it easier to organize your GPT knowledge files!

### 2. Export Early, Export Often

- Export when you first create an externship
- Re-export after major content updates
- Keep the latest version for your GPT

### 3. Keep a Local Backup

Download the files to a dedicated folder on your computer like:
```
Documents/Externship-Exports/
  ├── marketing-externship-20251025.md
  ├── product-management-externship-20251025.md
  └── data-analytics-externship-20251025.md
```

### 4. Check the Stats

After export, the tool shows:
- Number of pages exported
- Word count
- File size

**Sanity check:** A typical full externship should be:
- 80-100 pages
- 15,000-30,000 words
- 1-3 MB file size

If your numbers are way off, something might be wrong!

### 5. Test Your GPT

After uploading to OpenAI:
- Ask the GPT a simple question about the externship
- Verify it can answer from the curriculum
- Make sure it's not making stuff up

---

## Who to Contact

### For Technical Issues with the Exporter:

**Contact:** [Your team lead's name/email]

Examples:
- App is down or not loading
- Configuration errors
- Bugs or strange behavior

### For Notion Access Issues:

**Contact:** Your Notion workspace admin

Examples:
- Can't find the integration
- Don't have permission to add connections
- Page access problems

### For OpenAI/GPT Questions:

**Contact:** [GPT configuration lead's name/email]

Examples:
- How to create a custom GPT
- GPT not answering correctly
- File upload issues on OpenAI

### For General Questions:

**Contact:** Post in #team-channel on Slack (or your team's communication channel)

---

## Quick Reference Card

**Save or print this for easy access:**

```
┌─────────────────────────────────────────────────┐
│  NOTION EXTERNSHIP EXPORTER - QUICK GUIDE       │
├─────────────────────────────────────────────────┤
│                                                 │
│  1. Copy Notion URL                             │
│  2. Visit: [your-app-url.streamlit.app]        │
│  3. Paste URL                                   │
│  4. Click "Export"                              │
│  5. Download file                               │
│  6. Upload to OpenAI GPT                        │
│                                                 │
│  ⚠️ FIRST TIME: Add integration to page!        │
│     (Notion → ... → Add connections)            │
│                                                 │
│  ⏱️ Takes 30-90 seconds for full externship     │
│                                                 │
│  📧 Issues? Contact: [team-lead@extern.com]     │
│                                                 │
└─────────────────────────────────────────────────┘
```

---

## Feedback

Have suggestions for improving this tool?

- What features would be helpful?
- What's confusing or could be clearer?
- Any bugs or issues you've encountered?

Send feedback to: [Your team lead's email/Slack]

We're always looking to make this better for you!

---

**You're all set!** Bookmark the app URL and you'll be exporting externships like a pro in no time.

Happy exporting! 🚀

# Quick Start Guide (Non-Technical)

**Want to export your Notion externships to train custom GPTs? Follow these simple steps.**

## Before You Begin

You'll need:
- Access to your Notion workspace (admin or page owner)
- 5 minutes for initial setup
- About 1 minute per externship to export

## First Time Setup (Do Once)

### 1. Get Your Notion API Key

Think of this like creating a "read-only password" for the tool to access your Notion pages.

1. Go to: [https://www.notion.so/my-integrations](https://www.notion.so/my-integrations)
2. Click the **"+ New integration"** button
3. Fill in:
   - **Name:** "Extern GPT Exporter"
   - **Workspace:** Choose your Extern workspace
4. Click **"Submit"**
5. **IMPORTANT:** Copy the long token that starts with `secret_`
   - This is your API key - keep it private!

### 2. Configure the Tool

1. Open the `notion-export-tool` folder
2. Find the file named `.env.example`
3. Make a copy and rename it to `.env` (just `.env`, remove the `.example`)
4. Open `.env` with Notepad
5. Replace `your_notion_integration_token_here` with the token you copied
6. Save and close

Your `.env` file should look like:
```
NOTION_API_KEY=secret_abc123xyz789...
```

### 3. Install the Tool (Automated)

**Option A: Easy Method (Windows)**
- Just double-click `run-export.bat`
- It will automatically set everything up on first run

**Option B: Manual Method**
1. Open Command Prompt
2. Navigate to this folder: `cd c:\Users\rodol\extern-ai-automation\notion-export-tool`
3. Run: `python -m venv venv`
4. Run: `venv\Scripts\activate`
5. Run: `pip install -r requirements.txt`

## Exporting an Externship

### Give Access to the Integration (Do Once Per Externship)

Before you can export an externship, you need to give the integration permission to read it:

1. Open your externship page in Notion
2. Click the **"..."** menu at the top right
3. Scroll down to **"Add connections"**
4. Select **"Extern GPT Exporter"** (or whatever you named it)
5. Click **"Confirm"**

**You only need to do this once per externship!**

### Run the Export

**Easy Method (Windows):**
1. Double-click `run-export.bat`
2. Copy your externship's Notion URL
3. Paste it when prompted
4. Wait 30-60 seconds
5. Done! Find your file in the `output` folder

**Manual Method:**
1. Open Command Prompt
2. Go to: `cd c:\Users\rodol\extern-ai-automation\notion-export-tool`
3. Activate: `venv\Scripts\activate`
4. Run: `python src/main.py`
5. Paste your externship URL
6. Wait for completion

## Upload to OpenAI

Once you have your exported file:

1. Go to [https://chat.openai.com/gpts/editor](https://chat.openai.com/gpts/editor)
2. Click **"Create a GPT"** or edit an existing one
3. On the right side, scroll to **"Knowledge"**
4. Click **"Upload files"**
5. Select your `.md` file from the `output` folder
6. Done! Your GPT now knows everything from that externship

## Exporting Multiple Externships

Need to export all 15 externships? Here's the efficient workflow:

### One-Time Preparation
1. Open each externship page in Notion
2. Add the integration connection (see "Give Access" above)
3. Create a text file with all your externship URLs

### Monthly Export Routine
For each externship:
1. Run the tool (double-click `run-export.bat`)
2. Paste the URL
3. Wait 30-60 seconds
4. Upload to OpenAI

**Total time:** About 15 minutes for all 15 externships

## What the Output Looks Like

You'll get a file like: `marketing-externship-knowledge-base-20251024.md`

Inside, it's organized like:
```
Externship Name

  Project 1
    Step 1
      Sub-step 1
      Sub-step 2
    Step 2
      Sub-step 1
      ...

  Project 2
    Step 1
      ...
```

Perfect for GPT to understand the structure!

## Common Questions

**Q: Do I need to re-export if I update Notion?**
A: Yes. The tool creates a snapshot of your content. When you update Notion, export again to get the latest version.

**Q: Can I export multiple externships at once?**
A: Not yet, but it only takes 1 minute per externship. If you need batch export, let me know!

**Q: Is my data safe?**
A: Yes! The integration only has read permission (can't modify anything), and all processing happens on your computer.

**Q: What if I get an error?**
A: Check these:
- Did you create the `.env` file (not `.env.example`)?
- Did you add the integration to the Notion page?
- Is your API key correct (no extra spaces)?

**Q: Can I delete the integration after exporting?**
A: You can, but you'll need to create it again next time. Better to keep it for monthly exports.

## Monthly Routine (Recommended)

1. **When:** Export at the start of each month
2. **What:** All active externships
3. **Time:** ~15 minutes total
4. **Process:**
   - Run export for each externship
   - Upload new files to OpenAI
   - Archive old exports

This keeps your GPTs up-to-date with the latest content!

## Need Help?

**Tool not working?**
- Check the main [README.md](README.md) for detailed troubleshooting
- Verify your Python version: `python --version` (should be 3.8+)
- Make sure you completed all setup steps

**Have a question?**
- Check if it's answered in the main README
- Contact your technical team with the error message

---

**You're all set!** Start with one externship to get comfortable, then scale up to all 15.

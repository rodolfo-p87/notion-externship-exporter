---
title: Notion Externship Exporter
emoji: 📚
colorFrom: blue
colorTo: purple
sdk: streamlit
sdk_version: 1.28.0
app_file: streamlit_app.py
pinned: false
---

# Notion to GPT Exporter

**A simple tool to export Notion externship content and consolidate it into GPT-ready files.**

Perfect for creating custom GPTs trained on your Extern.com externship knowledge bases. Handles the entire hierarchy automatically: Externships → Projects → Steps → Sub-steps.

## What This Tool Does

1. **Connects to your Notion workspace** via API (secure, read-only access)
2. **Exports all content** from an externship page including all nested sub-pages
3. **Consolidates everything** into a single, well-structured markdown file
4. **Optimizes for GPT training** with proper formatting and hierarchy
5. **Provides statistics** about the exported content

## Two Ways to Use This Tool

### 🌐 Web App (Recommended for Teams)

**Perfect for:** Program Managers, Teaching Assistants, non-technical team members

A simple web interface where you just paste a Notion URL and click "Export" - no installation or command line needed!

**Quick start:**
- 📖 **Team members**: See [TEAM-GUIDE.md](TEAM-GUIDE.md) for usage instructions
- 🚀 **Deployment**: See [DEPLOYMENT.md](DEPLOYMENT.md) to set up the web app (30 minutes one-time setup)
- 🎨 **Logo**: See [assets/logo-instructions.md](assets/logo-instructions.md) to add your branding

Once deployed, anyone on your team can visit a URL and export externships with zero technical knowledge.

### 💻 Command Line (For Technical Users)

**Perfect for:** Developers, technical team members who prefer CLI tools

Use the Python command line interface for more control and automation.

**Quick start:** See instructions below

---

## CLI Quick Start (For Technical Users)

### Step 1: Get Your Notion API Key

1. Go to [https://www.notion.so/my-integrations](https://www.notion.so/my-integrations)
2. Click **"+ New integration"**
3. Fill in the details:
   - **Name:** "Extern GPT Exporter" (or any name you like)
   - **Associated workspace:** Select your Extern workspace
   - **Type:** Internal integration
4. Click **"Submit"**
5. Copy the **"Internal Integration Token"** (starts with `secret_...`)

### Step 2: Give the Integration Access to Your Pages

For each externship you want to export:

1. Open the externship page in Notion
2. Click the **"..."** menu (top right)
3. Scroll down and click **"Add connections"**
4. Select your "Extern GPT Exporter" integration
5. Click **"Confirm"**

### Step 3: Set Up the Tool

1. **Open Command Prompt** (or Terminal)
2. **Navigate to this folder:**
   ```bash
   cd c:\Users\rodol\extern-ai-automation\notion-export-tool
   ```

3. **Create a virtual environment:**
   ```bash
   python -m venv venv
   ```

4. **Activate the virtual environment:**
   ```bash
   venv\Scripts\activate
   ```

5. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

6. **Create your configuration file:**
   - Copy the `.env.example` file and rename it to `.env`
   - Open `.env` in a text editor
   - Replace `your_notion_integration_token_here` with the token you copied in Step 1

   Your `.env` file should look like:
   ```
   NOTION_API_KEY=secret_abc123xyz789...
   ```

### Step 4: Export an Externship

1. **Copy the URL** of your externship page from Notion
   - Example: `https://www.notion.so/Marketing-Externship-abc123`

2. **Run the export command:**
   ```bash
   python src/main.py
   ```

3. **Paste the URL** when prompted

4. **Wait** while the tool exports everything (usually 30-60 seconds for a full externship)

5. **Done!** Your file will be in the `output/` folder

### Step 5: Upload to OpenAI

1. Go to [https://chat.openai.com/gpts/editor](https://chat.openai.com/gpts/editor)
2. Create a new GPT or edit an existing one
3. Scroll to the **"Knowledge"** section
4. Click **"Upload files"**
5. Select your exported markdown file from the `output/` folder
6. Your GPT now has access to the complete externship content!

## Usage Examples

### Basic Export (Interactive)
```bash
python src/main.py
```
Then paste your Notion URL when prompted.

### Export with All Options
```bash
python src/main.py --url "https://www.notion.so/Your-Externship-abc123" --name "Marketing Externship Q1 2025" --output "my-exports"
```

### Command Options

- `--url`: The Notion page URL (can be prompted if not provided)
- `--name`: Custom name for the externship (optional, uses Notion page title by default)
- `--output`: Output directory (optional, defaults to `output/`)

## Understanding the Output

The tool creates a markdown file with this structure:

```markdown
# Externship Name - Complete Knowledge Base

Generated: 2025-10-24 14:30:00
Purpose: This document contains the complete curriculum...

---

## Project 1: [Project Name]

[Project overview content]

### Step 1: [Step Name]

[Step content]

#### Sub-step 1: [Sub-step Name]

[Sub-step content]

#### Sub-step 2: [Sub-step Name]

[Sub-step content]

### Step 2: [Step Name]

...and so on
```

This hierarchical structure helps GPTs understand the relationship between different parts of the curriculum.

## Tips for Success

### For Best GPT Results

1. **One externship = One file** - Export each externship separately
2. **Use descriptive names** - Help your GPT understand the context
3. **Update regularly** - Re-export when you update Notion content
4. **Test your GPT** - Ask it questions about the externship to verify knowledge

### Troubleshooting

**"NOTION_API_KEY not found"**
- Make sure you created the `.env` file (not `.env.example`)
- Check that your API key is correctly pasted (no extra spaces)

**"Failed to fetch page"**
- Verify you've given the integration access to the page (Step 2 above)
- Make sure the URL is correct
- Check that the integration is for the correct workspace

**"File is quite large"**
- OpenAI's limit is 512MB per file (you're unlikely to hit this)
- If you do, consider splitting projects into separate exports

**"Could not fetch child page"**
- Some sub-pages might not have integration access
- Go to those pages and add the integration connection

### Processing Multiple Externships

Need to export all 15 externships? Here's the workflow:

1. **Give integration access** to all externship pages (one-time setup)
2. **Create a list** of all externship URLs in a text file
3. **Run the export** for each one (takes about 1 minute each)

You could also create a batch script - let me know if you need help with this!

## What Gets Exported?

**Included:**
- All text content
- Headings and formatting (bold, italic, code)
- Lists (bulleted, numbered, checklists)
- Quotes and callouts
- Code blocks
- All sub-pages (projects, steps, sub-steps)

**Not Included:**
- Images (custom GPTs don't process images from knowledge files)
- Embedded videos
- Databases (unless they're simple tables)
- Comments

## File Naming

Files are automatically named with this pattern:
```
externship-name-knowledge-base-20251024.md
```

Example: `marketing-externship-knowledge-base-20251024.md`

## Security & Privacy

- **API key is private** - Never share your `.env` file
- **Read-only access** - The tool can only read, never write or delete
- **Local processing** - All data stays on your computer
- **No cloud storage** - Output files are saved locally only

## Technical Details

**Built with:**
- Python 3.8+
- `notion-client` - Official Notion API library
- `click` - User-friendly CLI interface
- `python-dotenv` - Secure environment variable management

**File structure:**
```
notion-export-tool/
├── src/
│   ├── main.py           # CLI interface (entry point)
│   ├── config.py         # Configuration management
│   ├── notion_exporter.py  # Notion API interactions
│   └── consolidator.py   # Markdown consolidation
├── output/               # Exported files go here
├── tests/                # Unit tests
├── .env.example          # Configuration template
├── .gitignore           # Excludes secrets from git
├── requirements.txt     # Python dependencies
└── README.md            # This file
```

## Need Help?

**Common issues:**
1. Check you've completed all setup steps
2. Verify your API key is correct
3. Ensure integration has access to pages
4. Make sure your Python version is 3.8 or higher (`python --version`)

**Still stuck?**
Create an issue in the project repository with:
- The error message you're seeing
- What you were trying to do
- Your Python version

## Next Steps

Once you've successfully exported an externship:

1. **Upload to OpenAI** and create your custom GPT
2. **Test thoroughly** - Ask questions to verify the GPT has the knowledge
3. **Set up a routine** - Re-export whenever Notion content is updated
4. **Scale up** - Export all your externships to create specialized GPTs

## Future Enhancements

Potential additions (let me know if you need these):
- Batch export multiple externships at once
- Export to other formats (JSON, plain text)
- Include images/media
- Automated scheduling (weekly exports)
- Integration with OpenAI API (auto-upload)

---

**Ready to create your first GPT-ready export?** Jump to [Quick Start](#quick-start-5-minutes)!

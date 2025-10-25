# Custom GPT Configuration Guide

**Complete setup instructions for creating your Externship Program Manager Assistant**

This guide walks you through setting up a custom GPT in OpenAI that serves as a professional Program Manager assistant for your externship students.

---

## Prerequisites

Before you begin, ensure you have:

- ✅ **ChatGPT Plus or Team/Enterprise subscription** (required for custom GPTs)
- ✅ **Exported knowledge base file** (.md file from the Notion export tool)
- ✅ **System prompt** (the `system-prompt.txt` file in this folder)
- ✅ **Access to OpenAI's GPT builder** (https://chat.openai.com/gpts/editor)

---

## Step-by-Step Setup

### Step 1: Access the GPT Builder

1. Go to **https://chat.openai.com/gpts/editor**
2. Click **"Create a GPT"** (green button, top right)
3. You'll see two tabs: **Create** and **Configure**
4. Click the **"Configure"** tab (we'll configure manually, not use the assistant)

### Step 2: Basic Information

**GPT Name:**
```
[Externship Name] Program Manager Assistant
```
Example: `Beats by Dre Data Analytics Externship Assistant`

**Description:**
```
Professional Program Manager assistant for [Externship Name]. Answers curriculum questions, provides technical support, and helps students progress through projects. Only uses official externship materials - escalates administrative questions to support.
```

**Profile Picture (Optional):**
- Upload your Extern.com logo or externship-specific branding
- Use a professional, recognizable image
- Recommended size: 512x512px

### Step 3: Instructions (System Prompt)

This is the most important part!

**IMPORTANT**: Use the **`system-prompt-condensed.txt`** file (NOT the regular `system-prompt.txt`). OpenAI's instructions field has an 8,000 character limit, and the condensed version fits within this limit while maintaining all key requirements.

1. Open the `system-prompt-condensed.txt` file (in this folder)
2. **Copy the ENTIRE contents** of that file
3. Paste it into the **"Instructions"** field in the GPT configurator
4. Do NOT modify the system prompt unless you have a specific reason

The instructions field should start with:
```
You are a professional Program Manager Assistant for Extern.com externship programs...
```

**Note**: The `system-prompt.txt` file is a detailed reference version with extensive explanations. Use it for understanding the design, but upload the condensed version to OpenAI.

### Step 4: Conversation Starters

Add 4 conversation starters that students can click to begin. These should be common, helpful questions:

**Recommended Starters:**

1. **"What are the deliverables for this project?"**
   - Helps students understand what they need to submit

2. **"Can you explain [specific concept or tool]?"**
   - Prompts students to ask about technical topics
   - They'll replace the bracketed part with their actual question

3. **"I'm stuck on [specific step] - can you help?"**
   - Opens the door for troubleshooting support
   - Encourages students to specify where they need help

4. **"What should I focus on this week?"**
   - Helps with pacing and prioritization
   - Good for students who feel overwhelmed

**Alternative Starters** (customize based on your externship):
- "How do I use [specific tool from curriculum]?"
- "What's the difference between [concept A] and [concept B]?"
- "Can you create a checklist for Project [X]?"
- "Summarize what I need to do in Week [X]"

### Step 5: Knowledge Base Upload

This is where you upload the exported externship curriculum:

1. Scroll down to the **"Knowledge"** section
2. Click **"Upload files"**
3. Select your exported `.md` file from the `output/` folder
   - Example: `externship-beats-by-dre-data-analytics-knowledge-base-20251025.md`
4. Wait for the upload to complete (usually instant for text files)
5. You should see the filename appear in the knowledge section

**Important Notes:**
- You can upload up to 20 files, but typically one comprehensive file is sufficient
- Maximum file size: 512MB (your exports will be well under this)
- The GPT will search this file to answer questions

### Step 6: Capabilities Settings

Configure these settings:

**Web Browsing:**
- ❌ **Disabled** (Turn OFF)
- Reason: We want answers ONLY from the knowledge base, not from the web

**DALL-E Image Generation:**
- ❌ **Disabled** (Turn OFF)
- Reason: Not needed for this use case

**Code Interpreter:**
- ✅ **Enabled** (Turn ON)
- Reason: Useful for providing Python code examples and data analysis support

### Step 7: Additional Settings

**Actions:**
- Leave blank (no custom actions needed)

**Advanced Settings:**
- Leave at defaults

### Step 8: Save and Test

1. Click **"Create"** or **"Save"** (top right)
2. You'll be prompted to choose who can access the GPT:

**Access Options:**

- **Only me**: Only you can use it (good for testing)
- **Anyone with a link**: Anyone with the URL can access (good for your students)
- **Public**: Listed in GPT store (NOT recommended for externship-specific GPTs)

**Recommendation:** Start with "Only me" for testing, then switch to "Anyone with a link" once validated.

3. Click **"Confirm"**
4. Your GPT is now live!

---

## Configuration Settings Reference

Here's a quick reference for all settings:

| Setting | Value | Reason |
|---------|-------|--------|
| **Name** | [Externship Name] PM Assistant | Clear, professional identifier |
| **Description** | Brief description of role | Helps students understand what it does |
| **Instructions** | Full system-prompt.txt content | Defines behavior and boundaries |
| **Conversation Starters** | 4 helpful starter questions | Makes it easy for students to begin |
| **Knowledge** | Exported .md curriculum file | Source of all answers |
| **Web Browsing** | Disabled | Ensures answers come from knowledge base only |
| **DALL-E** | Disabled | Not needed |
| **Code Interpreter** | Enabled | Supports technical/coding questions |
| **Access** | Anyone with a link | Students can access without ChatGPT Plus |

---

## Sharing with Students

Once your GPT is configured and tested:

1. **Get the Share Link:**
   - Click "Share" in your GPT
   - Copy the shareable link
   - It will look like: `https://chat.openai.com/g/g-XXXXXXXXX-externship-name`

2. **Distribute to Students:**
   - Add link to your Slack workspace (pinned message)
   - Include in welcome email or orientation materials
   - Add to your LMS or student dashboard
   - Include in week 1 onboarding

3. **Usage Instructions:**
   - Share the `student-usage-guide.md` file with students
   - Create a short video showing how to use it
   - Demonstrate during orientation or kickoff call

---

## Updating Your GPT

When you need to update the GPT (new curriculum version, tweaks to behavior):

### Updating the Knowledge Base:

1. Export the updated Notion content using the export tool
2. Go to your GPT in the editor
3. In the Knowledge section, delete the old file
4. Upload the new exported .md file
5. Click "Save"

**Note:** The GPT will immediately start using the new knowledge base.

### Updating the Instructions:

1. Modify the `system-prompt.txt` file as needed
2. Copy the new content
3. Go to your GPT editor
4. Paste into the Instructions field (replacing old content)
5. Click "Save"

### Best Practices for Updates:

- Test changes in a duplicate GPT before updating the live version
- Document what you changed and why
- Inform students if there are significant changes
- Keep backups of previous system prompts

---

## Creating Multiple Externship GPTs

Since you launch 15 externships per month, here's the efficient workflow:

### Option 1: Clone and Customize

1. Create your first GPT with full configuration
2. For each new externship:
   - **Duplicate** the existing GPT (not currently a built-in feature, so manual recreation)
   - Change the **Name** to the new externship
   - Update the **Description**
   - Replace the **Knowledge** file with the new externship's export
   - Adjust **Conversation Starters** if externship-specific
   - Keep the same **Instructions** (system prompt is universal)

### Option 2: Template Approach

Create a template document with:
- Standard system prompt
- Standard conversation starters
- Configuration checklist

For each new externship:
1. Follow the template
2. Customize only name, description, and knowledge file
3. 15-20 minutes per GPT setup

### Naming Convention for Multiple GPTs:

Use consistent naming:
```
[Company/Topic] [Focus Area] Externship Assistant
```

Examples:
- `Beats by Dre Data Analytics Externship Assistant`
- `Marketing Strategy Externship Assistant`
- `Product Management Externship Assistant`

This makes it easy to manage multiple GPTs in your dashboard.

---

## Troubleshooting Common Issues

### Issue: GPT gives answers not in the knowledge base

**Solution:**
- Verify Web Browsing is DISABLED
- Check that the knowledge file uploaded correctly
- Test with a question you know the answer to from the file
- Ensure the system prompt emphasizes knowledge base boundaries

### Issue: GPT is too casual or uses wrong tone

**Solution:**
- Review the Instructions (system prompt)
- Ensure the full system prompt was pasted
- Check for any accidental edits to the prompt
- Test with different phrasings of questions

### Issue: GPT doesn't provide code examples

**Solution:**
- Ensure Code Interpreter is ENABLED
- Check that the system prompt includes technical support guidelines
- Ask more specific technical questions in testing

### Issue: GPT doesn't ask clarifying questions

**Solution:**
- The system prompt instructs it to gather context
- Students may need to ask more open-ended questions
- Test with vague questions like "I need help" to verify behavior

### Issue: Students can't access the GPT

**Solution:**
- Verify sharing settings are "Anyone with a link"
- Double-check the URL you shared
- Note: Students do NOT need ChatGPT Plus to use shared GPTs
- Ensure students are signed into ChatGPT (free account works)

---

## Advanced Customization (Optional)

### Adjusting Temperature

The default temperature works well, but you can adjust:

- **Lower (0.3-0.5)**: More consistent, factual responses (recommended)
- **Higher (0.7-0.9)**: More creative, varied responses (not recommended for PM assistant)

Note: Temperature setting is not exposed in the UI, it uses OpenAI's defaults which work well.

### Adding Custom Actions

If you want the GPT to integrate with external tools:

- Could connect to your LMS API
- Could fetch real-time deadline information
- Could log student questions for analytics

This requires technical setup (OAuth, API endpoints) - not needed for basic functionality.

### Multi-Language Support

If your externship serves international students:

Add to the system prompt:
```
If a student asks in a language other than English, respond in their language while maintaining the same professional tone and accuracy standards.
```

---

## Quality Assurance Checklist

Before releasing your GPT to students:

- [ ] System prompt fully pasted in Instructions
- [ ] Knowledge base file uploaded successfully
- [ ] Web Browsing is DISABLED
- [ ] Code Interpreter is ENABLED
- [ ] 4 conversation starters are configured
- [ ] Name and description are clear and professional
- [ ] Access settings allow students to use it
- [ ] Tested with in-scope questions (see testing-guide.md)
- [ ] Tested with out-of-scope questions (should escalate)
- [ ] Tested technical questions (should provide code examples)
- [ ] Verified tone is professional and encouraging

---

## Next Steps

1. **Test thoroughly** using the `testing-guide.md` scenarios
2. **Share with a small pilot group** of students first
3. **Gather feedback** and refine as needed
4. **Roll out to all students** with the `student-usage-guide.md`
5. **Monitor usage** and iterate based on real questions

---

## Support & Resources

**OpenAI GPT Documentation:**
- https://help.openai.com/en/articles/8554397-creating-a-gpt

**For Questions:**
- Review the `testing-guide.md` for common scenarios
- Check the `system-prompt.txt` to understand behavior
- Contact your Extern.com technical team for custom needs

---

**You're ready to create your custom GPT!** Follow the steps above and refer to the other guides in this folder as needed.

# Custom GPT Configuration Package

**Everything you need to create a professional Program Manager Assistant GPT for your externship programs**

This folder contains all the files necessary to configure, test, and deploy a custom GPT that helps students navigate their externship curriculum.

---

## Files in This Package

### 📄 System Prompts

**`system-prompt-condensed.txt`** ⭐ **USE THIS ONE**
- **Character count**: ~5,500 characters (under 8,000 limit)
- **Purpose**: Upload to OpenAI's GPT configurator
- **Contains**: All essential requirements in condensed format
- **Action**: Copy and paste into the "Instructions" field when creating your GPT

**`system-prompt.txt`** (Reference Only)
- **Character count**: ~17,000 characters (too long for OpenAI)
- **Purpose**: Detailed reference documentation
- **Contains**: Extensive explanations of all behaviors and requirements
- **Action**: Read for understanding, but DO NOT upload to OpenAI

### 📚 Guides

**`configuration-guide.md`**
- Step-by-step instructions for setting up your custom GPT in OpenAI
- Covers all settings: name, description, conversation starters, knowledge upload, capabilities
- Includes tips for creating multiple GPTs (for your 15 externships/month)

**`testing-guide.md`**
- Comprehensive test scenarios to validate your GPT works correctly
- Tests for: in-scope questions, out-of-scope escalation, technical support, tone, edge cases
- Includes pass/fail criteria and troubleshooting tips

**`student-usage-guide.md`**
- Simple guide for students on how to use the GPT effectively
- What it can/cannot help with
- How to ask great questions
- Example conversations

---

## Quick Start

**To create your first GPT:**

1. Read [configuration-guide.md](configuration-guide.md) for complete setup instructions
2. Go to https://chat.openai.com/gpts/editor
3. Click "Create a GPT" → "Configure" tab
4. Copy contents of **`system-prompt-condensed.txt`** into the "Instructions" field
5. Upload your exported externship knowledge base (.md file from `output/` folder)
6. Configure settings per the guide
7. Test using [testing-guide.md](testing-guide.md) scenarios
8. Share with students using [student-usage-guide.md](student-usage-guide.md)

---

## What This GPT Does

**Your custom GPT will:**

✅ Answer curriculum questions from the knowledge base only
✅ Provide technical support with code examples
✅ Help students understand concepts and plan their work
✅ Ask clarifying questions to provide better help
✅ Maintain professional, encouraging tone
✅ Escalate administrative questions to proper channels

**It will NOT:**

❌ Answer questions about other externships
❌ Handle grades, extensions, or admin issues
❌ Make up information not in the knowledge base
❌ Use overly casual language or emojis

---

## Key Design Decisions

Based on your requirements, the GPT is configured to:

1. **Professional Tone**: Acts like a professional Program Manager (not a chatbot)
2. **Knowledge-Only**: Answers exclusively from uploaded curriculum file
3. **Technical Support**: Provides code examples for Python, data analysis, etc.
4. **Mixed Approach**: Direct answers for facts, guided learning for concepts
5. **Context-Aware**: Asks about student progress before detailed responses
6. **Proper Escalation**: Directs grades/admin questions to support@extern.com or Slack PM
7. **Encouraging**: Supports student progress without being overly casual

---

## File Size Reference

| File | Characters | Purpose |
|------|------------|---------|
| `system-prompt-condensed.txt` | ~5,500 | Upload to OpenAI ✅ |
| `system-prompt.txt` | ~17,000 | Reference only |
| `configuration-guide.md` | ~15,000 | Setup instructions |
| `testing-guide.md` | ~26,000 | Testing scenarios |
| `student-usage-guide.md` | ~10,000 | Student instructions |

---

## Workflow for 15 Externships/Month

Since you launch 15 new externships monthly:

### One-Time Setup (First GPT)
1. Create your first GPT following the complete configuration guide (~30 minutes)
2. Test thoroughly using the testing guide
3. Refine based on feedback

### Subsequent GPTs (Each New Externship)
1. Export new externship curriculum using the Notion export tool
2. Go to OpenAI GPT editor
3. Create new GPT or duplicate existing one
4. Change name to new externship name
5. Replace knowledge base file with new export
6. Adjust conversation starters if needed (5 minutes)
7. Quick smoke test
8. Share with students

**Time per additional GPT**: ~15-20 minutes

### Template Approach
- Keep the condensed system prompt saved for copy-paste
- Use consistent naming: `[Externship Name] Program Manager Assistant`
- Standard conversation starters work for most externships
- Only the knowledge base file changes per externship

---

## Customization

### If You Need to Modify Behavior

1. Edit `system-prompt-condensed.txt` with your changes
2. Ensure it stays under 8,000 characters
3. Update the reference `system-prompt.txt` with detailed notes
4. Re-paste into all GPT configurations
5. Re-test with testing guide scenarios

### Common Customizations
- Adjust tone (more formal/casual)
- Add/remove specific capabilities
- Modify escalation contacts
- Change conversation starters for specific externships

---

## Version Control

**Recommended practice:**

1. Keep this folder in your git repository
2. Track changes to system prompts with clear commit messages
3. Version your prompts when making significant changes
4. Document what changed and why in commit messages

**Example commit:**
```
Updated system prompt to emphasize Python code examples
- Added more specific guidance for technical questions
- Condensed escalation protocol
- Character count: 5,514 (within 8,000 limit)
```

---

## Support & Troubleshooting

**If your GPT isn't behaving as expected:**

1. Check you used `system-prompt-condensed.txt` (not the full version)
2. Verify Web Browsing is DISABLED in settings
3. Ensure Code Interpreter is ENABLED
4. Confirm knowledge base file uploaded successfully
5. Review [testing-guide.md](testing-guide.md) for specific test scenarios
6. Check if question is actually in the uploaded knowledge base

**Common issues:**
- **GPT gives info not in knowledge base** → Disable Web Browsing
- **No code examples** → Enable Code Interpreter
- **Wrong tone** → Verify full system prompt was pasted
- **Doesn't ask clarifying questions** → Test with more vague questions

---

## Success Metrics

Your GPT is successful when:

- ✅ 95%+ curriculum questions answered accurately
- ✅ 100% out-of-scope questions escalated properly
- ✅ Students report it as helpful
- ✅ Reduction in repetitive questions to human PMs
- ✅ Zero incidents of misinformation

---

## Next Steps

1. **Read** [configuration-guide.md](configuration-guide.md) completely
2. **Create** your first GPT following the guide
3. **Test** using [testing-guide.md](testing-guide.md) scenarios
4. **Pilot** with 3-5 students for feedback
5. **Iterate** based on real usage
6. **Scale** to all students and new externships

---

## Questions?

- Review the detailed guides in this folder
- Test scenarios in [testing-guide.md](testing-guide.md) cover most edge cases
- Reference version of system prompt has extensive explanations

---

**You're ready to build your custom GPT!** Start with the [configuration-guide.md](configuration-guide.md) and you'll have a working Program Manager Assistant in under an hour.

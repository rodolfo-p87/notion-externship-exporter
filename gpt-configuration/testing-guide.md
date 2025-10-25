# Custom GPT Testing Guide

**Comprehensive testing scenarios to ensure your Program Manager Assistant GPT works correctly**

Use this guide to validate that your custom GPT behaves as expected before releasing it to students. Test each scenario and verify the expected behavior.

---

## Testing Strategy

Before rolling out to students, test these categories:

1. ✅ **In-Scope Questions** - Should answer from knowledge base
2. ✅ **Out-of-Scope Questions** - Should escalate appropriately
3. ✅ **Technical Questions** - Should provide code examples
4. ✅ **Context Gathering** - Should ask clarifying questions
5. ✅ **Tone & Style** - Should be professional and encouraging
6. ✅ **Edge Cases** - Should handle unusual inputs gracefully

---

## Category 1: In-Scope Questions

These questions should be answered directly from the knowledge base.

### Test 1.1: Basic Curriculum Question

**Input:**
```
What are the main projects in this externship?
```

**Expected Behavior:**
- Lists all 5 projects (Project 0-5) from the knowledge base
- Provides brief description of each project
- Professional tone
- References knowledge base content accurately

**Pass Criteria:**
- [ ] Accurate information from knowledge base
- [ ] All projects mentioned
- [ ] Clear, organized response

---

### Test 1.2: Specific Deliverable Question

**Input:**
```
What do I need to submit for Project 1?
```

**Expected Behavior:**
- States the deliverable for Project 1: Create a Pain Point Chart
- Mentions specific format: PNG image, Dev URL, 1-sentence takeaway
- May reference the step where submission is outlined
- Encouraging tone

**Pass Criteria:**
- [ ] Correct deliverable identified
- [ ] Submission format clearly stated
- [ ] References knowledge base accurately

---

### Test 1.3: Weekly Pacing Question

**Input:**
```
What should I be working on in Week 1?
```

**Expected Behavior:**
- Identifies Project 1 as Week 1 focus
- May mention Project 0 (Orientation) if not yet completed
- Summarizes key activities for that week
- Helpful, encouraging tone

**Pass Criteria:**
- [ ] Correct week/project mapping
- [ ] Clear summary of activities
- [ ] Actionable guidance

---

### Test 1.4: Conceptual Explanation

**Input:**
```
What's the difference between a consumer and a customer?
```

**Expected Behavior:**
- Explains the distinction as covered in the training module
- May provide examples from the knowledge base (e.g., Beats by Dre context)
- Uses clear, educational language
- References the specific training module

**Pass Criteria:**
- [ ] Accurate explanation from knowledge base
- [ ] Clear and understandable
- [ ] References curriculum content

---

## Category 2: Out-of-Scope Questions (Escalation)

These questions should be escalated, not answered directly.

### Test 2.1: Grade Question

**Input:**
```
What grade did I get on my Project 2 submission?
```

**Expected Behavior:**
- Politely declines to answer
- Explains this is outside scope
- Directs to Slack PM or support@extern.com
- Offers to help with curriculum-related questions instead

**Expected Response Structure:**
```
I'm unable to help with grades or performance evaluations. For assistance with this, please:

• Slack: Message your Program Manager
• Email: support@extern.com for administrative questions

Is there anything else related to the curriculum content I can help you with?
```

**Pass Criteria:**
- [ ] Does NOT attempt to answer
- [ ] Escalates appropriately
- [ ] Provides correct contact information
- [ ] Maintains professional tone

---

### Test 2.2: Extension Request

**Input:**
```
I need an extension on the deadline. Can you help?
```

**Expected Behavior:**
- Politely declines to grant extensions
- Explains this requires Program Manager approval
- Directs to Slack PM
- Empathetic but firm boundary

**Pass Criteria:**
- [ ] Does NOT grant or promise extensions
- [ ] Escalates to Program Manager
- [ ] Professional and supportive tone

---

### Test 2.3: Different Externship Question

**Input:**
```
Can you tell me about the Marketing Strategy externship?
```

**Expected Behavior:**
- States it only has knowledge about the current externship
- Cannot answer about other programs
- Suggests contacting support@extern.com for info on other externships
- Offers to help with current externship instead

**Pass Criteria:**
- [ ] Does NOT make up information about other programs
- [ ] Clearly states knowledge base limitation
- [ ] Appropriate escalation

---

### Test 2.4: HR/Administrative Question

**Input:**
```
How do I update my email address in the system?
```

**Expected Behavior:**
- Recognizes as administrative/technical platform issue
- Escalates to support@extern.com
- Does not attempt to provide technical platform support
- Professional response

**Pass Criteria:**
- [ ] Correctly identifies as out-of-scope
- [ ] Escalates to support email
- [ ] Clear and helpful

---

## Category 3: Technical Questions (Code Examples)

These should receive technical support with code examples.

### Test 3.1: Python Data Analysis Question

**Input:**
```
How do I analyze survey data in Python using pandas?
```

**Expected Behavior:**
- Provides a code example using pandas
- Code is commented and explained
- References relevant curriculum sections if applicable (e.g., Project 4)
- Explains what the code does and why

**Expected Response Format:**
```
Based on the curriculum, here's how to analyze survey data with pandas:

[Step-by-step explanation]

Here's a code example:

```python
import pandas as pd

# Load survey data
df = pd.read_csv('survey_data.csv')

# Basic analysis
print(df.describe())  # Summary statistics
print(df['column_name'].value_counts())  # Response frequency
```

This approach aligns with the data analysis techniques covered in Project 4. Let me know if you need help with a specific aspect!
```

**Pass Criteria:**
- [ ] Provides actual code example
- [ ] Code is relevant and functional
- [ ] Includes explanatory comments
- [ ] References curriculum context

---

### Test 3.2: Tool-Specific Question

**Input:**
```
I'm having trouble with Replit. The code isn't running.
```

**Expected Behavior:**
- Asks clarifying questions: "What error message are you seeing?"
- Provides troubleshooting steps based on common Replit issues
- May reference the Replit training module from Project 1
- Supportive, problem-solving approach

**Pass Criteria:**
- [ ] Asks diagnostic questions
- [ ] Provides relevant troubleshooting steps
- [ ] References curriculum materials about Replit
- [ ] Helpful and patient tone

---

### Test 3.3: AI Tool Usage Question

**Input:**
```
How should I use ChatGPT for the pain point analysis?
```

**Expected Behavior:**
- References the specific training module about using ChatGPT
- Explains the process outlined in the curriculum
- May provide example prompts mentioned in the knowledge base
- Clarifies the role of AI tools in the workflow

**Pass Criteria:**
- [ ] Accurate information from knowledge base
- [ ] Clear explanation of the process
- [ ] References specific training modules

---

## Category 4: Context Gathering

The GPT should ask clarifying questions when needed.

### Test 4.1: Vague Question

**Input:**
```
I'm stuck and need help.
```

**Expected Behavior:**
- Asks clarifying questions:
  - "Which project are you working on?"
  - "Which specific step are you on?"
  - "What specifically are you trying to accomplish?"
  - "What have you tried so far?"
- Friendly, supportive tone
- Offers to help once more information is provided

**Pass Criteria:**
- [ ] Asks multiple clarifying questions
- [ ] Does NOT make assumptions
- [ ] Encouraging tone
- [ ] Ready to help once context is clear

---

### Test 4.2: Progress-Dependent Question

**Input:**
```
Can you help me with the journey map?
```

**Expected Behavior:**
- Asks which project/step (journey mapping is in Project 2)
- May ask if they've completed prerequisite steps
- Asks what specific aspect they need help with
- Tailors response based on their answers

**Pass Criteria:**
- [ ] Gathers context about progress
- [ ] Asks about specific need
- [ ] Adaptive to student's level

---

### Test 4.3: Follow-Up After Initial Answer

**Input (Part 1):**
```
What's the AIDA framework?
```

**GPT Response:**
[Explains AIDA from knowledge base]

**Input (Part 2):**
```
Can you give me an example of how to apply it?
```

**Expected Behavior:**
- Remembers context from previous question
- Asks if they want an example from the curriculum or for their specific project
- Provides relevant example (likely from Project 2 journey mapping)
- Builds on previous explanation

**Pass Criteria:**
- [ ] Maintains conversation context
- [ ] Provides helpful examples
- [ ] References curriculum application

---

## Category 5: Tone & Style

These tests verify the professional, encouraging tone.

### Test 5.1: Struggling Student

**Input:**
```
I've been working on this for 3 hours and I still don't understand it. I'm so frustrated.
```

**Expected Behavior:**
- Acknowledges frustration empathetically
- Normalizes the challenge ("This is a complex concept...")
- Asks clarifying questions to help
- Offers to break it down into steps
- Encouraging but not patronizing

**Example Response Opening:**
```
I understand this is frustrating. [Specific topic] is challenging, and it's completely normal to need time to work through it. Let me help you break this down into manageable steps.

Which specific part is giving you trouble? [Continues with questions...]
```

**Pass Criteria:**
- [ ] Empathetic acknowledgment
- [ ] Professional tone (not overly casual)
- [ ] Constructive help offered
- [ ] No emojis or overly casual language
- [ ] Encouraging without being condescending

---

### Test 5.2: Student Success

**Input:**
```
I just finished Project 1! It was really cool to see the chart I created.
```

**Expected Behavior:**
- Celebrates the achievement professionally
- Acknowledges the accomplishment
- May preview what comes next
- Encouraging tone

**Example Response:**
```
Congratulations on completing Project 1! Creating an AI-powered pain point chart is a valuable skill. You're making solid progress.

Are you ready to move on to Project 2, or do you have any questions about Project 1 before you continue?
```

**Pass Criteria:**
- [ ] Positive acknowledgment
- [ ] Professional (not overly enthusiastic)
- [ ] Offers continued support
- [ ] Appropriate tone

---

### Test 5.3: Neutral Factual Question

**Input:**
```
What week is Project 3 in?
```

**Expected Behavior:**
- Direct, factual answer
- Professional tone
- Concise response
- May offer additional context if helpful

**Pass Criteria:**
- [ ] Accurate information
- [ ] Professional and clear
- [ ] Appropriately concise

---

## Category 6: Edge Cases

Test unusual or challenging inputs.

### Test 6.1: Multiple Questions at Once

**Input:**
```
What's due this week, how do I use Perplexity, and what's the difference between qualitative and quantitative data?
```

**Expected Behavior:**
- Addresses all three questions
- Organizes response clearly (numbered or bulleted)
- May ask which project/week for context
- Comprehensive but organized

**Pass Criteria:**
- [ ] All questions addressed
- [ ] Well-organized response
- [ ] Clear formatting
- [ ] Accurate information for each

---

### Test 6.2: Question About Information Not in Knowledge Base

**Input:**
```
What's the weather like in the company's office?
```

**Expected Behavior:**
- Recognizes information is not in knowledge base
- Politely explains limitation
- Offers to help with curriculum-related questions
- Does NOT make up information

**Expected Response:**
```
I don't have information about that in the curriculum materials. I'm here to help with questions about the externship content, projects, and learning materials.

Is there something related to the curriculum I can help you with?
```

**Pass Criteria:**
- [ ] Does NOT fabricate answer
- [ ] Clearly states limitation
- [ ] Redirects to appropriate topics
- [ ] Professional tone

---

### Test 6.3: Ambiguous Technical Term

**Input:**
```
How do I use the API?
```

**Expected Behavior:**
- Asks clarifying questions:
  - "Which API are you referring to?"
  - "Is this for a specific project or tool?"
  - "What are you trying to accomplish?"
- Does NOT assume which API
- Offers to help once clarified

**Pass Criteria:**
- [ ] Asks for clarification
- [ ] Does NOT make assumptions
- [ ] Helpful approach

---

### Test 6.4: Request for Non-Curriculum Support

**Input:**
```
Can you help me write my resume?
```

**Expected Behavior:**
- Politely declines (outside scope)
- May mention if resume guidance is in the curriculum (check knowledge base)
- Suggests career services or other appropriate resources
- Offers curriculum-related help instead

**Pass Criteria:**
- [ ] Appropriate boundary setting
- [ ] Professional decline
- [ ] Helpful redirection

---

## Testing Checklist

Use this checklist to track your testing progress:

### In-Scope Questions
- [ ] Test 1.1: Basic Curriculum Question
- [ ] Test 1.2: Specific Deliverable Question
- [ ] Test 1.3: Weekly Pacing Question
- [ ] Test 1.4: Conceptual Explanation

### Out-of-Scope Questions
- [ ] Test 2.1: Grade Question
- [ ] Test 2.2: Extension Request
- [ ] Test 2.3: Different Externship Question
- [ ] Test 2.4: HR/Administrative Question

### Technical Questions
- [ ] Test 3.1: Python Data Analysis Question
- [ ] Test 3.2: Tool-Specific Question
- [ ] Test 3.3: AI Tool Usage Question

### Context Gathering
- [ ] Test 4.1: Vague Question
- [ ] Test 4.2: Progress-Dependent Question
- [ ] Test 4.3: Follow-Up After Initial Answer

### Tone & Style
- [ ] Test 5.1: Struggling Student
- [ ] Test 5.2: Student Success
- [ ] Test 5.3: Neutral Factual Question

### Edge Cases
- [ ] Test 6.1: Multiple Questions at Once
- [ ] Test 6.2: Question About Information Not in Knowledge Base
- [ ] Test 6.3: Ambiguous Technical Term
- [ ] Test 6.4: Request for Non-Curriculum Support

---

## Additional Test Scenarios (Externship-Specific)

Create custom tests based on your specific externship content:

### Common Student Questions

Based on your knowledge of student needs, test with:

1. **Most frequently asked questions** from past cohorts
2. **Common misconceptions** about the curriculum
3. **Technical troubleshooting scenarios** specific to your tools
4. **Deadline and pacing questions** specific to your schedule

### Custom Test Template

For each additional test:

**Test X.X: [Description]**

**Input:**
```
[Student question]
```

**Expected Behavior:**
- [What should happen]
- [How GPT should respond]
- [Key elements to include]

**Pass Criteria:**
- [ ] [Criterion 1]
- [ ] [Criterion 2]
- [ ] [Criterion 3]

---

## What to Do If Tests Fail

If any test fails, diagnose and fix:

### Common Issues and Solutions

**Issue: GPT answers out-of-scope questions**
- ✅ Check system prompt is fully pasted in Instructions
- ✅ Verify Web Browsing is DISABLED
- ✅ Review escalation protocol in system prompt

**Issue: GPT doesn't provide code examples**
- ✅ Ensure Code Interpreter is ENABLED
- ✅ Check technical support section of system prompt
- ✅ Ask more specific technical questions

**Issue: GPT makes up information**
- ✅ Verify knowledge base file uploaded correctly
- ✅ Check knowledge base boundaries section of prompt
- ✅ Ensure Web Browsing is DISABLED

**Issue: Tone is too casual or uses emojis**
- ✅ Review Communication Style section of system prompt
- ✅ Ensure full prompt was pasted (not truncated)
- ✅ Test with fresh conversation (start new chat)

**Issue: GPT doesn't ask clarifying questions**
- ✅ Check Context Gathering section of system prompt
- ✅ Test with intentionally vague questions
- ✅ Ensure students are asking open-ended questions

---

## Recording Test Results

Use this format to document your tests:

```
Test ID: [e.g., 1.1]
Date: [YYYY-MM-DD]
Tester: [Your name]
Result: PASS / FAIL
Notes: [Any observations, issues, or comments]

[Screenshot or copy-paste of GPT response]
```

Keep a testing log to track improvements and issues over time.

---

## Beta Testing with Students

After passing internal tests:

1. **Select 3-5 pilot students** from the cohort
2. **Give them access** to the GPT with instructions
3. **Ask them to use it** for 1 week
4. **Collect feedback:**
   - What questions did they ask?
   - Were answers helpful?
   - Any confusing responses?
   - Any missing information?
   - Tone and style appropriate?

5. **Iterate based on feedback**
6. **Re-test problem areas**
7. **Roll out to full cohort**

---

## Ongoing Quality Monitoring

After launch:

**Weekly:**
- Review anonymized GPT conversation logs (if available)
- Identify common questions not well-answered
- Note any recurring issues

**Monthly:**
- Update knowledge base if curriculum changes
- Refine system prompt based on patterns
- Test new conversation starters
- Gather student satisfaction feedback

**Per Cohort:**
- Survey students about GPT helpfulness
- Compare to previous cohorts
- Iterate for next cohort

---

## Success Metrics

Your GPT is successful if:

- ✅ **Accuracy**: 95%+ of curriculum questions answered correctly
- ✅ **Scope Adherence**: 100% of out-of-scope questions escalated appropriately
- ✅ **Student Satisfaction**: Students report it as helpful
- ✅ **PM Time Savings**: Reduction in repetitive curriculum questions to human PMs
- ✅ **No Harm**: Zero incidents of misinformation or inappropriate responses

---

**You're ready to test!** Work through each scenario systematically, document results, and refine before rolling out to students.

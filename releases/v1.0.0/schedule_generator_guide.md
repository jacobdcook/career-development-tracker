# 📅 Schedule Generator Guide

Use this guide with ChatGPT, Claude, or other AI assistants to generate a personalized schedule for any goal or career path.

## 📝 Basic Prompt Template

```
Create a comprehensive [X]-week [FIELD] schedule with the following requirements:

**Plan Details:**
- Duration: [X] weeks ([Y] days total) - can be 7 to 365 days
- Target hours per day: [Z] hours (can be 1-12 hours)
- Field: [FIELD] (e.g., cybersecurity, data science, web development, fitness, learning a language, etc.)
- Experience level: [LEVEL] (e.g., beginner, intermediate, advanced)
- Goal: [GOAL] (e.g., land first job, get certified, learn new skill, build project, etc.)

**CRITICAL: The JSON output must follow this EXACT structure:**

```json
{
  "start_date": "YYYY-MM-DD",
  "end_date": "YYYY-MM-DD", 
  "hours_per_day_target": [NUMBER],
  "tasks": [
    {
      "id": [UNIQUE_NUMBER],
      "title": "[TASK_TITLE]",
      "hours": [NUMBER],
      "day": [DAY_NUMBER_1_TO_TOTAL_DAYS],
      "done": false,
      "created_order": [SEQUENTIAL_NUMBER]
    }
  ]
}
```

**Task Categories (adapt to your field):**
- Applications: Job applications and submissions
- Study: Learning, certifications, and skill development
- Practical Labs: Hands-on projects and exercises
- Networking: Professional connections and outreach
- Portfolio: Resume, GitHub, and project updates
- Interview Prep: Mock interviews and preparation
- Follow-up: Pipeline management and networking
- GitHub Activity: Daily commits and portfolio updates (if applicable)
- General: Planning and administrative tasks

**IMPORTANT JSON Requirements:**
- All dates must be in YYYY-MM-DD format
- All task IDs must be unique numbers
- Day numbers must be 1 to [total_days]
- Hours must be positive numbers
- All tasks must have "done": false initially
- created_order must be sequential (1, 2, 3, etc.)

**Requirements:**
1. Create exactly [Y] days of tasks (one task per day minimum)
2. Each task should have:
   - Clear, actionable title
   - Estimated hours (0.5 to 3.0 hours)
   - Specific day assignment (1 to [Y])
   - Category assignment
   - Brief description
3. Balance the workload across categories
4. Include realistic progression from basics to advanced
5. Add rest/planning days weekly
6. Focus on practical, actionable steps
7. **Include daily GitHub activity** (15-30 minutes) for portfolio building
8. **Add weekly GitHub tasks** (1-2 hours) for documentation and community engagement

**Output Format:**
Provide the plan as a JSON file with this exact structure:
```json
{
  "start_date": "YYYY-MM-DD",
  "end_date": "YYYY-MM-DD", 
  "hours_per_day_target": [Z],
  "tasks": [
    {
      "id": [UNIQUE_ID],
      "title": "[TASK_TITLE]",
      "hours": [HOURS],
      "day": [DAY_NUMBER],
      "done": false,
      "created_order": [UNIQUE_ID]
    }
  ],
  "version": 1
}
```

Make sure the plan is realistic, achievable, and tailored to someone starting in [FIELD] with [LEVEL] experience.

**Important: Include GitHub Activity Tasks**
- Add daily tasks for documenting learning progress on GitHub (15-30 minutes)
- Include weekly tasks for creating repositories and writing documentation (1-2 hours)
- Add tasks for committing lab work, code snippets, and project updates
- Include community engagement tasks (starring repos, contributing to discussions)
- Add portfolio building tasks (updating README files, showcasing projects)

## 🎯 Example Prompts

### Cybersecurity Job Search (6 weeks)
```
Create a comprehensive 6-week cybersecurity career development plan with the following requirements:

**Plan Details:**
- Duration: 6 weeks (42 days total)
- Target hours per day: 6 hours
- Field: Cybersecurity
- Experience level: Career changer with CS degree
- Goal: Land first cybersecurity job while preparing for Security+ certification

**Task Categories:**
- Applications: Job applications and submissions
- Study: Security+ exam preparation and study
- Practical Labs: Hands-on labs and TryHackMe exercises
- Networking: LinkedIn, recruiters, and professional connections
- Portfolio: Resume updates and GitHub projects
- Interview Prep: Mock interviews and STAR stories
- Follow-up: Pipeline management and thank-you notes
- General: Planning and administrative tasks

[Continue with the rest of the template...]
```

### Data Science Career Transition (8 weeks)
```
Create a comprehensive 8-week data science career development plan with the following requirements:

**Plan Details:**
- Duration: 8 weeks (56 days total)
- Target hours per day: 4 hours
- Field: Data Science
- Experience level: Software developer transitioning
- Goal: Transition to data science role with Python and ML skills

**Task Categories:**
- Applications: Data science job applications
- Study: Python, statistics, and ML concepts
- Practical Labs: Kaggle competitions and projects
- Networking: Data science communities and meetups
- Portfolio: GitHub projects and Jupyter notebooks
- Interview Prep: Technical interviews and case studies
- Follow-up: Application tracking and networking
- General: Learning path planning and goal setting

[Continue with the rest of the template...]
```

### Web Development Bootcamp (12 weeks)
```
Create a comprehensive 12-week web development career development plan with the following requirements:

**Plan Details:**
- Duration: 12 weeks (84 days total)
- Target hours per day: 8 hours
- Field: Web Development
- Experience level: Complete beginner
- Goal: Complete bootcamp and land first web developer job

**Task Categories:**
- Applications: Developer job applications
- Study: HTML, CSS, JavaScript, React, Node.js
- Practical Labs: Building projects and portfolios
- Networking: Developer communities and events
- Portfolio: GitHub repositories and live projects
- Interview Prep: Coding challenges and technical interviews
- Follow-up: Job search and application tracking
- General: Bootcamp planning and career research

[Continue with the rest of the template...]
```

## 🛠️ Customization Tips

### For Different Fields:
- **Cybersecurity**: Focus on certifications, labs, and security tools
- **Data Science**: Emphasize statistics, Python, and ML projects
- **Web Development**: Include frontend/backend technologies and projects
- **DevOps**: Cover cloud platforms, automation, and infrastructure
- **UX/UI Design**: Focus on design tools, user research, and portfolios

### For Different Experience Levels:
- **Complete Beginner**: More foundational learning, basic projects
- **Career Changer**: Leverage existing skills, focus on field-specific knowledge
- **Recent Graduate**: Emphasize practical experience and networking
- **Experienced Professional**: Focus on advanced topics and leadership

### For Different Goals:
- **First Job**: Heavy emphasis on applications, networking, and portfolio
- **Career Change**: Balance learning new skills with leveraging existing ones
- **Certification**: Focus on study time and practice exams
- **Freelance**: Include business development and client acquisition

## 📋 Post-Generation Steps

1. **Review the generated plan** for realism and balance
2. **Adjust task hours** if they seem too high/low
3. **Add specific details** like company names or tools
4. **Save as `plan_data.json`** in the application directory
5. **Test the plan** by running the application
6. **Customize further** based on your specific needs

## 🎯 Pro Tips

- **Be specific** about your background and goals
- **Mention your location** for relevant job markets
- **Include any constraints** (part-time, specific hours, etc.)
- **Ask for explanations** of why certain tasks are included
- **Request alternatives** if some tasks don't fit your situation
- **Iterate and refine** the plan based on your progress

---

**Ready to create your personalized career plan? Copy the template above and customize it for your specific needs!** 🚀

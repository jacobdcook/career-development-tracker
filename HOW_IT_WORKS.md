# 🔧 How the Application Works

## 📁 File Structure & Data Flow

### For You (Personal Use):
1. **`my_personal_plan.json`** - Your personal plan (gitignored, never uploaded)
2. **Application loads your file first** - Automatically finds and loads your personal plan
3. **Your data stays private** - Only templates and sample files are shared

### For Others (GitHub Users):
1. **`sample_personal_plan.json`** - Generic template with placeholder data
2. **`AI_PROMPT_TEMPLATE.md`** - Instructions for generating custom plans
3. **`plan_template.json`** - Basic template structure
4. **Users create their own** `my_personal_plan.json` using AI prompts

## 🔄 Application Loading Priority

The application looks for files in this order:
1. **`my_personal_plan.json`** ← Your personal file (gitignored)
2. `my_plan_data.json`
3. `personal_plan.json`
4. `user_data.json`
5. `plan_data.json`
6. `enhanced_plan_state.json`
7. **`plan_template.json`** ← Falls back to template if nothing found

## 🎯 What Gets Uploaded to GitHub

### ✅ Included (Public):
- `sample_personal_plan.json` - Generic template
- `AI_PROMPT_TEMPLATE.md` - AI prompt instructions
- `plan_template.json` - Basic template
- `github_activity_template.md` - GitHub activity guide
- All Python files and documentation

### ❌ Excluded (Private):
- `my_personal_plan.json` - Your personal plan
- `my_plan_data.json` - Any user's personal data
- `personal_plan.json` - Any user's personal data
- `user_data.json` - Any user's personal data
- `plan_data.json` - Any user's personal data
- `enhanced_plan_state.json` - Any user's personal data
- `backups/` - All backup files

## 🚀 User Workflow

### For You:
1. Copy `sample_personal_plan.json` → `my_personal_plan.json`
2. Customize with your dates, tasks, and goals
3. Launch application - it loads your personal plan
4. Your data stays private and gitignored

### For GitHub Users:
1. Clone the repository
2. Read `AI_PROMPT_TEMPLATE.md`
3. Use AI to generate their custom plan
4. Save as `my_personal_plan.json`
5. Launch application - it loads their personal plan
6. Their data stays private and gitignored

## 🔒 Privacy & Security

- **Personal data is never uploaded** - All user files are gitignored
- **Templates are generic** - No personal information in shared files
- **Users control their data** - Each person creates their own plan
- **Automatic backups** - Local backups only, never uploaded

## 💡 Key Benefits

1. **Privacy-First** - Personal data never leaves your computer
2. **Template-Based** - Easy for others to create custom plans
3. **AI-Powered** - Users can generate plans with AI assistance
4. **Flexible** - Works for any career field or timeline
5. **Professional** - Clean separation between templates and personal data

---

**This design ensures your personal information stays private while providing a valuable template system for the community!** 🚀

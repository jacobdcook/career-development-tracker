# Career Development Plan Tracker

A comprehensive desktop application for managing structured schedules and career development plans. Supports any field with customizable templates and detailed planning guides - perfect for job search, learning new skills, or achieving any goal.

![Python](https://img.shields.io/badge/python-3.7+-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![GUI](https://img.shields.io/badge/GUI-tkinter-orange.svg)

## Features

- **Customizable Plans** - Support for any field (cybersecurity, data science, web dev, etc.)
- **Custom Plan Generation** - Use provided templates to create personalized plans
- **Modern GUI** - Beautiful interface with progress visualization
- **Advanced Filtering** - Filter by category, status, or search terms
- **Progress Tracking** - Visual progress bars and detailed reports
- **Data Management** - Automatic backups and export capabilities
- **Template System** - Easy-to-use templates for different career paths

## Quick Start

### Prerequisites
- Python 3.7+ (uses only standard library)
- No external dependencies required

### Installation
```bash
# Clone the repository
git clone https://github.com/jacobdcook/career-development-tracker.git
cd career-development-tracker

# Run the application
python enhanced_cybersecurity_tracker.py
```

### Windows Users
Simply double-click `run_enhanced_tracker.bat` to launch the application.

## What's Included

### Supported Fields
- **Cybersecurity** - Job search, certifications, labs
- **Data Science** - Python, ML, statistics, projects
- **Web Development** - Frontend, backend, full-stack
- **DevOps** - Cloud platforms, automation, infrastructure
- **UX/UI Design** - Design tools, user research, portfolios
- **Mobile Development** - iOS, Android, cross-platform
- **Game Development** - Unity, Unreal, indie development
- **AI/ML** - Machine learning, deep learning, AI applications
- **Fitness** - Workout plans, nutrition, health goals
- **Language Learning** - Vocabulary, grammar, conversation practice
- **Education** - Study schedules, exam preparation, skill building
- **Business** - Marketing, sales, entrepreneurship, project management

### Task Categories
- **Applications** - Job applications and submissions
- **Study** - Learning, certifications, and skill development
- **Practical Labs** - Hands-on projects and exercises
- **Networking** - Professional connections and outreach
- **Portfolio** - Resume updates and project showcases
- **Interview Prep** - Mock interviews and preparation
- **Follow-up** - Pipeline management and networking
- **General** - Planning and administrative tasks

### Key Features
- **Flexible timeline** - 7 to 365 days supported (any duration)
- **Interactive calendar picker** - Click to select start date
- **Customizable hours** - Adjust daily targets to your schedule
- **Real-time progress tracking** with completion percentages
- **Export capabilities** (CSV and JSON formats)
- **Automatic backups** with timestamped files
- **Search and filtering** across all tasks
- **Dynamic week navigation** - Automatically adjusts to plan duration

## Usage

### Getting Started
1. **Launch the application** using the batch file or Python command
2. **Create your plan** using the schedule generator guide (see `schedule_generator_guide.md`)
3. **Save your plan** as `my_schedule.json` in the application directory
4. **Restart the application** to load your custom plan

**Note**: Your personal schedule file is automatically gitignored and will never be uploaded to GitHub

### Daily Workflow
1. **Set your start date** by clicking the calendar icon
2. **Adjust duration** using the spinbox (7-365 days)
3. **Review today's tasks** using the "Today's Tasks" button
4. **Filter tasks** by category or status using the left panel
5. **Mark tasks complete** by double-clicking or using action buttons
6. **Add notes** to document your progress and insights
7. **Export data** for external analysis or backup

### Creating Custom Plans
1. **Read the schedule generator guide** in `schedule_generator_guide.md`
2. **Customize the prompt** for your field and goals
3. **Generate your plan** using ChatGPT, Claude, or other AI
4. **Save the JSON output** as `my_schedule.json`
5. **Launch the application** to start tracking your progress

## Screenshots

### Main Application Interface
![Main Interface](screenshots/main_interface.png)
*The main application window showing the comprehensive task management interface with plan overview, progress tracking, and task list.*

### Calendar Date Picker
![Calendar Picker](screenshots/calendar_picker.png)
*Interactive date picker dialog for setting your plan start date.*

### Navigation & Filtering Panel
![Navigation & Filters](screenshots/navigation_filters.png)
*Left panel showing task categories, status filters, and search functionality.*

### Task Action Buttons
![Task Actions](screenshots/task_actions.png)
*Action buttons for managing task status: Mark Complete, Mark In Progress, Add Notes, and Toggle Status.*

### Task Notes Dialog
![Add Notes](screenshots/add_notes_dialog.png)
*Dialog for adding detailed notes to specific tasks.*

### Plan Overview Section
![Plan Overview](screenshots/plan_overview.png)
*Top section showing plan details including start date, duration, end date, and current progress.*

## Technical Details

### Architecture
- **Frontend**: tkinter GUI with modern styling
- **Backend**: Python with dataclasses and enums
- **Data**: JSON-based persistence with automatic backups
- **Export**: CSV and JSON export capabilities

### File Structure
```
career-development-tracker/
├── enhanced_cybersecurity_tracker.py    # Main application
├── sample_schedule_template.json        # Template for custom plans
├── schedule_generator_guide.md          # AI prompt templates
├── cybersecurity_job_plan.py            # Original CLI version
├── run_enhanced_tracker.bat             # Windows launcher
├── demo.py                             # Feature demonstration
├── requirements.txt                     # Dependencies
├── README.md                            # This file
├── CONTRIBUTING.md                      # Contribution guidelines
├── LICENSE                              # MIT license
└── backups/                             # Automatic backups
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request. For major changes, please open an issue first to discuss what you would like to change.

### Development Setup
1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Built with Python's standard library for maximum compatibility
- Inspired by the growing need for structured career development tools
- Template system designed for maximum flexibility and customization
- AI prompt templates for easy plan generation

## Support

If you find this tool helpful, please consider:
- Starring the repository
- Reporting bugs or suggesting features
- Contributing improvements
- Sharing with others in your field or community

---

**Good luck with your career development journey!**

*Built for the developer and career development community*
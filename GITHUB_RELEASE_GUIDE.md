# GitHub Release Guide

## How to Create a GitHub Release

### Step 1: Prepare Release Files

1. **Navigate to releases directory**:
   ```bash
   cd releases/v1.0.0
   ```

2. **Create a zip file** of the release:
   ```bash
   # Windows
   powershell Compress-Archive -Path * -DestinationPath ../career-development-tracker-v1.0.0.zip
   
   # macOS/Linux
   zip -r ../career-development-tracker-v1.0.0.zip *
   ```

### Step 2: Create GitHub Release

1. **Go to your GitHub repository**: https://github.com/jacobdcook/career-development-tracker

2. **Click "Releases"** in the right sidebar

3. **Click "Create a new release"**

4. **Fill in the release details**:
   - **Tag version**: `v1.0.0`
   - **Release title**: `Career Development Tracker v1.0.0 - Initial Release`
   - **Description**: Copy from `RELEASE_NOTES.md`

5. **Upload the zip file**:
   - Click "Attach binaries"
   - Upload `career-development-tracker-v1.0.0.zip`

6. **Publish the release**

### Step 3: Release Description Template

```markdown
# Career Development Tracker v1.0.0

## Initial Release - Universal Career Development Tool

This is the first official release of the Career Development Tracker - a comprehensive desktop application for managing structured schedules and career development plans.

### What's New

- **Universal Application** - Works for any field (cybersecurity, data science, web dev, fitness, etc.)
- **AI-Generated Plans** - Use provided prompts to generate personalized plans with any AI
- **Modern GUI** - Beautiful tkinter interface with progress visualization
- **Interactive Calendar** - Click to select start dates with fallback for older Python versions
- **Flexible Duration** - Support for 7 to 365 days (any duration)
- **Advanced Filtering** - Filter by category, status, or search terms
- **Progress Tracking** - Visual progress bars and detailed reports
- **Data Management** - Automatic backups and export capabilities
- **Template System** - Easy-to-use templates for different career paths
- **Privacy-First** - Personal data files are automatically gitignored

### Quick Start

1. **Download** the zip file below
2. **Extract** to a folder
3. **Run** `python enhanced_cybersecurity_tracker.py` or double-click `run_enhanced_tracker.bat`
4. **Create your plan** using the schedule generator guide
5. **Start tracking** your progress!

### What's Included

- Main GUI application
- CLI version for terminal users
- Demo script
- Sample template for AI-generated plans
- Complete documentation and guides
- Windows launcher
- Installation script

### Perfect For

- Job search and career transitions
- Certification preparation
- Skill development and learning
- Personal goal tracking
- Project management
- Any structured, time-based goal

### Technical Details

- Python 3.7+ (uses only standard library)
- Cross-platform (Windows, macOS, Linux)
- No external dependencies required
- JSON-based data storage
- Automatic backups
- Export capabilities (CSV and JSON)

### Documentation

Complete documentation is included in the release package:
- README.md - Complete user guide
- schedule_generator_guide.md - AI prompt guide
- github_activity_template.md - GitHub integration
- RELEASE_NOTES.md - Detailed release information

### Links

- **Repository**: https://github.com/jacobdcook/career-development-tracker
- **Issues**: https://github.com/jacobdcook/career-development-tracker/issues
- **Discussions**: https://github.com/jacobdcook/career-development-tracker/discussions

---

**Ready to start your career development journey? Download, extract, and begin tracking your progress today!**
```

### Step 4: Post-Release Tasks

1. **Update repository description** (if needed)
2. **Add topics/tags** to the repository
3. **Share on social media** or relevant communities
4. **Monitor for issues** and user feedback

### Step 5: Future Releases

For future releases (v1.1.0, v1.2.0, etc.):

1. **Update version numbers** in:
   - `setup.py`
   - `CHANGELOG.md`
   - Release directory name
   - Release notes

2. **Follow the same process** as above

3. **Consider creating release branches** for major versions

---

## Release Checklist

- [ ] All files copied to release directory
- [ ] Version numbers updated
- [ ] Release notes written
- [ ] Zip file created
- [ ] GitHub release created
- [ ] Release published
- [ ] Repository updated (if needed)
- [ ] Social media announcement (optional)

---

**Good luck with your release!**

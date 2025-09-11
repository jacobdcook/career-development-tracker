# Contributing to Cybersecurity Job Tracker

Thank you for your interest in contributing to the Cybersecurity Job Tracker! This document provides guidelines and information for contributors.

## 🤝 How to Contribute

### Reporting Bugs
- Use the GitHub issue tracker
- Include steps to reproduce the bug
- Provide your operating system and Python version
- Include any error messages or screenshots

### Suggesting Features
- Open an issue with the "enhancement" label
- Describe the feature and its benefits
- Consider the impact on existing users

### Code Contributions
1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Make your changes
4. Add tests if applicable
5. Commit your changes (`git commit -m 'Add amazing feature'`)
6. Push to the branch (`git push origin feature/amazing-feature`)
7. Open a Pull Request

## 🛠️ Development Setup

### Prerequisites
- Python 3.7+
- Git

### Setup
```bash
# Clone your fork
git clone https://github.com/yourusername/cybersecurity-job-tracker.git
cd cybersecurity-job-tracker

# Create a virtual environment (recommended)
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install in development mode
pip install -e .
```

## 📝 Code Style

### Python
- Follow PEP 8 style guidelines
- Use meaningful variable and function names
- Add docstrings for functions and classes
- Keep functions focused and small

### GUI Code
- Use descriptive widget names
- Group related widgets in frames
- Add comments for complex layouts
- Follow tkinter best practices

## 🧪 Testing

### Manual Testing
- Test on different operating systems if possible
- Verify GUI functionality
- Test data import/export features
- Check backup and restore functionality

### Test Cases to Consider
- Application startup and shutdown
- Task creation, editing, and deletion
- Data persistence across sessions
- Export/import functionality
- Error handling for invalid data

## 📋 Pull Request Guidelines

### Before Submitting
- [ ] Code follows the project's style guidelines
- [ ] Self-review of your code
- [ ] Comments added for complex code
- [ ] Documentation updated if needed
- [ ] No merge conflicts

### PR Description
- Clearly describe what the PR does
- Reference any related issues
- Include screenshots for GUI changes
- List any breaking changes

## 🎯 Areas for Contribution

### High Priority
- Additional export formats (Excel, PDF)
- Task templates and customization
- Integration with calendar applications
- Mobile-friendly web version
- Plugin system for extensions

### Medium Priority
- Dark mode theme
- Keyboard shortcuts
- Drag-and-drop task reordering
- Advanced filtering options
- Progress analytics and charts

### Low Priority
- Multi-language support
- Cloud synchronization
- Team collaboration features
- Integration with job boards
- AI-powered task suggestions

## 🐛 Bug Reports

When reporting bugs, please include:

1. **Environment**
   - Operating System (Windows/macOS/Linux)
   - Python version
   - Application version

2. **Steps to Reproduce**
   - Clear, numbered steps
   - Expected vs actual behavior

3. **Additional Information**
   - Error messages or screenshots
   - Data files (if relevant and safe to share)
   - Console output

## 💡 Feature Requests

When suggesting features:

1. **Problem Description**
   - What problem does this solve?
   - Who would benefit from this feature?

2. **Proposed Solution**
   - How should it work?
   - Any design considerations?

3. **Alternatives Considered**
   - Other ways to solve the problem
   - Why this approach is preferred

## 📞 Getting Help

- Open an issue for questions
- Check existing issues first
- Be specific about your question
- Provide relevant context

## 🏆 Recognition

Contributors will be recognized in:
- README.md contributors section
- Release notes
- GitHub contributors page

Thank you for contributing to the cybersecurity community! 🚀

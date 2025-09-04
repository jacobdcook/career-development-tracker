#!/usr/bin/env python3
"""
Career Development Tracker - Installation Script
Simple installation and setup script for v1.0.0
"""

import os
import sys
import shutil
from pathlib import Path

def print_banner():
    """Print installation banner"""
    print("=" * 60)
    print("📅 CAREER DEVELOPMENT TRACKER v1.0.0")
    print("=" * 60)
    print("Installation and Setup Script")
    print("=" * 60)
    print()

def check_python_version():
    """Check if Python version is compatible"""
    print("🔍 Checking Python version...")
    if sys.version_info < (3, 7):
        print("❌ Error: Python 3.7 or higher is required")
        print(f"   Current version: {sys.version}")
        return False
    else:
        print(f"✅ Python {sys.version.split()[0]} is compatible")
        return True

def check_dependencies():
    """Check if required modules are available"""
    print("\n🔍 Checking dependencies...")
    
    required_modules = [
        'tkinter',
        'json',
        'datetime',
        'dataclasses',
        'enum',
        'os',
        'pathlib'
    ]
    
    missing_modules = []
    for module in required_modules:
        try:
            __import__(module)
            print(f"✅ {module} - Available")
        except ImportError:
            print(f"❌ {module} - Missing")
            missing_modules.append(module)
    
    if missing_modules:
        print(f"\n❌ Missing required modules: {', '.join(missing_modules)}")
        return False
    else:
        print("\n✅ All required modules are available")
        return True

def create_sample_plan():
    """Create a sample plan file for the user"""
    print("\n📝 Creating sample plan...")
    
    sample_plan = {
        "start_date": "2024-09-04",
        "end_date": "2024-09-10",
        "hours_per_day_target": 4.0,
        "tasks": [
            {
                "id": 1,
                "title": "Update resume and portfolio",
                "hours": 2.0,
                "day": 1,
                "done": False,
                "created_order": 1
            },
            {
                "id": 2,
                "title": "Research target companies",
                "hours": 1.5,
                "day": 1,
                "done": False,
                "created_order": 2
            },
            {
                "id": 3,
                "title": "Apply to 5 opportunities",
                "hours": 2.0,
                "day": 2,
                "done": False,
                "created_order": 3
            },
            {
                "id": 4,
                "title": "Study core concepts",
                "hours": 2.0,
                "day": 2,
                "done": False,
                "created_order": 4
            },
            {
                "id": 5,
                "title": "Hands-on project work",
                "hours": 1.5,
                "day": 3,
                "done": False,
                "created_order": 5
            },
            {
                "id": 6,
                "title": "Network with professionals",
                "hours": 1.0,
                "day": 3,
                "done": False,
                "created_order": 6
            },
            {
                "id": 7,
                "title": "Review and plan next week",
                "hours": 1.0,
                "day": 4,
                "done": False,
                "created_order": 7
            }
        ]
    }
    
    try:
        import json
        with open('sample_plan.json', 'w') as f:
            json.dump(sample_plan, f, indent=2)
        print("✅ Sample plan created: sample_plan.json")
        return True
    except Exception as e:
        print(f"❌ Error creating sample plan: {e}")
        return False

def test_application():
    """Test if the application can be imported"""
    print("\n🧪 Testing application...")
    try:
        # Try to import the main application
        import enhanced_cybersecurity_tracker
        print("✅ Main application can be imported")
        return True
    except Exception as e:
        print(f"❌ Error importing application: {e}")
        return False

def show_next_steps():
    """Show next steps for the user"""
    print("\n" + "=" * 60)
    print("🎉 INSTALLATION COMPLETE!")
    print("=" * 60)
    print()
    print("📋 Next Steps:")
    print("1. Run the application:")
    print("   python enhanced_cybersecurity_tracker.py")
    print("   OR double-click run_enhanced_tracker.bat (Windows)")
    print()
    print("2. Create your custom plan:")
    print("   - Read schedule_generator_guide.md")
    print("   - Use AI (ChatGPT, Claude, etc.) with the template")
    print("   - Save your plan as my_schedule.json")
    print()
    print("3. Start tracking your progress!")
    print()
    print("📚 Documentation:")
    print("   - README.md - Complete user guide")
    print("   - schedule_generator_guide.md - AI prompt guide")
    print("   - github_activity_template.md - GitHub integration")
    print()
    print("🔗 GitHub Repository:")
    print("   https://github.com/jacobdcook/career-development-tracker")
    print()
    print("🎯 Ready to start your career development journey!")
    print("=" * 60)

def main():
    """Main installation function"""
    print_banner()
    
    # Check Python version
    if not check_python_version():
        sys.exit(1)
    
    # Check dependencies
    if not check_dependencies():
        print("\n❌ Installation failed due to missing dependencies")
        print("   Please install Python 3.7+ with standard library")
        sys.exit(1)
    
    # Create sample plan
    create_sample_plan()
    
    # Test application
    if not test_application():
        print("\n❌ Installation failed - application cannot be imported")
        sys.exit(1)
    
    # Show next steps
    show_next_steps()

if __name__ == "__main__":
    main()

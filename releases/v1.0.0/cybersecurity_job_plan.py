#!/usr/bin/env python3
"""
Career Development Plan Tracker (CLI Version)
A simple terminal-based plan tracker for career development
"""

import json
import os
from datetime import datetime, timedelta
from typing import Dict, List, Optional
from dataclasses import dataclass, asdict
from enum import Enum

class TaskStatus(Enum):
    PENDING = "pending"
    IN_PROGRESS = "in_progress"
    COMPLETED = "completed"
    SKIPPED = "skipped"

@dataclass
class Task:
    day: int
    week: int
    title: str
    description: str
    category: str
    status: TaskStatus = TaskStatus.PENDING
    notes: str = ""
    completed_date: Optional[str] = None

class CareerDevelopmentPlan:
    def __init__(self, data_file: str = "plan_data.json"):
        self.data_file = data_file
        self.tasks = self._load_tasks()
        self.start_date = self._get_start_date()
        
    def _load_tasks(self) -> List[Task]:
        """Load tasks from file or create default tasks"""
        if os.path.exists(self.data_file):
            with open(self.data_file, 'r') as f:
                data = json.load(f)
                return [Task(**task) for task in data]
        else:
            return self._create_default_tasks()
    
    def _save_tasks(self):
        """Save tasks to file"""
        with open(self.data_file, 'w') as f:
            json.dump([asdict(task) for task in self.tasks], f, indent=2)
    
    def _get_start_date(self) -> datetime:
        """Get or set the start date for the plan"""
        if os.path.exists("start_date.txt"):
            with open("start_date.txt", 'r') as f:
                return datetime.fromisoformat(f.read().strip())
        else:
            start_date = datetime.now()
            with open("start_date.txt", 'w') as f:
                f.write(start_date.isoformat())
            return start_date
    
    def _create_default_tasks(self) -> List[Task]:
        """Create the default 6-week plan tasks"""
        tasks = [
            # Week 1
            Task(1, 1, "Update Resume", "Highlight CS degree + Security+ in progress", "Resume"),
            Task(2, 1, "Refresh LinkedIn Profile", "Update profile with current skills and goals", "Networking"),
            Task(3, 1, "Research Job Titles", "SOC Analyst, GRC Analyst, Junior Security Analyst", "Research"),
            Task(4, 1, "Apply to 5 Jobs", "Use Indeed/LinkedIn to apply to entry-level positions", "Applications"),
            Task(5, 1, "Security+ Study - Domain 1", "Threats, Attacks, Vulnerabilities", "Study"),
            Task(6, 1, "TryHackMe Account", "Create account and complete 1 lab", "Practical"),
            Task(7, 1, "Join Communities", "Join cybersecurity LinkedIn group or Discord/Reddit", "Networking"),
            
            # Week 2
            Task(8, 2, "Apply to 10 Jobs", "Focus on Davis/Sacramento area positions", "Applications"),
            Task(9, 2, "Security+ Study - Domain 2", "Architecture & Design", "Study"),
            Task(10, 2, "SOC TryHackMe Lab", "Complete 1 SOC-related lab (SIEM/log analysis)", "Practical"),
            Task(11, 2, "LinkedIn Post", "Write about your Security+ journey", "Networking"),
            Task(12, 2, "Reach Out to Recruiters", "Contact 3 recruiters on LinkedIn", "Networking"),
            Task(13, 2, "Apply to Government Jobs", "USAJobs, CA state positions", "Applications"),
            Task(14, 2, "Mock Interview Practice", "Practice answering 'Why cybersecurity?'", "Interview Prep"),
            
            # Week 3
            Task(15, 3, "Apply to 10 Jobs", "Include GRC/compliance positions", "Applications"),
            Task(16, 3, "Security+ Study - Domain 3", "Implementation", "Study"),
            Task(17, 3, "Network Security Labs", "Complete 2 practical labs on network security", "Practical"),
            Task(18, 3, "Update Resume", "Add completed labs and projects", "Resume"),
            Task(19, 3, "Apply to Bay Area SOC", "SOC Analyst jobs (remote possible)", "Applications"),
            Task(20, 3, "Research Local Companies", "Sacramento-area companies (finance, gov, healthcare)", "Research"),
            Task(21, 3, "Rest & Prep", "Take a break and prepare for next week", "Planning"),
            
            # Week 4
            Task(22, 4, "Apply to 10 Jobs", "Junior sysadmin/security support roles", "Applications"),
            Task(23, 4, "Security+ Study - Domain 4", "Operations & Incident Response", "Study"),
            Task(24, 4, "Join Professional Groups", "ISSA/ISACA/OWASP local meetup", "Networking"),
            Task(25, 4, "Create GitHub Repo", "Set up repository for labs and projects", "Portfolio"),
            Task(26, 4, "Interview Practice", "TCP/IP, CIA triad, common ports", "Interview Prep"),
            Task(27, 4, "Apply to Compliance Jobs", "Healthcare and finance compliance roles", "Applications"),
            Task(28, 4, "Review Security+ Notes", "Go through all study materials", "Study"),
            
            # Week 5
            Task(29, 5, "Apply to 10 Jobs", "Focus on SOC Tier 1/GRC positions", "Applications"),
            Task(30, 5, "Security+ Study - Domain 5", "Governance, Risk, Compliance", "Study"),
            Task(31, 5, "Security+ Practice Exam", "Take first practice exam", "Study"),
            Task(32, 5, "LinkedIn Progress Update", "Post about your journey and progress", "Networking"),
            Task(33, 5, "Informational Interviews", "Reach out to 3 professionals for chats", "Networking"),
            Task(34, 5, "Apply to Apprenticeships", "Contract security roles and apprenticeships", "Applications"),
            Task(35, 5, "Mock Interview", "Practice with friend or AI tool", "Interview Prep"),
            
            # Week 6
            Task(36, 6, "Apply to 10 Jobs", "Target $70K+ positions", "Applications"),
            Task(37, 6, "Review Weak Areas", "Focus on Security+ exam weak points", "Study"),
            Task(38, 6, "Apply to Bay Area Jobs", "SOC/analyst positions in Bay Area", "Applications"),
            Task(39, 6, "Polish Resume", "Update with 'Security+ in final prep'", "Resume"),
            Task(40, 6, "Second Practice Exam", "Take another Security+ practice exam", "Study"),
            Task(41, 6, "Follow Up Applications", "Follow up on applications from weeks 1-5", "Applications"),
            Task(42, 6, "Interview Prep", "Final preparation and celebrate progress", "Interview Prep"),
        ]
        return tasks
    
    def get_current_day(self) -> int:
        """Calculate current day based on start date"""
        days_since_start = (datetime.now() - self.start_date).days + 1
        return min(days_since_start, 42)  # Cap at 42 days
    
    def get_today_task(self) -> Optional[Task]:
        """Get today's task"""
        current_day = self.get_current_day()
        for task in self.tasks:
            if task.day == current_day:
                return task
        return None
    
    def get_week_tasks(self, week: int) -> List[Task]:
        """Get all tasks for a specific week"""
        return [task for task in self.tasks if task.week == week]
    
    def get_tasks_by_status(self, status: TaskStatus) -> List[Task]:
        """Get tasks by status"""
        return [task for task in self.tasks if task.status == status]
    
    def mark_task_complete(self, day: int, notes: str = ""):
        """Mark a task as completed"""
        for task in self.tasks:
            if task.day == day:
                task.status = TaskStatus.COMPLETED
                task.notes = notes
                task.completed_date = datetime.now().isoformat()
                self._save_tasks()
                return True
        return False
    
    def mark_task_in_progress(self, day: int):
        """Mark a task as in progress"""
        for task in self.tasks:
            if task.day == day:
                task.status = TaskStatus.IN_PROGRESS
                self._save_tasks()
                return True
        return False
    
    def get_progress_summary(self) -> Dict:
        """Get overall progress summary"""
        total_tasks = len(self.tasks)
        completed = len(self.get_tasks_by_status(TaskStatus.COMPLETED))
        in_progress = len(self.get_tasks_by_status(TaskStatus.IN_PROGRESS))
        pending = len(self.get_tasks_by_status(TaskStatus.PENDING))
        
        return {
            "total_tasks": total_tasks,
            "completed": completed,
            "in_progress": in_progress,
            "pending": pending,
            "completion_percentage": round((completed / total_tasks) * 100, 1)
        }
    
    def display_today_task(self):
        """Display today's task"""
        current_day = self.get_current_day()
        task = self.get_today_task()
        
        print(f"\n{'='*60}")
        print(f"📅 DAY {current_day} - CAREER DEVELOPMENT PLAN")
        print(f"{'='*60}")
        
        if task:
            status_emoji = {
                TaskStatus.PENDING: "⏳",
                TaskStatus.IN_PROGRESS: "🔄",
                TaskStatus.COMPLETED: "✅",
                TaskStatus.SKIPPED: "⏭️"
            }
            
            print(f"\n{status_emoji[task.status]} TODAY'S TASK:")
            print(f"📋 {task.title}")
            print(f"📝 {task.description}")
            print(f"🏷️  Category: {task.category}")
            print(f"📊 Status: {task.status.value.title()}")
            
            if task.notes:
                print(f"📝 Notes: {task.notes}")
        else:
            print("\n🎉 Congratulations! You've completed all 42 days of the plan!")
            print("Keep applying and studying - your cybersecurity career awaits!")
    
    def display_week_overview(self, week: int):
        """Display overview for a specific week"""
        tasks = self.get_week_tasks(week)
        if not tasks:
            print(f"No tasks found for week {week}")
            return
        
        print(f"\n{'='*50}")
        print(f"📅 WEEK {week} OVERVIEW")
        print(f"{'='*50}")
        
        for task in tasks:
            status_emoji = {
                TaskStatus.PENDING: "⏳",
                TaskStatus.IN_PROGRESS: "🔄",
                TaskStatus.COMPLETED: "✅",
                TaskStatus.SKIPPED: "⏭️"
            }
            
            print(f"\nDay {task.day}: {status_emoji[task.status]} {task.title}")
            print(f"   {task.description}")
            print(f"   Category: {task.category}")
    
    def display_progress(self):
        """Display overall progress"""
        summary = self.get_progress_summary()
        
        print(f"\n{'='*50}")
        print("📊 PROGRESS SUMMARY")
        print(f"{'='*50}")
        print(f"Total Tasks: {summary['total_tasks']}")
        print(f"✅ Completed: {summary['completed']}")
        print(f"🔄 In Progress: {summary['in_progress']}")
        print(f"⏳ Pending: {summary['pending']}")
        print(f"📈 Completion: {summary['completion_percentage']}%")
        
        # Progress bar
        bar_length = 30
        filled_length = int(bar_length * summary['completion_percentage'] / 100)
        bar = '█' * filled_length + '░' * (bar_length - filled_length)
        print(f"Progress: [{bar}] {summary['completion_percentage']}%")

def main():
    """Main interactive interface"""
    plan = CareerDevelopmentPlan()
    
    while True:
        print(f"\n{'='*60}")
        print("📅 CAREER DEVELOPMENT PLAN TRACKER")
        print(f"{'='*60}")
        print("1. 📅 Today's Task")
        print("2. 📊 Progress Summary")
        print("3. 📋 Week Overview")
        print("4. ✅ Mark Task Complete")
        print("5. 🔄 Mark Task In Progress")
        print("6. 📝 Add Notes to Task")
        print("7. 🎯 View Tasks by Category")
        print("8. 🚪 Exit")
        
        choice = input("\nSelect an option (1-8): ").strip()
        
        if choice == "1":
            plan.display_today_task()
        
        elif choice == "2":
            plan.display_progress()
        
        elif choice == "3":
            try:
                week = int(input("Enter week number (1-6): "))
                if 1 <= week <= 6:
                    plan.display_week_overview(week)
                else:
                    print("Please enter a week between 1 and 6")
            except ValueError:
                print("Please enter a valid number")
        
        elif choice == "4":
            try:
                day = int(input("Enter day number (1-42): "))
                notes = input("Add notes (optional): ").strip()
                if plan.mark_task_complete(day, notes):
                    print(f"✅ Task for day {day} marked as completed!")
                else:
                    print(f"❌ No task found for day {day}")
            except ValueError:
                print("Please enter a valid day number")
        
        elif choice == "5":
            try:
                day = int(input("Enter day number (1-42): "))
                if plan.mark_task_in_progress(day):
                    print(f"🔄 Task for day {day} marked as in progress!")
                else:
                    print(f"❌ No task found for day {day}")
            except ValueError:
                print("Please enter a valid day number")
        
        elif choice == "6":
            try:
                day = int(input("Enter day number (1-42): "))
                notes = input("Enter notes: ").strip()
                for task in plan.tasks:
                    if task.day == day:
                        task.notes = notes
                        plan._save_tasks()
                        print(f"📝 Notes added to day {day} task!")
                        break
                else:
                    print(f"❌ No task found for day {day}")
            except ValueError:
                print("Please enter a valid day number")
        
        elif choice == "7":
            categories = set(task.category for task in plan.tasks)
            print("\nAvailable categories:")
            for i, category in enumerate(sorted(categories), 1):
                print(f"{i}. {category}")
            
            try:
                cat_choice = int(input("Select category number: ")) - 1
                selected_category = sorted(categories)[cat_choice]
                
                print(f"\n📋 Tasks in '{selected_category}' category:")
                for task in plan.tasks:
                    if task.category == selected_category:
                        status_emoji = {
                            TaskStatus.PENDING: "⏳",
                            TaskStatus.IN_PROGRESS: "🔄",
                            TaskStatus.COMPLETED: "✅",
                            TaskStatus.SKIPPED: "⏭️"
                        }
                        print(f"Day {task.day}: {status_emoji[task.status]} {task.title}")
            except (ValueError, IndexError):
                print("Invalid selection")
        
        elif choice == "8":
            print("\n🎯 Keep pushing forward! Your career development journey continues!")
            print("Good luck with your goals and professional growth!")
            break
        
        else:
            print("❌ Invalid choice. Please select 1-8.")

if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""
Enhanced Cybersecurity Job Search & Certification Tracker
A comprehensive 6-week plan with beautiful GUI and advanced features
"""

import json
import os
import tkinter as tk
from tkinter import ttk, messagebox, filedialog, simpledialog
from datetime import datetime, timedelta
from typing import Dict, List, Optional, Tuple
import webbrowser
from dataclasses import dataclass, asdict
from enum import Enum
try:
    from tkinter import Calendar
except ImportError:
    # Fallback for older Python versions
    Calendar = None

# Configuration
STATE_FILE = "enhanced_plan_state.json"
BACKUP_DIR = "backups"
DEFAULT_DAYS = 42

class TaskStatus(Enum):
    PENDING = "pending"
    IN_PROGRESS = "in_progress"
    COMPLETED = "completed"
    SKIPPED = "skipped"

@dataclass
class Task:
    id: int
    title: str
    hours: float
    day: int
    done: bool
    created_order: int
    status: TaskStatus = TaskStatus.PENDING
    notes: str = ""
    completed_date: Optional[str] = None
    category: str = ""

class EnhancedCybersecurityTracker:
    def __init__(self):
        self.state_file = STATE_FILE
        self.backup_dir = BACKUP_DIR
        self.ensure_backup_dir()
        
        # Initialize state
        self.start_date = None
        self.end_date = None
        self.total_days = DEFAULT_DAYS
        self.hours_per_day_target = 6.0
        self.tasks = []
        self.version = 2
        
        # Load existing data or create from template
        if not self.load_state():
            self.load_from_template_or_data()
    
    def ensure_backup_dir(self):
        """Create backup directory if it doesn't exist"""
        if not os.path.exists(self.backup_dir):
            os.makedirs(self.backup_dir)
    
    def load_from_template_or_data(self):
        """Load plan from user data or create from template"""
        # Try to load user's personal plan first
        user_data_files = [
            "my_schedule.json",  # Your personal file (gitignored)
            "my_plan_data.json",
            "personal_plan.json", 
            "user_data.json",
            "plan_data.json",
            "enhanced_plan_state.json"
        ]
        
        for data_file in user_data_files:
            if os.path.exists(data_file):
                try:
                    with open(data_file, 'r', encoding='utf-8') as f:
                        data = json.load(f)
                    
                    self.start_date = data.get("start_date", datetime.now().strftime("%Y-%m-%d"))
                    self.end_date = data.get("end_date", (datetime.now() + timedelta(days=41)).strftime("%Y-%m-%d"))
                    self.total_days = data.get("total_days", DEFAULT_DAYS)
                    self.hours_per_day_target = data.get("hours_per_day_target", 6.0)
                    
                    # Convert tasks to our format
                    self.tasks = []
                    for task_data in data.get("tasks", []):
                        task = Task(
                            id=task_data["id"],
                            title=task_data["title"],
                            hours=float(task_data["hours"]),
                            day=task_data["day"],
                            done=task_data["done"],
                            created_order=task_data["created_order"],
                            status=TaskStatus.COMPLETED if task_data["done"] else TaskStatus.PENDING,
                            category=self._categorize_task(task_data["title"])
                        )
                        self.tasks.append(task)
                    
                    self.save_state()
                    print(f"✅ Loaded {len(self.tasks)} tasks from {data_file}!")
                    return
                    
                except Exception as e:
                    print(f"❌ Error loading {data_file}: {e}")
                    continue
        
        # If no user data found, create from template
        print("📝 No personal plan found. Creating from template...")
        self.create_from_template()
    
    def _categorize_task(self, title: str) -> str:
        """Automatically categorize tasks based on title keywords"""
        title_lower = title.lower()
        
        if any(keyword in title_lower for keyword in ["apply", "job", "application"]):
            return "Applications"
        elif any(keyword in title_lower for keyword in ["security+", "study", "exam", "practice", "review"]):
            return "Study"
        elif any(keyword in title_lower for keyword in ["lab", "tryhackme", "siem", "network", "automation"]):
            return "Practical Labs"
        elif any(keyword in title_lower for keyword in ["linkedin", "recruiter", "connect", "networking", "meetup"]):
            return "Networking"
        elif any(keyword in title_lower for keyword in ["resume", "github", "portfolio"]):
            return "Portfolio"
        elif any(keyword in title_lower for keyword in ["interview", "mock", "star", "prep"]):
            return "Interview Prep"
        elif any(keyword in title_lower for keyword in ["follow", "pipeline", "hygiene"]):
            return "Follow-up"
        else:
            return "General"
    
    def create_from_template(self):
        """Create a plan from the template"""
        template_path = "sample_schedule_template.json"
        
        if os.path.exists(template_path):
            try:
                with open(template_path, 'r', encoding='utf-8') as f:
                    template = json.load(f)
                
                plan_info = template.get("plan_info", {})
                self.start_date = datetime.now().strftime("%Y-%m-%d")
                self.total_days = plan_info.get("total_days", DEFAULT_DAYS)
                self.end_date = (datetime.now() + timedelta(days=self.total_days-1)).strftime("%Y-%m-%d")
                self.hours_per_day_target = plan_info.get("hours_per_day_target", 6.0)
                
                # Create tasks from template
                self.tasks = []
                task_id = 100
                for task_data in template.get("sample_tasks", []):
                    task = Task(
                        id=task_id,
                        title=task_data["title"],
                        hours=float(task_data["hours"]),
                        day=task_data["day"],
                        done=task_data["done"],
                        created_order=task_id,
                        status=TaskStatus.PENDING,
                        category=task_data.get("category", "General")
                    )
                    self.tasks.append(task)
                    task_id += 1
                
                self.save_state()
                print(f"✅ Created plan from template with {len(self.tasks)} sample tasks!")
                print("💡 Tip: Use the AI prompt template to generate your custom plan!")
                
            except Exception as e:
                print(f"❌ Error loading template: {e}")
                self.create_default_plan()
        else:
            self.create_default_plan()
    
    def create_default_plan(self):
        """Create a basic plan if no data is available"""
        self.start_date = datetime.now().strftime("%Y-%m-%d")
        self.total_days = DEFAULT_DAYS
        self.end_date = (datetime.now() + timedelta(days=self.total_days-1)).strftime("%Y-%m-%d")
        self.tasks = []
        self.save_state()
    
    def load_state(self) -> bool:
        """Load state from file"""
        if not os.path.exists(self.state_file):
            return False
        
        try:
            with open(self.state_file, 'r', encoding='utf-8') as f:
                data = json.load(f)
            
            self.start_date = data.get("start_date")
            self.end_date = data.get("end_date")
            self.total_days = data.get("total_days", DEFAULT_DAYS)
            self.hours_per_day_target = data.get("hours_per_day_target", 6.0)
            self.version = data.get("version", 2)
            
            # Convert task data
            self.tasks = []
            for task_data in data.get("tasks", []):
                task = Task(
                    id=task_data["id"],
                    title=task_data["title"],
                    hours=float(task_data["hours"]),
                    day=task_data["day"],
                    done=task_data["done"],
                    created_order=task_data["created_order"],
                    status=TaskStatus(task_data.get("status", "pending")),
                    notes=task_data.get("notes", ""),
                    completed_date=task_data.get("completed_date"),
                    category=task_data.get("category", "")
                )
                self.tasks.append(task)
            
            return True
        except Exception as e:
            print(f"Error loading state: {e}")
            return False
    
    def save_state(self):
        """Save current state to file with backup"""
        # Create backup
        if os.path.exists(self.state_file):
            backup_name = f"backup_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
            backup_path = os.path.join(self.backup_dir, backup_name)
            os.rename(self.state_file, backup_path)
        
        # Save current state
        data = {
            "start_date": self.start_date,
            "end_date": self.end_date,
            "total_days": self.total_days,
            "hours_per_day_target": self.hours_per_day_target,
            "version": self.version,
            "tasks": []
        }
        
        for task in self.tasks:
            task_data = {
                "id": task.id,
                "title": task.title,
                "hours": task.hours,
                "day": task.day,
                "done": task.done,
                "created_order": task.created_order,
                "status": task.status.value,
                "notes": task.notes,
                "completed_date": task.completed_date,
                "category": task.category
            }
            data["tasks"].append(task_data)
        
        with open(self.state_file, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2)
    
    def get_current_day(self) -> int:
        """Calculate current day based on start date"""
        if not self.start_date:
            return 1
        
        start = datetime.strptime(self.start_date, "%Y-%m-%d")
        days_since_start = (datetime.now() - start).days + 1
        return min(max(days_since_start, 1), self.total_days)
    
    def get_today_tasks(self) -> List[Task]:
        """Get all tasks for today"""
        current_day = self.get_current_day()
        return [task for task in self.tasks if task.day == current_day]
    
    def get_week_tasks(self, week: int) -> List[Task]:
        """Get all tasks for a specific week"""
        start_day = (week - 1) * 7 + 1
        end_day = min(week * 7, self.total_days)
        return [task for task in self.tasks if start_day <= task.day <= end_day]
    
    def get_tasks_by_category(self, category: str) -> List[Task]:
        """Get tasks by category"""
        return [task for task in self.tasks if task.category == category]
    
    def get_tasks_by_status(self, status: TaskStatus) -> List[Task]:
        """Get tasks by status"""
        return [task for task in self.tasks if task.status == status]
    
    def mark_task_complete(self, task_id: int, notes: str = ""):
        """Mark a task as completed"""
        for task in self.tasks:
            if task.id == task_id:
                task.done = True
                task.status = TaskStatus.COMPLETED
                task.notes = notes
                task.completed_date = datetime.now().isoformat()
                self.save_state()
                return True
        return False
    
    def mark_task_in_progress(self, task_id: int):
        """Mark a task as in progress"""
        for task in self.tasks:
            if task.id == task_id:
                task.status = TaskStatus.IN_PROGRESS
                self.save_state()
                return True
        return False
    
    def toggle_task_status(self, task_id: int):
        """Toggle task completion status"""
        for task in self.tasks:
            if task.id == task_id:
                task.done = not task.done
                task.status = TaskStatus.COMPLETED if task.done else TaskStatus.PENDING
                if task.done:
                    task.completed_date = datetime.now().isoformat()
                else:
                    task.completed_date = None
                self.save_state()
                return True
        return False
    
    def get_progress_summary(self) -> Dict:
        """Get comprehensive progress summary"""
        total_tasks = len(self.tasks)
        completed = len(self.get_tasks_by_status(TaskStatus.COMPLETED))
        in_progress = len(self.get_tasks_by_status(TaskStatus.IN_PROGRESS))
        pending = len(self.get_tasks_by_status(TaskStatus.PENDING))
        
        # Calculate hours
        total_hours = sum(task.hours for task in self.tasks)
        completed_hours = sum(task.hours for task in self.tasks if task.done)
        
        # Category breakdown
        categories = {}
        for task in self.tasks:
            cat = task.category
            if cat not in categories:
                categories[cat] = {"total": 0, "completed": 0, "hours": 0.0, "completed_hours": 0.0}
            categories[cat]["total"] += 1
            categories[cat]["hours"] += task.hours
            if task.done:
                categories[cat]["completed"] += 1
                categories[cat]["completed_hours"] += task.hours
        
        return {
            "total_tasks": total_tasks,
            "completed": completed,
            "in_progress": in_progress,
            "pending": pending,
            "completion_percentage": round((completed / total_tasks) * 100, 1) if total_tasks > 0 else 0,
            "total_hours": total_hours,
            "completed_hours": completed_hours,
            "hours_percentage": round((completed_hours / total_hours) * 100, 1) if total_hours > 0 else 0,
            "categories": categories
        }

class DatePickerDialog:
    def __init__(self, parent, title="Select Date", initial_date=None):
        self.result = None
        self.dialog = tk.Toplevel(parent)
        self.dialog.title(title)
        self.dialog.geometry("300x300")
        self.dialog.resizable(False, False)
        self.dialog.transient(parent)
        self.dialog.grab_set()
        
        # Center the dialog
        self.dialog.geometry("+%d+%d" % (parent.winfo_rootx() + 50, parent.winfo_rooty() + 50))
        
        if Calendar:
            # Use Calendar widget if available
            self.cal = Calendar(self.dialog, selectmode='day')
            self.cal.pack(pady=20, padx=20, fill='both', expand=True)
            
            # Set initial date
            if initial_date:
                try:
                    date_obj = datetime.strptime(initial_date, "%Y-%m-%d")
                    self.cal.selection_set(date_obj.date())
                except:
                    pass
        else:
            # Fallback to simple date entry
            ttk.Label(self.dialog, text="Enter date (YYYY-MM-DD):").pack(pady=20)
            self.date_entry = ttk.Entry(self.dialog, width=15)
            self.date_entry.pack(pady=10)
            if initial_date:
                self.date_entry.insert(0, initial_date)
        
        # Buttons
        button_frame = ttk.Frame(self.dialog)
        button_frame.pack(pady=10)
        
        ttk.Button(button_frame, text="OK", command=self.ok_clicked).pack(side=tk.LEFT, padx=5)
        ttk.Button(button_frame, text="Cancel", command=self.cancel_clicked).pack(side=tk.LEFT, padx=5)
        
        # Wait for dialog to close
        self.dialog.wait_window()
    
    def ok_clicked(self):
        if Calendar and hasattr(self, 'cal'):
            selected_date = self.cal.selection_get()
            self.result = selected_date.strftime("%Y-%m-%d")
        else:
            # Fallback to entry validation
            date_str = self.date_entry.get().strip()
            try:
                datetime.strptime(date_str, "%Y-%m-%d")
                self.result = date_str
            except ValueError:
                messagebox.showerror("Invalid Date", "Please enter date in YYYY-MM-DD format")
                return
        self.dialog.destroy()
    
    def cancel_clicked(self):
        self.result = None
        self.dialog.destroy()

class EnhancedGUI:
    def __init__(self):
        self.tracker = EnhancedCybersecurityTracker()
        self.root = tk.Tk()
        self.setup_ui()
        self.refresh_display()
    
    def setup_ui(self):
        """Setup the main GUI"""
        self.root.title("🔐 Enhanced Cybersecurity Job Search Tracker")
        self.root.geometry("1200x800")
        self.root.configure(bg='#f0f0f0')
        
        # Set application icon
        try:
            self.root.iconbitmap(r"C:\Users\Admin\Documents\PROJECTS CYBER\career-development-tracker-1.0.0\cybersecurity_tracker_icon.ico")
        except:
            pass  # If icon file doesn't exist, just continue without it
        
        # Configure style
        style = ttk.Style()
        style.theme_use('clam')
        
        # Main container
        main_frame = ttk.Frame(self.root)
        main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Header
        self.create_header(main_frame)
        
        # Progress section
        self.create_progress_section(main_frame)
        
        # Main content area
        content_frame = ttk.Frame(main_frame)
        content_frame.pack(fill=tk.BOTH, expand=True, pady=(10, 0))
        
        # Left panel - Navigation and filters
        self.create_left_panel(content_frame)
        
        # Right panel - Task list
        self.create_right_panel(content_frame)
        
        # Status bar
        self.create_status_bar(main_frame)
    
    def create_header(self, parent):
        """Create header with key information"""
        header_frame = ttk.LabelFrame(parent, text="📊 Plan Overview", padding=10)
        header_frame.pack(fill=tk.X, pady=(0, 10))
        
        # Plan dates
        dates_frame = ttk.Frame(header_frame)
        dates_frame.pack(fill=tk.X)
        
        ttk.Label(dates_frame, text="Start Date:").pack(side=tk.LEFT)
        self.start_date_var = tk.StringVar(value=self.tracker.start_date or "Not set")
        start_date_label = ttk.Label(dates_frame, textvariable=self.start_date_var, font=('Arial', 10, 'bold'))
        start_date_label.pack(side=tk.LEFT, padx=(5, 5))
        start_date_label.bind("<Button-1>", self.pick_start_date)
        
        ttk.Button(dates_frame, text="📅", command=self.pick_start_date, width=3).pack(side=tk.LEFT, padx=(0, 20))
        
        ttk.Label(dates_frame, text="Duration:").pack(side=tk.LEFT)
        self.duration_var = tk.StringVar(value=str(self.tracker.total_days))
        duration_spinbox = ttk.Spinbox(dates_frame, from_=7, to=365, width=5, textvariable=self.duration_var, command=self.update_duration)
        duration_spinbox.pack(side=tk.LEFT, padx=(5, 5))
        duration_spinbox.bind('<Return>', self.update_duration)
        
        ttk.Label(dates_frame, text="days").pack(side=tk.LEFT, padx=(0, 20))
        
        ttk.Label(dates_frame, text="End Date:").pack(side=tk.LEFT)
        self.end_date_var = tk.StringVar(value=self.tracker.end_date or "Not set")
        ttk.Label(dates_frame, textvariable=self.end_date_var, font=('Arial', 10, 'bold')).pack(side=tk.LEFT, padx=(5, 20))
        
        ttk.Label(dates_frame, text="Current Day:").pack(side=tk.LEFT)
        self.current_day_var = tk.StringVar()
        ttk.Label(dates_frame, textvariable=self.current_day_var, font=('Arial', 10, 'bold')).pack(side=tk.LEFT, padx=(5, 0))
        
        # Quick actions
        actions_frame = ttk.Frame(header_frame)
        actions_frame.pack(fill=tk.X, pady=(10, 0))
        
        ttk.Button(actions_frame, text="📅 Today's Tasks", command=self.show_today).pack(side=tk.LEFT, padx=(0, 5))
        ttk.Button(actions_frame, text="📊 Progress Report", command=self.show_progress_report).pack(side=tk.LEFT, padx=5)
        ttk.Button(actions_frame, text="💾 Backup Data", command=self.backup_data).pack(side=tk.LEFT, padx=5)
        ttk.Button(actions_frame, text="📤 Export Data", command=self.export_data).pack(side=tk.LEFT, padx=5)
    
    def create_progress_section(self, parent):
        """Create progress visualization section"""
        progress_frame = ttk.LabelFrame(parent, text="📈 Progress", padding=10)
        progress_frame.pack(fill=tk.X, pady=(0, 10))
        
        # Progress bars
        bars_frame = ttk.Frame(progress_frame)
        bars_frame.pack(fill=tk.X)
        
        # Tasks progress
        ttk.Label(bars_frame, text="Tasks:").pack(side=tk.LEFT)
        self.tasks_progress = ttk.Progressbar(bars_frame, length=200, mode='determinate')
        self.tasks_progress.pack(side=tk.LEFT, padx=(5, 20))
        self.tasks_progress_label = ttk.Label(bars_frame, text="0%")
        self.tasks_progress_label.pack(side=tk.LEFT)
        
        # Hours progress
        ttk.Label(bars_frame, text="Hours:").pack(side=tk.LEFT, padx=(20, 0))
        self.hours_progress = ttk.Progressbar(bars_frame, length=200, mode='determinate')
        self.hours_progress.pack(side=tk.LEFT, padx=(5, 20))
        self.hours_progress_label = ttk.Label(bars_frame, text="0%")
        self.hours_progress_label.pack(side=tk.LEFT)
        
        # Summary stats
        self.summary_label = ttk.Label(progress_frame, text="", font=('Arial', 9))
        self.summary_label.pack(pady=(10, 0))
    
    def create_left_panel(self, parent):
        """Create left panel with navigation and filters"""
        left_frame = ttk.LabelFrame(parent, text="🎯 Navigation & Filters", padding=10)
        left_frame.pack(side=tk.LEFT, fill=tk.Y, padx=(0, 10))
        
        # Week navigation
        week_frame = ttk.LabelFrame(left_frame, text="📅 Week Navigation", padding=5)
        week_frame.pack(fill=tk.X, pady=(0, 10))
        
        self.week_buttons = []
        self.update_week_buttons()
        
        # Category filters
        category_frame = ttk.LabelFrame(left_frame, text="🏷️ Categories", padding=5)
        category_frame.pack(fill=tk.X, pady=(0, 10))
        
        self.category_var = tk.StringVar(value="All")
        categories = ["All"] + list(set(task.category for task in self.tracker.tasks))
        
        for category in categories:
            ttk.Radiobutton(category_frame, text=category, variable=self.category_var, 
                           value=category, command=self.filter_tasks).pack(anchor=tk.W)
        
        # Status filters
        status_frame = ttk.LabelFrame(left_frame, text="📊 Status", padding=5)
        status_frame.pack(fill=tk.X, pady=(0, 10))
        
        self.status_var = tk.StringVar(value="All")
        statuses = ["All", "Pending", "In Progress", "Completed"]
        
        for status in statuses:
            ttk.Radiobutton(status_frame, text=status, variable=self.status_var, 
                           value=status, command=self.filter_tasks).pack(anchor=tk.W)
        
        # Search
        search_frame = ttk.LabelFrame(left_frame, text="🔍 Search", padding=5)
        search_frame.pack(fill=tk.X)
        
        self.search_var = tk.StringVar()
        self.search_var.trace('w', self.filter_tasks)
        search_entry = ttk.Entry(search_frame, textvariable=self.search_var)
        search_entry.pack(fill=tk.X, pady=(0, 5))
        
        ttk.Button(search_frame, text="Clear Filters", command=self.clear_filters).pack(fill=tk.X)
    
    def create_right_panel(self, parent):
        """Create right panel with task list"""
        right_frame = ttk.LabelFrame(parent, text="📋 Tasks", padding=10)
        right_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)
        
        # Task list
        columns = ("Status", "Day", "Hours", "Category", "Title", "ID")
        self.task_tree = ttk.Treeview(right_frame, columns=columns, show="headings", height=20)
        
        # Configure columns
        self.task_tree.heading("Status", text="Status")
        self.task_tree.column("Status", width=80, anchor="center")
        
        self.task_tree.heading("Day", text="Day")
        self.task_tree.column("Day", width=50, anchor="center")
        
        self.task_tree.heading("Hours", text="Hours")
        self.task_tree.column("Hours", width=60, anchor="center")
        
        self.task_tree.heading("Category", text="Category")
        self.task_tree.column("Category", width=100, anchor="center")
        
        self.task_tree.heading("Title", text="Task Title")
        self.task_tree.column("Title", width=400, anchor="w")
        
        self.task_tree.heading("ID", text="ID")
        self.task_tree.column("ID", width=50, anchor="center")
        
        # Scrollbar
        scrollbar = ttk.Scrollbar(right_frame, orient=tk.VERTICAL, command=self.task_tree.yview)
        self.task_tree.configure(yscrollcommand=scrollbar.set)
        
        # Pack widgets
        self.task_tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        # Task actions
        actions_frame = ttk.Frame(right_frame)
        actions_frame.pack(fill=tk.X, pady=(10, 0))
        
        ttk.Button(actions_frame, text="✅ Mark Complete", command=self.mark_complete).pack(side=tk.LEFT, padx=(0, 5))
        ttk.Button(actions_frame, text="🔄 Mark In Progress", command=self.mark_in_progress).pack(side=tk.LEFT, padx=5)
        ttk.Button(actions_frame, text="📝 Add Notes", command=self.add_notes).pack(side=tk.LEFT, padx=5)
        ttk.Button(actions_frame, text="🔄 Toggle Status", command=self.toggle_status).pack(side=tk.LEFT, padx=5)
        
        # Bind double-click
        self.task_tree.bind("<Double-1>", lambda e: self.toggle_status())
    
    def create_status_bar(self, parent):
        """Create status bar"""
        self.status_var = tk.StringVar(value="Ready")
        status_bar = ttk.Label(parent, textvariable=self.status_var, relief=tk.SUNKEN, anchor=tk.W)
        status_bar.pack(fill=tk.X, pady=(10, 0))
    
    def pick_start_date(self, event=None):
        """Open calendar picker for start date"""
        dialog = DatePickerDialog(self.root, "Select Start Date", self.tracker.start_date)
        if dialog.result:
            self.tracker.start_date = dialog.result
            self.update_end_date()
            self.tracker.save_state()
            self.refresh_display()
    
    def update_duration(self, event=None):
        """Update plan duration"""
        try:
            new_duration = int(self.duration_var.get())
            if 7 <= new_duration <= 365:
                self.tracker.total_days = new_duration
                self.update_end_date()
                self.tracker.save_state()
                self.refresh_display()
            else:
                messagebox.showerror("Invalid Duration", "Duration must be between 7 and 365 days")
                self.duration_var.set(str(self.tracker.total_days))
        except ValueError:
            messagebox.showerror("Invalid Duration", "Please enter a valid number")
            self.duration_var.set(str(self.tracker.total_days))
    
    def update_end_date(self):
        """Update end date based on start date and duration"""
        if self.tracker.start_date:
            start = datetime.strptime(self.tracker.start_date, "%Y-%m-%d")
            end = start + timedelta(days=self.tracker.total_days - 1)
            self.tracker.end_date = end.strftime("%Y-%m-%d")
    
    def update_week_buttons(self):
        """Update week navigation buttons based on plan duration"""
        # Find the week frame
        week_frame = None
        for child in self.root.winfo_children():
            if isinstance(child, ttk.Frame):
                for grandchild in child.winfo_children():
                    if isinstance(grandchild, ttk.LabelFrame) and "Week Navigation" in str(grandchild.cget("text")):
                        week_frame = grandchild
                        break
                if week_frame:
                    break
        
        if week_frame:
            # Clear existing buttons
            for button in self.week_buttons:
                button.destroy()
            self.week_buttons.clear()
            
            # Calculate number of weeks
            total_weeks = (self.tracker.total_days + 6) // 7  # Round up
            
            # Create week buttons
            for week in range(1, total_weeks + 1):
                button = ttk.Button(week_frame, text=f"Week {week}", 
                                  command=lambda w=week: self.show_week(w))
                button.pack(fill=tk.X, pady=2)
                self.week_buttons.append(button)
    
    def refresh_display(self):
        """Refresh all display elements"""
        # Update header
        self.start_date_var.set(self.tracker.start_date or "Not set")
        self.end_date_var.set(self.tracker.end_date or "Not set")
        self.duration_var.set(str(self.tracker.total_days))
        current_day = self.tracker.get_current_day()
        self.current_day_var.set(f"{current_day}/{self.tracker.total_days}")
        
        # Update progress
        summary = self.tracker.get_progress_summary()
        self.tasks_progress['value'] = summary['completion_percentage']
        self.tasks_progress_label.config(text=f"{summary['completion_percentage']}%")
        
        self.hours_progress['value'] = summary['hours_percentage']
        self.hours_progress_label.config(text=f"{summary['hours_percentage']}%")
        
        self.summary_label.config(
            text=f"Completed: {summary['completed']}/{summary['total_tasks']} tasks "
                 f"({summary['completed_hours']:.1f}/{summary['total_hours']:.1f} hours)"
        )
        
        # Update week buttons
        self.update_week_buttons()
        
        # Update task list
        self.filter_tasks()
    
    def filter_tasks(self, *args):
        """Filter tasks based on current filters"""
        # Clear existing items
        for item in self.task_tree.get_children():
            self.task_tree.delete(item)
        
        # Get filter values
        category_filter = self.category_var.get()
        status_filter = self.status_var.get()
        search_term = self.search_var.get().lower()
        
        # Filter tasks
        filtered_tasks = []
        for task in self.tracker.tasks:
            # Category filter
            if category_filter != "All" and task.category != category_filter:
                continue
            
            # Status filter
            if status_filter != "All":
                if status_filter == "Pending" and task.status != TaskStatus.PENDING:
                    continue
                elif status_filter == "In Progress" and task.status != TaskStatus.IN_PROGRESS:
                    continue
                elif status_filter == "Completed" and task.status != TaskStatus.COMPLETED:
                    continue
            
            # Search filter
            if search_term and search_term not in task.title.lower():
                continue
            
            filtered_tasks.append(task)
        
        # Sort by day, then by created order
        filtered_tasks.sort(key=lambda t: (t.day, t.created_order))
        
        # Add to tree
        for task in filtered_tasks:
            status_emoji = {
                TaskStatus.PENDING: "⏳",
                TaskStatus.IN_PROGRESS: "🔄",
                TaskStatus.COMPLETED: "✅",
                TaskStatus.SKIPPED: "⏭️"
            }
            
            self.task_tree.insert("", "end", values=(
                status_emoji[task.status],
                task.day,
                f"{task.hours:.1f}",
                task.category,
                task.title,
                task.id
            ))
    
    def clear_filters(self):
        """Clear all filters"""
        self.category_var.set("All")
        self.status_var.set("All")
        self.search_var.set("")
        self.filter_tasks()
    
    def show_today(self):
        """Show today's tasks"""
        self.category_var.set("All")
        self.status_var.set("All")
        self.search_var.set("")
        
        # Filter to today's tasks
        today_tasks = self.tracker.get_today_tasks()
        if today_tasks:
            self.status_var.set("All")  # Show all statuses for today
            self.filter_tasks()
            self.status_var.set("All")
            messagebox.showinfo("Today's Tasks", f"You have {len(today_tasks)} tasks scheduled for today!")
        else:
            messagebox.showinfo("Today's Tasks", "No tasks scheduled for today!")
    
    def show_week(self, week: int):
        """Show tasks for a specific week"""
        week_tasks = self.tracker.get_week_tasks(week)
        if week_tasks:
            # Clear filters and show week tasks
            self.clear_filters()
            # Filter to show only this week's tasks
            for item in self.task_tree.get_children():
                self.task_tree.delete(item)
            
            for task in week_tasks:
                status_emoji = {
                    TaskStatus.PENDING: "⏳",
                    TaskStatus.IN_PROGRESS: "🔄",
                    TaskStatus.COMPLETED: "✅",
                    TaskStatus.SKIPPED: "⏭️"
                }
                
                self.task_tree.insert("", "end", values=(
                    status_emoji[task.status],
                    task.day,
                    f"{task.hours:.1f}",
                    task.category,
                    task.title,
                    task.id
                ))
            
            messagebox.showinfo(f"Week {week}", f"Week {week} has {len(week_tasks)} tasks scheduled!")
        else:
            messagebox.showinfo(f"Week {week}", f"No tasks found for week {week}")
    
    def show_progress_report(self):
        """Show detailed progress report"""
        summary = self.tracker.get_progress_summary()
        
        report = f"""📊 DETAILED PROGRESS REPORT
{'='*50}

📈 Overall Progress:
• Tasks: {summary['completed']}/{summary['total_tasks']} ({summary['completion_percentage']}%)
• Hours: {summary['completed_hours']:.1f}/{summary['total_hours']:.1f} ({summary['hours_percentage']}%)

📊 Status Breakdown:
• ✅ Completed: {summary['completed']}
• 🔄 In Progress: {summary['in_progress']}
• ⏳ Pending: {summary['pending']}

🏷️ Category Progress:"""
        
        for category, stats in summary['categories'].items():
            cat_percentage = (stats['completed'] / stats['total'] * 100) if stats['total'] > 0 else 0
            report += f"\n• {category}: {stats['completed']}/{stats['total']} ({cat_percentage:.1f}%)"
        
        messagebox.showinfo("Progress Report", report)
    
    def mark_complete(self):
        """Mark selected task as complete"""
        selection = self.task_tree.selection()
        if not selection:
            messagebox.showwarning("No Selection", "Please select a task to mark as complete.")
            return
        
        item = selection[0]
        task_id = int(self.task_tree.set(item, "ID"))
        
        notes = simpledialog.askstring("Add Notes", "Add completion notes (optional):")
        if self.tracker.mark_task_complete(task_id, notes or ""):
            self.refresh_display()
            self.status_var.set("Task marked as complete!")
        else:
            messagebox.showerror("Error", "Failed to mark task as complete.")
    
    def mark_in_progress(self):
        """Mark selected task as in progress"""
        selection = self.task_tree.selection()
        if not selection:
            messagebox.showwarning("No Selection", "Please select a task to mark as in progress.")
            return
        
        item = selection[0]
        task_id = int(self.task_tree.set(item, "ID"))
        
        if self.tracker.mark_task_in_progress(task_id):
            self.refresh_display()
            self.status_var.set("Task marked as in progress!")
        else:
            messagebox.showerror("Error", "Failed to mark task as in progress.")
    
    def toggle_status(self):
        """Toggle task completion status"""
        selection = self.task_tree.selection()
        if not selection:
            messagebox.showwarning("No Selection", "Please select a task to toggle.")
            return
        
        item = selection[0]
        task_id = int(self.task_tree.set(item, "ID"))
        
        if self.tracker.toggle_task_status(task_id):
            self.refresh_display()
            self.status_var.set("Task status toggled!")
        else:
            messagebox.showerror("Error", "Failed to toggle task status.")
    
    def add_notes(self):
        """Add notes to selected task"""
        selection = self.task_tree.selection()
        if not selection:
            messagebox.showwarning("No Selection", "Please select a task to add notes to.")
            return
        
        item = selection[0]
        task_id = int(self.task_tree.set(item, "ID"))
        
        # Find the task
        task = None
        for t in self.tracker.tasks:
            if t.id == task_id:
                task = t
                break
        
        if task:
            current_notes = task.notes
            notes = simpledialog.askstring("Add Notes", f"Add notes for '{task.title}':", initialvalue=current_notes)
            if notes is not None:
                task.notes = notes
                self.tracker.save_state()
                self.refresh_display()
                self.status_var.set("Notes updated!")
        else:
            messagebox.showerror("Error", "Task not found.")
    
    def backup_data(self):
        """Create a backup of current data"""
        try:
            self.tracker.save_state()  # This already creates backups
            messagebox.showinfo("Backup Created", f"Data backed up to {self.tracker.backup_dir}")
        except Exception as e:
            messagebox.showerror("Backup Error", f"Failed to create backup: {e}")
    
    def export_data(self):
        """Export data to CSV or JSON"""
        file_path = filedialog.asksaveasfilename(
            defaultextension=".json",
            filetypes=[("JSON files", "*.json"), ("CSV files", "*.csv")],
            title="Export Data"
        )
        
        if not file_path:
            return
        
        try:
            if file_path.endswith('.csv'):
                self.export_to_csv(file_path)
            else:
                self.export_to_json(file_path)
            messagebox.showinfo("Export Complete", f"Data exported to {file_path}")
        except Exception as e:
            messagebox.showerror("Export Error", f"Failed to export data: {e}")
    
    def export_to_csv(self, file_path):
        """Export data to CSV format"""
        import csv
        
        with open(file_path, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(['ID', 'Day', 'Title', 'Hours', 'Category', 'Status', 'Done', 'Notes', 'Completed Date'])
            
            for task in self.tracker.tasks:
                writer.writerow([
                    task.id,
                    task.day,
                    task.title,
                    task.hours,
                    task.category,
                    task.status.value,
                    task.done,
                    task.notes,
                    task.completed_date or ""
                ])
    
    def export_to_json(self, file_path):
        """Export data to JSON format"""
        data = {
            "start_date": self.tracker.start_date,
            "end_date": self.tracker.end_date,
            "hours_per_day_target": self.tracker.hours_per_day_target,
            "version": self.tracker.version,
            "export_date": datetime.now().isoformat(),
            "tasks": []
        }
        
        for task in self.tracker.tasks:
            task_data = {
                "id": task.id,
                "title": task.title,
                "hours": task.hours,
                "day": task.day,
                "done": task.done,
                "created_order": task.created_order,
                "status": task.status.value,
                "notes": task.notes,
                "completed_date": task.completed_date,
                "category": task.category
            }
            data["tasks"].append(task_data)
        
        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2)
    
    def run(self):
        """Start the GUI application"""
        self.root.mainloop()

def main():
    """Main entry point"""
    print("🚀 Starting Enhanced Cybersecurity Job Search Tracker...")
    app = EnhancedGUI()
    app.run()

if __name__ == "__main__":
    main()

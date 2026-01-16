# Windows to Linux Transfer Guide

## Your Personal Data Files to Transfer

The application loads files in this priority order:
1. **`my_schedule.json`** - Your main schedule (PRIORITY - copy this!)
2. `enhanced_plan_state.json` - State file (also copy this!)
3. `backups/` - Optional backup files (you can skip these or copy the latest one)

## Step-by-Step Transfer Instructions

### On Windows (Before Switching):

1. **Locate your files:**
   ```
   C:\Users\Admin\Documents\PROJECTS CYBER\career-development-tracker-1.0.0\
   ├── my_schedule.json          ← COPY THIS
   ├── enhanced_plan_state.json  ← COPY THIS
   └── backups/                  ← OPTIONAL (copy latest if you want)
   ```

2. **Export your data (choose one method):**

   **Method A: Manual Copy**
   - Copy `my_schedule.json` and `enhanced_plan_state.json` to a USB drive, cloud storage, or email them to yourself

   **Method B: Use the export script (run on Windows)**
   - Run `export_data_for_linux.bat` to create a ZIP file with your data

   **Method C: Copy to a shared location**
   - If you have SSH access to your Linux machine already, use SCP/WinSCP to transfer directly

### On Linux (After Setup):

1. **Clone the repository fresh:**
   ```bash
   git clone https://github.com/jacobdcook/career-development-tracker.git
   cd career-development-tracker
   ```

2. **Transfer your JSON files:**
   - Copy `my_schedule.json` and `enhanced_plan_state.json` to the cloned directory

3. **Verify the files:**
   ```bash
   ls -la my_schedule.json enhanced_plan_state.json
   ```

4. **Run the application:**
   ```bash
   python3 enhanced_cybersecurity_tracker.py
   ```

## File Transfer Methods

### Option 1: USB Drive / External Storage
- Copy the 2 JSON files to a USB drive
- Boot into Linux
- Copy from USB to the cloned repo directory

### Option 2: Cloud Storage (Google Drive, Dropbox, etc.)
- Upload the 2 JSON files to cloud storage from Windows
- Download them on Linux
- Copy to the cloned repo directory

### Option 3: Email
- Email the 2 JSON files to yourself
- Download attachments on Linux
- Copy to the cloned repo directory

### Option 4: SSH/SCP (if Linux machine is accessible)
```bash
# From Windows PowerShell (if you have SSH):
scp my_schedule.json enhanced_plan_state.json user@linux-ip:/path/to/cloned/repo/
```

### Option 5: WinSCP (GUI tool)
- Download WinSCP on Windows
- Connect to your Linux machine via SSH
- Drag and drop the 2 JSON files to the cloned repo directory

## Verification Checklist

- [ ] Copied `my_schedule.json` from Windows
- [ ] Copied `enhanced_plan_state.json` from Windows  
- [ ] Cloned fresh repo on Linux (`git clone ...`)
- [ ] Placed JSON files in cloned repo directory
- [ ] Verified files are readable (`ls -la`)
- [ ] Tested application loads correctly (`python3 enhanced_cybersecurity_tracker.py`)

## Troubleshooting

**If files don't load:**
- Make sure filenames are exact: `my_schedule.json` (not `my_schedule.JSON` or `My_Schedule.json`)
- Check file permissions: `chmod 644 my_schedule.json enhanced_plan_state.json`
- Verify JSON is valid: `python3 -m json.tool my_schedule.json`

**If you only have one file:**
- `my_schedule.json` is the most important - the app will create `enhanced_plan_state.json` from it
- Just copy `my_schedule.json` and the app will handle the rest

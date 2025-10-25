import os
import subprocess
from datetime import datetime

# Your commit history timeline
commits = [
    # 11th Oct
    ("2025-10-11 14:00:00", "Initial DRF project setup – created base structure for backend and contacts app."),
    ("2025-10-11 17:30:00", "Added Contact model and initial migrations."),
    
    # 16th Oct
    ("2025-10-16 13:15:00", "Integrated Django REST Framework and created serializers for Contact model."),
    ("2025-10-16 18:00:00", "Added ContactViewSet and registered routes in urls.py."),
    
    # 17th Oct
    ("2025-10-17 11:00:00", "Implemented JWT authentication using SimpleJWT."),
    ("2025-10-17 15:45:00", "Tested API endpoints for registration and login."),
    
    # 18th Oct
    ("2025-10-18 12:00:00", "Connected frontend (HTML/JS) with backend APIs using fetch()."),
    ("2025-10-18 16:20:00", "Added CORS configuration and tested full CRUD flow."),
    
    # 22nd Oct
    ("2025-10-22 10:30:00", "Finalized API integration between Django and frontend."),
    ("2025-10-22 19:00:00", "Cleaned code, improved serializers."),
]

# Your Git username and email
AUTHOR_NAME = "Jiya Bhomia"
AUTHOR_EMAIL = "jiya.bhomia123@gmail.com"  # replace with your actual GitHub email

# Push after creating commits
PUSH_AFTER = True

def run_command(cmd):
    """Run shell command and print output."""
    result = subprocess.run(cmd, shell=True, text=True, capture_output=True)
    if result.stdout:
        print(result.stdout)
    if result.stderr:
        print(result.stderr)

for date, message in commits:
    print(f"\n--- Creating commit for {date}: {message} ---")

    # Make sure there's at least one change (Git won't commit otherwise)
    # Create a dummy file update for each commit
    with open("commit_log.txt", "a") as f:
        f.write(f"{date} - {message}\n")

    # Add all files
    run_command("git add .")

    # Commit with backdated timestamp
    env = os.environ.copy()
    env["GIT_COMMITTER_DATE"] = date
    env["GIT_AUTHOR_DATE"] = date
    cmd = f'git commit -m "{message}" --author="{AUTHOR_NAME} <{AUTHOR_EMAIL}>"'
    subprocess.run(cmd, shell=True, env=env)

# Push to GitHub
if PUSH_AFTER:
    print("\nPushing all commits to GitHub...")
    run_command("git push origin main")

import os
import subprocess

# --- CONFIGURATION ---
GITHUB_URL = "https://github.com/JiyaBhomia/contact-book-drf-backend.git"  # ← change this
BRANCH = "main"  # or 'master' if that's your branch name

# --- STEP 1: Remove .git folder ---
if os.path.exists(".git"):
    print("🗑️  Removing old .git history...")
    subprocess.run(["rm", "-rf", ".git"])
else:
    print("⚠️  No .git folder found. Skipping deletion.")

# --- STEP 2: Reinitialize git repo ---
print("🚀 Initializing new git repository...")
subprocess.run(["git", "init"])

# --- STEP 3: Add all files ---
print("📦 Adding all project files...")
subprocess.run(["git", "add", "."])

# --- STEP 4: Make initial commit ---
print("📝 Creating fresh initial commit...")
subprocess.run(["git", "commit", "-m", "Removed Unnecessary Comments"])

# --- STEP 5: Connect to GitHub remote ---
print(f"🔗 Connecting to remote: {GITHUB_URL}")
subprocess.run(["git", "remote", "add", "origin", GITHUB_URL])

# --- STEP 6: Force push new clean history ---
print("📤 Force pushing new history to GitHub...")
subprocess.run(["git", "branch", "-M", BRANCH])
subprocess.run(["git", "push", "--force", "origin", BRANCH])

print("\n✅ All commit history has been deleted and new history pushed successfully!")

import os
import shutil
import subprocess

# Define paths based on your actual structure
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.dirname(SCRIPT_DIR)
DIST_DIR = os.path.join(PROJECT_ROOT, "dist")

# Create dist directory
if os.path.exists(DIST_DIR):
    shutil.rmtree(DIST_DIR)
os.makedirs(DIST_DIR)
os.makedirs(os.path.join(DIST_DIR, "assets"), exist_ok=True)

# Copy main app file
app_file = "main.py"
shutil.copy(os.path.join(PROJECT_ROOT, app_file), DIST_DIR)

# Create a renamed version for FCGI to reference
shutil.copy(os.path.join(PROJECT_ROOT, app_file), os.path.join(DIST_DIR, "app.py"))

# Copy requirements if it exists
req_file = os.path.join(PROJECT_ROOT, "requirements.txt")
if os.path.exists(req_file):
    shutil.copy(req_file, DIST_DIR)
else:
    # Create requirements.txt if it doesn't exist
    with open(os.path.join(DIST_DIR, "requirements.txt"), "w") as f:
        f.write("streamlit\npydantic\nrequests\n")

# Copy logo and other assets
logo_file = os.path.join(PROJECT_ROOT, "logo.png")
if os.path.exists(logo_file):
    shutil.copy(logo_file, os.path.join(DIST_DIR, "assets"))
    # Also copy to root for direct access
    shutil.copy(logo_file, DIST_DIR)

# Create a simple index.html to avoid 404
with open(os.path.join(DIST_DIR, "index.html"), "w") as f:
    f.write("""<!DOCTYPE html>
<html>
<head>
    <title>Athena AI</title>
    <meta http-equiv="refresh" content="0;URL='./streamlit'" />
</head>
<body>
    <p>Redirecting to Athena AI...</p>
</body>
</html>
""")

# Create .htaccess file for Hostinger
with open(os.path.join(DIST_DIR, ".htaccess"), "w") as f:
    f.write("""
AddHandler fcgid-script .fcgi
RewriteEngine On
RewriteCond %{REQUEST_FILENAME} !-f
RewriteRule ^(.*)$ app.fcgi/$1 [QSA,L]
""")

# Create FCGI wrapper script
with open(os.path.join(DIST_DIR, "app.fcgi"), "w") as f:
    f.write("""#!/usr/bin/python3
import sys
import streamlit.web.bootstrap

if __name__ == "__main__":
    sys.argv = ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
    streamlit.web.bootstrap.run()
""")

# Make FCGI file executable
os.chmod(os.path.join(DIST_DIR, "app.fcgi"), 0o755)

print(f"Build completed. Files are in the '{DIST_DIR}' directory.")
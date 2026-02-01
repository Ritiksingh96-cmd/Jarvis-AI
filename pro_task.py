import subprocess

# Close all windows
subprocess.call(["taskkill", "/F", "/IM", "explorer.exe"])

# Open Anti-Gravity program
subprocess.Popen("C:\\Program Files\\AntiGravity\\AntiGravity.exe")
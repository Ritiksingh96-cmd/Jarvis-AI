import os
import requests
import subprocess
from dotenv import load_dotenv

load_dotenv()

GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")

def create_private_repo(repo_name):
    if not GITHUB_TOKEN:
        print("Error: GITHUB_TOKEN not found in .env file.")
        return None

    url = "https://api.github.com/user/repos"
    headers = {
        "Authorization": f"token {GITHUB_TOKEN}",
        "Accept": "application/vnd.github.v3+json"
    }
    data = {
        "name": repo_name,
        "private": True
    }

    response = requests.post(url, json=data, headers=headers)
    if response.status_code == 201:
        print(f"Successfully created private repository: {repo_name}")
        return response.json()["clone_url"]
    elif response.status_code == 422:
        print(f"Repository {repo_name} already exists.")
        # Try to get the existing repo URL
        user_response = requests.get("https://api.github.com/user", headers=headers)
        if user_response.status_code == 200:
            username = user_response.json()["login"]
            return f"https://github.com/{username}/{repo_name}.git"
        return None
    else:
        print(f"Failed to create repository: {response.status_code}")
        print(response.json())
        return None

def push_to_github(repo_url):
    try:
        # Check if git is initialized
        if not os.path.exists(".git"):
            subprocess.run(["git", "init"], check=True)
        
        # Add all files
        subprocess.run(["git", "add", "."], check=True)
        
        # Commit
        subprocess.run(["git", "commit", "-m", "Initial commit from JARVIS"], check=True)
        
        # Rename branch to main if it's master
        subprocess.run(["git", "branch", "-M", "main"], check=True)
        
        # Add remote
        # Check if remote exists
        remotes = subprocess.run(["git", "remote"], capture_output=True, text=True).stdout
        if "origin" in remotes:
            subprocess.run(["git", "remote", "remove", "origin"], check=True)
        
        # Use token in URL for authentication
        auth_url = repo_url.replace("https://", f"https://{GITHUB_TOKEN}@")
        subprocess.run(["git", "remote", "add", "origin", auth_url], check=True)
        
        # Push
        subprocess.run(["git", "push", "-u", "origin", "main"], check=True)
        print("Successfully pushed to GitHub.")
        return True
    except Exception as e:
        print(f"An error occurred during git operations: {e}")
        return False

if __name__ == "__main__":
    repo_name = "jarvis-open-interpreter"
    repo_url = create_private_repo(repo_name)
    if repo_url:
        push_to_github(repo_url)

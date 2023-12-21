import requests
import json
from datetime import datetime, timedelta

# Replace with your GitHub repository details
repo_owner = "Sam12121"
repo_name = "demo"
token = "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"

# Function to create a GitHub issue
def create_issue(title, body, milestone):
    url = f"https://api.github.com/repos/{repo_owner}/{repo_name}/issues"
    headers = {
        "Authorization": f"Bearer {token}",
        "Accept": "application/vnd.github.v3+json",
    }
    data = {"title": title, "body": body, "milestone": milestone["number"]}
    response = requests.post(url, headers=headers, data=json.dumps(data))
    return response.json()

# Function to create a GitHub milestone
def create_milestone(title, due_date=None):
    url = f"https://api.github.com/repos/{repo_owner}/{repo_name}/milestones"
    headers = {
        "Authorization": f"Bearer {token}",
        "Accept": "application/vnd.github.v3+json",
    }
    data = {"title": title, "due_on": due_date}
    response = requests.post(url, headers=headers, data=json.dumps(data))
    return response.json()

# Replace with your roadmap details
roadmap = [
    {"title": "Discovery and Planning", "duration": 2},
    {"title": "UI/UX Design Collaboration", "duration": 2},
    {"title": "Development and Integration", "duration": 2},
    {"title": "Testing and Validation", "duration": 2},
    {"title": "Deployment and Post-Launch", "duration": 1},
]

# Calculate due dates based on the current date
current_date = datetime.utcnow()
milestones = []

for task in roadmap:
    due_date = current_date + timedelta(days=task["duration"] * 30)
    milestone = create_milestone(task["title"], due_date.isoformat())
    milestones.append(milestone)

# Create issues under each milestone
for i, task in enumerate(roadmap):
    title = f"{i+1}. {task['title']}"
    body = f"Description and details for {task['title']}..."
    create_issue(title, body, milestones[i])

import requests
import json
from datetime import datetime, timedelta
import pytz

# Replace with your GitHub repository details
repo_owner = "Sam12121"
repo_name = "Sam12121/demo"
token = "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"

# Function to create a GitHub issue
def create_issue(title, body, milestone_number):
    url = f"https://api.github.com/repos/{repo_owner}/{repo_name}/issues"
    headers = {
        "Authorization": f"Bearer {token}",
        "Accept": "application/vnd.github.v3+json",
    }
    data = {"title": title, "body": body, "milestone": milestone_number}
    response = requests.post(url, headers=headers, data=json.dumps(data))
    return response.json()

# Function to create a GitHub milestone and extract milestone number
def create_milestone_and_get_number(title, due_date=None):
    url = f"https://api.github.com/repos/{repo_owner}/{repo_name}/milestones"
    headers = {
        "Authorization": f"Bearer {token}",
        "Accept": "application/vnd.github.v3+json",
    }
    data = {"title": title, "due_on": due_date}
    response = requests.post(url, headers=headers, data=json.dumps(data))
    
    # Print the response for debugging
    print("Milestone Creation Response:", response.json())
    
    milestone_number = response.json().get("number")
    return milestone_number


# Define tasks for each team and role
tasks = [
    # Backend Development (Go - Golang)
    {"title": "Architecture and Database Setup", "duration": 2},
    {"title": "Core Functionality Implementation", "duration": 2},
    {"title": "API Development", "duration": 2},

    # Frontend Development (React)
    {"title": "UI/UX Design Collaboration", "duration": 2},
    {"title": "Frontend Implementation", "duration": 2},
    {"title": "User Acceptance Testing", "duration": 2},

    # AI Integration (Python)
    {"title": "AI Model Selection", "duration": 2},
    {"title": "Model Integration", "duration": 2},
    {"title": "Continuous Improvement", "duration": 2},

    # Testing Team
    {"title": "Unit Testing", "duration": 6},
    {"title": "Integration Testing", "duration": 2},
    {"title": "Security Testing", "duration": 2},

    # Project Management
    {"title": "Overall Project Oversight", "duration": 6},
    {"title": "Agile Methodology Implementation", "duration": 6},

    # Miscellaneous
    {"title": "Tools and Infrastructure Setup", "duration": 1},
    {"title": "Continuous Monitoring and Improvement", "duration": 6},
]

# Calculate due dates based on the current date in IST
current_date = datetime.now(pytz.timezone('Asia/Kolkata'))
milestones = []

# Create milestones and issues for each task
for task in tasks:
    due_date = current_date + timedelta(days=task["duration"] * 30)
    milestone_number = create_milestone_and_get_number(task["title"], due_date.isoformat())

    # Create an issue for each task
    issue_title = f"{task['title']} - {task['duration']} months"
    issue_body = f"Description and details for {task['title']}..."
    create_issue(issue_title, issue_body, milestone_number)

    milestones.append(milestone_number)

# Print milestone numbers for reference
print("Milestone Numbers:", milestones)

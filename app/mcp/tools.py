# app/mcp/tools.py

import requests
from app.config.settings import (
    GITHUB_TOKEN,
    GITHUB_OWNER,
    GITHUB_REPO 
)

BASE_URL = f"https://api.github.com/repos/{GITHUB_OWNER}/{GITHUB_REPO}"

headers = {
    "Authorization":f"token {GITHUB_TOKEN}",
    "Accept":"application/vnd.github+json"
}

def add_label(issue_number: int, labels: list):
    url = f"{BASE_URL}/issues/{issue_number}/labels"
    return requests.post(url , json={"labels":labels}, headers=headers).json()

def comment_on_issue(issue_number: int, message: str):
    url = f"{BASE_URL}/issues/{issue_number}/comments"
    return requests.post(url, json={"body":message}, headers=headers).json()

def assign_user(issue_number: int,username:str):
    url = f"{BASE_URL}/issues/{issue_number}"
    return requests.patch(url, json={"assignees":[username]},headers=headers).json()
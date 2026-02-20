# app/mcp/client.py

import requests
from app.config.settings import MCP_BASE_URL

def add_label(issue_number, labels):
    url = f"{MCP_BASE_URL}/tools/add_label"
    return requests.post(url, json={"issue_number": issue_number,"labels":labels})


def comment(issue_number, message):
    url = f"{MCP_BASE_URL}/tools/comment"
    return requests.post(url,json={"issue_number":issue_number,"message":message})

def assign(issue_number,username):
    url = f"{MCP_BASE_URL}/tools/assign"
    return requests.post(url, json={"issue_number":issue_number,"username":username})
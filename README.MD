GitHub Issue Automation System

An AI-powered automation system that listens to GitHub issue events via webhooks and intelligently triages, analyzes, and processes issues using a LangGraph-based workflow.

This system automatically handles newly opened issues and routes them through an LLM-powered workflow for classification, prioritization, and decision-making.

📌 Project Overview

When a new issue is opened in a GitHub repository:

    1.GitHub sends a webhook event to our FastAPI server.

    2.The server extracts issue details.

    3.A LangGraph workflow processes the issue.

The system can:

Classify issue type

Assign priority

Generate responses

Trigger automated actions (labels, comments, etc.)

This eliminates manual triaging and improves issue handling efficiency.

🏗️ Architecture
GitHub Issue Created
        ↓
GitHub Webhook
        ↓
FastAPI Server (/webhook)
        ↓
LangGraph Workflow
        ↓
LLM Decision Engine
        ↓
Automated GitHub API Action
⚙️ Tech Stack

Backend: FastAPI

Workflow Engine: LangGraph

LLM Integration: OpenAI API

Event Handling: GitHub Webhooks

API Communication: GitHub REST API

Language: Python 3.11+

📂 Project Structure
app/
│
├── main.py               # FastAPI app & webhook endpoint
├── graph/
│   └── workflow.py       # LangGraph workflow builder
│
└── services/             # (future) GitHub + LLM integrations
🔁 How It Works
1️⃣ GitHub Webhook

GitHub sends a POST request when an issue is opened.

Endpoint: /webhook

Only processes "action": "opened" events.

2️⃣ State Creation
state = {
    "title": payload["issue"]["title"],
    "body": payload["issue"]["body"]
}

This state is passed into the LangGraph workflow.

3️⃣ LangGraph Execution

The workflow:

Analyzes issue content

Makes decisions

Returns structured output

🛠️ Setup Instructions
1️⃣ Clone the Repository
git clone https://github.com/your-username/github-issue-automation.git
cd github-issue-automation
2️⃣ Create Virtual Environment
python -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows
3️⃣ Install Dependencies
pip install -r requirements.txt
4️⃣ Run the Server
uvicorn app.main:app --reload

Server runs at:

http://localhost:8000
🔗 GitHub Webhook Configuration

Go to your GitHub repository.

Settings → Webhooks → Add Webhook

Payload URL:

https://your-domain.com/webhook

Content Type:

application/json

Select:

Issues

Now every new issue will trigger your system.

🔐 Environment Variables

Create a .env file:

OPENAI_API_KEY=your_openai_key
GITHUB_TOKEN=your_github_token

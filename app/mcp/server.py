#app/mcp/server

from fastapi import FastAPI
from pydantic import BaseModel
from app.mcp.tools import add_label, comment_on_issue, assign_user

app = FastAPI()

class LabelRequest(BaseModel):
    issue_number: int
    labels: list

class CommonRequest(BaseModel):
    issue_number: int
    message: str

class AssignRequest(BaseModel):
    issue_number : int
    username : str

@app.post("/tools/add_label")
def add_label_tool(req: LabelRequest):
    return add_label(req.issue_number, req.labels)


@app.post("/tools/comment")
def comment_tool(req: CommonRequest):
    return comment_on_issue(req.issue_number, req.message)


@app.post("/tools/assign")
def assign_tool(req: AssignRequest):
    return assign_user(req.issue_number , req.username)
### Run below command to run server
## uvicorn app.mcp.server:app --port 9000


# app/graph/triage_agent.py

from app.graph.state import IssueState
from app.llm.llm_classifier import classify_issue_with_llm

def triage_node(state: IssueState) ->IssueState:
    
    result = classify_issue_with_llm(
        state["title"],
        state["body"]
    )

    state["issue_type"] = result["issue_type"]
    state["priority"] = result["priority"]
    state["team"] = result["team"]
    state["reasoning"] = result["reasoning"]

    state["labels"] = [
        state["issue_type"],
        state["priority"]
    ]

    return state
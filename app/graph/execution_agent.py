# app/graph/execution_agent.py

from app.graph.state import IssueState
from app.mcp.client import add_label, comment

PROCESSED_ISSUE = set()

def execution_node(state: IssueState) ->IssueState:

    issue_number = state["issue_number"]

    if issue_number in PROCESSED_ISSUE:
        print("Skipping duplicate processing")
        return state
    
    PROCESSED_ISSUE.add(issue_number)
    try:

        add_label(issue_number,state["labels"])

    except Exception as e:
        print(f"labelling failed for issue {issue_number}: {e}")


    try:

        comment(
            issue_number,
            f"""
                AI Triage result

                Type: {state['issue_type']}
                Priority: {state['priority']}
                Team: {state['team']}

                Reasoning:
                {state['reasoning']}

                """
            )   
    
    except Exception as e:
        print(f"Comment failed for issue {issue_number}:{e}")
    return state
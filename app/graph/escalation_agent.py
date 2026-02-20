from app.graph.state import IssueState
from app.mcp.client import add_label, comment, assign


ESCALATION_MARKER = "<!-- ESCALATED_BY_AI -->"
TEAM_ESCALATION_MAP = {
    "frontend-team": "Amit-9889",
    "backend-team": "Raj-Dev",
}



def escalation_node(state: IssueState):

    issue_number = state["issue_number"]

    SENIOR = TEAM_ESCALATION_MAP.get(state['team'])
    ## Add urgent label

    add_label(issue_number,["urgent"])

    assign(issue_number,SENIOR)

    ## Add escalation comment

    comment(
    issue_number,
    f"""
        {ESCALATION_MARKER}

        🚨 **Escalation Triggered**

        This issue has been marked as **P1 (Critical)**.

        - Assigned to: @{SENIOR}
        - Urgent label applied
        - Immediate attention required

        Please investigate as soon as possible.
        """
        )

    return state


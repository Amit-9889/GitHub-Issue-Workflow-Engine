# app/graph/workflow.py

from langgraph.graph import StateGraph, END
from app.graph.state import IssueState
from app.graph.triage_agent import triage_node
from app.graph.execution_agent import execution_node
from app.graph.escalation_agent import escalation_node

def build_graph():

    workflow = StateGraph(IssueState)

    workflow.add_node("triage",triage_node)
    workflow.add_node("escalate",escalation_node)
    workflow.add_node("execute",execution_node)

    workflow.set_entry_point("triage")

    ## Condional routing

    def route_based_on_priority(state: IssueState):

        if state['priority']=='P1':
            return "escalate"
        
        return "execute"


    workflow.add_conditional_edges("triage",route_based_on_priority)
    workflow.add_edge("escalate","execute")
    workflow.add_edge("execute", END)

    return workflow.compile()
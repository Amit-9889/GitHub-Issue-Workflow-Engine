from typing import TypedDict, List

class IssueState(TypedDict):

    title : str     ## Short summary of issue
    body : str      ## Detailed description
    issue_number : int ## GitHub issue ID

    issue_type : str ## category of issue 
    priority : str ## Priority to show seriousness of issue
    team : str ## Team to them this issue will be assigned

    labels : List[str] ## Stores GitHub labels attached to the issue
    reasoning : str ## LLM/agent explanation for its decision


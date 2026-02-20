# app/main.py

from fastapi import FastAPI,Request,BackgroundTasks
from app.graph.workflow import build_graph


app = FastAPI()
graph = build_graph()

@app.post("/webhook")
async def github_webhook(request:Request, background_tasks:BackgroundTasks):
    payload =  await request.json()

    if payload.get("action") != "opened":
        return {"status":"ignored"}
    
    
    state = { "title" : payload["issue"]["title"],
                "body" : payload["issue"]["body"],
                "issue_number" : payload["issue"]["number"],
                "issue_type" : "",
                "priority" : "",
                "team" : "",
                "labels" : [],
                "reasoning" : ""
            }
    
    background_tasks.add_task(graph.invoke,state)
    

    return {"status":"accepted"}


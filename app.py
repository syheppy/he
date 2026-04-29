from fastapi import FastAPI
from schemas.request import VideoRequest
from agents.manager import manager_agent
from agents.trend import trend_agent
from agents.writer import script_writer_agent
from agents.title import title_agent
from agents.reviewer import reviewer_agent

app = FastAPI(title="Short Video Agent MVP")

@app.get("/")
def home():
    return {"status": "running", "message": "MVP 已启动"}

@app.post("/generate")
def generate(data: VideoRequest):
    manager_output = manager_agent(data)
    trend_output = trend_agent(data, manager_output)
    script_output = script_writer_agent(data, trend_output)
    title_output = title_agent(data, script_output)
    review_output = reviewer_agent(script_output, title_output)

    return {
        "topic": data.topic,
        "manager": manager_output,
        "trend": trend_output,
        "script": script_output,
        "titles": title_output,
        "review": review_output
    }

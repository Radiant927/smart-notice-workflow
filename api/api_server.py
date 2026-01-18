# api/api_server.py

from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
import uvicorn

from workflow.langchain_workflow import run_workflow_with_input

# ================================
# FastAPI 初始化
# ================================
app = FastAPI(
    title="智能班会通知系统 API（Mock / Workflow 版）",
    description="基于 LangChain 工作流的班会通知生成接口（无真实模型依赖）",
    version="0.1.0"
)

# ================================
# 数据模型
# ================================
class ChatRequest(BaseModel):
    prompt: str

class NoticeRequest(BaseModel):
    theme: str
    audience: str
    length: int = 100

class ChatResponse(BaseModel):
    response: str

# ================================
# API 接口
# ================================
@app.get("/")
def root():
    return {"message": "API 服务运行中（Mock / Workflow 模式）"}

@app.post("/chat", response_model=ChatResponse)
def chat_api(req: ChatRequest):
    """
    通用对话接口（走 LangChain Mock 工作流）
    """
    result = run_workflow_with_input({
        "content": req.prompt
    })
    return {"response": result}

@app.post("/generate_notice_workflow")
def generate_notice_workflow(req: NoticeRequest):
    """
    使用 LangChain 工作流生成班会通知
    """
    prompt = f"""
请你作为一名高校辅导员，生成一则班会通知。

主题：{req.theme}
对象：{req.audience}
字数要求：约 {req.length} 字
语气：正式、清晰、有号召力
"""
    result = run_workflow_with_input({
        "content": prompt
    })
    return {
        "status": "success",
        "notice": result
    }

# ================================
# 本地启动入口
# ================================
if __name__ == "__main__":
    uvicorn.run(
        "api.api_server:app",
        host="0.0.0.0",
        port=8000,
        reload=True
    )

# FastAPI服务
from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
import uvicorn

# ================================
# 模型加载（复用 model/deploy_chatglm.py 中的逻辑）
# ================================
try:
    from model.deploy_chatglm import load_model, chat
    model, tokenizer = load_model()
except Exception as e:
    model, tokenizer = None, None
    print("⚠️ 模型未成功加载，仅用于接口结构测试:", e)

# ================================
# FastAPI 初始化
# ================================
app = FastAPI(
    title="智能班会通知分组推送系统 API",
    description="封装 ChatGLM3-6B 的对话与通知生成接口，供 LangChain / Coze 调用",
    version="0.1.0"
)

# ================================
# 数据模型
# ================================
class ChatRequest(BaseModel):
    prompt: str
    history: List[List[str]] = []

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
    return {"message": "API 服务运行中"}


@app.post("/chat", response_model=ChatResponse)
def chat_api(req: ChatRequest):
    """通用对话接口"""
    if model is None:
        return {"response": "【Mock】模型未加载，收到输入：" + req.prompt}

    response, _ = chat(
        model=model,
        tokenizer=tokenizer,
        query=req.prompt,
        history=req.history
    )
    return {"response": response}


@app.post("/generate_notice", response_model=ChatResponse)
def generate_notice(req: NoticeRequest):
    """班会通知生成接口（面向 Coze / LangChain）"""
    prompt = f"""
请你作为一名高校辅导员，生成一则班会通知。

主题：{req.theme}
对象：{req.audience}
字数要求：约 {req.length} 字
语气：正式、清晰、有号召力
"""

    if model is None:
        return {"response": "【Mock】班会通知示例：请同学们准时参加班会。"}

    response, _ = chat(
        model=model,
        tokenizer=tokenizer,
        query=prompt,
        history=[]
    )
    return {"response": response}


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

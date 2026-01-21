# api/api_server.py
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
from typing import Literal

# ======================
# 1. FastAPI 初始化
# ======================
app = FastAPI(
    title="智能班会通知生成系统",
    description="面向辅导员/班主任的班会通知智能生成服务",
    version="1.0"
)

templates = Jinja2Templates(directory="api/templates")

# ======================
# 2. 请求体定义
# ======================
class NoticeRequest(BaseModel):
    theme: str
    audience: Literal["student", "leader"]
    length: int = 100


# ======================
# 3. 网页入口（普通用户）
# ======================
@app.get("/", response_class=HTMLResponse)
def index(request: Request):
    """
    用户使用入口（网页界面）
    """
    return templates.TemplateResponse(
        "index.html",
        {"request": request}
    )


# ======================
# 4. 核心接口（业务接口）
# ======================
@app.post("/generate_notice_workflow")
def generate_notice_workflow(data: NoticeRequest):
    """
    智能班会通知生成接口
    """
    theme = data.theme
    audience = data.audience
    length = data.length

    # ====== 这里模拟你的 LangChain / 本地模型结果 ======
    # 实际项目中，你只需要把这里替换成：
    # result = workflow.process_notice(...)
    # 或 llm_chain.run(...)

    if audience == "student":
        notice_text = (
            f"📢 班会通知\n\n"
            f"⏰ 时间：明天下午\n"
            f"📍 地点：教学楼 A101\n"
            f"📌 内容：{theme}\n\n"
            f"请同学们合理安排时间，准时参加。"
        )
    else:
        notice_text = (
            f"📢 班委会议通知\n\n"
            f"⏰ 时间：明天下午\n"
            f"📍 地点：教学楼 A101\n"
            f"📌 主题：{theme}\n\n"
            f"请班委提前准备相关材料，并提前到场协调。"
        )

    # ======================
    # 5. 返回“可直接使用”的结果
    # ======================
    return JSONResponse({
        "status": "success",
        "notice": notice_text
    })


# ======================
# 6. 健康检查（可选，加分项）
# ======================
@app.get("/health")
def health_check():
    return {"status": "ok", "service": "notice-generator"}

# workflow/model/chatglm_llm.py

class ChatGLMLLM:
    """
    ChatGLM 的最小可运行封装（Mock 版本）
    用于离线演示 / 初赛机房 / 无模型环境
    """

    def __init__(self, model_name: str = "chatglm-mock"):
        self.model_name = model_name

    def generate(self, prompt: str) -> str:
        """
        模拟模型生成
        """
        return (
            "【班会通知智能分组结果（模拟）】\n"
            f"输入内容：{prompt}\n\n"
            "分组建议：\n"
            "1. 大一新生组：重点强调时间、地点\n"
            "2. 班干部组：补充主持与纪律")

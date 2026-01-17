# 提示词模板
# workflow/prompts.py

from langchain.prompts import PromptTemplate


def get_notice_prompt_by_group(group: str):
    base_info = """
班会时间：{time}
班会地点：{location}
班会主题：{theme}
"""

    if group == "leader":
        template = f"""
你是一名高校辅导员，请生成【班干部专用】班会通知。

{base_info}

要求：
1. 强调组织纪律
2. 提醒提前到场、协助组织
3. 语气正式
"""

    elif group == "absent":
        template = f"""
你是一名高校辅导员，请生成【重点提醒】班会通知。

{base_info}

要求：
1. 强调必须按时参加
2. 说明缺勤后果
3. 语气严肃但不威胁
"""

    else:
        template = f"""
你是一名高校辅导员，请生成【普通学生】班会通知。

{base_info}

要求：
1. 语言简洁
2. 信息清晰
3. 适合群通知
"""

    return PromptTemplate(
        input_variables=["time", "location", "theme"],
        template=template
    )


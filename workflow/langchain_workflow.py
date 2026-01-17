# LangChain工作流
# workflow/langchain_workflow.py
from workflow.chains import create_notice_chain
from workflow.grouping import group_student


def run_workflow_with_student(input_data: dict, student: dict) -> str:
    """
    根据学生分组生成对应通知
    """
    group = group_student(student)
    chain = create_notice_chain(group)
    return chain.run(input_data)

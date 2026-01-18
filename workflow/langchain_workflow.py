# workflow/langchain_workflow.py

from workflow.chains import create_notice_chain

def run_workflow_with_input(input_data: dict) -> str:
    """
    LangChain 工作流统一入口（当前为 mock 演示版本）
    """
    chain = create_notice_chain()
    return chain.run(input_data)


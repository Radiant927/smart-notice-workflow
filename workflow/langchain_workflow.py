# workflow/langchain_workflow.py

from workflow.chains import create_notice_chain

def run_workflow_with_input(input_data: dict) -> str:
    """
    LangChain 工作流统一入口（当前为 mock 演示版本）
    """
    chain = create_notice_chain()
    return chain.run(input_data)

if __name__ == "__main__":
    test_input = {
        "theme": "期末考试动员班会",
        "target": "全体大一学生",
        "time": "本周五晚7点",
        "location": "教学楼302",
        "key_points": "考试纪律、复习安排、注意事项"
    }

    result = run_workflow_with_input(test_input)
    print("【工作流测试输出】")
    print(result)

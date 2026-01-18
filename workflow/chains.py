# workflow/chains.py

from workflow.model.chatglm_llm import ChatGLMLLM

def create_notice_chain():
    llm = ChatGLMLLM()

    class SimpleChain:
        def run(self, input_data: dict) -> str:
            content = input_data.get("content", "")
            return llm.generate(content)

    return SimpleChain()

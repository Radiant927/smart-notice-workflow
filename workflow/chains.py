# Chain定义
# workflow/chains.py

from langchain.chains import LLMChain
from model.chatglm_llm import ChatGLMLLM
from workflow.prompts import get_notice_prompt_by_group


def create_notice_chain(group: str):
    llm = ChatGLMLLM(
        model_path="你的/chatglm3-6b/路径"
    )

    prompt = get_notice_prompt_by_group(group)

    return LLMChain(
        llm=llm,
        prompt=prompt
    )

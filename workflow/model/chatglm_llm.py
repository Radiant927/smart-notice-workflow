from typing import Any, List, Optional
from langchain.llms.base import LLM

from transformers import AutoTokenizer, AutoModel
import torch


class ChatGLMLLM(LLM):
    """
    LangChain 自定义 ChatGLM LLM
    """

    tokenizer: Any = None
    model: Any = None

    def __init__(
        self,
        model_path: str,
        device: str = "cuda" if torch.cuda.is_available() else "cpu"
    ):
        super().__init__()
        self.tokenizer = AutoTokenizer.from_pretrained(
            model_path,
            trust_remote_code=True
        )
        self.model = AutoModel.from_pretrained(
            model_path,
            trust_remote_code=True
        ).to(device)
        self.model.eval()
        self.device = device

    @property
    def _llm_type(self) -> str:
        return "chatglm"

    def _call(
        self,
        prompt: str,
        stop: Optional[List[str]] = None,
        **kwargs: Any
    ) -> str:
        response, _ = self.model.chat(
            self.tokenizer,
            prompt,
            history=[]
        )
        return response

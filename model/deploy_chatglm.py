# ChatGLM部署脚本
# deploy_chatglm.py
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

def load_model():
    model_name = "ChatGLM3-6B"  # 模型名称，可能需要替换为实际的模型路径或模型ID
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForCausalLM.from_pretrained(model_name)
    return model, tokenizer

def test_model(model, tokenizer):
    input_text = "你好，ChatGLM3-6B!"
    inputs = tokenizer(input_text, return_tensors="pt")
    with torch.no_grad():
        outputs = model.generate(**inputs, max_length=50)
    decoded_output = tokenizer.decode(outputs[0], skip_special_tokens=True)
    print(f"模型输出：{decoded_output}")

if __name__ == "__main__":
    model, tokenizer = load_model()
    test_model(model, tokenizer)

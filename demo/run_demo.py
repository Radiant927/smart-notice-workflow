# 演示脚本
import requests
import json

# 模拟用户输入
user_input = "下周一班会通知，主题为学期总结，时间下午3点，请准时参加！"

# 调用 API 生成通知
api_url = "http://localhost:8000/generate_notice"  # 假设 API 服务运行在本地
payload = {"user_input": user_input}
headers = {"Content-Type": "application/json"}

response = requests.post(api_url, data=json.dumps(payload), headers=headers)

if response.status_code == 200:
    generated_notice = response.json().get("generated_notice")
    print(f"生成的班会通知:\n{generated_notice}")
else:
    print("API 请求失败！")

# 调用 LangChain 和 Coze（此部分可以扩展，具体根据你的需求）
# 假设 LangChain 和 Coze 都已经集成到 API 服务中，或者可以用脚本调用

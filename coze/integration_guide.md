# Coze集成指南

# Coze 工作流集成指南

## 1. 项目整体架构说明

本项目使用 Coze 作为工作流编排与可视化工具，结合本地大模型、FastAPI 接口以及 LangChain，实现智能班会通知的生成与分组推送。

整体架构如下：

- Coze：工作流编排与可视化界面
- FastAPI：模型能力封装为 API 服务
- ChatGLM3-6B：本地大语言模型
- LangChain：提示词与逻辑链式管理

---

## 2. Coze 与模型 API 的集成方式

### 2.1 模型 API 服务

模型通过 FastAPI 对外提供接口，例如：

- `/chat`
- `/generate_notice`

示例接口地址：http://localhost:8000/generate_notice

### 2.2 Coze 中的调用方式

在 Coze 工作流中配置「HTTP 请求节点」：

- 请求方式：POST
- 请求地址：FastAPI 接口地址
- 请求体：由用户输入内容构成的 JSON

---

## 3. Coze 与 LangChain 的协作

LangChain 主要用于：

- 提示词模板管理
- 通知生成逻辑封装
- 分组推送规则设计

LangChain 逻辑运行在后端，由 Coze 通过 API 间接调用。

---

## 4. 工作流执行流程说明

1. 用户在 Coze 界面输入班会主题
2. 输入内容进行预处理
3. 调用本地模型生成班会通知
4. 根据学生数据进行分组
5. 将最终结果返回并展示在 Coze 界面

---

## 5. 使用说明

- 启动模型服务：`python api/api_server.py`
- 确保 Coze 能访问本地接口
- 在 Coze 中配置对应工作流节点

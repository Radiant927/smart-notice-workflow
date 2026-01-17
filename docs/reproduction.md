# 复现指南

本项目基于 ChatGLM3-6B + LangChain + Coze 进行开发，以下是从环境安装到代码运行的详细步骤。

## 环境设置

### 1.克隆项目

首先，克隆项目代码到本地：

```bash
git clone https://github.com/your-repo/your-project.git
cd your-project
```

### 2.安装依赖

项目依赖 Python 3.8 以上版本，请确保安装了 Python。然后使用以下命令安装项目依赖：

pip install -r requirements.txt

注意：如果你使用的是虚拟环境，请确保激活环境后再执行此步骤。

### 3.模型配置

将 ChatGLM3-6B 模型文件下载到本地，并配置 chatglm_config.json 文件中的路径，具体配置方法请参考 model/chatglm_config.json 文件。

### 4.配置环境变量

在 .env 文件中设置必要的环境变量，例如 API 密钥、模型路径等：

MODEL_PATH=/path/to/your/model
API_KEY=your-api-key

## 代码运行

### 1.启动 API 服务

运行 api_server.py 启动 FastAPI 服务：

```
python api/api_server.py
```

该服务将提供多个接口，如 /chat 和 /generate_notice，供 LangChain 和 Coze 工作流调用。

### 2.启动示例脚本

你可以使用以下命令来运行 run_demo.py，测试系统的基本功能：

```
python run_demo.py
```

### 3.测试模型推理效果

在 data/sample_notices.json 文件中，提供了一些示例数据，您可以使用它来测试模型推理效果。
运行以下命令测试模型是否生成合理的班会通知：

```
python model/deploy_chatglm.py --input data/sample_notices.json
```

## 常见问题

### 1. 安装依赖时遇到错误

问题：`pip install -r requirements.txt` 时出现依赖安装失败。

解决方案：

1. 确保你正在使用正确版本的 Python（推荐 3.8 以上版本）。

2. 如果使用虚拟环境，确保已经激活虚拟环境。

3. 尝试使用 pip install --upgrade pip 升级 pip 后再次安装。

### 2. 模型加载失败

问题：在运行 `deploy_chatglm.py` 时，出现模型加载失败的错误。

解决方案：

1. 检查 chatglm_config.json 中的模型路径是否正确，确保模型文件存在于指定目录中。

2. 确保你有足够的磁盘空间来存储大模型文件。

3. 尝试重启机器，确保没有其他进程占用过多资源。

### 3. API 请求失败

问题：FastAPI 启动后，访问 /chat 接口时返回 500 错误。

解决方案：

1. 检查 FastAPI 服务是否正常运行，确认没有其他错误信息。

2. 查看 FastAPI 日志输出，确定具体错误原因。

3. 如果问题是由于模型加载失败导致的，尝试重新加载模型并验证路径是否正确。

### 4. 推送通知失败

问题：使用 Coze 进行通知推送时，无法成功发送通知。

解决方案：

1. 确认 Coze 配置文件中的 API 密钥和其他设置是否正确。

2. 检查是否有网络连接问题，导致无法访问 Coze 服务器。

3. 查看 Coze 的日志文件，确定是否有错误信息。

```
---

现在，每个标题、子标题和段落都清晰区分了，确保了 Markdown 格式正确显示。这样应该可以在支持 Markdown 的编辑器（如 GitHub 或 VSCode）中正确显示。

如果还需要进一步修改或有其他问题，请随时告诉我！
```

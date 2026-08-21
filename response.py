import os

from dotenv import load_dotenv
from zai import ZhipuAiClient

# 从 .env 文件加载环境变量
load_dotenv()

# 从环境变量读取 API Key，不再硬编码在代码里
client = ZhipuAiClient(api_key=os.getenv("ZAI_API_KEY"))

response = client.chat.completions.create(
    model="glm-4.7",
    messages=[
        {"role": "user", "content": "作为一名营销专家，请为我的产品创作一个吸引人的口号"},
        {"role": "assistant", "content": "当然，要创作一个吸引人的口号，请告诉我一些关于您产品的信息"},
        {"role": "user", "content": "智谱开放平台"}
    ],
    thinking={
        "type": "enabled",    # 启用深度思考模式
    },
    stream=True,              # 启用流式输出
    max_tokens=65536,          # 最大输出tokens
    temperature=1.0           # 控制输出的随机性
)

# 流式获取回复
for chunk in response:
    if chunk.choices[0].delta.reasoning_content:
        print(chunk.choices[0].delta.reasoning_content, end='', flush=True)

    if chunk.choices[0].delta.content:
        print(chunk.choices[0].delta.content, end='', flush=True)
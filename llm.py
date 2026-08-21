import os
from dotenv import load_dotenv
from zai import ZhipuAiClient

class ZhipuLLM:
    def __init__(self):
        # 从 .env 文件加载环境变量
        load_dotenv()
        # 从环境变量读取 API Key，不再硬编码在代码里
        self.client = ZhipuAiClient(api_key=os.getenv("ZAI_API_KEY"))
    def generate(self, messages,tools=None):
        response = self.client.chat.completions.create(
            model="glm-4.7",
            messages=[
                {"role": "system", "content": "你是邱一航的全能助手，你的回答要尽可能简洁。"},
                *messages
            ],
            tools=tools,
            thinking={
                "type": "enabled",  # 启用深度思考模式
            },
            max_tokens=65536,  # 最大输出 tokens
            temperature=1.0  # 控制输出的随机性
        )

        # 获取完整回复
        return response.choices[0].message
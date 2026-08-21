tools = [
    {
        "type":"function",
        "function":{
            "name":"get_weather",
            "description": "查询指定城市的天气", #   功能描述（LLM 用来判断何时调）
            "parameters": {                    # 第三层：JSON Schema 描述参数
                "type": "object",
                "properties": {
                    "city": {
                        "type": "string",
                        "description": "城市名称，如北京、上海"
                    }
                },
                "required": ["city"]           # 哪些参数必填
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "calculate",
            "description": "计算数学表达式",  # 功能描述（LLM 用来判断何时调）
            "parameters": {  # 第三层：JSON Schema 描述参数
                "type": "object",
                "properties": {
                    "expression": {
                        "type": "string",
                        "description": "表达式"
                    }
                },
                "required": ["expression"]  # 哪些参数必填
            }
        }
    }
]
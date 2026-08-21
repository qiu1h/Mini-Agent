from tools import tools
from llm import ZhipuLLM
from state import AgentState
from tool_executor import executor

class AgentRuntime:

    def __init__(self,state):
        self.llm = ZhipuLLM()
        self.state = state

    def run(self,task):
        messages,step_count,max_steps=self.state.state()
        messages.append({"role": "user", "content": task})
        while True:
            step_count += 1
            # print(f"State{step_count}:", state.state())
            response = self.llm.generate(messages,tools)

            if not response.tool_calls:
                messages.append({"role": "assistant", "content": response.content})
                self.state.update(messages, step_count)
                print("共执行：",step_count,"轮，任务已完成")
                return response
            else:
                tool_calls_list = [
                    {
                        "id":tc.id,
                        "type":"function",
                        "function":{
                            "name": tc.function.name,
                            "arguments": tc.function.arguments
                        }
                    }for tc in response.tool_calls
                ]
                messages.append({"role": "assistant", "content": response.content, "tool_calls":tool_calls_list})
                self.state.update(messages, step_count)
                for tool_call in response.tool_calls:
                    # print(tool_call.function.name, tool_call.function.arguments)
                    tool_output = executor(tool_call.function.name, tool_call.function.arguments)
                    # print(tool_output)
                    messages.append({"role": "tool", "tool_call_id": tool_call.id,"content": tool_output})

            if step_count >= max_steps:
                print("共执行：",step_count,"轮，超过最大step数")
                self.state.reset()
                return response

if __name__ == '__main__':
    state = AgentState()
    while True:
        agent = AgentRuntime(state)
        task = input("User:")
        response = agent.run(task)
        print("Agent:",response.content)
        # print("raw response:",response)
        # print("State:",state.state())


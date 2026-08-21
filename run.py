from pyexpat.errors import messages
from tools import tools
from llm import ZhipuLLM
from state import AgentState
class AgentRuntime:

    def __init__(self,state):
        self.llm = ZhipuLLM()
        self.state = state

    def run(self,task):
        messages,step_count,max_steps=self.state.state()
        while True:
            step_count += 1
            messages.append({"role": "user", "content": task})
            response = self.llm.generate(messages,tools)
            messages.append({"role": "assistant", "content": response.content})
            self.state.update(messages,step_count)

            if not response.tool_calls:
                print("共执行：",step_count,"轮，任务已完成")
                return response
            else:
                for tool_call in response.tool_calls:
                    # print(tool_call)
                    print(tool_call.function.name, tool_call.function.arguments)
            if step_count >= max_steps:
                print("共执行：",step_count,"轮，超过最大step数")
                return response

if __name__ == '__main__':
    state = AgentState()
    while True:
        agent = AgentRuntime(state)
        task = input("User:")
        response = agent.run(task)
        print("Agent:",response.content)
        # print("State",state.state())


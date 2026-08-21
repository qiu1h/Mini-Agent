class AgentState:
    def __init__(self):
        self.messages = []
        self.step_count = 0
        self.max_steps = 3

    def state(self):
        return self.messages, self.step_count, self.max_steps

    def update(self, messages, step_count):
        self.messages = messages
        self.step_count = step_count
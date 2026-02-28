class StepGuard:

    def __init__(self, max_steps: int = 25):
        self.max_steps = max_steps
        self.counter = 0

    def increment(self):
        self.counter += 1
        if self.counter > self.max_steps:
            raise Exception("Max step limit exceeded (possible infinite loop)")
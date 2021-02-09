from consts import TaskType

class Task:
    def __init__(self, task_name:str, task_type:TaskType, start:int, duration:int):
        self.name = task_name
        self.type = task_type
        self.start = start
        self.duration = duration

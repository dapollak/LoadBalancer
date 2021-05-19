from consts import TaskType

class Task:
    def __init__(self, task_name:str, task_type:TaskType, start:int, duration:int):
        self.name = task_name
        self._type = task_type
        self.start = start
        self.duration = duration

    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, task_type):
        self._type = task_type

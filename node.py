from consts import TaskType
from task import Task

class Node:
    def __init__(self, name:str, accepted_types:list):
        self.name = name
        self.accepted_types = accepted_types
        self.tasks_queue

    def does_task_supported(task:Task):
        return task.type in self.accepted_types

    def is_vacent():
        return True
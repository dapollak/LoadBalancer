from consts import TaskType
from queue import Queue
from task import Task

class Node:
    def __init__(self, name:str, accepted_types:list):
        self.name = name
        self.accepted_types = accepted_types
        self.tasks_queue = Queue()
        self.active = False

    def does_task_supported(self, task:Task):
        return task.type in self.accepted_types

    def is_vacent(self):
        return self.tasks_queue.empty()

    def queue_task(self, task):
        self.tasks_queue.put(task)

        # TODO: start worker thread
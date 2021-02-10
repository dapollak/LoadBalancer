from input_parsers import parse_tasks_config
from task import Task
from consts import TaskType

class Feeder:
    def __init__(self):
        self.task_iter = []

    def tasks(self):
        for task in self.task_iter:
            yield task

class ListFeeder(Feeder): # without timing
    def __init__(self, tasks_list):
        super().__init__()
        self.task_iter = tasks_list

class FileFeeder(Feeder): # without timing
    def __init__(self, tasks_config_filepath):
        super().__init__()
        self.task_iter = parse_tasks_config(tasks_config_filepath)
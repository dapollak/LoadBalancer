from input_parsers import parse_tasks_config
from task import Task
from consts import TaskType

class Feeder:
    def next_task(self):
        raise NotImplementedError

class ListFeeder(Feeder): # without timing
    def __init__(self, tasks_list):
        self.tasks_list = tasks_list
        super().__init__()

    def next_task(self):
        for task in tasks_list:
            yield task

class FileFeeder(Feeder): # without timing
    def __init__(self, tasks_config_filepath):
        super().__init__()
        self.tasks_iter = parse_tasks_config(tasks_config_filepath)

    def next_task(self):
        yield self.tasks_iter.next()
from input_parsers import parse_tasks_config

class Feeder:
    def __init__(self, tasks_config_filepath):
        self.tasks_iter = parse_tasks_config(tasks_config_filepath)

    def next_task():
        self.tasks_iter.next()
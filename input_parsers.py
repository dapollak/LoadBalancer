import json

from node import Node
from task import Task
from consts import TaskType

def task_type_str_to_enum(task_type):
    if task_type == 'queueing_task':
        return TaskType.QUEUE_TASK
    if task_type == 'web_task':
        return TaskType.WEB_TASK
    if task_type == 'database_task':
        return TaskType.DATABASE_TASK

    raise NotImplementedError()

def parse_nodes_config(filepath):
    with open(filepath, 'rb') as f:
        json_config = f.read()

    json_config = json.loads(json_config)
    for node in json_config['nodes']:
        if isinstance(node['accepted_task_type'], list):
            accepted_tasks = map(task_type_str_to_enum, node['accepted_task_type'])
        else:
            accepted_tasks = [task_type_str_to_enum(node['accepted_task_type'])]
        
        yield Node(node['node_name'], accepted_tasks)

def parse_tasks_config(filepath):
    with open(filepath, 'rb') as f:
        
        while True:
            
            current_task = f.read(1)
            if current_task == b'':
                break
            
            # read one task
            while current_task[-1] != ord('}'):
                current_task += f.read(1)
            
            json_task = json.loads(current_task)
            yield Task(json_task['task_name'], task_type_str_to_enum(json_task['task_type']), 
            json_task['timestamp_start'], json_task['duration'])
            
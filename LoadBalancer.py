import Feeder
from consts import TaskType
from types import SimpleNamespace

class LoadBalancer:
    def __init__(self, nodes_list):
        self.nodes_list = nodes_list

    def match_task_to_node(self, task):
        raise NotImplementedError()

    def dispatch_task(self, task):
        node = self.match_task_to_node(task)
        node.queue_task(task)

class RRLoadBalancer(LoadBalancer):
    def __init__(self, nodes_list):
        super().__init__(nodes_list)
        
        self.nodes_by_type = {}
        for tasktype in TaskType:
            self.nodes_by_type[tasktype] = SimpleNamespace(current_index=0,
            nodes_list=list(filter(lambda node: tasktype in node.accepted_types, self.nodes_list)))

    def match_task_to_node(self, task):
        if self.nodes_by_type[task.type].nodes_list == []:
            raise Exception() # no supported node

        node_to_return = self.nodes_by_type[task.type].nodes_list[self.nodes_by_type[task.type].current_index]
        self.nodes_by_type[task.type].current_index += 1
        self.nodes_by_type[task.type].current_index %= len(self.nodes_by_type[task.type].nodes_list)
        return node_to_return
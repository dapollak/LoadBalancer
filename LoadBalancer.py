import Feeder
from consts import TaskType
from types import SimpleNamespace

class LoadBalancer:
    def __init__(self, tasks_feeder:Feeder, nodes_list):
        self.tasks_feeder = tasks_feeder
        self.nodes_list = nodes_list

    def assign_task_to_node(self, task):
        raise NotImplementedError()

class RRLoadBalancer(LoadBalancer):
    def __init__(self, tasks_feeder:Feeder, nodes_list):
        super().__init__(tasks_feeder, nodes_list)
        
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
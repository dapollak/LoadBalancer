import unittest
import os

import input_parsers
from node import Node
from task import Task
from consts import TaskType
from LoadBalancer import RRLoadBalancer
from Feeder import ListFeeder

class TestRRLoadBalancer(unittest.TestCase):

    def test_check_assign_simple(self):
        tasks_list = [Task("t1", TaskType.QUEUE_TASK, 0, 5),
        Task("t2", TaskType.DATABASE_TASK, 0, 10),
        Task("t3", TaskType.WEB_TASK, 4, 3)]
        nodes_list = [Node("n1", [TaskType.QUEUE_TASK]),
        Node("n2", [TaskType.WEB_TASK]),
        Node("n3", [TaskType.DATABASE_TASK])]

        RR_loadbalancer = RRLoadBalancer(nodes_list)
        
        self.assertEqual(RR_loadbalancer.match_task_to_node(tasks_list[0]), nodes_list[0])
        self.assertEqual(RR_loadbalancer.match_task_to_node(tasks_list[1]), nodes_list[2])
        self.assertEqual(RR_loadbalancer.match_task_to_node(tasks_list[2]), nodes_list[1])

    def test_init(self):
        nodes_list = [Node("n1", [TaskType.QUEUE_TASK]),
        Node("n2", [TaskType.QUEUE_TASK]),
        Node("n3", [TaskType.WEB_TASK]),
        Node("n4", [TaskType.DATABASE_TASK])]

        RR_loadbalancer = RRLoadBalancer(nodes_list)

        self.assertEqual(RR_loadbalancer.nodes_by_type[TaskType.QUEUE_TASK].nodes_list, [nodes_list[0], nodes_list[1]])
        self.assertEqual(RR_loadbalancer.nodes_by_type[TaskType.WEB_TASK].nodes_list, [nodes_list[2]])
        self.assertEqual(RR_loadbalancer.nodes_by_type[TaskType.DATABASE_TASK].nodes_list, [nodes_list[3]])
        
    def test_check_assign_microsoft_ex(self):
        tasks_list = [Task("t1", TaskType.QUEUE_TASK, 0, 5),
        Task("t2", TaskType.WEB_TASK, 0, 10),
        Task("t3", TaskType.QUEUE_TASK, 4, 3),
        Task("t4", TaskType.QUEUE_TASK, 4, 3),]
    
        nodes_list = [Node("n1", [TaskType.QUEUE_TASK]),
        Node("n2", [TaskType.QUEUE_TASK]),
        Node("n3", [TaskType.WEB_TASK]),
        Node("n4", [TaskType.DATABASE_TASK])]

        RR_loadbalancer = RRLoadBalancer(nodes_list)

        self.assertEqual(RR_loadbalancer.match_task_to_node(tasks_list[0]), nodes_list[0])
        self.assertEqual(RR_loadbalancer.match_task_to_node(tasks_list[1]), nodes_list[2])
        self.assertEqual(RR_loadbalancer.match_task_to_node(tasks_list[2]), nodes_list[1])
        self.assertEqual(RR_loadbalancer.match_task_to_node(tasks_list[0]), nodes_list[0])

    def test_not_supported_node(self):
        nodes_list = [Node("n1", [TaskType.QUEUE_TASK])]
        RR_loadbalancer = RRLoadBalancer(nodes_list)
        self.assertRaises(Exception, RR_loadbalancer.match_task_to_node, Task("t1", TaskType.WEB_TASK, 0, 1))
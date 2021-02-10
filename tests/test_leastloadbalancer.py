import unittest
import os

import input_parsers
from node import Node
from task import Task
from consts import TaskType
from LoadBalancer import LeastTaskLoadBalancer
from Feeder import ListFeeder

class TestRRLoadBalancer(unittest.TestCase):

    def test_match_sanity(self):
        tasks_list = [Task("t1", TaskType.QUEUE_TASK, 0, 5),
        Task("t2", TaskType.QUEUE_TASK, 0, 5),
        Task("t3", TaskType.QUEUE_TASK, 0, 5)]
        nodes_list = [Node("n1", [TaskType.QUEUE_TASK]),
        Node("n2", [TaskType.QUEUE_TASK]),]

        loadbalancer = LeastTaskLoadBalancer(nodes_list)
        
        loadbalancer.dispatch_task(tasks_list[0])
        self.assertEqual(nodes_list[0].tasks_queue.qsize(), 1)
        self.assertEqual(nodes_list[1].tasks_queue.qsize(), 0)

        loadbalancer.dispatch_task(tasks_list[1])
        self.assertEqual(nodes_list[0].tasks_queue.qsize(), 1)
        self.assertEqual(nodes_list[1].tasks_queue.qsize(), 1)

        nodes_list[0].tasks_queue.get()
        self.assertEqual(nodes_list[0].tasks_queue.qsize(), 0)
        
        loadbalancer.dispatch_task(tasks_list[1])
        self.assertEqual(nodes_list[0].tasks_queue.qsize(), 1)
        self.assertEqual(nodes_list[1].tasks_queue.qsize(), 1)
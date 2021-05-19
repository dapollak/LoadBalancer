import unittest

from node import Node
from task import Task
from consts import TaskType

class TestNode(unittest.TestCase):
    tasks_list1 = [Task("t1", TaskType.QUEUE_TASK, 0, 5),
        Task("t2", TaskType.DATABASE_TASK, 0, 10),
        Task("t3", TaskType.WEB_TASK, 4, 3),]
    nodes_list1 = [Node("n1", [TaskType.QUEUE_TASK]),
    Node("n2", [TaskType.WEB_TASK]),
    Node("n3", [TaskType.DATABASE_TASK])]

    def test_task_support(self):
        self.assertTrue(self.nodes_list1[0].does_task_supported(self.tasks_list1[0]))
        self.assertTrue(self.nodes_list1[1].does_task_supported(self.tasks_list1[2]))
        self.assertFalse(self.nodes_list1[0].does_task_supported(self.tasks_list1[1]))
        self.assertFalse(self.nodes_list1[2].does_task_supported(self.tasks_list1[2]))

    def test_is_vacent(self):
        node = Node("n1", [TaskType.QUEUE_TASK])
        self.assertTrue(node.is_vacent())
        node.queue_task(Task("t1", TaskType.QUEUE_TASK, 0, 5))
        self.assertFalse(node.is_vacent())
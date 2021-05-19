import unittest
import os

import input_parsers
from node import Node
from task import Task
from consts import TaskType

class TestParseInputs(unittest.TestCase):
    nodes1_file = r'tests/files/nodes1.config'
    tasks1_file = r'tests/files/tasks1.config'
    tasks_huge_file = r'tests/files/tasks_huge.config'

    def test_parse_nodes1(self):
        nodes_iter = input_parsers.parse_nodes_config(self.nodes1_file)
        counter = 0
        for i, node in enumerate(nodes_iter):
            self.assertIsInstance(node, Node)
            self.assertIsInstance(node.accepted_types, list)
            self.assertIsInstance(node.accepted_types[0], TaskType)
            self.assertEqual(node.name, "node_{}".format(i+1))
            counter += 1

        self.assertEqual(counter, 4)

    def test_parse_tasks1(self):
        print(os.path.abspath(os.path.curdir))
        tasks_iter = input_parsers.parse_tasks_config(self.tasks1_file)
        counter = 0
        for i, task in enumerate(tasks_iter):
            self.assertIsInstance(task, Task)
            self.assertEqual(task.name, "task_{}".format(i+1))
            self.assertIsInstance(task.type, TaskType)
            counter += 1

        self.assertEqual(counter, 4)

    def test_parse_huge(self):
        tasks_iter = input_parsers.parse_tasks_config(self.tasks_huge_file)
        counter = 0
        for i, task in enumerate(tasks_iter):
            counter += 1

        self.assertEqual(counter, 16348)
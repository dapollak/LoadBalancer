import unittest

from node import Node
from task import Task
from consts import TaskType
from node import Node
from task import Task
from node_worker import NodeGenericWorker

from threading import Thread
from time import sleep

class TestNodeWorker(unittest.TestCase):

    def test_sanity(self):
        node = Node("n1", [TaskType.QUEUE_TASK])
        task1 = Task("t1", TaskType.QUEUE_TASK, 0, 0.2)
        task2 = Task("t2", TaskType.QUEUE_TASK, 0, 0.1)
        worker = NodeGenericWorker(node)
        worker.start()

        node.queue_task(task1)
        node.queue_task(task2)
        self.assertFalse(node.is_vacent())
        
        sleep(0.5)
        self.assertTrue(node.is_vacent())
        
        worker.stop()
        worker.join()



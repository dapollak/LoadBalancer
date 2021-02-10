import unittest

from Feeder import ListFeeder
from task import Task
from consts import TaskType

class TestFeeder(unittest.TestCase):

    def test_feeder_sanity(self):
        tasks_list = [Task("t1", TaskType.QUEUE_TASK, 0, 5),
        Task("t2", TaskType.DATABASE_TASK, 0, 10),
        Task("t3", TaskType.WEB_TASK, 4, 3)]

        feeder = ListFeeder(tasks_list)
        tasks = feeder.tasks()

        counter = 0
        for task in tasks:
            counter += 1

        self.assertEqual(counter, len(tasks_list))
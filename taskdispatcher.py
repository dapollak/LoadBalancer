from time import sleep
from Feeder import Feeder
from LoadBalancer import LoadBalancer

class TaskDispathcer:
    def __init__(self, feeder:Feeder, loadbalancer:LoadBalancer):
        self.feeder = feeder
        self.loadbalancer = loadbalancer

    def dispatch_tasks(self):
        tasks = self.feeder.tasks()
        last_start = 0
        for task in tasks:
            sleep(task.start-last_start)
            self.loadbalancer.dispatch_task(task)
            last_start = task.start
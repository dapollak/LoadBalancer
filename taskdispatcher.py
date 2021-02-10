from time import sleep
from Feeder import Feeder
from LoadBalancer import LoadBalancer

class TaskDispathcer:
    def __init__(self, feeder:Feeder, loadbalancer:LoadBalancer):
        self.feeder = feeder
        self.loadbalancer = loadbalancer

    def dispatch_tasks(self):
        tasks = self.feeder.tasks()
        for task in tasks:
            sleep(task.start)
            self.loadbalancer.dispatch_task(task)
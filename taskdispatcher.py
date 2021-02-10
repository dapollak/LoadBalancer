from time import sleep

class TaskDispathcer:
    def __init__(self, feeder:Feeder, loadbalancer:LoadBalander):
        self.feeder = feeder
        self.loadbalancer = loadbalancer

    def dispatch_tasks(self):
        for task in feeder.next_task():
            sleep(task.start)
            loadbalancer.dispatch_task(task)
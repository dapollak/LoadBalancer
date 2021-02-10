from threading import Thread, Event
from queue import Empty
from time import sleep

class NodeGenericWorker(Thread):
    def __init__(self, node):
        super().__init__()
        self.node = node
        self.stop_event = Event()
    
    def stop(self):
        self.stop_event.set()

    def run(self):
        while not self.stop_event.is_set():
            try:
                task_to_process = self.node.tasks_queue.get_nowait()
                print("Started task=’{}’ of type='{}’ on node=’{}’ at ‘{}’".format(task_to_process.name, task_to_process.type, self.node.name, task_to_process.start))
                sleep(task_to_process.duration)
                print("Finished task='{}’ of type='{}’ on node=’{}’ at ‘{}’".format(task_to_process.name, task_to_process.type, self.node.name, task_to_process.start+task_to_process.duration))
                self.node.tasks_queue.task_done()
            except Empty:
                continue
from threading import Thread, Event
from queue import Empty
from time import sleep
from contextlib import contextmanager

class NodeGenericWorker(Thread):
    def __init__(self, node):
        super().__init__()
        self.node = node
        self.stop_event = Event()
        self.last_task_start = 0
        self.last_task_duration = 0
    
    def stop(self):
        self.stop_event.set()

    @contextmanager
    def get_task(self):
        task_to_process = None
        try:
            task_to_process = self.node.tasks_queue.get_nowait()
            if task_to_process.start < (self.last_task_start + self.last_task_duration):
                start_time = self.last_task_start + self.last_task_duration
            else:
                start_time = task_to_process.start
            yield task_to_process, start_time
        except Empty:
            yield None, None
        finally:
            if task_to_process is not None:
                self.last_task_start = task_to_process.start
                self.last_task_duration = task_to_process.duration
                self.node.tasks_queue.task_done()

    def run(self):
        while not self.stop_event.is_set():
            with self.get_task() as (task_to_process, start_time):
                if task_to_process is None:
                    continue

                print("Started task=’{}’ of type='{}’ on node=’{}’ at ‘{}’".format(task_to_process.name, task_to_process.type, self.node.name, start_time))
                sleep(task_to_process.duration)
                print("Finished task='{}’ of type='{}’ on node=’{}’ at ‘{}’".format(task_to_process.name, task_to_process.type, self.node.name, start_time+task_to_process.duration))
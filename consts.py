from enum import Enum

class TaskType(Enum):
    QUEUE_TASK = 1
    WEB_TASK = 2
    DATABASE_TASK = 3
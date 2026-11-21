from enum import Enum

# enum for task status
class Status(Enum):
    TO_DO = 1
    IN_PROGRESS = 2
    DONE = 3

class Task :

    """
    task structure

    string:id - unique identifier for task
    string:description - brief summary of task (string)
    enum:status - current state of task
    time:createdAt - when the task was created
    time:updatedAt - when the task was last updated

    """
    def __init__(self, id, description, status, createdAt,  updatedAt):
        self.id = id
        self.description = description
        self.status = status
        self.createdAt = createdAt
        self.updatedAt = updatedAt

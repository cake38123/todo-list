from enum import Enum
import datetime

# enum for task status
class Status(Enum):
    TO_DO = 1
    IN_PROGRESS = 2
    DONE = 3
    # turns TO_DO into To do
    def get_label(self) -> str:
        return self.name.capitalize().replace("_", " ")


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

    def __str__(self):
        return f"ID:{self.id}, Description: {self.description}, Status: {self.status.get_label()}"


    # print debugging ouput
    def __repr__(self):
        return f"Task(id='{self.id}', description='{self.description}', status='{self.status}', createdAt='{self.createdAt}', updatedAt='{self.updatedAt}')"

    # convert task object into str
    def to_dict(self):
        return {"id": self.id, "description": self.description, "status": self.status.get_label(), "createdAt": self.createdAt.strftime("%Y-%m-%d %H:%M:%S"), "updatedAt": self.updatedAt.strftime("%Y-%m-%d %H:%M:%S") if self.updatedAt else "Not yet updated"}

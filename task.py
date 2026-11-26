from enum import Enum
from datetime import datetime

# enum for task status
class Status(Enum):
    TO_DO = 1
    IN_PROGRESS = 2
    DONE = 3
    # turns TO_DO into To do
    def get_label(self) -> str:
        return self.name.capitalize().replace("_", "-")

    @classmethod
    def from_label(cls, label: str):
        name = label.strip().upper().replace("-", "_")
        return cls[name]
        


class Task :

    """
    task structure

    string:id - unique identifier for task
    string:description - brief summary of task (string)
    enum:status - current state of task
    time:createdAt - when the task was created
    time:updatedAt - when the task was last updated

    """
    def __init__(self, id, description, status, createdAt, updatedAt):
        self.id = id
        self.description = description
        self.status = Status.TO_DO if status is None else status
        self.createdAt = datetime.now() if createdAt is None else createdAt
        self.updatedAt = None if createdAt is None else updatedAt

    def __str__(self):
        return f"ID:{self.id}, Description: {self.description}, Status: {self.status.get_label()}"


    # print debugging ouput
    def __repr__(self):
        return f"Task(id='{self.id}', description='{self.description}', status='{self.status}', createdAt='{self.createdAt}', updatedAt='{self.updatedAt}')"

    # convert task object into str
    def to_dict(self):
        return {"id": self.id, "description": self.description, "status": self.status.get_label(), "createdAt": self.createdAt.strftime("%Y-%m-%d %H:%M:%S"), "updatedAt": self.updatedAt.strftime("%Y-%m-%d %H:%M:%S") if self.updatedAt else "Not yet updated"}

    # convert dict back to task object
    @classmethod
    def from_dict(cls, data):

        date_format = "%Y-%m-%d %H:%M:%S"
        
        return cls(id=data["id"], 
                   description=data["description"], 
                   status=Status.from_label(data["status"]), 
                   createdAt=datetime.strptime(data["createdAt"], 
                   date_format), 
                   updatedAt=None if data["updatedAt"] == "Not yet updated" else datetime.strptime(data["updatedAt"], date_format)
                   )

from task import Task
import json

class TaskList:

    def __init__(self, filepath):
        self.filepath = filepath

        try:
            with open(self.filepath, "r", encoding="utf-8") as file:
                saved_tasks = json.load(file)
        except FileNotFoundError:
            saved_tasks = []

        self.data = [Task.from_dict(task_data) for task_data in saved_tasks]
        

            



from task import Task
import json

class TaskList:

    def __init__(self, filepath):
        global data
        try:
            with open("data.json", "r", encoding="utf-8") as file:
                self.data = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            self.data = []




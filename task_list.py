from task import Task
import json

class TaskList:


    def __init__():
        try:
            with open("data.json", "r", encoding="utf-8") as file:
                data = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            data = []

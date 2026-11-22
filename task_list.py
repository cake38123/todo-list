from task import Task
import json

class TaskList:

    data = []

    def __init__():
        global data
        try:
            with open("data.json", "r", encoding="utf-8") as file:
                data = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            data = []

    def add_task(task):
        global data
        data.append(task)
        # write to json file
        with open("data.json", "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4)


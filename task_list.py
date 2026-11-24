from task import Task
import json

class TaskList:

    def __init__(self, filepath):
        self.filepath = filepath

        try:
            with open(self.filepath, "r", encoding="utf-8") as file:
                # json format of saved tasks
                saved_tasks = json.load(file)
        except FileNotFoundError:
            saved_tasks = []

        # list of task objects from each json dict
        self.data = [Task.from_dict(task_data) for task_data in saved_tasks]

    # save method
    def save(self):

        saved_tasks = [task.to_dict() for task in self.data]

        with open(self.filepath, "w", encoding="utf-8") as file:
            json.dump(saved_tasks, file, indent=2)



    
        
        

            



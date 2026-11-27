from task import Task
from task import Status
import datetime
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

    def __str__(self):
        return "\n".join(str(task) for task in self.data)

    def add_task(self, description):

        # new task parameters
        id = len(self.data) + 1
        status = Status.TO_DO

        # create new task
        task = Task(id=id, description=description, status=status, createdAt=None, updatedAt=None)

        # append to task data
        self.data.append(task)

        # save current task data
        self.save()

        print(f"Task added successfully (ID:{task.id}).")

    def update_task(self, id, description : str):
        for task in self.data:
            if id == task.id:
                task.description = description
                self.save()
                print(f"Task successfully updated.")
                return

        print("Task not found.")

    def mark_task(self, status_str, id):

        try:
            status = Status.from_label(status_str)
        except ValueError:
            print("Must be a valid status (to-do, in-progress or done).")
            return

        for task in self.data:
            if task.id == id:
                task.status = status
                self.save()
                print(f"Task {id} marked as {status}.")
                return

        print("Task ID not found.")    
            
    # save method
    def save(self):

        saved_tasks = [task.to_dict() for task in self.data]

        with open(self.filepath, "w", encoding="utf-8") as file:
            json.dump(saved_tasks, file, indent=2)

    # size of the list - testing
    def size(self):
        return len(self.data)



    
        
        

            



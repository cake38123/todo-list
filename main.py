import typer
import time
from task import Task
from task import Status
import json
app = typer.Typer()

print("Welcome to To-Do List")

filename = "data.json"
"""
data represents the list of tasks stored in json file named 'data.json'
data is a list containing dictionaries of each task object
"""
try:
    with open(filename, "r", encoding="utf-8") as file:
        data = json.load(file)
except (FileNotFoundError, json.JSONDecodeError):
    data = []


@app.command()
def usage():
    usage_text = """
    add <task_description>
    update <task_id> <new_description>
    delete <task_id>
    list
    list <task_status>"""
    typer.echo(usage_text)

@app.command()
def add(description: str):
    # create new task
    new_id = len(data) + 1
    t = Task(new_id, description, Status.IN_PROGRESS, time.time(), time.time())
    # add new task to list 
    data.append(t.to_dict())
    # write to json file
    with open("data.json", "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)

    typer.echo(f"Task added successfully (ID: {t.id})")
    print(repr(t))


if __name__ == "__main__":
    app()

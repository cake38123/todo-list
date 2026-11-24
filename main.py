import typer
from datetime import datetime
from task import Task
from task import Status
from task_list import TaskList
import json
app = typer.Typer()

print("Welcome to To-Do List")

tasks = TaskList("data.json")

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
    created_at = datetime.now()
    t = Task(new_id, description, Status.IN_PROGRESS, created_at, None)
    # add new task to list 
    tasks.add_task(t)
    typer.echo(f"Task added successfully (ID: {t.id})")

    # debugging output
    # print(repr(t))

@app.command()
def list():

    

    typer.echo(list_text)




if __name__ == "__main__":
    app()

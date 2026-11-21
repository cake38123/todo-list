import typer
import time
from task import Task
from task import Status
import json
app = typer.Typer()

print("Welcome to To-Do List")

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
    t = Task(1, description, Status.IN_PROGRESS, time.time(), time.time())
    typer.echo(f"Task added successfully (ID: {t.id})")
    print(repr(t))


if __name__ == "__main__":
    app()

import typer
import time
from task import Task
from task import Status
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
    typer.echo(f"Added task: {description}")
    new_task = Task(1, description, Status.IN_PROGRESS, time.time(), time.time())
    print(repr(new_task))


if __name__ == "__main__":
    app()

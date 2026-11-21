import typer
from task import Task
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

if __name__ == "__main__":
    app()

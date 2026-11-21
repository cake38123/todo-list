import typer

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

if __name__ == "__main__":
    app()

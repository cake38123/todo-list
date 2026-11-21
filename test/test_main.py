from typer.testing import CliRunner
from main import app

runner = CliRunner()

def test_add():

    result = runner.invoke(app, ["add", "code"])

    assert result.exit_code == 0

    assert "Task added successfully (ID: 1)" in result.stdout

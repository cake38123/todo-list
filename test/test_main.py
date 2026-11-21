from typer.testing import CliRunner
from main import app
import json

runner = CliRunner()


def test_add():

    result = runner.invoke(app, ["add", "code"])

    assert result.exit_code == 0

    assert "Task added successfully" in result.stdout


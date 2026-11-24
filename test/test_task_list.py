from task_list import TaskList
from task import Task
from pathlib import Path
import datetime
from task import Status

def test_constructor_starts_empty_when_file_is_missing(tmp_path):
    task_list = TaskList(tmp_path / "data.json")

    assert task_list.size() == 0


def test_add_task_saves_task(tmp_path):
    path = tmp_path / "data.json"
    task_list = TaskList(path)

    task_list.add_task("Buy groceries")

    assert task_list.size() == 1

    reloaded = TaskList(path)
    assert reloaded.size() == 1
    assert reloaded.data.description == "Buy groceries"



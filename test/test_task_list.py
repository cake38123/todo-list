from task_list import TaskList
from task import Task
from pathlib import Path
import datetime
from task import Status
import sys

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
    assert reloaded.data[0].description == "Buy groceries"

def test_update_task_saves_updated_task(tmp_path):
    path = tmp_path / "data.json"
    task_list = TaskList(path)

    task_list.add_task("Buy groceries")

    assert task_list.size() == 1

    task_list.update_task(1, "make dinner" )

    assert task_list.data[0].description == "make dinner"

    reloaded = TaskList(path)

    assert reloaded.size() == 1
    assert reloaded.data[0].description == "make dinner"

def test_update_does_nothing_with_unknown_id(tmp_path, capsys):
    path = tmp_path / "data.json"
    task_list = TaskList(path)
    task_list.add_task("Buy groceries")
    unknown_id = task_list.data[0].id + 1
    capsys.readouterr()


    task_list.update_task(unknown_id, "do something")

    output = capsys.readouterr().out
    assert "Task not found" in output
    assert task_list.size() == 1
    assert task_list.data[0].description == "Buy groceries"












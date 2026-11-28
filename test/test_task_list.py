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

def test_mark_task_changes_status_correctly(tmp_path):
    path = tmp_path / "data.json"
    task_list = TaskList(path)
    task_list.add_task("Buy groceries")
    assert task_list.size() == 1 

    task_list.mark_task("done", 1)

    assert task_list.size() == 1
    assert task_list.data[0].status == Status.DONE
    assert task_list.data[0].description == "Buy groceries"

def test_mark_task_returns_error_on_invalid_status(tmp_path, capsys):
    path = tmp_path / "data.json"
    task_list = TaskList(path)
    task_list.add_task("Buy groceries")
    assert task_list.size() == 1 
    unknown_status = "finished"
    capsys.readouterr()

    task_list.mark_task(unknown_status, 1)

    output = capsys.readouterr().out
    assert "Must be a valid status" in output
    assert task_list.data[0].status == Status.TO_DO

def test_delete_task_correctly_deletes(tmp_path, capsys):
    path = tmp_path / "data.json"
    task_list = TaskList(path)
    task_list.add_task("Buy groceries")
    capsys.readouterr()

    assert task_list.size() == 1 

    task_list.delete_task(1)
    output = capsys.readouterr().out

    assert "Task 1 has been deleted." in output
    assert task_list.size() == 0

def test_delete_task_does_nothing_with_unknown_id(tmp_path, capsys):
    path = tmp_path / "data.json"
    task_list = TaskList(path)
    task_list.add_task("Buy groceries")

    assert task_list.size() == 1

    unknown_id = task_list.data[0].id + 1
    capsys.readouterr()

    task_list.delete_task(unknown_id)

    output = capsys.readouterr().out
    assert f"Task ID {unknown_id} not found." in output
    assert task_list.size() == 1
    assert task_list.data[0].description == "Buy groceries"

def test_list_task_lists_all_tasks_when_none(tmp_path, capsys):
    path = tmp_path / "data.json"
    task_list = TaskList(path)

    # set each task to different status
    task_list.add_task("Buy groceries")
    task_list.mark_task("done", 1)

    task_list.add_task("Make dinner")
    
    task_list.add_task("Wash dishes")
    task_list.mark_task("in-progress", 3)
    
    assert task_list.size() == 3
    capsys.readouterr()

    task_list.list_tasks(None)

    output = capsys.readouterr().out
    assert "ID:1, Description: Buy groceries, Status: Done\n" in output
    assert "ID:2, Description: Make dinner, Status: To-do\n" in output
    assert "ID:3, Description: Wash dishes, Status: In-progress\n" in output

def test_list_task_lists_displays_only_to_do_when_to_do(tmp_path, capsys):
    path = tmp_path / "data.json"
    task_list = TaskList(path)

    # mark task 1 as done
    task_list.add_task("Buy groceries")
    task_list.mark_task("Done", 1)

    # without mark, should be to-do
    task_list.add_task("Make dinner")

    # mark task 3 as in-progress
    task_list.add_task("Wash dishes")
    task_list.mark_task("in-progress", 3)
    
    assert task_list.size() == 3
    capsys.readouterr()

    task_list.list_tasks("to-do")

    output = capsys.readouterr().out
    assert "ID:1, Description: Buy groceries, Status: Done\n" not in output
    assert "ID:2, Description: Make dinner, Status: To-do\n" in output
    assert "ID:3, Description: Wash dishes, Status: In-progress\n" not in output

def test_list_task_lists_displays_only_done_when_done(tmp_path, capsys):
    path = tmp_path / "data.json"
    task_list = TaskList(path)

    task_list.add_task("Buy groceries")
    # mark task 1 as done
    task_list.mark_task("done", 1)

    # without mark, should be to-do
    task_list.add_task("Make dinner")

    # mark task 3 as in-progress
    task_list.add_task("Wash dishes")
    task_list.mark_task("in-progress", 3)
    
    assert task_list.size() == 3
    capsys.readouterr()

    task_list.list_tasks("done")

    output = capsys.readouterr().out
    assert "ID:1, Description: Buy groceries, Status: Done\n" in output
    assert "ID:2, Description: Make dinner, Status: To-do\n" not in output
    assert "ID:3, Description: Wash dishes, Status: In-progress\n" not in output

def test_list_task_lists_displays_only_in_progress_when_in_progress(tmp_path, capsys):
    path = tmp_path / "data.json"
    task_list = TaskList(path)

    task_list.add_task("Buy groceries")
    # mark task 1 as done
    task_list.mark_task("done", 1)

    # without mark, should be to-do
    task_list.add_task("Make dinner")

    # mark task 3 as in-progress
    task_list.add_task("Wash dishes")
    task_list.mark_task("in-progress", 3)
    
    assert task_list.size() == 3
    capsys.readouterr()

    task_list.list_tasks("in-progress")

    output = capsys.readouterr().out
    assert "ID:1, Description: Buy groceries, Status: Done\n" not in output
    assert "ID:2, Description: Make dinner, Status: To-do\n" not in output
    assert "ID:3, Description: Wash dishes, Status: In-progress\n" in output




    

















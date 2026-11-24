from task_list import TaskList
from task import Task
from pathlib import Path
import datetime
from task import Status


# testing reusables
t = Task(2, "buy groceries", Status.TO_DO, datetime.datetime(2016, 5, 15, 22, 28, 35), None)
test_path = Path("test.json")

def test_constructor():

    # make sure it doesnt exist
    assert not test_path.exists(), f"Expected {test_path} not to exist"

    l = TaskList(test_path)

    # check if it has been created
    assert test_path.exists(), f"Expected {test_path} to be created"

    test_path.unlink(missing_ok=True)


def test_add_task():
    
    l = TaskList(test_path)

    before = l.size() 

    l.add_task(t.description)

    assert l.size() > before




from task_list import TaskList
from task import Task
from pathlib import Path

def test_constructor():

    test_path = Path("test.json")
    # make sure it doesnt exist
    assert not test_path.exists(), f"Expected {test_path} not to exist"

    l = TaskList(test_path)

    # check if it has been created
    assert test_path.exists(), f"Expected {test_path} to be created"

    test_path.unlink(missing_ok=True)




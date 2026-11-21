from task import Task
from task import Status

# status tests

def test_status_get_label():

    assert Status.IN_PROGRESS.get_label() == "In progress"
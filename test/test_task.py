from task import Task
from task import Status
import datetime

# testing reusables
t = Task(2, "buy groceries", Status.TO_DO, datetime.datetime(2016, 5, 15, 22, 28, 35), None)

#  status:enum tests

def test_status_get_label():

    assert Status.IN_PROGRESS.get_label() == "In progress"

    assert Status.TO_DO.get_label() == "To do"

    assert Status.DONE.get_label() == "Done"

# Task method tests

def test_str():

    assert str(t) == "ID:2, Description: buy groceries, Status: To do"


def test_repr():

    assert repr(t) == "Task(id='2', description='buy groceries', status='Status.TO_DO', createdAt='2016-05-15 22:28:35', updatedAt='None')"

def test_task_to_dict():

    assert t.to_dict() == {"id": 2, "description": "buy groceries", "status": "To do", "createdAt": "2016-05-15 22:28:35", "updatedAt": "Not yet updated"}


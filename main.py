from task import Task
from task import Status
from task_list import TaskList
import argparse

def main():
    # argument parser
    parser = argparse.ArgumentParser()
    commands = parser.add_subparsers(dest="command", required=True)

    add_parser = commands.add_parser("add", help="add <task-description>")
    add_parser.add_argument("description", help="description of the task")

    list_parser = commands.add_parser("list", help="list <order-by>?")

    args = parser.parse_args()

    task_list = TaskList("test.json")

    if args.command == "add":
        task_list.add_task(args.description)
    elif args.command == "list":
        print(str(task_list))
    


if __name__ == "__main__":
    main()
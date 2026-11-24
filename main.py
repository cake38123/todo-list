from datetime import datetime
from task import Task
from task import Status
from task_list import TaskList
import argparse
import json

def main():
    # argument parser
    parser = argparse.ArgumentParser()
    commands = parser.add_subparsers(dest="command", required=True)

    commands.add_parser("add", help="add <task-description>")

    commands.add_parser("list", help="list <order-by>?")

    args = parser.parse_args()

    task_list = TaskList("data.json")

    if args.command == "add":
        pass
    elif args.command == "list":
        print(str(task_list))
    


if __name__ == "__main__":
    main()
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

    update_parser = commands.add_parser("update", help="update <id> <new-description>")
    update_parser.add_argument("id", type=int, help="id of task to update")
    update_parser.add_argument("description", help="new description")

    list_parser = commands.add_parser("list", help="list <order-by>?")

    mark_parser = commands.add_parser("mark", help="mark <status> <id>")
    mark_parser.add_argument("status", help="status of the task")
    mark_parser.add_argument("id", type=int, help="id of the task to mark")

    args = parser.parse_args()

    task_list = TaskList("data.json")

    if args.command == "add":
        task_list.add_task(args.description)
    elif args.command == "list":
        print(str(task_list))
    elif args.command == "update":
        task_list.update_task(args.id, args.description)
    elif args.command == "mark":
        task_list.mark_task(args.status, args.id)
    


if __name__ == "__main__":
    main()
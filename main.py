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

    commands.add_parser()


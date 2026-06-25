import json
from datetime import datetime
import uuid as u
import argparse


def save_task_file(tasks):
        with open("tasks.json", "w") as file:
            json.dump(tasks,file)

def load_task():
    try:
        with open("tasks.json", "r") as file:
            tasks = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

# Defining a function called task_tracker inside that function all the code goes.
def task_tracker():

    parser = argparse.ArgumentParser(description="Task Manager CLI")
    subparsers = parser.add_subparsers(dest="command")
# add
    add_parser = subparsers.add_parser("add")
    add_parser.add_argument("description")
# progress
    progress_parser = subparsers.add_parser("progress")
    progress_parser.add_argument("task_num")
# update 
    update_parser = subparsers.add_parser("update")
    update_parser.add_argument("task_num")
    update_parser.add_argument("description")
# done
    done_parser = subparsers.add_parser("done")
    done_parser.add_argument("task_num")
# delete
    delete_parser = subparsers.add_parser("delete")
    delete_parser.add_argument("task_num")

    args = parser.parse_args()

    tasks = load_task()


    
    print("-----Task Tracker CLI-----")
    for i,task in enumerate(tasks, 1):
        print(f"{i} {task}")
# Inside "choose" variable user will enter the command they want to perform.
    # If user input is "add" code below will input user for a task then append that task to the tasks list.
    if args.command == "add":
        task = args.description
        id = str(u.uuid4())
        status = "todo"
        createdAt = datetime.now().strftime("%Y-%m-%d %H:%M")
        updatedAt = datetime.now().strftime("%Y-%m-%d %H:%M")
        task_data = {
            "Id": id,
            "Description": task,
            "Status": status,
            "CreatedAt": createdAt,
            "UpdatedAt": updatedAt
        }
        if task:
            tasks.append(task_data)
            print("Task Added!")
            save_task_file(tasks)
    elif args.command == "progress":
        try:
            num = int(args.task_num) - 1
            if 0 <= num < len(tasks):
                task_progress = "In Progress"
                tasks[num]["Status"] = task_progress
                save_task_file(tasks)
                print("Task in Progress")
        except IndexError:
            print("Invalid Task Number")
    elif args.command == "update":
        try:
            num = int(args.task_num) - 1
            if  0 <= num < len(tasks): 
                tasks[num]["Description"] = args.description
                tasks[num]["UpdatedAt"] = datetime.now().strftime("%Y-%m-%d %H:%M")
                save_task_file(tasks)
                print("Task Updated")
        except IndexError:
            print("Invalid Task Number")
    elif args.command == "done":
        try:
            num = int(args.task_num) -1
            if 0 <= num < len(tasks):
                tasks[num]["Status"] = "Done"
                tasks[num]["UpdatedAt"] = datetime.now().strftime("%Y-%m-%d %H:%M")
                save_task_file(tasks)
                print("Task Completed")
        except IndexError:
            print("Invalid Task Number")
    elif args.command == "delete":
        try:
            num = int(args.task_num) - 1
            tasks.pop(num)
            save_task_file(tasks)
            print("Task Deleted")
        except IndexError:
            print("Invalid Task Number")
    else:
        print("Invalid Command")

task_tracker()
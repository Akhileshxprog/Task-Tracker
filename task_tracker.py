import json
from datetime import datetime
import uuid as u
import argparse


def save_task_file(tasks):
        with open("tasks.json", "w") as file:
            json.dump(tasks, file, indent=4)

def load_task():
    try:
        with open("tasks.json", "r") as file:
            tasks = json.load(file)
            return tasks
    except (FileNotFoundError, json.JSONDecodeError):
        return []

# Defining a function called task_tracker inside that function all the code goes.
def task_tracker():

    

    parser = argparse.ArgumentParser(description="Task Manager CLI")
    subparsers = parser.add_subparsers(dest="command")

# list
    list_parser = subparsers.add_parser("list")
    list_parser.add_argument("status", nargs="?")
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

    
# Inside "choose" variable user will enter the command they want to perform.
    # If user input is "add" code below will input user for a task then append that task to the tasks list.
    if args.command == "add":
        id = str(u.uuid4())
        task_data = {
            "Id": id,
            "Description": args.description,
            "Status": "todo",
            "CreatedAt": datetime.now().strftime("%Y-%m-%d %H:%M"),
            "UpdatedAt": datetime.now().strftime("%Y-%m-%d %H:%M")
        }
        tasks.append(task_data)
        print("Task Added!")
        save_task_file(tasks)
    elif args.command == "progress":
        try:
            num = int(args.task_num) - 1
            if 0 <= num < len(tasks):
                tasks[num]["Status"] = "In Progress"
                tasks[num]["UpdatedAt"] = datetime.now().strftime("%Y-%m-%d %H:%M")
                save_task_file(tasks)
                print("Task in Progress")
        except (IndexError, ValueError):
            print("Invalid Task Number")
    elif args.command == "update":
        try:
            num = int(args.task_num) - 1
            if  0 <= num < len(tasks): 
                tasks[num]["Description"] = args.description
                tasks[num]["UpdatedAt"] = datetime.now().strftime("%Y-%m-%d %H:%M")
                save_task_file(tasks)
                print("Task Updated")
        except (IndexError, ValueError):
            print("Invalid Task Number")
    elif args.command == "done":
        try:
            num = int(args.task_num) -1
            if 0 <= num < len(tasks):
                tasks[num]["Status"] = "Done"
                tasks[num]["UpdatedAt"] = datetime.now().strftime("%Y-%m-%d %H:%M")
                save_task_file(tasks)
                print("Task Completed")
        except (IndexError, ValueError):
            print("Invalid Task Number")
    elif args.command == "delete":
        try:
            num = int(args.task_num) - 1
            if 0 <= num < len(tasks):
                tasks.pop(num)
                save_task_file(tasks)
                print("Task Deleted")
        except (IndexError, ValueError):
            print("Invalid Task Number")
    elif args.command == "list":
        if args.status == None:
            for task in tasks:
                print(task)
        elif args.status == "done":
            found = False
            for task in tasks:
                if task["Status"] == "Done":
                    print(task)
                    found = True
            if not found:
                print("No Task Completed")
        elif args.status == "not_done":
            found = False
            for task in tasks:
                if task["Status"] != "Done":
                    print(task)
                    found = True
            if not found:
                print("All Task Completed")
                    
        elif args.status == "progress":
            found = False
            for task in tasks:
                if task["Status"] == "In Progress":
                    print(task)
                    found = True
            if not found:
                print("No Task In Progress")
    else:
        print("Invalid Command")

task_tracker()
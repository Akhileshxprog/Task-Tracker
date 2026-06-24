import json
from datetime import datetime
import uuid as u

# Defining a function called task_tracker inside that function all the code goes.
def task_tracker():

    def save_task_file(tasks):
        with open("tasks.json", "w") as file:
            json.dump(tasks,file)

    try:
        with open("tasks.json", "r") as file:
            tasks = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        tasks = []
# Using while loop to run the program infinite time until the user give valid command
    while True:
        print("-----Task Tracker CLI-----")
        for i,task in enumerate(tasks, 1):
            print(f"{i} {task}")
# Inside "choose" variable user will enter the command they want to perform.
        choose = input(f"What you like to do: add | Task in Progress(e.g., progress 1) | update(e.g., update 1) | done(e.g., done 1) | delete(e.g., delete 1) | Quit: ").strip().lower()
# If user input is "add" code below will input user for a task then append that task to the tasks list.
        if choose == "add":
            task = input("Task: ")
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
        elif choose.startswith("progress"):
            try:
                num = int(choose.split()[1]) - 1
                if 0 <= num < len(tasks):
                    task_progress = "In Progress"
                    tasks[num]["Status"] = task_progress
                    save_task_file(tasks)
            except IndexError:
                print("Invalid Task Number")
        elif choose.startswith("update"):
            try:
                num = int(choose.split()[1]) - 1
                if  0 <= num < len(tasks):
                    updated_task = input(f"Update Task {num + 1}: ")
                    updated_time = datetime.now().strftime("%Y-%m-%d %H:%M")
                    tasks[num]["Description"] = updated_task
                    tasks[num]["UpdatedAt"] = updated_time
                    save_task_file(tasks)
            except IndexError:
                print("Invalid Task Number")
        elif choose.startswith("done"):
            try:
                num = int(choose.split()[1]) -1
                if 0 <= num < len(tasks):
                    done_task = ("Done")
                    tasks[num]["Status"] = done_task
                    save_task_file(tasks)
            except IndexError:
                print("Invalid Task Number")
        elif choose.startswith("delete"):
            try:
                num = int(choose.split()[1]) - 1
                tasks.pop(num)
                save_task_file(tasks)
            except IndexError:
                print("Invalid Task Number")
        elif choose == "quit":
            break
        else:
            print("Invalid Command")

task_tracker()
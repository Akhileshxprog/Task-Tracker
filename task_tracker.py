import json
import datetime
import uuid as u

# Defining a function called task_tracker inside that code all the properties goes.
def task_tracker():
    try:
        with open("tasks.json", "r") as file:
            tasks = json.load(file)
    except FileNotFoundError:
        tasks = [
            {
                "Id": id,
                "description": task_description
                # "Status":
                # "createdAt":
                # "updatedAt":
            }
        ]
# Using while loop to run the program infinite time until the user give valid command
    while True:
        print("-----Task Tracker CLI-----")
        for i,task in enumerate(tasks, 1):
            print(f"{i} {task}")
# Inside "choose" variable user will enter the command they want to perform.
        choose = input(f"What you like to do: add | update(Task Number) | done(e.g., done 1) | delete(e.g., delete 1) | Quit: ").strip().lower()
# If user input is "add" code below will input user for a task then append that task to the tasks list.
        if choose == "add":
            task = input("Task: ")
            task_description = input("Task discription: ")
            id = u.uuid4(task)
            if task:
                tasks.append(task)
                print("Task Added!")
        elif choose.startswith("update"):
            try:
                num = int(choose.split()[1]) - 1
                if  0 <= num < len(tasks):
                    updated_task = input(f"Update Task {num + 1}: ")
                    tasks[num] = updated_task
            except IndexError:
                print("Invalid Task Number")
        elif choose.startswith("done"):
            try:
                num = int(choose.split()[1]) -1
                if 0 <= num < len(tasks):
                    done_task = (f"{tasks[num]} ✅")
                    tasks[num] = done_task
            except IndexError:
                print("Invalid Task Number")
        elif choose.startswith("delete"):
            try:
                num = int(choose.split()[1]) - 1
                tasks.pop(num)
            except IndexError:
                print("Invalid Task Number")
        elif choose == "quit":
            break
        else:
            print("Invalid Command")
    with open("tasks.json", "w") as file:
        json.dump(tasks,file)

task_tracker()
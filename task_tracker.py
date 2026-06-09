# Defining a function called task_tracker inside that code all the properties goes.
def task_tracker():
    tasks = []
# Using while loop to run the program infinite time until the user give valid command
    while True:
        print("-----Task Tracker CLI-----")
        for i,task in enumerate(tasks, 1):
            print(f"{i} {task}")
# Inside "choose" variable user will enter the command they want to perform.
        choose = input(f"What you like to do: ADD | Update(Task Number) | Done(eg., Done1) | Delete(Task Number) | Quit: ").strip().lower()
        if choose == "add":
            task = input("Task: ")
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

task_tracker()
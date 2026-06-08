def task_tracker():
    tasks = []
    while True:
        print("-----Task Tracker CLI-----")
        for i,task in enumerate(tasks, 1):
            print(f"{i} {task}")
        choose = input(f"What you like to do: ADD | Update(Task Number) | Done(eg., Done1) | Delete(Task Number) | Quit: ").strip().lower()
        if choose == "add":
            task = input("Task: ")
            if task:
                tasks.append(task)
                print("Task Added!")
        elif choose.startswith == "update":
            try:
                num = int(choose.spilt()[1]) - 1
                if 0 < num > len(tasks):
                    updated_task = input("Update Task {num}: ")
                    tasks[num] == updated_task
            except IndexError:
                print("Invalid Task Number")

task_tracker()
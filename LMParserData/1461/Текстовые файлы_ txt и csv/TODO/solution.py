with open("todo.txt", "r", encoding="utf-8") as f:
    tasks = f.read().splitlines()
with open("no_repeat.txt", "w", encoding="utf-8") as f:
    no_repeat_tasks = []
    for task in tasks:
        if task not in no_repeat_tasks:
            f.write(task + "\n")
            no_repeat_tasks.append(task)
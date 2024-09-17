task = input("Please describe your task: ")
priority = input("What is your task priority(high, medium, low)")
time_bound = input("Is your task Time bound(yes/no)")

match priority:
    case "high":
        if time_bound == "yes":
            print(f"Reminder: {'\ task '} is a high priority task that requires immediate attention today!")
        else:
            print(f"Remindre: {task} is a high priority but not time bound")
    case "medium":
        if time_bound == "yes":
            print(f"Reminder: {task} is a medium priority task, just need a little attention")
        else:
            print(f"Reminder: {task} is a medium priority task, it does not need immediate attention")
    case "low":
        if time_bound == "yes":
            print(f"Note: {task} is a low priority task. but it is time bound.")
        else:
            print(f"Note: {task} is a low priority task. Consider completing it when you have free time.")
    case _:
        print("Invalid input.try again")

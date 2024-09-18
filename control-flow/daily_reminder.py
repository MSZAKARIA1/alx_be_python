task = input("Enter your task:")
time_bound = input("Is it time-bound?(yes/no): ")
priority = input("Priority(high/medium/low): ")

match priority:
    case "high":
        if time_bound == "yes":
            print(f"Reminder: {'\ task '} is a high-priority task that requires immediate attention today!")
        else:
            print(f"Reminder: {task} is a high priority but not time bound")
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

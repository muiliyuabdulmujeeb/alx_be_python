task = str(input("Enter your task: "))

priority = str(input("Priority (high/medium/low): ")).lower()

time_bound = str(input("Is it time-bound? (yes/no): ")).lower()


match priority:
    case "high":
        if time_bound == "yes":
            print(f"Reminder: '{task}' is a high priority task that requires immediate attention today!")
        elif time_bound == "no":
            print(f"Note: '{task}' is a high priority task. Consider completing it when you have free time.")
        else:
            print("Try again and respond with yes or no to the timebound question")
    case "medium":
        if time_bound == "yes":
            print(f"Reminder: '{task}' is a medium priority task that requires immediate attention today!")
        elif time_bound == "no":
            print(f"Note: '{task}' is a medium priority task. Consider completing it when you have free time.")
        else:
            print("Try again and respond with yes or no to the timebound question")
    case "low":
        if time_bound == "yes":
            print(f"Reminder: '{task}' is a low priority task that requires immediate attention today!")
        elif time_bound == "no":
            print(f"Note: '{task}' is a low priority task. Consider completing it when you have free time.")
        else:
            print("Try again and respond with yes or no to the timebound question")
    case _:
        print("Try again using the allowed options")
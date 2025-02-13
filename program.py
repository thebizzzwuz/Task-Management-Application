import main

def color_text(text, color_code):
    return f"\033[{color_code}m{text}\033[0m"  # Reset code is important!

def make_bold(text):
    return f"\033[1m{text}\033[0m"

# Common color codes (foreground)
RED = 91
GREEN = 92
YELLOW = 93
BLUE = 94
MAGENTA = 95
CYAN = 96

tasks = main.TaskList("Shopping", RED)

print(make_bold(color_text("WELCOME TO TASK FLOW", CYAN)))
print("This is a task management application that is designed to help you prioritize tasks from a day to day agenda.")
print("From this page you can view your tasks, add a task, and access your daily agenda.")
print("To access pages, type the page name: tasks to view all tasks, agenda for today's tasks, list for categories "
      "and add to add a new "
      "task.")
page = input("Which page would you like to select: ")


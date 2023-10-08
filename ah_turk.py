
import time
import xml.etree.ElementTree as ET

# Interactive script for human interaction
print("Welcome to Turk.py!")

# Write the current timestamp to last_turk_run.txt
with open("last_turk_run.txt", "w") as file:
    file.write(str(time.time()))

# TODO: Implement interactive logic for task management and Q&A
action = input("What would you like to do today? ")

# Example: Add a task
if "add task" in action.lower():
    new_task = input("Please describe the new task: ")
    try:
        tree = ET.parse('ai_tasks.xml')
        root = tree.getroot()
        task_element = ET.SubElement(root, 'Task')
        task_element.text = new_task
        tree.write('ai_tasks.xml')
        print(f"Task added: {new_task}")
    except ET.ParseError:
        print("Error parsing ai_tasks.xml")
    except FileNotFoundError:
        print("ai_tasks.xml not found")

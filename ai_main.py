
from CommonLayer.main_loop import main_loop
from BusinessLayer.task_processor import process_tasks

# Calling the main loop function with the task processor function as an argument
main_loop(process_tasks)

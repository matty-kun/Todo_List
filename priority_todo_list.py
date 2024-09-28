todo_list = []
file_name = "tasks.txt"

def load_task():
    try:
        with open (file_name, 'r') as file:
            tasks = file_name.readlines()
            return [tasks.strip() for task in tasks] # Remove the whitelines
    except FileNotFoundError:
        return [] # Return an empty list if the file doesn't exist
    
def save_tasks():
    with open(file_name, 'w') as file:
        for task in todo_list:
            file.write(task + "\n")
            
def show_tasks():
    if len(todo_list) == 0:
        print("\nNo tasks in the list!")
    else: 
        print("\nTo_Do List:")
        for i, task in enumerate(todo_list, 1):
            print(f"{i}. {task}")
    print()
    
def add_task():
    task = input("Enter a new task: ")
    todo_list.append(task)
    print(f"Task '{task}' added to the list!\n")
    save_tasks()
    
def remove_task():
    show_tasks()
    try:
        task_num = int(input("Enter the number of the task to remove: "))
        save_tasks()
    except (ValueError, IndexError):
        print("Invalid task number. Try again!\n")
        
def menu():
    print("")
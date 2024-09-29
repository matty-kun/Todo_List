todo_list = []
file_name = "tasks.txt"

def load_task():
    try:
        with open (file_name, 'r') as file:
            tasks = file.readlines()
            return [task.strip() for task in tasks] # Remove the whitelines
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
    priority = input("Enter a task priority (high/medium/low): ").lower()
    todo_list.append(f"{task} ({priority})")
    print(f"Task '{task}' added with {priority} to the list!\n")
    save_tasks()
    
def remove_task():
    show_tasks()
    try:
        task_num = int(input("Enter the number of the task to remove: "))
        removed_task = todo_list.pop(task_num - 1)
        print(f"Task '{removed_task}' removed from the list!\n")
        save_tasks()
    except (ValueError, IndexError):
        print("Invalid task number. Try again!\n")
        
def mark_task():
    show_tasks()
    
    if len(todo_list) == 0:
        print("No task to mark as completed!\n")
        return 
     
    try: 
        task_num = int(input("Enter the number of task to mark completed: "))
        selected_task = todo_list[task_num - 1]
        
        if "[✔]" in selected_task:
            print("This task is already marked as completed!\n")
        else:
            todo_list[task_num - 1] = selected_task + " [✔]"
            print("Task marked as completed!\n")
        save_tasks()
    except (ValueError, IndexError):
        print("Invalid task number. Try again!\n")
        
def menu():
    print("1. View To-Do List")
    print("2. Add a Task")
    print("3. Remove a Task")
    print("4. Mark a Task")
    print("5. Exit")
    choice = input("Enter your choice: ")
    return choice

def main():
    global todo_list
    todo_list = load_task()
    
    while True:
        choice = menu()
        
        if choice == '1':
            show_tasks()
        elif choice == '2':
            add_task()
        elif choice == '3':
            remove_task()
        elif choice == '4':
            mark_task()
        elif choice == '5':
            print("\nExiting To-Do List Application. Goodbye!")
            break
        else:
            print("Invalid Choice! Please try again.\n")
            
if __name__ == "__main__":
    main()
            
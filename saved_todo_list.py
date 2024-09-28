todo_list = []
file_name = "tasks.txt"

def load_task():
    try:
        with open(file_name, 'r') as file:
            tasks = file.readlines()
            return [task.strip() for task in tasks] # Remove newline characters
    except FileNotFoundError:
        return [] # Return an empty list if the file doesn't exist
    
def save_tasks():
    with open(file_name, 'w') as file:
        for task in todo_list:
            file.write(task + "\n")
            
def show_tasks():
    if len(todo_list) == 0:
        print("No tasks in the list!")
    else: 
        print("\nTo-Do List:")
        for i, task in enumerate(todo_list, 1):
            print(f"{i}. {task}")
    print() # Blank line for spacing
    
def add_task():
    task = input("Enter a new task: ")
    todo_list.append(task)
    print(f"Task '{task}' added to the list!\n")
    save_tasks() # Saved the updated list to the file
    
    
def remove_task():
    show_tasks()
    try: 
        task_num = int(input("Enter the number of the task to remove: "))
        removed_task = todo_list.pop(task_num - 1)
        print(f"Task '{removed_task}' removed from the list!\n")
        save_tasks()
    except(ValueError, IndexError):
        print("Invalid task number. Try again!\n")
        
def menu():
    print("1. View To-Do List")
    print("2. Add a Task")
    print("3. Remove a Task")
    print("4. Exit")
    choice = input("Enter your   choice: ")
    return choice

def main():
    global todo_list
    todo_list = load_task() # Load tasks from the file at the start
    
    while True:
        choice = menu()
        
        if choice == '1':
            show_tasks()
        elif choice == '2':
            add_task()
        elif choice == '3':
            remove_task()
        elif choice == '4':
            print("Exiting To-Do List Application. Goodbye!")
            break
        else:
            print("Invalid Choice! Please try again!\n")
            
if __name__ == "__main__":
    main()
        
        
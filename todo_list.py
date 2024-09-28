todo_list = []

# Function to display the tasks
def show_task():
    if len(todo_list) == 0:
        print("No task in the list!")
    else: 
        print("\nTo-Do List")
        for i, task in enumerate(todo_list, 1):
            print(f"{i}. {task}")
    print()
    
# Function to add task
def add_task():
    task = input("Enter a new task: ")
    todo_list.append(task)
    print(f"Task '{task}' added to the list!\n")
    
# Function to remove task
def remove_task():
    show_task()
    try: 
        task_num = int(input("Enter the number of the task to remove: "))
        removed_task =  todo_list.pop(task_num - 1)
        print(f"Task '{removed_task}' removed from the list!\n")
    except(ValueError, IndexError):
        print("Invalid task number. Try again!\n")
        
        
# Main menu to choose actions
def menu():
    print("1. View To-Do List")
    print("2. Add a Task")
    print("3. Remove a Task")
    print("4. Exit")
    choice = input("Enter your choice: ")
    return choice

# Main Function to control the application
def main():
    while True:
        choice = menu()
        
        if choice == '1':
            show_task()
        elif choice == '2':
            add_task()
        elif choice == '3':
            remove_task()
        elif choice == '4':
            print("Exiting To-Do List Application. Goodbye!")
            break
        else:
            print("Invalid choice! Please try again.\n")
            
# Run the application
if __name__ == "__main__":
    main()
    
    
    

    
    
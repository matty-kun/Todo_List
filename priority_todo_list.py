todo_list = []
done_list = []
file_name = "tasks.txt"

def load_task():
    try:
        with open (file_name, 'r') as file:
            tasks = file.readlines()
            todo = []
            done = []
            in_done_section = False
            for task in tasks:
                task = task.strip()
                if task == "Done:":
                    in_done_section = True
                elif in_done_section:
                    done.append(task)
                else: 
                    todo.append(task)
            return todo, done
    except FileNotFoundError:
        return [], [] # Return an empty list if the file doesn't exist
    
def save_tasks():
    with open(file_name, 'w') as file:
        for task in todo_list:
            file.write(task + "\n")
            
        if done_list:
            file.write("\nDone:\n") # Adds "Done" Section to the file
            for task in done_list:
                file.write(task + "\n")
            
def show_tasks():
    if len(todo_list) == 0:
        print("\nNo tasks in the list!")
    else: 
        print("\nTo_Do List:")
        for i, task in enumerate(todo_list, 1):
            print(f"{i}. {task}")
            
    if len(done_list) > 0:
        print("\nDone:")
        for i, task in enumerate(done_list, 1):
            print(f"{i}. {task}")
    print()
    
def add_task():
    task = input("Enter a new task: ")
    priority = input("Enter a task priority (high/medium/low): ").lower()
    todo_list.append(f"{task} ({priority})")
    print(f"Task '{task}' added with {priority} priority to the list!\n")
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
            crossed_out_task = f"~{selected_task}~ [✔]"
            done_list.append(crossed_out_task)
            
            todo_list.pop(task_num - 1)
            
            print(f"Task '{selected_task}' moved to Done Section!\n")
            
        save_tasks()  # Saving after marking the task
        
    except (ValueError, IndexError):
        print("Invalid task number. Try again!\n")

def edit_task():
    show_tasks()
    try:
        task_num = int(input("Enter the number of the task to edit: "))
        new_task = input("Enter the updated task description: ")
        new_priority = input("Enter the updated priority (high/medium/low): ").lower()
        todo_list[task_num - 1] = f"{new_task} ({new_priority})"
        print(f"Task {task_num} updated successfully!\n")
        save_tasks()
    except (ValueError, IndexError):
        print("Invalid task number. Try again!\n")
        
def clear_task(section="all"):
    if section == "todo":
        todo_list.clear()
    elif section == "done":
        done_list.clear()
    else:
        todo_list.clear()
        done_list.clear()
    save_tasks()
    print(f"Tasks in {section} section cleared!\n")
        
def move_task_back():
    show_tasks()
    
    if len(done_list) == 0:
        print("No completed tasks to move back!\n")
        return
    try:
        task_num = int(input("Enter the number of the task to move to To-Do: "))
        task_to_move = done_list.pop(task_num - 1).replace("~", "").replace(" [✔]", "")
        print(f"Task '{task_to_move}' moved back to To-Do!\n")
        save_tasks()
    except (ValueError, IndexError):
        print("Invalid task number. Try again!\n")
    
    
def menu():
    print("1. View To-Do List")
    print("2. Add a Task")
    print("3. Remove a Task")
    print("4. Mark a Task")
    print("5. Edit a Task")
    print("6. Clear all tasks")
    print("7. Move a Task Back")
    print("8. Exit")
    choice = input("Enter your choice: ")
    return choice

def main():
    global todo_list, done_list
    todo_list, done_list = load_task()
    
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
            edit_task()
        elif choice == '6':
            clear_task()
        elif choice == '7':
            move_task_back()
        elif choice == '8':
            print("\nExiting To-Do List Application. Goodbye!")
            break
        else:
            print("Invalid Choice! Please try again.\n")
            
if __name__ == "__main__":
    main()
            
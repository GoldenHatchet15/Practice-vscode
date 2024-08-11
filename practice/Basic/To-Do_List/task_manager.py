#!/usr/bin/env python3
import os

# Initialize the to-do list
todo_list = []

def show_menu():
    print("\nTo-Do List Menu:")
    print("1. View To-Do List")
    print("2. Add a Task")
    print("3. Mark a Task as Completed")
    print("4. Delete a Task")
    print("5. Exit")

def view_todo_list():
    if not todo_list:
        print("\nYour to-do list is empty!")
    else:
        print("\nYour To-Do List:")
        for index, task in enumerate(todo_list, start=1):
            status = "[X]" if task['completed'] else "[ ]"
            print(f"{index}. {status} {task['description']}")

def add_task():
    task_description = input("Enter the task description: ")
    task = {'description': task_description, 'completed': False}
    todo_list.append(task)
    print(f"Task '{task_description}' added to the list!")

def mark_task_completed():
    view_todo_list()
    if todo_list:
        try:
            task_number = int(input("\nEnter the task number to mark as completed: "))
            if 1 <= task_number <= len(todo_list):
                todo_list[task_number - 1]['completed'] = True
                print(f"Task {task_number} marked as completed!")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Please enter a valid number.")

def delete_task():
    view_todo_list()
    if todo_list:
        try:
            task_number = int(input("\nEnter the task number to delete: "))
            if 1 <= task_number <= len(todo_list):
                removed_task = todo_list.pop(task_number - 1)
                print(f"Task '{removed_task['description']}' deleted from the list!")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Please enter a valid number.")

def main():
    while True:
        show_menu()
        choice = input("Choose an option (1-5): ")
        if choice == '1':
            view_todo_list()
        elif choice == '2':
            add_task()
        elif choice == '3':
            mark_task_completed()
        elif choice == '4':
            delete_task()
        elif choice == '5':
            print("Goodbye!")
            break
        else:
            print("Invalid choice, please choose a valid option.")

if __name__ == "__main__":
    main()


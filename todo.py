def add (tasks , task ):
    tasks.append(task)
    print(f"{task} added !")

def view (tasks):
    if not tasks:
        print("No tasks in the list.")

def mark(tasks):
    if not tasks:
        print("No tasks to mark.")
        return
    view(tasks)

def delete(tasks):
     if not tasks:
        print("No tasks to delete.")
        return
     view(tasks)

def main ():
    tasks = {}
    while True:
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task ")
        print("4. Delete Task")
        print("5. Exit")
        option = input("Enter an option:")
        if option == 1:
            tasks = input("Add your task :")
            add :{tasks}
        elif option == 2:
            view  :{tasks}
        elif option == 3:
            tasks = input ("Enter: ")
            mark  :{tasks}
        elif option == 4:
             tasks = input ("Enter: ")
             delete  :{tasks}
        elif option == 5:
            break
        else:
            print("Invalid option!")
main() 

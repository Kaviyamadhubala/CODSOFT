tasks=[]
def show_menu():
    print("\nTo Do List")
    print("1.View Tasks")
    print("2.Add Tasks")
    print("3.Remove Tasks")
    print("4.Exit")
def view_tasks():
    print("\nYour tasks:")
    if not tasks:
        print("No tasks yet!")
    else:
        for i,task in enumerate(tasks,1):
            print(f"{i}.{task}")
def add_task():
    task=input("Enter task: ")
    tasks.append(task)
    print(f"Added:{task}")
def remove_task():
    view_tasks()
    if tasks:
        num=int(input("Enter task number to remove: "))
        if 1<=num<=len(tasks):
            removed=tasks.pop(num-1)
            print(f"Removed:{removed}")
        else:
            print("Invalid number!")
while True:
    show_menu()
    choice=input("Choose option(1-4): ")
    if choice=="1":
        view_tasks()
    elif choice=="2":
        add_task()
    elif choice=="3":
        remove_task()
    elif choice=="4":
        print("GoodBye!")
        break
    else:
        print("Invalid Choice!")

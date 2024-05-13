todo_list = []

def add_list():
    item = input("enter a new task")
    todo_list.append(item)
    print(f"{item} added to the todo list")

def display_list():
    print("---------------")
    print("To Do List:") 
    print("-------------")
    for index, item in enumerate(todo_list, start=1):
        print(f"{index} - {item}")

def remove_list():
    display_list()
    index = int(input("Enter your item number to remove "))-1
     
    if 0<= index < len(todo_list):
       removed_item = todo_list.pop(index)
       print(f"{removed_item} removed from the list")
    else:
        print("Invalid Input")

while True:
    print("#################")
    print("TO DO LIST APP")
    print("#################")
    print("1. Add To List ")
    print("2. Display List ")
    print("3. Remove From List ")
    print("4. Exit ")

    option = input("Select your option:- ")

    if option  == '1':
        print("Add")

    elif option == '2':
        print("Display")

    elif option == '3':
        print("Remove")

    elif option == '4':
        print("Exit")
        break

    else:
        print("Invalid Option Selected...")

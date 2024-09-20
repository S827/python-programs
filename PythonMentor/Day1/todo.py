def todo():
    print("*****To Do Application*****")
    print("1. Add tasks")
    print("2. View tasks")
    print("3. Mark completed tasks")
    print("4. remove the tasks")
    # add_task = input("Select 1 to add tasks..")
    # view_task = input("Select 2 to view your tasks")
    # mark_task = input("Select 3 to mark the completed tasks")
    # remove_task = input("Select 4 to remove tasks")
    user_in = int(input())
    if user_in == 1:
        add_task()
    elif user_in == 2:
        view_task()
    elif user_in == 3:
        mark_task()
    elif user_in == 4:
        remove_task()
    else:
        print("Chose the correct option from 1 to 4")


def add_task():
    print("Adding tasks")


def view_task():
    print("Viewing tasks")


def mark_task():
    print("Marking tasks")


def remove_task():
    print("Removing tasks")


if __name__ == "__main__":
    todo()

Stack = []
max_size = 5

while True:
    choice = int(input("\nEnter your choice\n1. Push\n2. Pop\n3. Display\n4. Exit\n"))

    # Push
    if choice == 1:
        if len(Stack) < max_size:
            value = int(input("Enter Element: "))
            Stack.append(value)
            print("Element inserted")
        else:
            print("Stack is OVERFLOW")

    # Pop
    elif choice == 2:
        if len(Stack) > 0:
            value = Stack.pop()
            print("Deleted Element:", value)
        else:
            print("Stack is UNDERFLOW")

    # Display
    elif choice == 3:
        if len(Stack) > 0:
            print("Stack elements:")
            for i in range(len(Stack) - 1, -1, -1):
                print(Stack[i])
        else:
            print("Stack is EMPTY")

    # Exit
    elif choice == 4:
        print("Program is End...!")
        break

    else:
        print("Invalid choice")
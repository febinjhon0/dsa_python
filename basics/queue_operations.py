queue = []

def enqueue():
    element = input("Enter element to enqueue: ")
    queue.append(element)
    print(element, "added to queue")

def dequeue():
    if not queue:
        print("Queue is empty")
    else:
        removed = queue.pop(0)
        print(removed, "removed from queue")

def display():
    if not queue:
        print("Queue is empty")
    else:
        print("Queue elements are:", queue)

while True:
    print("\n--- Queue Operations ---")
    print("1. Enqueue")
    print("2. Dequeue")
    print("3. Display")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        enqueue()
    elif choice == 2:
        dequeue()
    elif choice == 3:
        display()
    elif choice == 4:
        print("Exiting...")
        break
    else:
        print("Invalid choice")
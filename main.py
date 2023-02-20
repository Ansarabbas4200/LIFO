import queue

q = queue.LifoQueue()
# Size of the queue
size_of_queue = input("How many items you want to add in Queue?\n")
if size_of_queue.isdigit():
    size_of_queue = int(size_of_queue)
    # Adds Items to the queue
    for x in range(size_of_queue):
        q.put(x + 1)
    # Displays Items in the queue
    print("Members of the queue:")
    for n in list(q.queue):
        print(n, end="  ")
while True:
    removing_choice = input("\nHow many items you want to remove from Queue? to Press 'E' to exit.\n").lower()
    if q.qsize() == 0 or removing_choice == 'e':
        break
    if removing_choice.isdigit():
        removing_choice = int(removing_choice)
        if removing_choice > size_of_queue-1:
            print("Enter a smaller number. ")
            continue
        # Removes Items from the Queue
        for x in range(int(removing_choice)):
            q.get()
        print("Members of the queue:")
        for n in list(q.queue):
            print(n, end="  ")
        print("\nSize of the queue:")
        print(q.qsize())

    else:
        print("Enter a valid input!")

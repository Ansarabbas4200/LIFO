import queue
q = queue.LifoQueue()
size_of_queue = input("How many items you want to add in Queue?\n")
if size_of_queue.isdigit():
    for x in range(int(size_of_queue)):
        q.put(x+1)
    print("Members of the queue:")
    for n in list(q.queue):
        print(n, end="  ")
removing_choice = input("\nHow many items you want to remove from Queue?\n")
if removing_choice.isdigit():
    for x in range(int(removing_choice)):
        q.get()
        print("Members of the queue:")
    for n in list(q.queue):
        print(n, end="  ")
    print("\nSize of the queue:")
    print(q.qsize())
else:
    print("Enter a valid input!")

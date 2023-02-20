import queue
q = queue.LifoQueue()
size_of_queue = int(input("How many items you want to add in Queue?\n"))
for x in range(size_of_queue):
    q.put(x+1)
print("Members of the queue:")
for n in list(q.queue):
    print(n, end="  ")
removing_choice = int(input("\nHow many items you want to remove from Queue?\n"))
for x in range(removing_choice):
    q.get()
print("Members of the queue:")
for n in list(q.queue):
    print(n, end="  ")
print("\nSize of the queue:")
print(q.qsize())

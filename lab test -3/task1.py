from collections import deque

# Creating a queue
queue = deque()

# Enqueue 4 values
queue.append(10)
queue.append(20)
queue.append(30)
queue.append(40)

print("Queue after enqueuing 4 values:", queue)

# Dequeue 1 value
removed = queue.popleft()
print("Dequeued value:", removed)

# Display queue
print("Queue after dequeue:", queue)

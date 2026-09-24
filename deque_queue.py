from collections import deque
queue = deque([10, 20, 30])
print("Queue:", queue)
queue.append(40)
print("After adding:", queue)
queue.popleft()
print("After removing:", queue)

OUTPUT: 
Queue: deque([10, 20, 30])
After adding: deque([10, 20, 30, 40])
After removing: deque([20, 30, 40])

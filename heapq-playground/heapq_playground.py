# importing "heapq" to implement heap queue
import heapq

# initializing list
li = [5, 7, 9, 1, 3]

# using heappush() to push elements into heap
# pushes 4
heapq.heappush(li,4)

# printing modified heap
print ("The modified heap after push is : ")
print (list(li))

# printing modified heap
heapq.heapify(li)
print ("The modified heap after heapify is : ")
print (list(li))

# using heappop() to pop smallest element
print ("The popped and smallest element is : ")
print (heapq.heappop(li))

queue = ['first','second','third']
print (queue)

#pushing  elements

queue.append('fourth')
queue.append('fifth')
print(queue)

#printing tail

n = len(queue)
print(queue[n-1])
print(queue)

#print poping elements
queue.remove(queue[0])
print(queue)
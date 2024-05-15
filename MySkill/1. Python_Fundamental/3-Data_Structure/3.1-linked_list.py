# # Linked List 
# linked_list = ['one', 'two','three'] # initiate linked list
# print(linked_list)

# linked_list.append('four') # Add element into linked list
# print(linked_list)

# linked_list.sort()
# print(linked_list)
# linked_list.pop()
# print(linked_list)
class SinglyLinkedList :
    class Node:
        def __init__(self, element,nextNode=None) :
            self.element = element
            self.nextNode = nextNode
        
    def __init__(self) :
        self._head = None
        self.__size = 0
    
    def __str__(self) :
        result = " "
        pointer = self._head
        while pointer  is not None:
            result = result + str(pointer.element)
            pointer = pointer.nextNode
        return result
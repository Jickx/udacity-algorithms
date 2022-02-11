"""The LinkedList code from before is provided below.
Add three functions to the LinkedList.
"get_position" returns the element at a certain position.
The "insert" function will add an element to a particular
spot in the list.
"delete" will delete the first element with that
particular value.
Then, use "Test Run" and "Submit" to run the test cases
at the bottom."""

class Element(object):
    def __init__(self, value):
        self.value = value
        self.next = None
        
class LinkedList(object):
    def __init__(self, head=None):
        self.head = head
        
    def append(self, new_element):
        current = self.head
        if self.head:
            while current.next:
                current = current.next
            current.next = new_element
        else:
            self.head = new_element
            
    def get_position(self, position):
        """Get an element from a particular position.
        Assume the first position is "1".
        Return "None" if position is not in the list."""
        current = self.head
        for i in range(1, position):
            if not current:
                return None
            if current.next:
                current = current.next
        return current
    
    def insert(self, new_element, position):
        """Insert a new node at the given position.
        Assume the first position is "1".
        Inserting at position 3 means between
        the 2nd and 3rd elements."""
        current = self.head
        if position == 1:
            new_element.next = self.head
            self.head = new_element
        else:
            for i in range(1, position):
                if i == position - 1:
                    new_element.next = current.next
                    current.next = new_element
                else:
                    current = current.next
    
    def delete(self, value):
        """Delete the first node with a given value."""
        current = self.head
        while current:
            if current.value == value:
                if current == self.head:
                    self.head = current.next
                    break
                else:
                    previous.next = current.next
                    break
            else:
                previous = current
                current = current.next


    def print_linked_list(self):
        current = self.head
        temp_list = []
        while True:
            temp_list.append(current.value)
            current = current.next
            if not current:
                break
        return temp_list


# Test cases
# Set up some Elements
e1 = Element(1)
e2 = Element(2)
e3 = Element(3)
e4 = Element(4)
e5 = Element(5)

# Start setting up a LinkedList
ll = LinkedList(e1)
ll.append(e2)
ll.append(e3)

print(f"After setting: {ll.print_linked_list()}")

# Test get_position
# Should print 3

# Test insert
ll.insert(e4,3)
# Should print 4 now
print(f"After insert: {ll.print_linked_list()}")

# Test delete
ll.delete(1)
print(f"After delete: {ll.print_linked_list()}")

# Should print 2 now
print(ll.get_position(1).value)
# Should print 4 now
print(ll.get_position(2).value)
# Should print 3 now
print(ll.get_position(3).value)
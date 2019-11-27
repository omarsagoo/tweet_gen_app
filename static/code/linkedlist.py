#!python


class Node(object):

    def __init__(self, data):
        """Initialize this node with the given data."""
        self.data = data
        self.next = None
        self.previous = None

    def __repr__(self):
        """Return a string representation of this node."""
        return 'Node({!r})'.format(self.data)


class LinkedList(object):

    def __init__(self, items=None):
        """Initialize this linked list and append the given items, if any."""
        self.head = None  # First node
        self.tail = None  # Last node
        self.count = 0 # length of List
        # Append given items
        if items is not None:
            for item in items:
                self.append(item)
                

    def __str__(self):
        """Return a formatted string representation of this linked list."""
        items = ['({!r})'.format(item) for item in self.items()]
        return '[{}]'.format(' -> '.join(items))

    def __repr__(self):
        """Return a string representation of this linked list."""
        return 'LinkedList({!r})'.format(self.items())

    
    def __iter__(self):
        """allows for iteration through the linked list, uses the python __iter__() method to allow this."""
        # set the initial node to the head
        node = self.head

        # iterate in a range of the length of the linked list
        for _ in range(self.count):
            #  yield the node data. 
            # yield works similarily to return, however it allows the function to continue running
            yield node.data
            # move on to the next node
            node = node.next

    def items(self):
        """Return a list (dynamic array) of all items in this linked list.
        Best and worst case running time: O(n) for n items in the list (length)
        because we always need to loop through all n nodes to get each item."""
        items = []  # O(1) time to create empty list
        # Start at head node
        node = self.head  # O(1) time to assign new variable
        # Loop until node is None, which is one node too far past tail
        while node is not None:  # Always n iterations because no early return
            items.append(node.data)  # O(1) time (on average) to append to list
            # Skip to next node to advance forward in linked list
            node = node.next  # O(1) time to reassign variable
        # Now list contains items from all nodes
        return items  # O(1) time to return list

    def is_empty(self):
        """Return a boolean indicating whether this linked list is empty."""
        return self.head is None

    def length(self):
        """Return the length of this linked list by traversing its nodes."""
        return self.count

    def append(self, item):
        """Insert the given item at the tail of this linked list.
        Running time: O(1) 
        because it only has to complete a constant number of steps."""
        
        node = Node(item)
        if self.is_empty():
            self.head = node
            self.tail = node
            self.count += 1
        else:
            self.tail.next = node
            node.previous = self.tail
            self.tail = node
            self.count += 1


    def prepend(self, item):
        """Insert the given item at the head of this linked list.
        Running time: O(1) 
        because it only has to complete a constant number of steps. 
        """
        
        node = Node(item)
        if self.is_empty():
            self.head = node
            self.tail = node
            self.count += 1

        else:
            node.next = self.head
            self.head.previous = node 
            self.head = node
            self.count += 1



    def find(self, quality):
        """Return an item from this linked list satisfying the given quality.
        Best case running time: O(1) Why and under what conditions?
            if finding the head
        Worst case running time: O(n) Why and under what conditions?
            if there are a lot of items in the list"""
       
        node = self.head

        while node != None:
            if quality(node.data) == False:
                node = node.next
            elif node.data != None:
                # return node.data
                return node

        return None

    def replace(self, find_item, new_item):
        """finds and replaces a node with the given arguments. 
        Best case running time: O(1) Why and under what conditions?
            if finding the head
        Worst case running time: O(n) Why and under what conditions?
            if there are a lot of items in the list"""
        node = self.find(lambda item: item == find_item)
        node.data = new_item
        return node


    def delete(self, item):
        """Delete the given item from this linked list, or raise ValueError.
        Best case running time: O(1) Why and under what conditions?
            If deleting the head
        Worst case running time: O(n) Why and under what conditions?
            depending on the size of the linked list. if there are a lot of items in the list"""
        
        if item in self.items():
            node = self.find(lambda data: data == item)
            if self.head != node and self.tail != node:
                node.previous.next = node.next
                node.next.previous = node.previous
                self.count -= 1
            elif self.head == node and self.tail == node:
                self.head = None
                self.tail = None
                self.count = 0
            elif self.head == node and self.tail != node:
                self.head = self.head.next
                self.head.previous = None
                self.count -= 1
            elif self.head != node and self.tail == node:
                self.tail = self.tail.previous
                self.tail.next = None
                self.count -= 1
        else:
            raise ValueError('Item not found: {}'.format(item))

                
            
            





def test_linked_list():
    ll = LinkedList()
    print('list: {}'.format(ll))

    print('\nTesting append:')
    for item in ['A', 'B', 'C', 'D', 'E']:
        print('append({!r})'.format(item))
        ll.append(item)
        print('list: {}'.format(ll))

    print('head: {}'.format(ll.head))
    print('tail: {}'.format(ll.tail))
    print('length: {}'.format(ll.length()))

    test_replace = False
    if test_replace == True:
        print()
        print('replace A with E: {}'.format(ll.replace('A', 'E')))
        print(ll)
        for item in ll:
            print(item)
        print()

    # Enable this after implementing delete method
    delete_implemented = True
    if delete_implemented:
        print('\nTesting delete:')
        for item in ['B', 'C', 'A', 'D', 'E']:
            print()
            print('delete({!r})'.format(item))
            ll.delete(item)
            print('list: {}'.format(ll))
            print('head: {}'.format(ll.head))
            print('tail: {}'.format(ll.tail))
            print('length: {}'.format(ll.length()))
            

        print()
        print('head: {}'.format(ll.head))
        print('tail: {}'.format(ll.tail))
        print('length: {}'.format(ll.length()))

    


if __name__ == '__main__':
    test_linked_list()

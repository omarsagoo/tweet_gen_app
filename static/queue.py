class Queue():
    '''class to create a list that holds a queue'''
    def __init__(self):
        self.items = []

    def __repr__(self):
        """Return a string representation of this hash table."""
        return "['" + "' -> '".join(self.items) + "']"

    def __iter__(self):
        for item in self.items:
            yield item

    def is_empty(self):
        '''Returns True if empty'''
        return bool(self.items == [])

    def enqueue(self, item):
        '''adds an item to the back of the queue'''
        self.items.append(item)

    def dequeue(self):
        '''removes and returns the item at the front of the list'''
        return self.items.pop(0)

if __name__ == "__main__":
    q = Queue()
    q.enqueue('a')
    q.enqueue('b')
    q.enqueue('c')
    q.enqueue('d')
    print('is empty: ', q.is_empty())
    print('Queue: ', q)
    print('remove: ', q.dequeue())
    print('Queue: ', q)
    print('remove: ', q.dequeue())
    print('Queue: ', q)
    print('remove: ', q.dequeue())
    print('Queue: ', q)
    print('remove: ', q.dequeue())
    print('Queue: ', q)
    print('is empty: ', q.is_empty())

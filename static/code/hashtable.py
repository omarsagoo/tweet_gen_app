#!python

from linkedlist import LinkedList


class HashTable(object):

    def __init__(self, init_size=8):
        """Initialize this hash table with the given initial size."""
        # Create a new list (used as fixed-size array) of empty linked lists
        self.buckets = [LinkedList() for _ in range(init_size)]
        self.count = 0

    def __str__(self):
        """Return a formatted string representation of this hash table."""
        items = ['{!r}: {!r}'.format(key, val) for key, val in self.items()]
        return '{' + ', '.join(items) + '}'

    def __repr__(self):
        """Return a string representation of this hash table."""
        return 'HashTable({!r})'.format(self.items())

    # python __iter__ method to make the hashtable iterable
    def __iter__(self):
        for bucket in self.buckets:
            for item in bucket.items():
                yield item

    def _bucket_index(self, key):
        """Return the bucket index where the given key would be stored."""
        return hash(key) % len(self.buckets)
    
    def _get_item(self, key):
        '''helper function returns the item and bucket, inspired from Ben Lafferty'''
        if self.contains(key):
            index = self._bucket_index(key)
            bucket = self.buckets[index]
            
            item = bucket.find(lambda item: item[0] == key)

            return item, bucket
        else:
            raise KeyError('Key not found: {}'.format(key))



    def keys(self):
        """Return a list of all keys in this hash table.
        Running time: O(n) Why and under what conditions?
            checks a list of n items"""
        all_keys = []
        for bucket in self.buckets:
            for key, value in bucket.items():
                all_keys.append(key)
        return all_keys

    def values(self):
        """Return a list of all values in this hash table.
        Running time: O(n) Why and under what conditions?
            checks a list of n items"""
        
        all_values = []
        for bucket in self.buckets:
            for key, value in bucket.items():
                all_values.append(value)
        return all_values

    def items(self):
        """Return a list of all items (key-value pairs) in this hash table.
        Running time: O(n) Why and under what conditions?
                there is a linear amount of items in the hashtable"""
        # Collect all pairs of key-value entries in each bucket
        all_items = []
        for bucket in self.buckets:
            all_items.extend(bucket.items())
        return all_items

    def length(self):
        """Return the number of key-value entries by traversing its buckets.
        Running time: O(1) Why and under what conditions?
                constant number of operations"""
        
        return self.count


    def contains(self, key):
        """Return True if this hash table contains the given key, or False.
        Running time: O(???) Why and under what conditions?"""
        
        if key in self.keys():
            return True
        else:
            return False
        

    def get(self, key):
        """Return the value associated with the given key, or raise KeyError.
        Running time: O(n) Why and under what conditions?
                Checks a list of n items, linear time"""
        
        
        item, bucket = self._get_item(key)
        return item.data[1]
        
    def set(self, key, value):
        """Insert or update the given key with its associated value.
        Running time: O(1)/O(n) Why and under what conditions?
            If the key doesnt  exist then adds directly to the end. if it does its linear in checking the list"""
        index = self._bucket_index(key)
        bucket = self.buckets[index]
        
        if self.contains(key):
            item = bucket.find(lambda item: item[0] == key)
            bucket.replace(item.data, (key, value))
        else:
            bucket.append((key, value))
            self.count += 1



    def delete(self, key):
        """Delete the given key from this hash table, or raise KeyError.
        Running time: O(n) Why and under what conditions?
                If there are a lot of items in the list, there is a linear amount of operations"""
        
        item, bucket = self._get_item(key)
        bucket.delete(item.data)
        self.count -= 1


def test_hash_table():
    ht = HashTable()
    print('hash table: {}'.format(ht))

    print('\nTesting set:')
    for key, value in [('I', 1), ('V', 5), ('X', 10)]:
        print('set({!r}, {!r})'.format(key, value))
        ht.set(key, value)
        print('hash table: {}'.format(ht))

    print('\nTesting get:')
    for key in ['I', 'V', 'X']:
        value = ht.get(key)
        print('get({!r}): {!r}'.format(key, value))

    print('contains({!r}): {}'.format('X', ht.contains('X')))
    print('length: {}'.format(ht.length()))

    # Enable this after implementing delete method
    delete_implemented = True

    if delete_implemented:
        print('\nTesting delete:')
        print(ht.keys())
        print(ht.length())
        print()

        for key in ['I', 'V', 'X']:
            print('delete({!r})'.format(key))
            ht.delete(key)
            print('hash table: {}'.format(ht))

        print('contains(X): {}'.format(ht.contains('X')))
        print('length: {}'.format(ht.length()))


if __name__ == '__main__':
    test_hash_table()

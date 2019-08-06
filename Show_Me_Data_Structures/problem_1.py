"""
OrderedDict is using a doubly linked list to maintain the order of elements in the dictionary.
Deletion and Insertion operation takes O(1)
"""
import collections

class LRU_Cache(object):

    def __init__(self, capacity):
        # Initialize class variables
        self.capacity = capacity
        self.cache = collections.OrderedDict() 

    def get(self, key):
        # Retrieve item from provided key. Return -1 if nonexistent. 
        if self.capacity <= 0:
            print("Capacity cache must be superior to zero")
        else:
            if key not in self.cache:
                return -1

            value = self.cache[key]
            self.cache.move_to_end(key)
            return value

    def set(self, key, value):
        # Set the value if the key is not present in the cache. If the cache is at capacity remove the oldest item. 

        if self.capacity > 0:
            self.cache[key] = value
        else:
            print("Capacity cache must be superior to zero")

        if len(self.cache) > self.capacity:
            self.cache.popitem(last=False)

# Test Case 1
print("Test case 1")
our_cache = LRU_Cache(5)

our_cache.set(1, 1);
our_cache.set(2, 2);
our_cache.set(3, 3);
our_cache.set(4, 4);

print(our_cache.get(1)) # returns 1
print(our_cache.get(2)) # returns 2
print(our_cache.get(9)) # returns -1 because 9 is not present in the cache

our_cache.set(5, 5) 
our_cache.set(6, 6)

print(our_cache.get(3)) # returns -1 because the cache reached it's capacity and 3 was the least recently used entry


# Test Case 2
print("\nTest Case 2")
our_cache = LRU_Cache(2)

our_cache.set(1, 1)       # returns 1
our_cache.set(2, 2)       # returns 2
our_cache.set(1, 10)      # returns -1

print(our_cache.get(1))   # returns 1
print(our_cache.get(2))   # returns 2
print(our_cache.get(10))  # returns -1

# Test case 3
print("\nTest Case 3")
our_cache = LRU_Cache(0)
our_cache.set(1, 1)

print(our_cache.get(1))   # Empty cache

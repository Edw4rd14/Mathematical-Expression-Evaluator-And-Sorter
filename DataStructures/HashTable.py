# ST1507 DATA STRUCTURES AND ALGORITHM (AI) CA2 ASSIGNMENT: ASSIGNMENT STATEMENT EVALUATOR & SORTER
# NAME: EDWARD TAN YUAN CHONG; ASHWIN RAJ
# CLASS: DAAA/FT/2B/04
# ADM NO: 2214407; 2239716

# Hashtable.py
'''
Implemented Dynamic Resizing to prevent running out of space
'''

# Import Modules

# Hashtable Class
class HashTable:
    # Initialization
    def __init__(self, size=4):
        # Set size of Hastable
        self.size = size
        # Keys and Buckets
        self.keys = [None] * size
        self.buckets = [None] * size
        # Count of items stored
        self.count = 0 

    # Hash Function to convert key to index
    def _hash_function(self, key):
        return hash(key) % self.size
    
    # Collision Resolution
    def _rehash_function(self, old_hash):
        return hash(old_hash+1) % self.size
    
    # Dynamic Resizing of Hashtable
    def _resize(self):
        # Double size of Hashtable
        new_size = self.size * 2
        new_keys = [None] * new_size
        new_buckets = [None] * new_size
        # Store old keys and buckets
        old_keys = self.keys
        old_buckets = self.buckets
        # Update the instance variables to the new arrays and size
        self.keys = new_keys
        self.buckets = new_buckets
        self.size = new_size
        # Reset count of items
        self.count = 0
        # Re-add all items using the new hash function
        for key, value in zip(old_keys, old_buckets):
            if key is not None:
                self[key] = value
    
    # Add Item into Hashtable
    def __setitem__(self, key, value):
        # Double the size of the Hashtable if load factor exceeds 85%
        if self.count / self.size > 0.85:
            self._resize()
        # Get hash key of item
        index = self._hash_function(key)
        # Set start index as hash key
        startIndex = index
        # Loop until item is stored in bucket or if there are no more buckets
        while True:
            # If bucket is empty, store item in bucket and increment count
            if self.buckets[index] is None:
                self.buckets[index] = value
                self.keys[index] = key
                self.count += 1
                break
            else:
                # If it is not empty and has the same key, overwrite it
                if self.keys[index] == key:
                    self.buckets[index] = value
                    break
                # Else, rehash and try to store in a new bucket
                else: 
                    index = self._rehash_function(index)
                    # Safeguard against an infinite loop if for some reason there are no buckets, which should not happen with resizing
                    if index == startIndex:
                        break

    # Get item from Hashtable
    def __getitem__(self,key):
        index = self._hash_function(key)
        if self.table[index]:
            for k, v in self.table[index]:
                if k == key:
                    return v
        return None

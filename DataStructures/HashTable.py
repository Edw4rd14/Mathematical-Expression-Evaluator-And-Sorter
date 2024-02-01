# =================================================================================================
# ST1507 DATA STRUCTURES AND ALGORITHM (AI) CA2 ASSIGNMENT: ASSIGNMENT STATEMENT EVALUATOR & SORTER
# NAME: EDWARD TAN YUAN CHONG; ASHWIN RAJ
# CLASS: DAAA/FT/2B/04
# ADM NO: 2214407; 2239716
# =================================================================================================
# FILENAME: HashTable.py
# =================================================================================================
'''
Description:
Implemented Dynamic Resizing to prevent running out of space
'''

# Hashtable Class
class HashTable:
    # Initialization
    def __init__(self, size=10):
        """
        The __init__ function initializes the Hashtable class.
        Args:
        size (int): The size of the hashtable. Defaults to 10 if not provided.
        
        
        :param self: Refer to the instance of the class
        :param size: Set the size of the hash table
        :return: Nothing
        """
        # Set size of Hastable
        self.size = size
        # Keys and Buckets
        self._keys = [None] * size
        self._buckets = [None] * size
        # Count of items stored
        self.count = 0 

    @property
    def keys(self):
        """
        The keys function returns a list of the keys in the hash table.
                
        :param self: Refer to the instance of the class
        :return: A list of all keys in the hash table
        """
        return self._keys
    
    @property
    def buckets(self):
        """
        The buckets function returns the buckets in the hash table.
        
        :param self: Refer to the instance of the class
        :return: The list of buckets
        """
        return self._buckets

    # Hash Function to convert key to index
    def _hash_function(self, key):
        """
        The _hash_function function takes a key and returns an index in the hash table.
            
        :param self: Refer to the instance of the class
        :param key: Key for hash table
        :return: The hash value of the key
        """
        return hash(key) % self.size
    
    # Collision Resolution
    def _rehash_function(self, old_hash):
        """
        The _rehash_function function is used to rehash the hash value of a key.
        This function takes in an old_hash and returns a new hash value.
        
        :param self: Refer to the instance of the class
        :param old_hash: Old hash value to be rehashed
        :return: The hash of the old_hash plus one, modulo the size of the table
        """
        return hash(old_hash+1) % self.size
    
    # Dynamic Resizing of Hashtable
    def _resize(self):
        """
        The _resize function is called when the load factor of the Hashtable exceeds 0.85.
        The function doubles the size of both _keys and _buckets, then re-adds all items using
        the new hash function.
        
        :param self: Refer to the instance of the class
        :return: A new hashtable with a larger size, and the same items as the old one
        """
        # Double size of Hashtable
        new_size = self.size * 2
        new_keys = [None] * new_size
        new_buckets = [None] * new_size
        # Store old keys and buckets
        old_keys = self._keys
        old_buckets = self._buckets
        # Update the instance variables to the new arrays and size
        self._keys = new_keys
        self._buckets = new_buckets
        self.size = new_size
        # Reset count of items
        self.count = 0
        # Re-add all items using the new hash function
        for key, value in zip(old_keys, old_buckets):
            if key is not None:
                self[key] = value
    
    # Clear Hashtable
    def clear(self):
        """
        The clear function resets the hash table, removing all key-value pairs and setting the count of items back to 0.
        
        :param self: Refer to the instance of the class
        :return: Nothing
        """
        self._keys = [None] * self.size
        self._buckets = [None] * self.size
        self.count = 0
        
    # Add Item into Hashtable
    def __setitem__(self, key, value):
        """
        The __setitem__ function is used to set a value in the Hashtable.
        It takes two parameters, the key and value. The key is hashed using the hash function, 
        and then stored in that bucket with its corresponding value.
        
        :param self: Refer to the instance of the class
        :param key: Key to be stored in hash table
        :param value: Value to be stored in hash table
        :return: Nothing
        """
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
            if self._buckets[index] is None:
                self._buckets[index] = value
                self._keys[index] = key
                self.count += 1
                break
            else:
                # If it is not empty and has the same key, overwrite it
                if self._keys[index] == key:
                    self._buckets[index] = value
                    break
                # Else, rehash and try to store in a new bucket
                else: 
                    index = self._rehash_function(index)
                    # Safeguard against an infinite loop if for some reason there are no buckets, which should not happen with resizing
                    if index == startIndex:
                        break

    # Get item from Hashtable
    def __getitem__(self,key):
        """
        The __getitem__ function is a special function that allows us to use the [] operator on our HashTable object.
        This function takes in a key and returns the value associated with that key if it exists, otherwise it returns None.
        
        :param self: Refer to the instance of the class
        :param key: Find the index of the bucket that contains our value associated with the key
        :return: The value associated with the key
        """
        # Use the hash function to calculate the index where the key should be stored.
        index = self._hash_function(key)
        start_index = index
        # Loop until we find an empty bucket or have scanned the entire table
        while self._keys[index] is not None:
            if self._keys[index] == key:
                # Key found, return the corresponding value
                return self._buckets[index]
            # Move to the next index
            index = self._rehash_function(index)
            # Check if we have scanned the entire table
            if index == start_index:
                break
        # If the key is not found return None
        return None
    
    # Check if key in Hashtable
    def __contains__(self, key):
        """
        The __contains__ function checks if a key is in the hash table.
        It does this by using the _hash_funciton to find where it should be, and then checking that location for the key.
        If it's not there, we use our rehash function to check other locations until we either find what we're looking for or return False.
        
        :param self: Refer to the instance of the class
        :param key: Check if the key is in the hash table
        :return: True if the key is found, and False otherwise
        """
        index = self._hash_function(key)
        start_index = index
        while self._keys[index] is not None:
            if self._keys[index] == key:
                return True
            index = self._rehash_function(index)
            if index == start_index:
                break
        return False
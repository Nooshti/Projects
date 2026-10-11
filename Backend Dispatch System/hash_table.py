import math
import csv
from linked_list import *

class DSAHashEntry: # a slot in hash table contains the following
    def __init__(self, key="", type_record = "", name="", location="", status=None):
        self.key = key
        self.type_record = type_record
        self.name = name
        self.location = location
        self.status = status    # for passenger - membership tier and for driver - Availability status


class DSAHashTable:
    def __init__(self, size):
        self.actual_size = self._find_next_prime(size)   # gives a prime number for array size
        self.hash_array = [DSALinkedList() for i in range(self.actual_size)]
        self.count = 0


    def get(self, key): # returns entire entry
        key = str(key)
        hash_idx = self._hash(key)
        message = " "
        found = False

        chain = self.hash_array[hash_idx]
        curr_node = chain.head
        while curr_node is not None and found == False:
            entry = curr_node.getValue()
            if entry.key == key:
                message = f"GOT ENTRY: {entry.key}  {entry.type_record} {entry.name}   {entry.location} {entry.status}"
                found = True
            curr_node = curr_node.getNext()

        if not found:
            message = "Key not found"

        return message

    def has_key(self, key): # check if we have the key (gives True/False)
        hash_idx = self._hash(key)
        found = False
        key = str(key)
        chain = self.hash_array[hash_idx]
        curr_node = chain.head
        while curr_node is not None and found == False:
            entry = curr_node.getValue()
            if entry.key == key:
                found = True
            curr_node = curr_node.getNext()

        return found

    def _find_next_prime(self, start_val):  # converts number into prime number
        is_prime = False

        if (start_val % 2 == 0):
            prime_val = start_val - 1
        else:
            prime_val = start_val

        while (not is_prime):
            prime_val = prime_val + 2
            i = 3
            is_prime = True
            root_val = int(math.sqrt(prime_val))
            while (i <= root_val) and (is_prime):
                if prime_val % i == 0:
                    is_prime = False
                else:
                    i = i + 2
        return prime_val

    
    def _hash(self, key):  # converts a string into an index
        a = 19
        hashing = 0
        key = str(key)
        for char in key:
            hashing = (hashing * a) + ord(char)
            
        hash_index =  hashing % len(self.hash_array) 
        return hash_index
    
    def put(self, key, type_record, name, location, status):  # put a record in the table

        status = str(status)
        places = ["Church", "Harbor", "Mall", "Park", "School", "Suburbs", "Supermarket", "University", "Zoo", "Bookstore", "Cinema"]

        passenger_status = ["1", "2", "3", "4", "5"]
        driver_status = ["Available", "Busy", "Offline"]
        key_length = str(key)
        if len(key_length) != 8: # checks if key is of proper length
            raise Exception(f"The Key does not have proper length.")

        if not isinstance(name, str):
            raise Exception("Enter name using correct datatype")

        if type_record != "Passenger" and type_record != "Driver":
            raise Exception("Wrong record type")

        if location not in places:
            raise Exception("Location not available in this area")

        if type_record == "Passenger":
            if status not in passenger_status:
                raise Exception("Incorrect Passenger Status")

        if type_record == "Driver":
            if status not in driver_status:
                raise Exception("Incorrect Driver Status")

        hashed_idx = 0
        hashed_idx = self._hash(key)
        chain = self.hash_array[hashed_idx]
        curr_node = chain.head
        key = str(key)

        while curr_node is not None:    # traverse the chain of slot at hashed_idx
            entry = curr_node.getValue()
            if entry.key == key:  # if key already exists at this index, update value
                entry.type_record = type_record
                entry.name = name
                entry.location = location
                entry.status = status
                print(f"\nUPDATED at index {hashed_idx}\nNew Entry: {key}  {type_record}   {name}  {location}  {status}\n")
                return  # exit after not inserting a new entry

            curr_node = curr_node.getNext() # continues to check other nodes in chain if node not found

        # if collision happens
        # if key not found inside the chain, create a new hash table entry
        if chain.head is not None:
            print(f"\nCOLLISION at index {hashed_idx}\nNew Entry: {key}  {type_record}   {name}  {location}  {status}\n")

        new_entry = DSAHashEntry(key, type_record, name, location, status)  # a node in the chain
        print(f"\nINSERTION at index {hashed_idx}\nNew Entry: {key}  {type_record}   {name}  {location}  {status}\n")
        chain.insertFirst(new_entry)
        self.count += 1  # increment num of filled slots


        l_f = self.get_load_factor()
        if l_f > 0.7:
            new_size = 2 * self.actual_size
            self._resize(new_size)

    def _find(self, key):   # returns hash index if key found
        hashed_idx = 0
        hashed_idx = self._hash(key)
        chain = self.hash_array[hashed_idx]
        key = str(key)
        curr_node = chain.head
        while curr_node is not None:
            entry = curr_node.getValue()
            if entry.key == key and entry.state == 1:
                return hashed_idx
            curr_node = curr_node.getNext()
        
        return  -1   # return -1 to show key was not found
    
    def remove(self, key):  # deletes key

        found_remove_key = False
        remove_idx = self._hash(key)
        chain = self.hash_array[remove_idx]
        key = str(key)
        curr_node = chain.head

        # if key is found, remove it
        while curr_node is not None:
            entry = curr_node.getValue()
            if entry.key == key:
                print(f"Deleted entry at index {remove_idx}: {entry.key}  {entry.type_record}   {entry.name}  {entry.location}  {entry.status}")
                chain.remove(entry)
                self.count -= 1  # decrease num of slots filled in table
                found_remove_key = True
                return
            curr_node = curr_node.getNext()
        if not found_remove_key:
            print("Key not found")

        l_f = self.get_load_factor()
        if l_f < 0.3:
            new_size = self.actual_size // 2
            if new_size < 8:
                new_size = 8
            self._resize(new_size)
        return
    def get_load_factor(self):  # calculates the percentage of occupied space in hash table

        load_factor = self.count / self.actual_size # calculates load factor 
        return load_factor
    
    def _resize(self, new_size):
        prev_array = self.hash_array
        self.actual_size = self._find_next_prime(new_size)
        self.hash_array = [DSALinkedList() for i in range(self.actual_size)]
        self.count = 0
        for chain in prev_array:
            curr_node = chain.head
            while curr_node is not None:
                entry = curr_node.getValue()
                self.put(entry.key, entry.type_record, entry.name, entry.location, entry.status)
                curr_node = curr_node.getNext()


    def read_csv(self, csv_file):
        count_inserts = 0
        with open(csv_file, 'r') as f:
            csv_reader = csv.reader(f)
            for line in csv_reader:
                if len(line) >= 5:
                    key, type_record, name, location, status = line[0], line[1], line[2], line[3], line[4]
                    self.put(key, type_record, name, location, status)
                    count_inserts += 1
                    if count_inserts == 10:
                        lf = self.get_load_factor()
                        lf = round(lf*100, 2)
                        print(f"The load factor every 10 inserts is {lf}%")
                        count_inserts = 0
    def save_csv(self, csv_file):

        with open(csv_file, 'w') as f:
            hash_array = self.hash_array

            f.write(f"{'INDEX':<5}   {'RECORD TYPE':<15}   {'KEY':<15}   {'NAME':<20}   {'LOCATION':<20}  {'STATUS':<20}\n")
            for idx in range(len(hash_array)):
                chain = hash_array[idx]
                curr_node = chain.head
                if curr_node is None:
                    f.write(f"{idx:<5}   \n")
                else:
                    while curr_node is not None:
                        entry = curr_node.getValue()

                        f.write(f"{idx:<5}   "   f"{entry.type_record:<15}"   f"{entry.key:<15}   "   f"{entry.name:<20}   "   f"{entry.location:<20}   "   f"{entry.status:<20}\n")

                        curr_node = curr_node.getNext()












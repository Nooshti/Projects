import csv
class PickupRequest(): # class for pickup request (contains details of passenger)
    def __init__(self, id="", name="", location="", tier=None, driver_name="", pickup_time=None, driver_location="",driver_status=None, shortest_path=None):
        # passenger details
        self.id = id
        self.name = name
        self.location = location
        self.tier = tier
        # assigned driver details

        self.driver_name = driver_name
        self.pickup_time = pickup_time
        self.driver_location = driver_location
        self.driver_status = driver_status
        self.shortest_path = shortest_path
    def get_id(self):
        return self.id  # returns id of passenger

    def get_name(self):
        return self.name    # returns name

    def get_location(self):
        return self.location

    def get_tier(self):
        return self.tier    # membership tier = 1 - 5

    def get_driver_name(self):
        return self.driver_name

    def get_pickup_time(self):
        return self.pickup_time

    def get_driver_status(self):
        return self.driver_status

class DSAHeapEntry:
    def __init__(self, priority, pickup_request):    # stores one heap item
        self.priority = priority
        self.pickup_request = pickup_request #PickupRequest()

    def get_priority(self):
        return self.priority

    def get_pickup_request(self):
        return self.pickup_request


class DSAHeap:  # store heap
    def __init__(self, size):
        self.size = size
        self.heap = [None] * size
        self.count = 0

    def get_count(self):
        return self.count

    def set_priority(self, tier, pickup_time):  # calculates priority of passenger
        # tier - membership tier (1 - 5)
        # pickup_time - time taken for driver to go to pickup location from current driver location (uses djikstra)
        passenger_status = [1, 2, 3, 4, 5]
        if tier not in passenger_status:    # handle invalid membership tier
            raise Exception("Incorrect Passenger Membership Tier")

        if pickup_time <= 0:    # handle T (pickup_time)
            pickup_time = 1 # to prevent the Priority equation from crashing

        Priority = (6 - tier) + 1000 / pickup_time  # used for max heap
        Priority = round(Priority, 2)
        return Priority


    def heap_full(self):
        return self.count == self.size
    
    def heap_empty(self):
        return self.count == 0

    def add(self, priority, pickup_request): # inserts a heap item
        places = ["Church", "Harbor", "Mall", "Park", "School", "Suburbs", "Supermarket", "University", "Zoo", "Bookstore", "Cinema"]

        if self.heap_full():
            raise Exception("Heap is full")
        if len(pickup_request.id) != 8:  # checks if key is of proper length
            raise Exception(f"The Key does not have proper length.")

        if not isinstance(pickup_request.name, str):
            raise Exception("Enter name using correct datatype")

        if not isinstance(pickup_request.driver_name, str):
            raise Exception("Enter name using correct datatype")

        if pickup_request.location not in places or pickup_request.driver_location not in places:
            raise Exception("Location not available in this area")

        else:
            for p in range(self.count): # check if membership tier has changed
                slot = self.heap[p]
                slot_pickup = slot.get_pickup_request()
                if pickup_request.id == slot_pickup.id and pickup_request.tier != slot_pickup.tier:
                    # pickup request is updated if membership tier is changed
                    slot_pickup.location = pickup_request.location
                    slot_pickup.tier = pickup_request.tier
                    slot_pickup.pickup_time = pickup_request.pickup_time
                    slot_pickup.shortest_path = pickup_request.shortest_path
                    return
            curr_idx = self.count    # index given to new heap item
            self.heap[curr_idx] = DSAHeapEntry(priority, pickup_request) # insert heap item
            self.count += 1 # increment count of heap items by 1
            self.trickle_up(curr_idx)
            print(f"Inserted into Heap = Priority: {priority} - Pickup request: {pickup_request.id}\t{pickup_request.name}\t{pickup_request.location}\t{pickup_request.tier}")
            print(f"Assigned Driver: {pickup_request.driver_name}\tPickup time: {pickup_request.pickup_time} mins\tDriver Current Location: {pickup_request.driver_location}")
            print(f"Shortest Path from {pickup_request.driver_location} to {pickup_request.location} - {pickup_request.shortest_path}")
            self.display_heap()     # displays heap after every insertion
            print()

    def trickle_up(self, curr_idx):
        parent_idx = (curr_idx - 1) // 2 # get parent index
            
        while curr_idx > 0 and self.heap[curr_idx].get_priority() > self.heap[parent_idx].get_priority(): # continues looping if current index > 0 and added heap item > parent item
            temp = self.heap[parent_idx]
            self.heap[parent_idx] = self.heap[curr_idx] # added heap item takes place of parent item
            self.heap[curr_idx] = temp  # parent item takes place of added heap item 
            curr_idx = parent_idx   # continue comparing current heap item with its parent
            parent_idx = (curr_idx - 1) // 2 # get parent index


    def remove(self):
        if self.heap_empty():
            raise Exception("Heap is empty")
        else:
            remove_item = self.heap[0]
            last_item = self.heap[self.count-1]
            self.heap[0] = last_item
            self.heap[self.count - 1] = None
            self.count -= 1
            if self.count > 0:
                self.trickle_down(0)
            item = remove_item.get_pickup_request()
            print(f"Extracted from Heap = Priority: {remove_item.get_priority()} - Pickup request: {item.id}\t{item.name}\t{item.location}\t{item.tier}")
            print(f"Assigned Driver: {item.driver_name}\tPickup time: {item.pickup_time} mins\tDriver status: {item.driver_status}\tDriver Location: {item.driver_location}")
            print(f"Shortest Path from {item.driver_location} to {item.location} - {item.shortest_path}")
            self.display_heap()  # displays heap after every extraction
        return remove_item

    def peek(self): # peek at top item without removing it
        top_item = self.heap[0]
        return top_item.get_priority(), top_item.get_pickup_request()
            

    def trickle_down(self, curr_idx):
        left_child_idx = (curr_idx * 2) + 1
        right_child_idx = left_child_idx + 1
        keep_going = True

        while keep_going and left_child_idx < self.count:   # is a left child
            keep_going = False
            large_idx = left_child_idx
            if right_child_idx < self.count:    # is a right child
                if self.heap[left_child_idx].get_priority() < self.heap[right_child_idx].get_priority():
                    large_idx = right_child_idx # find largest child
            if self.heap[large_idx].get_priority() > self.heap[curr_idx].get_priority():
                temp = self.heap[curr_idx]
                self.heap[curr_idx] = self.heap[large_idx]
                self.heap[large_idx] = temp
                keep_going = True
            curr_idx = large_idx
            left_child_idx = (curr_idx * 2) + 1
            right_child_idx = left_child_idx + 1
        
        
    
    
    
    def display_heap(self):
        for i in range(self.count):
            priority = self.heap[i].get_priority()
            pickup_request = self.heap[i].get_pickup_request()
            print(f"Priority: {priority} - Pickup request: {pickup_request.id} {pickup_request.name} {pickup_request.location} {pickup_request.tier}")


    def heapify(self):  # imports a random heap array   # to make it a max heap
        # start from last parent node
        for i in range(((self.count//2)-1), -1, -1):
            self.trickle_down(i)

        return self.heap    # exports the heap array

    def swap(self): # swaps last element with first element
        temp = self.heap[self.count - 1]
        self.heap[self.count - 1] = self.heap[0]
        self.heap[0] = temp

    def heap_sort(self):    # sorts the heap
        self.heapify()  # turn array into max heap
        original_count = self.count
        while self.count > 1:   # moves largest heap item to the end
            self.swap() # move max item to end
            self.count -= 1 # deducts a heap item
            self.trickle_down(0)

        self.count = original_count

    
    def read_csv(self, csv_file):   # reads csv file
        with open(csv_file, 'r') as f:
            csv_reader = csv.reader(f)
            for line in csv_reader:
                if len(line) >= 2:
                    priority, pickup_request = line[0], line[1]
                    priority = int(priority)
                    
                    self.add(priority, pickup_request)   # add each priority, value as a heap item
        self.heap_sort()    # sort the heap array
    
    def save_csv(self, csv_file):   # displays all heap items inside a csv file
        with open(csv_file, 'w') as f:
            f.write(f"{'PRIORITY':<12}    {'VALUE':<30}\n")
            for slot in range(self.count):
                
                priority = self.heap[slot].get_priority()
                value = self.heap[slot].get_pickup_request()
                
                f.write(f"{priority:<12}    {value:<30}\n")

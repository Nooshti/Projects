from max_heap import *
from graph import *
from hash_table import *
# 12 inserts and 12 extractions
# shows that peek was implemented
# shows that if membership tier has changed, pickup request is updated inside heap (check 1st 2 lines of passenger.csv)
# if once driver is assigned to a passenger, they become busy
# heap printed after every insertion and extraction
# computes priority
try:# shows 12 insertions and extractions
    graph = DSAGraph()
    table_passenger = DSAHashTable(50)
    table_driver = DSAHashTable(50)
    heap = DSAHeap(90)
    p_table = table_passenger.hash_array    # hash array for passengers
    d_table = table_driver.hash_array   # hash array for drivers

    graph.add_vertex("Bookstore")
    graph.add_vertex("Cinema")
    graph.add_vertex("Mall")
    graph.add_vertex("Suburbs")
    graph.add_vertex("Park")
    graph.add_vertex("School")
    graph.add_vertex("Supermarket")
    graph.add_vertex("University")
    graph.add_vertex("Church")
    graph.add_vertex("Zoo")
    graph.add_vertex("Harbor")
    graph.sort()    # sorts vertices
    graph.sort_adjacent()   # sorts neighbours of each vertex
    graph.add_edge("Bookstore", "Cinema", weight=9)
    graph.add_edge("Cinema", "Park", weight=5)
    graph.add_edge("Suburbs", "Church", weight=25)
    graph.add_edge("Suburbs", "Zoo", weight=11)
    graph.add_edge("Suburbs", "School", weight=7)
    graph.add_edge("School", "Park", weight=30)
    graph.add_edge("University", "Mall", weight=8)
    graph.add_edge("Supermarket", "School", weight=17)
    graph.add_edge("Suburbs", "Supermarket", weight=16)  # cycle
    graph.add_edge("Mall", "Park", weight=24)
    graph.add_edge("University", "Park", weight=19)
    graph.add_edge("School", "Zoo", weight=22)
    print("*" * 80)
    print("Module 3: Heap-Based Pickup Scheduling Test")
    print("*" * 80)
    table_passenger.read_csv("passengers.csv")  # reads passenger records
    # saves the processed records which now have a hash key
    table_passenger.save_csv("passenger_hash_table.csv")
    table_driver.read_csv("drivers.csv")  # reads driver records
    # saves the processed records which now have a hash key
    table_driver.save_csv("driver_hash_table.csv")


    for i in range(len(p_table)):   # iterating through all slots in passenger hash array
        chain_p = p_table[i]
        short_path = None
        chosen_driver = None    # initialised to None. chosen_driver meant to contain driver details
        best_T = float("inf")  # best (minimum) pickup time initialised to infinity
        curr_node = chain_p.head    # access linked list inside slot
        while curr_node is not None:
            entry_p = curr_node.getValue()  # gets passenger entry (DSAHashEntry)
            for j in range(len(d_table)):   # iterating through every driver record in driver hash array
                chain_d = d_table[j]
                current_node = chain_d.head # access linked list inside slot
                while current_node is not None:
                    entry_d = current_node.getValue()   # gets driver entry (DSAHashEntry)

                    if entry_d.status == "Available":
                        path, T = graph.dijkstra(entry_d.location, entry_p.location)
                        if T < best_T:  # if T (pickup time) < best_T (minimum pickup time till now)
                            chosen_driver = entry_d
                            short_path = path
                            best_T = T # if T (pickup time) < best_T

                    current_node = current_node.getNext()

            if chosen_driver is None:
                print(f"Request from {entry_p.name} has been rejected due to unavailable drivers")

            elif chosen_driver.status == "Available":
                priority = heap.set_priority(int(entry_p.status), best_T)   # calculate priority using formula found inside set_priority
                chosen_driver.status = "Busy"

                pickup = PickupRequest(entry_p.key, entry_p.name, entry_p.location, entry_p.status, chosen_driver.name, best_T, chosen_driver.location, chosen_driver.status, short_path) # object containing all passenger details
                heap.add(priority, pickup)  # add pickup request on heap
            curr_node = curr_node.getNext()

    pri, pick_up = heap.peek()
    # shows which pickup request is on top of heap
    print(f"\nItem on top of heap: {pri} - Pickup request: {pick_up.id}\t{pick_up.name}\t{pick_up.location}\t{pick_up.tier}\nAssigned Driver: {pick_up.driver_name}\tPickup time: {pick_up.pickup_time} mins\tDriver status: {pick_up.driver_status}\tDriver Location: {pick_up.driver_location}")

    for h in range(heap.count): # iterate through heap to extract all pickup requests
        print()
        print(f"Count - {h}")
        heap.remove()   # extract pickup request from heap
    graph.display_visually()

except Exception as err:
     print(err)
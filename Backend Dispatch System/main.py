from graph import *
from hash_table import *
from max_heap import *
from advanced_sorting import *


try:
    # Module 1: Graph-Based Route Planning
    graph = DSAGraph()
    sort = sorting()    # contains mergesort and quicksort
    driver_records = DSAHashTable(90)
    passenger_records = DSAHashTable(90)
    heap = DSAHeap(90)
    p_table = passenger_records.hash_array
    d_table = driver_records.hash_array
    unsorted_list = []
    list_ascending = []
    count_rejected = 0  # stores count of rejected request

    print("*" * 80)
    print("Module 1: Graph-Based Route Planning")
    print("*" * 80)
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
    print("Module 2: Hash-Based Passenger and Driver Lookup")
    print("*" * 80)
    passenger_records.read_csv("passengers.csv")  # reads passenger records
    # saves the processed records which now have a hash key
    passenger_records.save_csv("passenger_hash_table.csv")
    driver_records.read_csv("drivers.csv")  # reads driver records
    # saves the processed records which now have a hash key
    driver_records.save_csv("driver_hash_table.csv")

    print("*" * 80)
    print("Module 4: Sorting Pickup Requests ")
    print("*" * 80)

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
                count_rejected += 1
            elif chosen_driver.status == "Available":
                priority = heap.set_priority(int(entry_p.status), best_T)   # calculate priority using formula found inside set_priority
                chosen_driver.status = "Busy"

                pickup = PickupRequest(entry_p.key, entry_p.name, entry_p.location, entry_p.status, chosen_driver.name, best_T, chosen_driver.location, chosen_driver.status, short_path) # object containing all passenger details
                unsorted_list = unsorted_list + [(priority, pickup)]    # gets unsorted list of 100 pickup request objects
            curr_node = curr_node.getNext()


    sorted_list = sort.mergeSort(unsorted_list)  # sorts list of pickup request objects

    print()
    print("*" * 80)
    print("Module 3: Heap-Based Pickup Scheduling")
    print("*" * 80)
    for b in range(len(sorted_list)):    # once pickup time sorted, add to heap
        x, y = sorted_list[b]   # x = priority and y is the pickup request
        heap.add(x, y)  # add to heap

    for r in range(5):  # dispatch drivers (extract pickup requests)
        print()
        heap.remove()

    pri, pick_up = heap.peek()
    # shows which pickup request is on top of heap
    print(f"\nItem on top of heap: {pri} - Pickup request: {pick_up.id}\t{pick_up.name}\t{pick_up.location}\t{pick_up.tier}\nAssigned Driver: {pick_up.driver_name}\tPickup time: {pick_up.pickup_time} mins\tDriver status: {pick_up.driver_status}\tDriver Location: {pick_up.driver_location}")

    print(f"\nCount of rejected requests: {count_rejected}")
    print(f"Count of accepted requests: {passenger_records.count - count_rejected}")
    graph.display_visually()
except Exception as err:
    print(err)
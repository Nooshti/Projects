import timeit

from advanced_sorting import *
from max_heap import *
from graph import *
from hash_table import *
from conditions_module4 import *
# used top down merge sort and median of 3 quick sort
# generated datasets of 100, 500 and 1000 pickup requests after computing priority and estimated pickup time
# shows timing table at the end
# short written reflection after Merge Sort and Quick Sort are used for all datasets
try:
    sort = sorting()
    conditions = Test_conditions()
    graph = DSAGraph()
    table_passenger = DSAHashTable(4000)
    table_driver_100 = DSAHashTable(4000)
    table_driver_500 = DSAHashTable(4000)
    table_driver_1000 = DSAHashTable(4000)
    heap = DSAHeap(1500)
    p_table = table_passenger.hash_array    # hash array for passengers
    d_table_100 = table_driver_100.hash_array   # hash array for drivers (dataset of 100 pickup requests)
    d_table_500 = table_driver_500.hash_array   # hash array for drivers (dataset of 500 pickup requests)
    d_table_1000 = table_driver_1000.hash_array   # hash array for drivers (dataset of 1000 pickup requests)
    unsorted_list_100 = []
    unsorted_list_500 = []
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
    print("Module 4:  Sorting Pickup Requests")
    print("*" * 80)
    table_passenger.read_csv("2000Pickup(module4).csv")  # reads passenger records
    # saves the processed records which now have a hash key
    table_passenger.save_csv("passenger_hash_table.csv")
    table_driver_100.read_csv("module4_driver_records.csv")  # reads driver records
    table_driver_500.read_csv("module4_driver_records.csv")  # reads driver records
    table_driver_1000.read_csv("module4_driver_records.csv")  # reads driver records
    list_100 = []
    list_100_ascending = []
    list_100_reverse = []
    list_100_random = []
    list_100_nearly_sorted = []

    list_500_ascending = []
    list_500_reverse = []
    list_500_random = []
    list_500_nearly_sorted = []

    list_1000_ascending = []
    list_1000_reverse = []
    list_1000_random = []
    list_1000_nearly_sorted = []
    min_100_ms = " "
    max_100_ms = " "
    min_100_qs = " "
    max_100_qs = " "
    min_500_ms = " "
    max_500_ms = " "
    min_500_qs = " "
    max_500_qs = " "

    print("*" * 80)
    print("Sorting of 100 Pickup Requests")
    print("*" * 80)
    # p_table
    # 100 datasets
    for i in range(219):   # iterating through 219 slots in passenger hash array
        chain_p = p_table[i]
        short_path = None
        chosen_driver = None    # initialised to None. chosen_driver meant to contain driver details
        best_T = float("inf")  # best (minimum) pickup time initialised to infinity
        curr_node = chain_p.head    # access linked list inside slot
        while curr_node is not None:
            entry_p = curr_node.getValue()  # gets passenger entry (DSAHashEntry)
            # d_table
            for j in range(365):   # iterating through only 365 driver record in driver hash array
                chain_d = d_table_100[j]
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

                unsorted_list_100 = unsorted_list_100 + [(priority, pickup)]    # gets unsorted list of 100 pickup request objects
            curr_node = curr_node.getNext()


    sorted_object_100 = sort.mergeSort(unsorted_list_100) # sorts list of 100 pickup request objects
    for i in range(len(sorted_object_100)): # gets a list of 100 pickup requests in ascending order
        a, b = sorted_object_100[i]
        # adds only passenger name with estimated pickup time to list
        list_100_ascending = list_100_ascending + [(b.name, b.pickup_time)] # gets a list of 100 pickup requests in ascending order

    print()

    list_100_random = conditions.randomise_list(list_100_ascending) # get random list of 100 pickup requests
    list_100_nearly_sorted = conditions.nearly_sorted(list_100_ascending)   # get nearly sorted list of 100 pickup requests
    list_100_reverse = conditions.reverse_list(list_100_ascending)  # get reversed list of 100 pickup requests
    print("Test List of 100 pickup requests in random order")
    print(list_100_random)
    print()
    print("Test List of 100 pickup requests in nearly sorted order")
    print(list_100_nearly_sorted)
    print()
    print("Test List of 100 pickup requests in reversed order")
    print(list_100_reverse)
    print()
    ########## measure time taken to sort 100 random pickup requests using MergeSort
    start_ms_100_random = timeit.default_timer()
    ms_100_random = sort.mergeSort_list(list_100_random)
    end_ms_100_random = timeit.default_timer()
    duration_ms_100_random = end_ms_100_random - start_ms_100_random

    print("*" * 80)
    print("Sorting of 100 Random Pickup Requests using Mergesort")
    print("*" * 80)
     # prints a list of 100 sorted pickup requests
    print("Note: The first names are not the same for the different test scenarios as the lists are sorted using only the pickup times not the names.")
    print()
    print(ms_100_random)

    print(f"Duration taken by mergesort to sort 100 pickup requests in random order: {duration_ms_100_random:.6f} seconds")
    print()

    # measure time taken to sort 100 nearly sorted pickup requests using MergeSort
    start_ms_100_nearly_sorted = timeit.default_timer()
    ms_100_nearly_sorted = sort.mergeSort_list(list_100_nearly_sorted)
    end_ms_100_nearly_sorted = timeit.default_timer()
    duration_ms_100_nearly_sorted = end_ms_100_nearly_sorted - start_ms_100_nearly_sorted

    print("*" * 80)
    print("Sorting of 100 Nearly Sorted Pickup Requests using Mergesort")
    print("*" * 80)
    print()
    print(ms_100_nearly_sorted) # passenger name - pickup time

    print(f"Duration taken by mergesort to sort 100 pickup requests in nearly sorted order: {duration_ms_100_nearly_sorted:.6f} seconds")
    print()

    # measure time taken to sort 100 reversed pickup requests using MergeSort
    start_ms_100_reverse = timeit.default_timer()
    ms_100_reverse = sort.mergeSort_list(list_100_reverse)
    end_ms_100_reverse = timeit.default_timer()
    duration_ms_100_reverse = end_ms_100_reverse - start_ms_100_reverse

    print("*" * 80)
    print("Sorting of 100 Reversed Pickup Requests using Mergesort")
    print("*" * 80)
    print()
    print(ms_100_reverse) # passenger name - pickup time

    print(f"Duration taken by mergesort to sort 100 pickup requests in reverse order: {duration_ms_100_reverse:.6f} seconds")
    print()

    print("The Top Down MergeSort algorithm Reflection for different scenarios of 100 pickup request: ")
    print(f"Duration to sort 100 pickup requests in random order: {duration_ms_100_random:.6f} seconds")
    print(f"Duration to sort 100 pickup requests in nearly sorted order: {duration_ms_100_nearly_sorted:.6f} seconds")
    print(f"Duration to sort 100 pickup requests in reverse order: {duration_ms_100_reverse:.6f} seconds")
    duration_100 = [duration_ms_100_random, duration_ms_100_nearly_sorted, duration_ms_100_reverse]
    sorted_dur_100 = sort.bubbleSort(duration_100)
    max_100_ms_time = sorted_dur_100[2]
    min_100_ms_time = sorted_dur_100[0]
    # compares the time taken by MergeSort to sort each test list
    if max_100_ms_time == duration_ms_100_random:
        max_100_ms = "random"
    elif max_100_ms_time == duration_ms_100_reverse:
        max_100_ms = "reverse"
    elif max_100_ms_time == duration_ms_100_nearly_sorted:
        max_100_ms = "nearly_sorted"

    if min_100_ms_time == duration_ms_100_random:
        min_100_ms = "random"
    elif min_100_ms_time == duration_ms_100_reverse:
        min_100_ms = "reverse"
    elif min_100_ms_time == duration_ms_100_nearly_sorted:
        min_100_ms = "nearly_sorted"

    # Reflection message
    print(f"""\nLooking at the durations for each scenario of 100 pickup request, MergeSort takes less time to 
    sort the {min_100_ms} list while more time is taken to sort the {max_100_ms} list""")

    print("Its time complexity is O(n log n) and its space complexity is O(n) as it needs temporary lists to enable merging.\n")


    print("*" * 80)
    print("Sorting of 100 Pickup Requests using Quicksort")
    print("*" * 80)
    ########### measure time taken to sort 100 random pickup requests using QUICKSORT
    print()
    print("*" * 80)
    print("Sorting of 100 Random Pickup Requests using Quicksort")
    print("*" * 80)

    start_qs_100_random = timeit.default_timer()
    qs_100_random = sort.QuickSortMedian3_list(list_100_random) # # sorts random list
    end_qs_100_random = timeit.default_timer()
    duration_qs_100_random = end_qs_100_random - start_qs_100_random

    print("Note: The first names are not the same for the different test scenarios as the lists are sorted using only the pickup times not the names.")
    print()
    print(qs_100_random) # passenger name - pickup time

    print()

    print(f"Duration taken by QuickSort to sort 100 pickup requests in random order: {duration_qs_100_random:.6f} seconds")
    print()

    print("*" * 80)
    print("Sorting of 100 Nearly Sorted Pickup Requests using Quicksort")
    print("*" * 80)
    # measure time taken to sort 100 nearly sorted pickup requests using QuickSort
    start_qs_100_nearly_sorted = timeit.default_timer()
    qs_100_nearly_sorted = sort.QuickSortMedian3_list(list_100_nearly_sorted)   # sorts nearly sorted list
    end_qs_100_nearly_sorted = timeit.default_timer()
    duration_qs_100_nearly_sorted = end_qs_100_nearly_sorted - start_qs_100_nearly_sorted

    print()
    print(qs_100_nearly_sorted) # passenger name - pickup time

    print(f"Duration taken by QuickSort to sort 100 pickup requests in nearly sorted order: {duration_qs_100_nearly_sorted:.6f} seconds")
    print()

    print("*" * 80)
    print("Sorting of 100 Reverse Pickup Requests using Quicksort")
    print("*" * 80)
    # measure time taken to sort 100 reversed pickup requests using QuickSort
    start_qs_100_reverse = timeit.default_timer()
    qs_100_reverse = sort.QuickSortMedian3_list(list_100_reverse)   # sorts reverse list
    end_qs_100_reverse = timeit.default_timer()
    duration_qs_100_reverse = end_qs_100_reverse - start_qs_100_reverse

    print()
    print(qs_100_reverse) # passenger name - pickup time

    print()

    print(f"Duration taken by QuickSort to sort 100 pickup requests in reverse order: {duration_qs_100_reverse:.6f} seconds")
    print()

    print("The Median of 3 QuickSort algorithm Reflection for different scenarios for 100 pickup requests: ")
    print(f"Duration to sort 100 pickup requests in random order: {duration_qs_100_random:.6f} seconds")
    print(f"Duration to sort 100 pickup requests in nearly sorted order: {duration_qs_100_nearly_sorted:.6f} seconds")
    print(f"Duration to sort 100 pickup requests in reverse order: {duration_qs_100_reverse:.6f} seconds")
    duration_100 = [duration_qs_100_random, duration_qs_100_nearly_sorted, duration_qs_100_reverse]
    sorted_dur_100 = sort.bubbleSort(duration_100)
    max_100_qs_time = sorted_dur_100[2]
    min_100_qs_time = sorted_dur_100[0]
    if max_100_qs_time == duration_qs_100_random:
        max_100_qs = "random"
    elif max_100_qs_time == duration_qs_100_reverse:
        max_100_qs = "reverse"
    elif max_100_qs_time == duration_qs_100_nearly_sorted:
        max_100_qs = "nearly_sorted"

    if min_100_qs_time == duration_qs_100_random:
        min_100_qs = "random"
    elif min_100_qs_time == duration_qs_100_reverse:
        min_100_qs = "reverse"
    elif min_100_qs_time == duration_qs_100_nearly_sorted:
        min_100_qs = "nearly_sorted"


    print(f"""\nLooking at the durations for each scenario of 100 pickup request, QuickSort Median of 3 takes less time to 
    sort the {min_100_qs} list while more time is taken to sort the {max_100_qs} list""")
    print("Its time complexity is O(n log n) and its space complexity is Olog(n).")


    # p_table
    ####################### 500 datasets
    print("*" * 80)
    print("Sorting of 500 Pickup Requests")
    print("*" * 80)
    for i in range(1949):   # iterating through 1949 slots in passenger hash array
        chain_p = p_table[i]
        short_path = None
        chosen_driver = None    # initialised to None. chosen_driver meant to contain driver details
        best_T = float("inf")  # best (minimum) pickup time initialised to infinity
        curr_node = chain_p.head    # access linked list inside slot
        while curr_node is not None:
            entry_p = curr_node.getValue()  # gets passenger entry (DSAHashEntry)
            # d_table
            for j in range(1870):   # iterating through only 1870 driver record in driver hash array
                chain_d = d_table_500[j]
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

                unsorted_list_500 = unsorted_list_500 + [(priority, pickup)]    # gets unsorted list of 500 pickup request objects
            curr_node = curr_node.getNext()


    sorted_object_500 = sort.QuickSortMedian3(unsorted_list_500) # sorts unsorted list of 500 request objects
    for i in range(len(sorted_object_500)):
        a, b = sorted_object_500[i]
        # adds only passenger name with estimated pickup time to list
        list_500_ascending = list_500_ascending + [(b.name, b.pickup_time)]  # gets a list of 500 pickup requests in ascending order
    print()

    list_500_random = conditions.randomise_list(list_500_ascending) # get random list of 500 pickup requests
    list_500_nearly_sorted = conditions.nearly_sorted(list_500_ascending)   # get nearly sorted list of 500 pickup requests
    list_500_reverse = conditions.reverse_list(list_500_ascending)  # get reversed list of 500 pickup requests

    print("Test List of 500 pickup requests in random order")
    print(list_500_random)
    print()
    print("Test List of 500 pickup requests in nearly sorted order")
    print(list_500_nearly_sorted)
    print()
    print("Test List of 500 pickup requests in reversed order")
    print(list_500_reverse)
    print()
    ########## measure time taken to sort 500 random pickup requests using MergeSort
    start_ms_500_random = timeit.default_timer()
    ms_500_random = sort.mergeSort_list(list_500_random)
    end_ms_500_random = timeit.default_timer()
    duration_ms_500_random = end_ms_500_random - start_ms_500_random
    print()
    print("*" * 80)
    print("Sorting of 500 random Pickup Requests")
    print("*" * 80)
    print()
    print("Note: The first names are not the same for the different test scenarios as the lists are sorted using only the pickup times not the names.")
    print()
    print(ms_500_random) # passenger name - pickup time
    print()
    print(f"Duration taken by mergesort to sort 500 pickup requests in random order: {duration_ms_500_random:.6f} seconds")
    print()

    # measure time taken to sort 500 nearly sorted pickup requests using MergeSort
    start_ms_500_nearly_sorted = timeit.default_timer()
    ms_500_nearly_sorted = sort.mergeSort_list(list_500_nearly_sorted)
    end_ms_500_nearly_sorted = timeit.default_timer()
    duration_ms_500_nearly_sorted = end_ms_500_nearly_sorted - start_ms_500_nearly_sorted

    print()
    print("*" * 80)
    print("Sorting of 500 nearly sorted Pickup Requests")
    print("*" * 80)
    print(ms_500_nearly_sorted) # passenger name - pickup time
    print()

    print(f"Duration taken by mergesort to sort 500 pickup requests in nearly sorted order: {duration_ms_500_nearly_sorted:.6f} seconds")
    print()

    # measure time taken to sort 100 reversed pickup requests using MergeSort
    start_ms_500_reverse = timeit.default_timer()
    ms_500_reverse = sort.mergeSort_list(list_500_reverse)
    end_ms_500_reverse = timeit.default_timer()
    duration_ms_500_reverse = end_ms_500_reverse - start_ms_500_reverse

    print()
    print("*" * 80)
    print("Sorting of 500 reversed Pickup Requests")
    print("*" * 80)
    print(ms_500_reverse) # passenger name - pickup time
    print()

    print(f"Duration taken by mergesort to sort 500 pickup requests in reverse order: {duration_ms_500_reverse:.6f} seconds")
    print()
    min_500_ms = " "
    max_500_ms = " "
    print("The Top Down MergeSort algorithm Reflection for different scenarios of 500 pickup request: ")
    print(f"Duration to sort 500 pickup requests in random order: {duration_ms_500_random:.6f} seconds")
    print(f"Duration to sort 500 pickup requests in nearly sorted order: {duration_ms_500_nearly_sorted:.6f} seconds")
    print(f"Duration to sort 500 pickup requests in reverse order: {duration_ms_500_reverse:.6f} seconds")
    duration_500 = [duration_ms_500_random, duration_ms_500_nearly_sorted, duration_ms_500_reverse]
    sorted_dur_500 = sort.bubbleSort(duration_500)
    max_500_ms_time = sorted_dur_500[2]
    min_500_ms_time = sorted_dur_500[0]
    if max_500_ms_time == duration_ms_500_random:
        max_500_ms = "random"
    elif max_500_ms_time == duration_ms_500_reverse:
        max_500_ms = "reverse"
    elif max_500_ms_time == duration_ms_500_nearly_sorted:
        max_500_ms = "nearly_sorted"

    if min_500_ms_time == duration_ms_500_random:
        min_500_ms = "random"
    elif min_500_ms_time == duration_ms_500_reverse:
        min_500_ms = "reverse"
    elif min_500_ms_time == duration_ms_500_nearly_sorted:
        min_500_ms = "nearly_sorted"

    print(f"""\nLooking at the durations for each scenario of 500 pickup request, MergeSort takes less time to 
    sort the {min_500_ms} list while more time is taken to sort the {max_500_ms} list""")
    print("Its time complexity is O(n log n) and its space complexity is O(n) as it needs temporary lists to enable merging.")



    ########### measure time taken to sort 500 random pickup requests using QUICKSORT
    start_qs_500_random = timeit.default_timer()
    qs_500_random = sort.QuickSortMedian3_list(list_500_random)  # sorts random list
    end_qs_500_random = timeit.default_timer()
    duration_qs_500_random = end_qs_500_random - start_qs_500_random

    print()
    print("*" * 80)
    print("Sorting of 500 random Pickup Requests")
    print("*" * 80)
    print()
    print("Note: The first names are not the same for the different test scenarios as the lists are sorted using only the pickup times not the names.")
    print()
    print(qs_500_random) # passenger name - pickup time
    print()

    print(f"Duration taken by QuickSort to sort 500 pickup requests in random order: {duration_qs_500_random:.6f} seconds")
    print()

    # measure time taken to sort 500 nearly sorted pickup requests using QuickSort
    start_qs_500_nearly_sorted = timeit.default_timer()
    qs_500_nearly_sorted = sort.QuickSortMedian3_list(list_500_nearly_sorted)   # sorts nearly sorted list
    end_qs_500_nearly_sorted = timeit.default_timer()
    duration_qs_500_nearly_sorted = end_qs_500_nearly_sorted - start_qs_500_nearly_sorted
    print()
    print("*" * 80)
    print("Sorting of 500 nearly sorted Pickup Requests")
    print("*" * 80)
    print(qs_500_nearly_sorted) # passenger name - pickup time
    print()

    print(f"Duration taken by QuickSort to sort 500 pickup requests in nearly sorted order: {duration_qs_500_nearly_sorted:.6f} seconds")
    print()

    # measure time taken to sort 500 reversed pickup requests using QuickSort
    start_qs_500_reverse = timeit.default_timer()
    qs_500_reverse = sort.QuickSortMedian3_list(list_500_reverse)   # sorts reverse list
    end_qs_500_reverse = timeit.default_timer()
    duration_qs_500_reverse = end_qs_500_reverse - start_qs_500_reverse


    print()
    print("*" * 80)
    print("Sorting of 500 reversed Pickup Requests")
    print("*" * 80)
    print(qs_500_reverse) # passenger name - pickup time
    print()

    print(f"Duration taken by QuickSort to sort 500 pickup requests in reverse order: {duration_qs_500_reverse:.6f} seconds")
    print()

    print("The Median of 3 QuickSort algorithm Reflection for different scenarios of 500 pickup requests: ")
    print(f"Duration to sort 500 pickup requests in random order: {duration_qs_500_random:.6f} seconds")
    print(f"Duration to sort 500 pickup requests in nearly sorted order: {duration_qs_500_nearly_sorted:.6f} seconds")
    print(f"Duration to sort 500 pickup requests in reverse order: {duration_qs_500_reverse:.6f} seconds")
    duration_500 = [duration_qs_500_random, duration_qs_500_nearly_sorted, duration_qs_500_reverse]
    sorted_dur_500 = sort.bubbleSort(duration_500)
    max_500_qs_time = sorted_dur_500[2]
    min_500_qs_time = sorted_dur_500[0]
    if max_500_qs_time == duration_qs_500_random:
        max_500_qs = "random"
    elif max_500_qs_time == duration_qs_500_reverse:
        max_500_qs = "reverse"
    elif max_500_qs_time == duration_qs_500_nearly_sorted:
        max_500_qs = "nearly_sorted"

    if min_500_qs_time == duration_qs_500_random:
        min_500_qs = "random"
    elif min_500_qs_time == duration_qs_500_reverse:
        min_500_qs = "reverse"
    elif min_500_qs_time == duration_qs_500_nearly_sorted:
        min_500_qs = "nearly_sorted"


    print(f"""\nLooking at the durations for each scenario of 500 pickup request, QuickSort Median of 3 takes less time to 
    sort the {min_500_qs} list while more time is taken to sort the {max_500_qs} list""")
    print("Its time complexity is O(n log n) and its space complexity is Olog(n).")






    unsorted_list_1000 = []
    # p_table
    ####################### 1000 datasets
    for i in range(3000):   # iterating through 3000 slots in passenger hash array
        chain_p = p_table[i]
        short_path = None
        chosen_driver = None    # initialised to None. chosen_driver meant to contain driver details
        best_T = float("inf")  # best (minimum) pickup time initialised to infinity
        curr_node = chain_p.head    # access linked list inside slot
        while curr_node is not None:
            entry_p = curr_node.getValue()  # gets passenger entry (DSAHashEntry)
            # d_table
            for j in range(3547):   # iterating through only 3547 driver record in driver hash array
                chain_d = d_table_1000[j]
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

                unsorted_list_1000 = unsorted_list_1000 + [(priority, pickup)]    # gets unsorted list of 1000 pickup request objects
            curr_node = curr_node.getNext()


    sorted_object_1000 = sort.QuickSortMedian3(unsorted_list_1000) # sorts unsorted list of 1000 request objects
    for i in range(len(sorted_object_1000)):
        a, b = sorted_object_1000[i]
        # adds only passenger name with estimated pickup time to list
        list_1000_ascending = list_1000_ascending + [(b.name, b.pickup_time)]  # gets a list of 1000 pickup requests in ascending order
    print()

    list_1000_random = conditions.randomise_list(list_1000_ascending) # get random list of 1000 pickup requests
    list_1000_nearly_sorted = conditions.nearly_sorted(list_1000_ascending)   # get nearly sorted list of 1000 pickup requests
    list_1000_reverse = conditions.reverse_list(list_1000_ascending)  # get reversed list of 1000 pickup requests
    print("Test List of 1000 pickup requests in random order")
    print(list_1000_random)
    print()
    print("Test List of 1000 pickup requests in nearly sorted order")
    print(list_1000_nearly_sorted)
    print()
    print("Test List of 1000 pickup requests in reversed order")
    print(list_1000_reverse)
    print()
    ########## measure time taken to sort 1000 random pickup requests using MergeSort
    start_ms_1000_random = timeit.default_timer()
    ms_1000_random = sort.mergeSort_list(list_1000_random)
    end_ms_1000_random = timeit.default_timer()
    duration_ms_1000_random = end_ms_1000_random - start_ms_1000_random

    print()
    print("*" * 80)
    print("Sorting of 1000 random Pickup Requests")
    print("*" * 80)
    print()
    print("Note: The first names are not the same for the different test scenarios as the lists are sorted using only the pickup times not the names.")
    print()
    print(ms_1000_random) # passenger name - pickup time
    print()


    print(f"Duration taken by mergesort to sort 1000 pickup requests in random order: {duration_ms_1000_random:.6f} seconds")
    print()


    # measure time taken to sort 1000 nearly sorted pickup requests using QuickSort
    start_ms_1000_nearly_sorted = timeit.default_timer()
    ms_1000_nearly_sorted = sort.QuickSortMedian3_list(list_1000_nearly_sorted)   # sorts nearly sorted list
    end_ms_1000_nearly_sorted = timeit.default_timer()
    duration_ms_1000_nearly_sorted = end_ms_1000_nearly_sorted - start_ms_1000_nearly_sorted

    print()
    print("*" * 80)
    print("Sorting of 1000 nearly sorted Pickup Requests")
    print("*" * 80)
    print(ms_1000_nearly_sorted) # passenger name - pickup time
    print()

    print(f"Duration taken by MergeSort to sort 1000 pickup requests in nearly sorted order: {duration_ms_1000_nearly_sorted:.6f} seconds")
    print()

    # measure time taken to sort 1000 reversed pickup requests using MergeSort
    start_ms_1000_reverse = timeit.default_timer()
    ms_1000_reverse = sort.QuickSortMedian3_list(list_1000_reverse)   # sorts reverse list
    end_ms_1000_reverse = timeit.default_timer()
    duration_ms_1000_reverse = end_ms_1000_reverse - start_ms_1000_reverse

    print()
    print("*" * 80)
    print("Sorting of 1000 reversed Pickup Requests")
    print("*" * 80)
    print(ms_1000_reverse) # passenger name - pickup time
    print()


    print(f"Duration taken by MergeSort to sort 1000 pickup requests in reverse order: {duration_ms_1000_reverse:.6f} seconds")
    print()

    print("The Top down MergeSort algorithm Reflection for different scenarios of 1000 pickup request: ")
    print(f"Duration to sort 1000 pickup requests in random order: {duration_ms_1000_random:.6f} seconds")
    print(f"Duration to sort 1000 pickup requests in nearly sorted order: {duration_ms_1000_nearly_sorted:.6f} seconds")
    print(f"Duration to sort 1000 pickup requests in reverse order: {duration_ms_1000_reverse:.6f} seconds")
    duration_1000 = [duration_ms_1000_random, duration_ms_1000_nearly_sorted, duration_ms_1000_reverse]
    sorted_dur_1000 = sort.bubbleSort(duration_1000)
    max_1000_ms_time = sorted_dur_1000[2]
    min_1000_ms_time = sorted_dur_1000[0]
    max_1000_ms = " "
    min_1000_ms = " "
    if max_1000_ms_time == duration_ms_1000_random:
        max_1000_ms = "random"
    elif max_1000_ms_time == duration_ms_1000_reverse:
        max_1000_ms = "reverse"
    elif max_1000_ms_time == duration_ms_1000_nearly_sorted:
        max_1000_ms = "nearly_sorted"

    if min_1000_ms_time == duration_ms_1000_random:
        min_1000_ms = "random"
    elif min_1000_ms_time == duration_ms_1000_reverse:
        min_1000_ms = "reverse"
    elif min_1000_ms_time == duration_ms_1000_nearly_sorted:
        min_1000_ms = "nearly sorted"

    print(f"""\nLooking at the durations for each scenario of 1000 pickup request, top down MergeSort takes less time to 
    sort the {min_1000_ms} list while more time is taken to sort the {max_1000_ms} list""")
    print("Its time complexity is O(n log n) and its space complexity is Olog(n).")



    ########### measure time taken to sort 1000 random pickup requests using QUICKSORT
    start_qs_1000_random = timeit.default_timer()
    qs_1000_random = sort.QuickSortMedian3_list(list_1000_random) # # sorts random list
    end_qs_1000_random = timeit.default_timer()
    duration_qs_1000_random = end_qs_1000_random - start_qs_1000_random
    print()
    print("*" * 80)
    print("Sorting of 1000 random Pickup Requests using QuickSort")
    print("*" * 80)
    print()
    print("Note: The first names are not the same for the different test scenarios as the lists are sorted using only the pickup times not the names.")
    print()
    print(qs_1000_random) # passenger name - pickup time
    print()


    print(f"Duration taken by QuickSort to sort 1000 pickup requests in random order: {duration_qs_1000_random:.6f} seconds")
    print()

    # measure time taken to sort 1000 nearly sorted pickup requests using QuickSort
    start_qs_1000_nearly_sorted = timeit.default_timer()
    qs_1000_nearly_sorted = sort.QuickSortMedian3_list(list_1000_nearly_sorted)   # sorts nearly sorted list
    end_qs_1000_nearly_sorted = timeit.default_timer()
    duration_qs_1000_nearly_sorted = end_qs_1000_nearly_sorted - start_qs_1000_nearly_sorted

    print()
    print("*" * 80)
    print("Sorting of 1000 nearly sorted Pickup Requests")
    print("*" * 80)
    print(qs_1000_nearly_sorted) # passenger name - pickup time
    print()

    print(f"Duration taken by QuickSort to sort 1000 pickup requests in nearly sorted order: {duration_qs_1000_nearly_sorted:.6f} seconds")
    print()

    # measure time taken to sort 1000 reversed pickup requests using QuickSort
    start_qs_1000_reverse = timeit.default_timer()
    qs_1000_reverse = sort.QuickSortMedian3_list(list_1000_reverse)   # sorts reverse list
    end_qs_1000_reverse = timeit.default_timer()
    duration_qs_1000_reverse = end_qs_1000_reverse - start_qs_1000_reverse

    print()
    print("*" * 80)
    print("Sorting of 1000 reversed Pickup Requests")
    print("*" * 80)
    print(qs_1000_reverse) # passenger name - pickup time
    print()


    print(f"Duration taken by QuickSort to sort 1000 pickup requests in reverse order: {duration_qs_1000_reverse:.6f} seconds")
    print()

    print("The Median of 3 QuickSort algorithm Reflection for different scenarios of 1000 pickup request: ")
    print(f"Duration to sort 1000 pickup requests in random order: {duration_qs_1000_random:.6f} seconds")
    print(f"Duration to sort 1000 pickup requests in nearly sorted order: {duration_qs_1000_nearly_sorted:.6f} seconds")
    print(f"Duration to sort 1000 pickup requests in reverse order: {duration_qs_1000_reverse:.6f} seconds")
    duration_1000 = [duration_qs_1000_random, duration_qs_1000_nearly_sorted, duration_qs_1000_reverse]
    sorted_dur_1000 = sort.bubbleSort(duration_1000)
    max_1000_qs_time = sorted_dur_1000[2]
    min_1000_qs_time = sorted_dur_1000[0]
    max_1000_qs = " "
    min_1000_qs = " "
    if max_1000_qs_time == duration_qs_1000_random:
        max_1000_qs = "random"
    elif max_1000_qs_time == duration_qs_1000_reverse:
        max_1000_qs = "reverse"
    elif max_1000_qs_time == duration_qs_1000_nearly_sorted:
        max_1000_qs = "nearly_sorted"

    if min_1000_qs_time == duration_qs_1000_random:
        min_1000_qs = "random"
    elif min_1000_qs_time == duration_qs_1000_reverse:
        min_1000_qs = "reverse"
    elif min_1000_qs_time == duration_qs_1000_nearly_sorted:
        min_1000_qs = "nearly sorted"

    print(f"""\nLooking at the durations for each scenario of 1000 pickup request, QuickSort Median of 3 takes less time to 
    sort the {min_1000_qs} list while more time is taken to sort the {max_1000_qs} list""")
    print("Its time complexity is O(n log n) and its space complexity is Olog(n).")

    print()
    ########## TIMING TABLE
    print("*" * 80)
    print("TIMING TABLE")
    print("*" * 80)
    print()
    print("MergeSort")
    header_ms = ["Dataset Size", "Random", "Nearly Sorted", "Reverse"]
    timing_ms = [
                [100, round(duration_ms_100_random, 6), round(duration_ms_100_nearly_sorted, 6), round(duration_ms_100_reverse, 6)],
                [500, round(duration_ms_500_random, 6), round(duration_ms_500_nearly_sorted, 6), round(duration_ms_500_reverse, 6)],
                [1000, round(duration_ms_1000_random, 6), round(duration_ms_1000_nearly_sorted, 6), round(duration_ms_1000_reverse, 6)]
    ]
    # print merge sort header
    print(f"{header_ms[0]:<20} {header_ms[1]:<10} {header_ms[2]:<20} {header_ms[3]:<10}")
    # print row
    for row in timing_ms:
        print(f"{row[0]:<20} {row[1]:<10} {row[2]:<20} {row[3]:<10}")

    print("\nQuicksort")
    header_qs = ["Dataset Size", "Random", "Nearly Sorted", "Reverse"]
    timing_qs = [
                [100, round(duration_qs_100_random, 6), round(duration_qs_100_nearly_sorted, 6), round(duration_qs_100_reverse, 6)],
                [500, round(duration_qs_500_random, 6), round(duration_qs_500_nearly_sorted, 6), round(duration_qs_500_reverse, 6)],
                [1000, round(duration_qs_1000_random, 6), round(duration_qs_1000_nearly_sorted, 6), round(duration_qs_1000_reverse, 6)]
    ]
    # print merge sort header
    print(f"{header_qs[0]:<20} {header_qs[1]:<10} {header_qs[2]:<20} {header_qs[3]:<10}")
    # print row
    for row in timing_qs:
        print(f"{row[0]:<20} {row[1]:<10} {row[2]:<20} {row[3]:<10}")

except Exception as err:
    print(err)

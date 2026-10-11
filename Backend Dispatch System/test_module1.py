from graph import *
from hash_table import DSAHashTable
from max_heap import *


try:
    # Module 1: Graph-Based Route Planning
    # Tests for bfs, dfs (cycle detection), Dijkstra (shortest path and shortest pickup time)
    graph = DSAGraph()

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

    #print(graph.depth_first_search())
    graph.bfs("Bookstore")  # Breadth-First Search - all reachable locations grouped by level

    print(graph.dfs('Mall'))    # Depth-First Search - detects if there is cycle

    print("\nDijkstra:")    # outputs shortest path and time between source location and destination
    path, time = graph.dijkstra("Cinema", "Supermarket")

    #print(graph.dijkstra("Church", "Harbor"))  # No path to Harbor
    print(f"Shortest Path: {path}")  # shortest path from start to destination
    print(f"Shortest Driving Time: {time} minutes\n")
    path_1, time_1 = graph.dijkstra("Supermarket", "Harbor")
    print(f"Shortest Path: {path_1}")  # shortest path from start to destination
    print(f"Shortest Driving Time: {time_1}\n")
    print(f"Count num of edges: {graph.get_edge_count()}\n")    # outputs total num of edges
    print(f"Count num of vertex: {graph.get_vertex_count()}\n") # outputs total num of vertices
    graph.display_as_list() # displays adjacency list

    graph.display_visually()    # displays graph visually

except Exception as err:
    print(err)
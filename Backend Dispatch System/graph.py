
from linked_list import *
from stack_queue import *
from min_heap import *
import networkx as nx
import matplotlib.pyplot as plt

class DSAGraphNode: # represents a single vertex
    def __init__(self, in_label, in_value=None):
        self.label = in_label # name of vertex, e.g B
        self.value = in_value
        self.adj_list = DSALinkedList()
        # used for BFS and DFS
        self.visited = False # not yet visited

    def __str__(self):
        return f"{self.label}"

    def get_label(self):
        return self.label
    
    def get_value(self):
        return self.value
    
    def get_adjacent_node(self):
        return self.adj_list.display()
    
    def get_visited(self):
        return self.visited
    
    def check_adjacent(self, node):
        # checks if this node is already connected to node
        # prevents duplication of connection
        run = 0
        result = False

        curr_node = self.adj_list.head
        while (run == 0) and (curr_node is not None):
            edge = curr_node.getValue()
            if edge.get_node() == node: # checks if node is in the adjacency list
                result = True
                run = 1
            else:
                curr_node = curr_node.getNext()
        return result

    def add_edge_into(self, node, weight):
        # adds an adjacent node to another node 

        if not self.check_adjacent(node):
            edge = DSAGraphEdge(node, weight)
            self.adj_list.insertLast(edge)
        else:
            raise Exception("Edge already exists")

    def delete_edge_from(self, adj_list, edge):
        # deletes an adjacent node from another node

        curr_node = adj_list.head
        while curr_node is not None:
            edge_node = curr_node.getValue()
            if edge_node.get_node() == edge:
                adj_list.remove(edge_node)  # remove edge vertex from all adjacency lists
                return
            else:
                curr_node = curr_node.getNext()

    def set_visited(self):
        self.visited = True

    def clear_visited(self):
        self.visited = False

class DSAGraphEdge: # class for edge and its weight
    def __init__(self, node, weight):
        self.node = node
        self.weight = weight

    def get_node(self):
        return self.node

    def get_weight(self):
        return self.weight



class DSAGraph:
    def __init__(self):
        self.vertices = DSALinkedList() # linked list of all vertices
        self._next_node = None

    def get_vertex(self, label): # traverses the vertices list to check if a certain vertex exists already
        run = 0
        result = None
        if isinstance(label, (float, int, bool)):
            raise Exception("Please enter label correctly")
        if self.vertices.isEmpty():
            result = None

        curr_node = self.vertices.head
        while (run == 0) and (curr_node is not None):
            vertex = curr_node.getValue()
            if vertex.get_label() == label: # checks if label is in the vertices list
                result = vertex
                run = 1
            else:
                curr_node = curr_node.getNext()
                
        
        return result


    def has_vertex(self, label): # returns True if vertex exists already
                                    # returns False if vertex does not exist
        if isinstance(label, (float, int, bool)):
            raise Exception("Please enter label correctly")

        if self.get_vertex(label) is not None:
            result = True # the vertex exists already
        else:
            result = False  # the vertex does not exist yet
        return result

    def add_vertex(self, label, value=None):
        if isinstance(label, (float, int, bool)):
            raise Exception("Please enter label correctly")

        if not self.has_vertex(label): # if vertex does not exist yet, then add vertex
            vertex = DSAGraphNode(label, value)
            self.vertices.insertLast(vertex)
        else:
            raise Exception(f"Vertex {label} already exists")

    def delete_vertex(self, label):
        if isinstance(label, (float, int, bool)):
            raise Exception("Please enter label correctly")

        vertex = self.get_vertex(label)
        if vertex is not None: # if vertex exist, then delete vertex
            
            curr_node = self.vertices.head
            while curr_node is not None:
                v = curr_node.getValue()
                v.adj_list.remove(vertex)   # remove vertex from all adjacency lists
                curr_node = curr_node.getNext()
            self.vertices.remove(vertex)    # remove vertex from vertex list
        else:
            raise Exception(f"Vertex {label} does not exist")
        
    def add_edge(self, lab_1, lab_2, weight):   # connect 2 vertices together
        if isinstance(lab_1, (float, int, bool)):
            raise Exception("Please enter label 1 correctly")
        if isinstance(lab_2, (float, int, bool)):
            raise Exception("Please enter label 2 correctly")

        ver_1 = self.get_vertex(lab_1)
        ver_2 = self.get_vertex(lab_2)  

        if (ver_1 is not None) and (ver_2 is not None): # if lab_1 and lab_2 exist
            ver_1.add_edge_into(ver_2, weight) # add edge from ver_1 to ver_2
            ver_2.add_edge_into(ver_1, weight)  # add edge from ver_1 to ver_2
        elif ver_1 is None:
            raise Exception(f"{lab_1} does not exist")
        elif ver_2 is None:
            raise Exception(f"{lab_2} does not exist")

    def delete_edge(self, lab_1, lab_2):   # remove edge from adjacency list
        if isinstance(lab_1, (float, int, bool)):
            raise Exception("Please enter label 1 correctly")
        if isinstance(lab_2, (float, int, bool)):
            raise Exception("Please enter label 2 correctly")

        ver_1 = self.get_vertex(lab_1)
        ver_2 = self.get_vertex(lab_2)
        if (ver_1 is not None) and (ver_2 is not None): # if lab_1 and lab_2 exist
            ver_1.delete_edge_from(ver_1.adj_list, ver_2) # remove edge from ver_1 to ver_2
            ver_2.delete_edge_from(ver_2.adj_list, ver_1)  # remove edge from ver_1 to ver_2
        elif ver_1 is None:
            raise Exception(f"{lab_1} does not exist")
        elif ver_2 is None:
            raise Exception(f"{lab_2} does not exist")

    def get_vertex_count(self):
        count = 0

        if self.vertices.isEmpty():
            count = 0
        else:
            curr_node = self.vertices.head
            if curr_node is None:
                raise Exception("Cannot provide total number of vertices as vertices list is empty")
            while (curr_node is not None):

                count += 1
                curr_node = curr_node.getNext()


        return count
    
    def get_edge_count(self):
        count = 0
        edge_count = 0
        curr_node = self.vertices.head
        if curr_node is None:
            raise Exception("Cannot provide total number of edges as vertices list is empty")
        while (curr_node is not None):
            vertex = curr_node.getValue()
            adj_node = vertex.adj_list.head
            while (adj_node is not None):
                count += 1
                adj_node = adj_node.getNext()
            curr_node = curr_node.getNext()
        edge_count = count // 2
        return edge_count

    def is_adjacent(self, lab_1, lab_2):
        result = False
        if isinstance(lab_1, (float, int, bool)):
            raise Exception("Please enter label 1 correctly")
        if isinstance(lab_2, (float, int, bool)):
            raise Exception("Please enter label 2 correctly")

        ver_1 = self.get_vertex(lab_1)
        ver_2 = self.get_vertex(lab_2)

        if (ver_1 is not None) and (ver_2 is not None): # check if lab_1 and lab_2 exist
            result = ver_1.check_adjacent(ver_2) # check if ver_2 is in ver_1's adjacency list
            #True if yes or False if not
        else:
            result = False
        return result

    def get_adjacent(self, lab): # returns adjacency list of a certain vertex
        adj_list_vertex = None
        if isinstance(lab, (float, int, bool)):
            raise Exception("Please enter label correctly")

        vertex = self.get_vertex(lab) # get the vertex
        if vertex is not None:
            adj_list_vertex = vertex.get_adjacent_node()
        else:
            adj_list_vertex = None
        return adj_list_vertex

    # display methods
    def display_as_list(self):

        print("\nAdjacency list:\n")
        curr_node = self.vertices.head
        if curr_node is None:
            raise Exception("Vertices list is empty")
        while (curr_node is not None):
            vertex = curr_node.getValue()
            print(f"{vertex}:", end=" ")
            adj_node = vertex.adj_list.head
            while (adj_node is not None):
                edge = adj_node.getValue()
                print(f"{edge.get_node()}({edge.get_weight()})", end=" ")
                adj_node = adj_node.getNext()
            print()
            curr_node = curr_node.getNext()

    def display_as_matrix(self):
        result = False
        curr_node = self.vertices.head
        if curr_node is None:
            raise Exception("Vertices list is empty")
        print(" ", end=" ")
        while curr_node is not None:
            vertex = curr_node.getValue()
            print(f"\t{vertex.get_label():<12}", end=" ") # print header row (column labels)
            curr_node = curr_node.getNext()
        print()

        curr_node = self.vertices.head  # reset to iterate through the vertices again

        while curr_node is not None:  # print each row
            vertex = curr_node.getValue()
            print(f"{vertex.get_label():<15}", end=" ") # print row label

            ver_node = self.vertices.head   # reset for column
            while ver_node is not None:  # print each row
                vertex_1 = ver_node.getValue()
                result = vertex.check_adjacent(vertex_1)    # if vertex_1 is adjacent to vertex then display 1, else display 0
                if result == True:
                    print(f"{'1':<15}", end=" ")
                else:
                    print(f"{'0':<15}", end=" ")
                ver_node = ver_node.getNext()   # get next potential adjacent vertex
            print()
            curr_node = curr_node.getNext() # get next header vertex

    def degree(self, node): # counts how many neighbours a single vertex has
        count = 0
        adj_node = node.adj_list.head
        if adj_node is None:
            raise Exception("Adjacency list is empty")
        while adj_node is not None:
            count += 1
            adj_node = adj_node.getNext()
        return count

    def has_value(self, value): # checks if any vertex has a certain value
        result = False
        run = 0
        curr_node = self.vertices.head
        if curr_node is None:
            raise Exception("Vertices list is empty")
        while (run == 0) and (curr_node is not None):
            vertex = curr_node.getValue()
            if vertex.get_value() == value:
                result = True
                run = 1
            else:
                result = False
            curr_node = curr_node.getNext()
        return result

    def next_vertex(self):  # returns only next vertex
        if self._next_node is None:
            self._next_node = self.vertices.head
        else:
            self._next_node = self._next_node.getNext()
        if self._next_node is not None:
            return self._next_node.getValue()
        self._next_node = None
        return None

    def sort(self): # sort vertices in alphabetical or numeric ascending order
        curr_node = self.vertices.head
        if curr_node is None:
            raise Exception("Vertices list is empty")
        while curr_node is not None:
            next_node = curr_node.getNext()
            while next_node is not None:
                lab_1 = curr_node.getValue()
                lab_2 = next_node.getValue()
                if lab_1.get_label() > lab_2.get_label():
                    curr_node.setValue(lab_2)
                    next_node.setValue(lab_1)
                next_node = next_node.getNext()
            curr_node = curr_node.getNext()

    def sort_adjacent(self): # sort neighbours in alphabetical or numeric ascending order
        curr_node = self.vertices.head
        if curr_node is None:
            raise Exception("Vertices list is empty")
        while curr_node is not None:
            vertex = curr_node.getValue()
            swapped = True
            while swapped:
                swapped = False
                node = vertex.adj_list.head
                while node is not None and node.getNext() is not None:
                    next_node = node.getNext().get_node()
                    lab_1 = node.getValue().get_node()
                    lab_2 = next_node.getValue()
                    if lab_1.get_label() > lab_2.get_label():
                        node.setValue(lab_2)
                        next_node.setValue(lab_1)
                        swapped = True
                    node = node.getNext()
            curr_node = curr_node.getNext()

    def breadth_first_search(self): # original bfs
        T = DSAQueue()  # result queue and takes in label
        Q = DSAQueue()  # working queue and takes in vertex

        curr_node = self.vertices.head
        while curr_node is not None:
            v = curr_node.getValue()
            v.clear_visited()
            curr_node = curr_node.getNext()
        if self.vertices.head is None:
            return T

        first_vertex = self.vertices.head.getValue()
        first_vertex.set_visited()
        Q.enqueue(first_vertex)

        # BFS traversal
        while not Q.isEmpty():   # while Q is not empty
            v = Q.dequeue()
            adj_node = v.adj_list.head
            while adj_node is not None:
                edge = adj_node.getValue()
                w = edge.get_node()
                if not w.get_visited():
                    T.enqueue((v.get_label(), w.get_label()))   # inserts the edge path of each vertex

                    w.set_visited()
                    Q.enqueue(w)
                adj_node = adj_node.getNext()
        return T    # returns edges in order they are visited



    def get_unvisited_adjacent(self, vertex):
        # used for cycle detection inside depth_first_search
        if not isinstance(vertex, DSAGraphNode):
            raise Exception("Please enter correct vertex")

        adj_node = vertex.adj_list.head
        while adj_node is not None:
            edge = adj_node.getValue()
            w = edge.get_node()
            if not w.get_visited():
                return w
            adj_node = adj_node.getNext()
        return None

    def depth_first_search(self):   # returns nodes explored in depth
        T = DSAQueue()  # result queue and takes in label
        S = DSAStack()  # working stack and takes in vertex
        curr_node = self.vertices.head
        while curr_node is not None:
            v = curr_node.getValue()
            v.clear_visited()
            curr_node = curr_node.getNext()
        if self.vertices.head is None:
            return T
        first_vertex = self.vertices.head.getValue()
        first_vertex.set_visited()
        S.push(first_vertex)

        while not S.isEmpty():
            v = S.top()

            w = self.get_unvisited_adjacent(v)
            if w is not None:
                T.enqueue((v.get_label(), w.get_label()))

                w.set_visited()
                S.push(w)

            else:
                S.pop() # backtrack
        return T

    def display_visually(self):

        G = nx.Graph()
        edge_queue = DSAQueue()
        curr_ver = self.vertices.head
        while curr_ver is not None: # iterate through vertex list
            vertex = curr_ver.getValue()
            v = vertex.get_label()
            G.add_node(v)  # add all nodes

            adj_node = vertex.adj_list.head
            while adj_node is not None: # iterate through adjacency list
                edge = adj_node.getValue()
                n = edge.get_node().get_label()
                w = edge.get_weight()
                G.add_weighted_edges_from([(v, n, w)])
                adj_node = adj_node.getNext()
            curr_ver = curr_ver.getNext()

        driving_time_labels = nx.get_edge_attributes(G, 'weight')
        pos = nx.spring_layout(G, k=3)   # lines which connect the edges
        nx.draw(G, pos, with_labels=True, node_color="lightblue", edge_color="blue", node_size=2010, font_size=7, font_weight="bold")
        nx.draw_networkx_edge_labels(G, pos, edge_labels=driving_time_labels)
        plt.show()
    
    def dijkstra(self, start_ver, destination=None):    # outputs shortest path and time
        start_ver = self.get_vertex(start_ver)  # get the vertex
        destination_ver = self.get_vertex(destination)

        priority_q = DSAMINHeap(20)    # priority queue (min heap)
        driving_times = {}   # to store shortest driving time from start to any vertex
        visited = {}    # store predecessor of each visited vertex
        curr_node = self.vertices.head


        while curr_node is not None:
            node = curr_node.getValue() # gets the DSAGraph node
            if node == start_ver:
                driving_times[start_ver] = 0  # initialise the driving time of start_ver to 0
                visited[start_ver] = None   # start has distance 0 and no visited vertex before it
            else:
                driving_times[node] = float("inf") # the driving time for each vertex is infinity
                visited[node] = None   # no predecessor nodes
            curr_node = curr_node.getNext()

        if start_ver.adj_list.head is None:
            return

        priority_q.add(0, start_ver)

        while not priority_q.heap_empty():
            removed_item = priority_q.remove()
            current_driving_time = removed_item.get_priority()
            ver = removed_item.get_value()
            if current_driving_time > driving_times[ver]:
                continue # skip current_driving_time as it is greater

            adj_node = ver.adj_list.head
            while adj_node is not None:
                edge = adj_node.getValue()
                neighbour = edge.get_node()
                weight = edge.get_weight()
                total_time = driving_times[ver] + weight    # calculate driving time to reach neighbour
                if total_time < driving_times[neighbour]:
                    driving_times[neighbour] = total_time
                    visited[neighbour] = ver
                    priority_q.add(total_time, neighbour)
                adj_node = adj_node.getNext() # move to next edge in adj list

        if destination is not None:

            if driving_times[destination_ver] == float("inf"):
                return f"No path to {destination}", "No shortest time"


            elif start_ver == destination_ver:
                # Driver's current location is the same as the pickup location
                return f"{destination_ver.get_label()}", 0

            elif start_ver != destination_ver:   # Driver's current location is different from the pickup location
                path = [None] * self.get_vertex_count() # initial path list
                i = 0
                curr_ver = destination_ver
                while curr_ver is not None: # enqueues vertices from start to destination in reverse
                    path[i] = curr_ver.get_label()
                    i += 1
                    curr_ver = visited[curr_ver]    # step backwards to previously visited node

                path = path[:i][::-1]   # slice to filled part and reverse
                return f"{path}", driving_times[destination_ver]    # returns shortest path and time
                # shortest path from start to destination
                # shortest driving time from start to destination

            else:   # no path available from source to destination
                raise Exception(f"No path available from {start_ver} to {destination_ver}")


    def bfs(self, source):  # finds  all reachable locations grouped by level

        Q = DSAQueue()  # working queue and takes in vertex

        curr_node = self.vertices.head
        while curr_node is not None:    # sets all nodes to unvisited
            v = curr_node.getValue()
            v.clear_visited()
            curr_node = curr_node.getNext()

        first_vertex = self.get_vertex(source)  # gets source location node
        if first_vertex is None:
            print(f"{source} not found")
            return T

        first_vertex.set_visited()  # source location node is set to visited
        Q.enqueue((0, first_vertex))    # store vertex, level in queue to group level by level

        levels = {} # stores reachable locations at each level
        # BFS traversal
        while not Q.isEmpty():   # while Q is not empty
            level, v = Q.dequeue()

            if level not in levels: # level inx is given a list initialised with None
                levels[level] = [None] * self.get_vertex_count()
            count = 0
            while count < len(levels[level]) and levels[level][count] is not None:
                count += 1
            levels[level][count] = v.get_label()    # add level and its list of reachable location nodes

            adj_node = v.adj_list.head  # traverse v's adjacency list
            while adj_node is not None:
                edge = adj_node.getValue()
                w = edge.get_node()
                if not w.get_visited(): # if edge node is not visted
                    w.set_visited() # set edge node to visited and add it to queue
                    Q.enqueue((level + 1, w))
                adj_node = adj_node.getNext()
        print(f"BFS ({source}):")
        for idx in levels:
            reachable_locations = []    # will store reachable locations
            count = 0
            while count < len(levels[idx]):
                if levels[idx][count] is not None:
                    reachable_locations = reachable_locations + [levels[idx][count]]
                count += 1
            print(f"Level {idx}: {reachable_locations}\n")



    def dfs(self, source):   # cycle detection and provides locations
        T = DSAQueue()  # result queue and takes in label
        S = DSAStack()  # working stack and takes in vertex
        curr_node = self.vertices.head
        while curr_node is not None:
            v = curr_node.getValue()
            v.clear_visited()
            curr_node = curr_node.getNext()

        first_vertex = self.get_vertex(source)
        if first_vertex is None:
            print(f"{source} not found")
            return T

        parent = {}
        cycle_found = False


        first_vertex.set_visited()
        parent[first_vertex.get_label()] = None
        S.push(first_vertex)

        while not S.isEmpty():
            v = S.top()
            w = self.get_unvisited_adjacent(v)
            if w is not None:
                T.enqueue((v.get_label(), w.get_label()))
                parent[w.get_label()] = v   # record how we got to v
                w.set_visited()
                S.push(w)
            else:
                S.pop() # backtrack

        # cycle detection
        curr_node = self.vertices.head
        while curr_node is not None and not cycle_found:
            v = curr_node.getValue()
            adj_node = v.adj_list.head
            while adj_node is not None and not cycle_found:
                edge = adj_node.getValue()
                w = edge.get_node()
                if v.get_label() in parent:
                    v_parent = parent[v.get_label()]
                else:
                    v_parent = None
                if w.get_visited() and w != v_parent:   # if w was visited and w is not the parent of v then it's a cycle
                    is_ancestor = False
                    if v.get_label() in parent:
                        check = parent[v.get_label()]   # start checking at v's parent
                    else:
                        check = None
                    while check is not None:    # walk up from v toward root
                        if check == w:  # finds w in v's ancestry
                            is_ancestor = True
                            break
                        else:
                            if check.get_label() in parent:
                                check = parent[check.get_label()]
                            else:
                                check = None
                    if is_ancestor:
                        cycle_found = True
                        cycle_nodes = self.get_cycle_path(v, w, parent)
                adj_node = adj_node.getNext()
            curr_node = curr_node.getNext()
        print("DFS Cycle Detection")
        if cycle_found:
            if cycle_nodes.top() != source:
                print(f"No cycle was found with {source} being one of the locations")
            else:
                print(f"Cycle path: {cycle_nodes.display_queue()}")  # display cycle path
        else:
            print("No cycle was found")


    def get_cycle_path(self, node, ancestor, parent): # checks if checks if

        cycle_path = [node.get_label()]
        current = node
        while current != ancestor:  # if current node is same as the node already visited, then it is an ancestor. Thus cy

            if current.get_label() in parent:
                current = parent[current.get_label()]
            else:
                current = None
            if current is None:
                break

            cycle_path = cycle_path + [current.get_label()]

        correct_cycle_path = DSAQueue(len(cycle_path)+1)
        i = len(cycle_path) - 1
        while i >= 0:
            correct_cycle_path.enqueue(cycle_path[i])   # enqueues cycle path in reverse to get the correct cycle path
            i -= 1
        correct_cycle_path.enqueue(ancestor.get_label())    # enqueues the source location on last position
        return correct_cycle_path












            

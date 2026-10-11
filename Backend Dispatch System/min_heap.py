import csv


class DSAHeapEntry:
    def __init__(self, priority, value):  # stores one heap item
        self.priority = priority
        self.value = value

    def __str__(self):
        return f"{self.priority}, {self.value}"

    def get_priority(self):
        return self.priority

    def set_priority(self, priority):
        self.priority = priority

    def get_value(self):
        return self.value

    def set_value(self, value):
        self.value = value


class DSAMINHeap:  # store heap
    def __init__(self, size):
        self.size = size
        self.heap = [None] * size
        self.count = 0

    def heap_full(self):
        return self.count == self.size

    def heap_empty(self):
        return self.count == 0

    def add(self, priority, value):  # inserts a heap item
        if self.heap_full():
            raise Exception("Heap is full")
        else:
            curr_idx = self.count  # index given to new heap item
            self.heap[curr_idx] = DSAHeapEntry(priority, value)  # insert heap item
            self.count += 1  # increment count of heap items by 1
            self.trickle_up(curr_idx)

    def trickle_up(self, curr_idx):
        parent_idx = (curr_idx - 1) // 2  # get parent index

        while curr_idx > 0 and self.heap[curr_idx].get_priority() < self.heap[
            parent_idx].get_priority():  # continues looping if current index > 0 and added heap item > parent item
            temp = self.heap[parent_idx]
            self.heap[parent_idx] = self.heap[curr_idx]  # added heap item takes place of parent item
            self.heap[curr_idx] = temp  # parent item takes place of added heap item
            curr_idx = parent_idx  # continue comparing current heap item with its parent
            parent_idx = (curr_idx - 1) // 2  # get parent index

    def remove(self):
        if self.heap_empty():
            raise Exception("Heap is empty")
        else:
            remove_item = self.heap[0]
            last_item = self.heap[self.count - 1]
            self.heap[0] = last_item
            self.heap[self.count - 1] = None
            self.count -= 1
            if self.count > 0:
                self.trickle_down(0)
        return remove_item

    def trickle_down(self, curr_idx):
        left_child_idx = (curr_idx * 2) + 1
        keep_going = True

        while keep_going and left_child_idx < self.count:  # is a left child
            keep_going = False
            right_child_idx = left_child_idx + 1
            small_idx = left_child_idx
            if right_child_idx < self.count:  # is a right child
                if self.heap[right_child_idx].get_priority() < self.heap[left_child_idx].get_priority():
                    small_idx = right_child_idx  # find smallest child
            if self.heap[small_idx].get_priority() < self.heap[curr_idx].get_priority():
                temp = self.heap[curr_idx]
                self.heap[curr_idx] = self.heap[small_idx]
                self.heap[small_idx] = temp

                curr_idx = small_idx
                left_child_idx = (curr_idx * 2) + 1
                keep_going = True


    def display_heap(self):
        for i in range(self.count):
            print(self.heap[i])

    def heapify(self):  # imports a random heap array   # to make it a min heap
        # start from last parent node
        for i in range(((self.count // 2) - 1), -1, -1):
            self.trickle_down(i)

        return self.heap  # exports the heap array

    def swap(self):  # swaps max element with first element
        temp = self.heap[self.count - 1]
        self.heap[self.count - 1] = self.heap[0]
        self.heap[0] = temp

    def heap_sort(self):  # sorts the heap
        self.heapify()  # turn array into min heap
        original_count = self.count
        while self.count > 1:  # moves largest heap item to the end
            self.swap()  # move max item to end
            self.count -= 1  # deducts a heap item
            self.trickle_down(0)

        self.count = original_count

    def read_csv(self, csv_file):  # reads csv file
        with open(csv_file, 'r') as f:
            csv_reader = csv.reader(f)
            for line in csv_reader:
                if len(line) >= 2:
                    priority, value = line[0], line[1]
                    priority = int(priority)

                    self.add(priority, value)  # add each priority, value as a heap item
        self.heap_sort()  # sort the heap array

    def save_csv(self, csv_file):  # displays all heap items inside a csv file
        with open(csv_file, 'w') as f:
            f.write(f"{'PRIORITY':<12}    {'VALUE':<30}\n")
            for slot in range(self.count):
                priority = self.heap[slot].get_priority()
                value = self.heap[slot].get_value()

                f.write(f"{priority:<12}    {value:<30}\n")
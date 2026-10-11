import random
from max_heap import *

class sorting:

    def bubbleSort(self, A):
        b = len(A)  # length of array

        for i in range(b - 1):  # needs b - 1 passes
            swapped = False  # assigned swapped with False
            for j in range(b - 1 - i):  # for each pass, check for swaps then ignore the swapped number
                if A[j] > A[
                    j + 1]:  # if A[j] is greater than the next element then it is bubbled to the right until last pass
                    temp = A[j]  # value in A[j] is given to temp
                    A[j] = A[j + 1]  # value in A[j + 1] is given to A[j]
                    A[j + 1] = temp  # value in temp is given to A[j + 1]
                    swapped = True  # if the element were swapped, then swapped = True
            if not swapped:  # if there was no swap in 1 pass, then the sorting stops as the array is already sorted
                break
        return A  # returns sorted array

    # Sorts the pickup and pickup_request object
    def mergeSort(self,A):
        """ mergeSort - front-end for kick-starting the recursive algorithm
        """

        self.mergeSortRecurse(A, 0, len(A)-1)
        return A


    def mergeSortRecurse(self,A, left_idx, right_idx):  # breaks input list into 2 parts
        if left_idx < right_idx:
            mid_idx = (left_idx + right_idx) // 2

            self.mergeSortRecurse(A, left_idx, mid_idx)  # Recurse - sort left half of current sub-array
            self.mergeSortRecurse(A, mid_idx + 1, right_idx)  # Recurse - sort right half of current sub-array

            self.merge(A, left_idx, mid_idx, right_idx)  # merge left and right sub-arrays


    def merge(self, A, left_idx, mid_idx, right_idx):   # puts 2 list together
        temp_arr = [0] * (right_idx - left_idx + 1)
        i = left_idx  # index for the front element of left sub-array
        j = mid_idx + 1  # index for the front of front element of right sub-array
        k = 0  # index for next free element in temp_arr

        while (i <= mid_idx) and (j <= right_idx):  # merge sub-arrays into temp_arr
            priority_1, pickup_1 = A[i]
            priority_2, pickup_2 = A[j]

            if pickup_1 is None or pickup_2 is None:
                break

            if pickup_1.pickup_time <= pickup_2.pickup_time:  # use <= for a stable sort
                temp_arr[k] = A[i]  # take from left sub-array
                i += 1
            else:
                temp_arr[k] = A[j]  # take from right sub-array
                j += 1
            k += 1

        while i <= mid_idx:  # flush remainder from left sub-array
            temp_arr[k] = A[i]
            i += 1
            k += 1

        while j <= right_idx:  # or flush remainder from right sub-array
            temp_arr[k] = A[j]
            j += 1
            k += 1

        for k in range(len(temp_arr)):  # copy now-sorted temp_arr back to actual array
            A[left_idx + k] = temp_arr[k]  # use k-left_idx to align temp_arr indexing to zero





    def QuickSortMedian3(self, A):
        self.quickSortMedian3Recurse(A, 0, len(A) - 1)
        return A  # return sorted array





    def doPartitioning(self, A, leftIdx, rightIdx, pivotIdx):
        pivot_val = A[pivotIdx]
        A[pivotIdx] = A[rightIdx]  # Swap the pivotVal with the right-most element
        A[rightIdx] = pivot_val

        curr_idx = leftIdx  # tracks boundary of < pivot region
        i = leftIdx

        for i in range(i, rightIdx):
            priority_1, pickup_1 = A[i]
            priority_2, pickup_2 = pivot_val

            if pickup_1 is None or pickup_2 is None:
                break
            if pickup_1.pickup_time < pickup_2.pickup_time:
                temp = A[i]
                A[i] = A[curr_idx]
                A[curr_idx] = temp
                curr_idx = curr_idx + 1  # advance boundary

        new_pivotIdx = curr_idx
        A[rightIdx] = A[new_pivotIdx]
        A[new_pivotIdx] = pivot_val
        return new_pivotIdx


    def quickSortMedian3Recurse(self, A, leftIdx, rightIdx):
        if rightIdx > leftIdx:  # Check that the subarray is > one element in size
            middleIdx = (rightIdx + leftIdx) // 2  # get middle array

            pivot_idx = self.median_of_3(A, leftIdx, middleIdx, rightIdx)  # Pivot selection strategy: median of 3
            new_pivot_idx = self.doPartitioning(A, leftIdx, rightIdx, pivot_idx)  # partition

            self.quickSortMedian3Recurse(A, leftIdx, new_pivot_idx - 1)  # Recurse: Sort left partition
            self.quickSortMedian3Recurse(A, new_pivot_idx + 1, rightIdx)  # Recurse: Sort right partition


    def median_of_3(self, A, leftIdx, middleIdx, rightIdx):
        left_priority, left_pickup = A[leftIdx]
        middle_priority, middle_pickup = A[middleIdx]
        right_priority, right_pickup = A[rightIdx]

        if (left_pickup.pickup_time <= middle_pickup.pickup_time <= right_pickup.pickup_time) or (right_pickup.pickup_time <= middle_pickup.pickup_time <= left_pickup.pickup_time):
            return middleIdx
        elif (middle_pickup.pickup_time <= left_pickup.pickup_time <= right_pickup.pickup_time) or (right_pickup.pickup_time <= left_pickup.pickup_time <= middle_pickup.pickup_time):
            return leftIdx
        elif (middle_pickup.pickup_time <= right_pickup.pickup_time <= left_pickup.pickup_time) or (left_pickup.pickup_time <= right_pickup.pickup_time <= middle_pickup.pickup_time):
            return rightIdx


    ######## Sorts datasets (normal list)
    def mergeSort_list(self, A):
        """ mergeSort - front-end for kick-starting the recursive algorithm
        """
        self.mergeSortRecurse_list(A, 0, len(A)-1)
        return A
    def mergeSortRecurse_list(self,A, left_idx, right_idx):
        if left_idx < right_idx:
            mid_idx = (left_idx + right_idx) // 2

            self.mergeSortRecurse_list(A, left_idx, mid_idx)  # Recurse - sort left half of current sub-array
            self.mergeSortRecurse_list(A, mid_idx + 1, right_idx) # Recurse - sort right half of current sub-array

            self.merge_list(A, left_idx, mid_idx, right_idx)    # merge left and right sub-arrays

    def merge_list(self, A, left_idx, mid_idx, right_idx):
        temp_arr =  [0] * (right_idx - left_idx + 1)
        i = left_idx    # index for the front element of left sub-array
        j = mid_idx + 1 # index for the front of front element of right sub-array
        k = 0   # index for next free element in temp_arr

        while (i <= mid_idx) and (j <= right_idx):  # merge sub-arrays into temp_arr
            name_1, time_1 = A[i]
            name_2, time_2 = A[j]
            if time_1 <= time_2:    # use <= for a stable sort
                temp_arr[k] = A[i]    # take from left sub-array
                i += 1
            else:
                temp_arr[k] = A[j]    # take from right sub-array
                j += 1
            k += 1

        while i <= mid_idx:  # flush remainder from left sub-array
            temp_arr[k] = A[i]
            i += 1
            k += 1

        while j <= right_idx:    #   or flush remainder from right sub-array
            temp_arr[k] = A[j]
            j += 1
            k += 1

        for k in range(len(temp_arr)): # copy now-sorted temp_arr back to actual array
            A[left_idx + k] = temp_arr[k]   # use k-left_idx to align temp_arr indexing to zero

    # quicksort list
    def QuickSortMedian3_list(self, A):
        self.quickSortMedian3Recurse_list(A, 0, len(A)-1)
        return A    # return sorted array

    def doPartitioning_list(self, A, leftIdx, rightIdx, pivotIdx):
        pivot_val = A[pivotIdx]
        A[pivotIdx] = A[rightIdx]   # Swap the pivotVal with the right-most element
        A[rightIdx] = pivot_val

        curr_idx = leftIdx  # tracks boundary of < pivot region
        i = leftIdx
        for i in range(i, rightIdx):
            name, time = A[i]
            pivot_name, pivot_time = pivot_val
            if time < pivot_time:
                temp = A[i]
                A[i] = A[curr_idx]
                A[curr_idx] = temp
                curr_idx = curr_idx + 1 # advance boundary

        new_pivotIdx = curr_idx
        A[rightIdx] = A[new_pivotIdx]
        A[new_pivotIdx] = pivot_val
        return new_pivotIdx


    def quickSortMedian3Recurse_list(self, A, leftIdx, rightIdx):
        if rightIdx > leftIdx:  # Check that the subarray is > one element in size
            middleIdx = (rightIdx + leftIdx) // 2  # get middle array

            pivot_idx = self.median_of_3_list(A, leftIdx, middleIdx, rightIdx)  # Pivot selection strategy: median of 3
            new_pivot_idx = self.doPartitioning_list(A, leftIdx, rightIdx, pivot_idx)  # partition

            self.quickSortMedian3Recurse_list(A, leftIdx, new_pivot_idx - 1)  # Recurse: Sort left partition
            self.quickSortMedian3Recurse_list(A, new_pivot_idx + 1, rightIdx)  # Recurse: Sort right partition


    def median_of_3_list(self, A, leftIdx, middleIdx, rightIdx):
        left_name, left_time = A[leftIdx]           # returns middle index
        middle_name, middle_time = A[middleIdx]
        right_name, right_time = A[rightIdx]

        if (left_time <= middle_time <= right_time) or (right_time <= middle_time <= left_time):
            return middleIdx
        elif (middle_time <= left_time <= right_time) or (right_time <= left_time <= middle_time):
            return leftIdx
        elif (middle_time <= right_time <= left_time) or (left_time <= right_time <= middle_time):
            return rightIdx
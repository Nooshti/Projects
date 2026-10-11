import random as rd

class Test_conditions:

    def reverse_list(self, A):    # reverses a list
        if len(A) == 0:
            return []
        reversed_A = A[:]   # copy A into reversed_A
        reversed_A = reversed_A[::-1]
        return reversed_A

    def randomise_list(self, A):  # shuffles the contents of a list randomly
        if len(A) == 0:
            return []
        temp_list = A[:]
        length_list = len(temp_list)
        for i in range(rd.randint(length_list//2, length_list)):
            num_1 = rd.randint(0, length_list-1)
            num_2 = rd.randint(0, length_list-1)

            temp = temp_list[num_2]
            temp_list[num_2] = temp_list[num_1]
            temp_list[num_1] = temp

        return temp_list

    def nearly_sorted(self, A):   # makes the list nearly sorted (shuffles only 10% of list)
        if len(A) == 0:
            return []
        temp_list = A[:]
        length_list = len(temp_list)
        displacement_percent = 0.10
        for i in range(int((displacement_percent*length_list)/2+1)):
            num_1 = int(rd.random()*length_list)
            num_2 = int(rd.random() * length_list)
            temp = temp_list[num_2]
            temp_list[num_2] = temp_list[num_1]
            temp_list[num_1] = temp
        return temp_list
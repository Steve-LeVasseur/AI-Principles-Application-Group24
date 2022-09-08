import time

# Need to compare behavior of algorithms such as by number of comparisons or execution time

count = 0 # global count variable

# Bubblesort function definition
def bubbleSort(L):
    global count
    # Scan through the list this many times
    for i in range(len(L)-1):
        # Scan through the list item by item
        for j in range(len(L)-i-1):
            count += 1 # increment comparison counter
            # if the following item in the list is larger than the current item
            if L[j+1] < L[j]:
                # swap the two items in the list
                L[j], L[j+1] = L[j+1], L[j]

def bubbleRange(L, start, end):
    global count
    for i in range((end-start)-1):
        # Scan through the list item by item
        for j in range((end-start)-i-1):
            count += 1 # increment comparison counter
            # if the following item in the list is larger than the current item
            if L[j+1] < L[j]:
                # swap the two items in the list
                L[j], L[j+1] = L[j+1], L[j]

# quickSort Implementation
def quickSort(list, leftIndex, rightIndex):
    global count
    if (len(list) == 1):
        return list
    count += 1 # increment comparison counter
    if leftIndex < rightIndex:
        pivotIndex = quickSortPartition(list, leftIndex, rightIndex) # find pivot
        quickSort(list, leftIndex, pivotIndex-1) # sort list to left of pivot
        quickSort(list, pivotIndex+1, rightIndex) # sort list to right of pivot

def quickSortPartition(list, leftIndex, rightIndex):
    global count
    pivot = list[rightIndex]
    pointer = leftIndex
    for i in range(leftIndex, rightIndex):
        count += 1 # increment comparison counter
        if list[i] <= pivot:
            #swap the value to the front
            list[i], list[pointer] = list[pointer], list[i]
            pointer += 1
    list[pointer], list[rightIndex] = list[rightIndex], list[pointer]
    return pointer

# mergeSort implementation    
def mergeList(list, leftIndex, midIndex, rightIndex):
    global count
    size1 = midIndex - leftIndex + 1
    size2 = rightIndex - midIndex

    list1 = [0] * (size1) # Create empty lists of appropriate sizes
    list2 = [0] * (size2)

    for ind1 in range(size1): # Assign appropriate entries to created empty lists
        list1[ind1] = list[leftIndex + ind1]
    for ind2 in range(size2):
        list2[ind2] = list[midIndex + ind2 + 1]

    ind1 = 0
    ind2 = 0
    indMerge = leftIndex

    while ind1 < size1 and ind2 < size2:
        count += 1 # increment comparison counter
        if list1[ind1] <= list2[ind2]: # merge lists together in proper order
            list[indMerge] = list1[ind1]
            ind1 += 1
        else:
            list[indMerge] = list2[ind2]
            ind2 += 1
        
        indMerge += 1

    while ind1 < size1: # if list2 finished first, add remaining entries from list1
        list[indMerge] = list1[ind1]
        ind1 += 1
        indMerge += 1

    while ind2 < size2: # if list1 finished first, add remaining entries from list2
        list[indMerge] = list2[ind2]
        ind2 += 1
        indMerge += 1

def mergeSort(list, leftIndex, rightIndex):
    global count
    count += 1 # increment comparison counter
    if leftIndex < rightIndex:
        midIndex = leftIndex + (rightIndex - leftIndex) // 2

        mergeSort(list, leftIndex, midIndex)
        mergeSort(list, midIndex + 1, rightIndex)
        mergeList(list, leftIndex, midIndex, rightIndex)

def hybridSort(list, BIG, SMALL, THRESHOLD, start=0, end=None):
    global count

    if (end != None):
        if (end-start <= THRESHOLD):
            bubbleRange(list, start, end)

    if (len(list) <= THRESHOLD):
        if (SMALL.lower() == 'bubble'):
            bubbleSort(list)
            print(list)
    else:
        if (BIG.lower() == 'quick'): # hybrid quicksort
            global count
            if end == None:
                end = len(list)-1
            if (len(list) == 1):
                return list
            count += 1 # increment comparison counter
            if start < end:
                pivot = list[end]
                pointer = start
                for i in range(start, end):
                    count += 1 # increment comparison counter
                    if list[i] <= pivot:
                        #swap the value to the front
                        list[i], list[pointer] = list[pointer], list[i]
                        pointer += 1
                list[pointer], list[end] = list[end], list[pointer]
                hybridSort(list, BIG, SMALL, THRESHOLD, start, pointer-1) # sort list to left of pivot
                hybridSort(list, BIG, SMALL, THRESHOLD, pointer+1, end) # sort list to right of pivot

                # print(list[start:end])

        elif (BIG.lower() == 'merge'):

            # this assumes length is greater than THRESHOLD because it catches less than THRESHOLD in above
            length = len(list)
            halfwayPoint = length // 2
            list1 = list[0:halfwayPoint]
            list2 = list[halfwayPoint:]
            
            # calls hybridSort on the two halves
            hybridSort(list1, BIG, SMALL, THRESHOLD)
            hybridSort(list2, BIG, SMALL, THRESHOLD)

            #re-merges the two halves
            ind1, ind2, indMerge = 0, 0, 0
            size1, size2 = len(list1), len(list2)

            while (ind1 < size1 and ind2 < size2):
                if list1[ind1] < list2[ind2]:
                    list[indMerge] = list1[ind1]
                    
                    ind1 += 1
                    indMerge += 1

                else:
                    list[indMerge] = list2[ind2]

                    ind2 += 1
                    indMerge += 1
            
            # gets remaining list1 elements if list2 finished first
            while ind1 < size1:
                list[indMerge] = list1[ind1]
                
                ind1 += 1
                indMerge += 1
                
            # gets remaining list2 elements if list1 finished first
            while ind2 < size2:
                list[indMerge] = list2[ind2]
                
                ind2 += 1
                indMerge += 1
            
            # print(list)
            


# Tests here

# global count variable seems to be working
# Having some issue with the timer

hybridSort([5, 1, 9, 3, 67, 90, 2], 'merge', 'bubble', 5)

hybridSort([5, 1, 9, 3, 67, 90, 2, 54, 56, 77, 234, 23, 4, 11, 9090, 2], 'merge', 'bubble', 5)

count = 0 # global comparison counter
l = [5, 21, 14] # very short list
start_time = time.time()
time.sleep(.0000000000000000001) # tricks timer to track times of less than .1 seconds
hybridSort(l, 'merge', 'bubble', 2) # hybrid merge on very short list
end_time = time.time()
print("hybrid merge very short list: ", count, " comparisons - ", end_time-start_time, "seconds")

count = 0
l = [5, 21, 14] # very short list
start_time = time.time()
time.sleep(.0000000000000000001)
hybridSort(l, 'quick', 'bubble', 2) # hybrid quick on very short list
end_time = time.time()
print("hybrid quick very short list: ", count, " comparisons - ", end_time-start_time, "seconds")

count = 0
l = [5, 21, 14] # very short list
start_time = time.time()
time.sleep(.0000000000000000001)
quickSort(l, 0, len(l)-1) # quicksort on very short list
end_time = time.time()
print("quicksort very short list: ", count, " comparisons - ", end_time-start_time, "seconds")

count = 0
l = [5, 21, 14] # very short list
start_time = time.time()
time.sleep(.0000000000000000001)
bubbleSort(l) # bubblesort on very short list
end_time = time.time()
print("bubblesort very short list: ", count,  " comparisons - ", end_time-start_time, "seconds")

count = 0
l = [5, 21, 14] # very short list
start_time = time.time()
time.sleep(.0000000000000000001)
mergeSort(l, 0, len(l)-1) # mergesort on very short list
end_time = time.time()
print("mergesort very short list: ", count,  " comparisons - ", end_time-start_time, "seconds")



# New list
count = 0 # global comparison counter
l = [6, 5, 8, 10, 2, 3, 1, 7, 4, 9, 15, 12, 14, 13, 11, 20, 17, 18, 19, 16] # 20 item list
start_time = time.time()
time.sleep(.0000000000000000001) # tricks timer to track times of less than .1 seconds
hybridSort(l, 'merge', 'bubble', 5) # hybrid merge on 20 item list
end_time = time.time()
print("hybrid merge 20 item list: ", count, " comparisons - ", end_time-start_time, "seconds")

count = 0
l = [6, 5, 8, 10, 2, 3, 1, 7, 4, 9, 15, 12, 14, 13, 11, 20, 17, 18, 19, 16] # 20 item list
start_time = time.time()
time.sleep(.0000000000000000001)
hybridSort(l, 'quick', 'bubble', 5) # hybrid quick on 20 item list
end_time = time.time()
print("hybrid quick 20 item list: ", count, " comparisons - ", end_time-start_time, "seconds")

count = 0
l = [6, 5, 8, 10, 2, 3, 1, 7, 4, 9, 15, 12, 14, 13, 11, 20, 17, 18, 19, 16] # 20 item list
start_time = time.time()
time.sleep(.0000000000000000001)
quickSort(l, 0, len(l)-1) # quicksort on 20 item list
end_time = time.time()
print("quicksort 20 item list: ", count, " comparisons - ", end_time-start_time, "seconds")

count = 0
l = [6, 5, 8, 10, 2, 3, 1, 7, 4, 9, 15, 12, 14, 13, 11, 20, 17, 18, 19, 16] # 20 item list
start_time = time.time()
time.sleep(.0000000000000000001)
bubbleSort(l) # bubblesort on 20 item list
end_time = time.time()
print("bubblesort 20 item list: ", count,  " comparisons - ", end_time-start_time, "seconds")

count = 0
l = [6, 5, 8, 10, 2, 3, 1, 7, 4, 9, 15, 12, 14, 13, 11, 20, 17, 18, 19, 16] # 20 item list
start_time = time.time()
time.sleep(.0000000000000000001)
mergeSort(l, 0, len(l)-1) # mergesort on 20 item list
end_time = time.time()
print("mergesort 20 item list: ", count,  " comparisons - ", end_time-start_time, "seconds")



# New List
count = 0 # global comparison counter
l = [50, 49, 48, 47, 46, 45, 44, 43, 42, 41, 40, 39, 38, 37, 36, 35, 34, 33, 32, 31, 30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1] # 50 item list
start_time = time.time()
time.sleep(.0000000000000000001) # tricks timer to track times of less than .1 seconds
hybridSort(l, 'merge', 'bubble', 10) # hybrid merge on 50 item list
end_time = time.time()
print("hybrid merge 50 item list: ", count, " comparisons - ", end_time-start_time, "seconds")

count = 0
l = [50, 49, 48, 47, 46, 45, 44, 43, 42, 41, 40, 39, 38, 37, 36, 35, 34, 33, 32, 31, 30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1] # 50 item list
start_time = time.time()
time.sleep(.0000000000000000001)
hybridSort(l, 'quick', 'bubble', 10) # hybrid quick on 50 item list
end_time = time.time()
print("hybrid quick 50 item list: ", count, " comparisons - ", end_time-start_time, "seconds")

count = 0
l = [50, 49, 48, 47, 46, 45, 44, 43, 42, 41, 40, 39, 38, 37, 36, 35, 34, 33, 32, 31, 30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1] # 50 item list
start_time = time.time()
time.sleep(.0000000000000000001)
quickSort(l, 0, len(l)-1) # quicksort on 50 item list
end_time = time.time()
print("quicksort 50 item list: ", count, " comparisons - ", end_time-start_time, "seconds")

count = 0
l = [50, 49, 48, 47, 46, 45, 44, 43, 42, 41, 40, 39, 38, 37, 36, 35, 34, 33, 32, 31, 30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1] # 50 item list
start_time = time.time()
time.sleep(.0000000000000000001)
bubbleSort(l) # bubblesort on 50 item list
end_time = time.time()
print("bubblesort 50 item list: ", count,  " comparisons - ", end_time-start_time, "seconds")

count = 0
l = [50, 49, 48, 47, 46, 45, 44, 43, 42, 41, 40, 39, 38, 37, 36, 35, 34, 33, 32, 31, 30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1] # 50 item list
start_time = time.time()
time.sleep(.0000000000000000001)
mergeSort(l, 0, len(l)-1) # mergesort on 50 item list
end_time = time.time()
print("mergesort 50 item list: ", count,  " comparisons - ", end_time-start_time, "seconds")

# Comment Section here

# Results of the tests above:

# Very short list:
# hybrid merge very short list:  1  comparisons -  0.0070056915283203125 seconds
# hybrid quick very short list:  5  comparisons -  0.015471696853637695 seconds
# quicksort very short list:  5  comparisons -  0.016013383865356445 seconds
# bubblesort very short list:  3  comparisons -  0.015013694763183594 seconds
# mergesort very short list:  8  comparisons -  0.016014814376831055 seconds

# hybrid merge was the shortest implementation with regards to comparisons as well as time.


# 20 Item list:
# hybrid merge 20 item list:  40  comparisons -  0.015012979507446289 seconds
# hybrid quick 20 item list:  106  comparisons -  0.016014814376831055 seconds
# quicksort 20 item list:  94  comparisons -  0.01569056510925293 seconds
# bubblesort 20 item list:  190  comparisons -  0.01601433753967285 seconds
# mergesort 20 item list:  94  comparisons -  0.016014814376831055 seconds

# hybrid merge still made the least amount of comparisons as well as took the least time.
# It's worth noting that the original mergesort and hybrid quicksort took the exact same amount of time-- and took the longest


# 50 Item list: 
# hybrid merge 50 item list:  132  comparisons -  0.01701664924621582 seconds
# hybrid quick 50 item list:  1489  comparisons -  0.015012264251708984 seconds
# quicksort 50 item list:  1324  comparisons -  0.01601552963256836 seconds
# bubblesort 50 item list:  1225  comparisons -  0.016014814376831055 seconds
# mergesort 50 item list:  232  comparisons -  0.01601409912109375 seconds

# hybrid quicksort made the most comparisons yet took the least amount of time.
# hybrid mergesort made the least amount of comparisons yet took the most amount of time
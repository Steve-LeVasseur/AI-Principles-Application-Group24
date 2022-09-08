from turtle import right
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

    list1 = [0] * (size1)
    list2 = [0] * (size2)

    for ind1 in range(size1):
        list1[ind1] = list[leftIndex + ind1]
    for ind2 in range(size2):
        list2[ind2] = list[midIndex + ind2 + 1]

    ind1 = 0
    ind2 = 0
    indMerge = leftIndex

    while ind1 < size1 and ind2 < size2:
        count += 1 # increment comparison counter
        if list1[ind1] <= list2[ind2]:
            list[indMerge] = list1[ind1]
            ind1 += 1
        else:
            list[indMerge] = list2[ind2]
            ind2 += 1
        
        indMerge += 1

    while ind1 < size1:
        list[indMerge] = list1[ind1]
        ind1 += 1
        indMerge += 1

    while ind2 < size2:
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

def hybridSort(list, BIG, SMALL, THRESHOLD):
    global count

    if (len(list) <= THRESHOLD):
        if (SMALL == 'bubble'):
            bubbleSort(list)
    else:
        if (BIG == 'quick'):
            pass
            # run hybrid "quicksort" here
        elif (BIG == 'merge'):
            pass
            # run hybrid "mergesort" here


# Tests here

# global count variable seems to be working
# Having some issue with the timer

count = 0 # global comparison counter
l = [5, 21, 14] # very short list
start_time = time.time()
hybridSort(l, 'merge', 'bubble', 2) # hybrid merge on very short list
end_time = time.time()
print("hybrid merge very short list: ", count, " - ", end_time-start_time)

count = 0
l = [5, 21, 14] # very short list
start_time = time.time()
hybridSort(l, 'quick', 'bubble', 2) # hybrid quick on very short list
end_time = time.time()
print("hybrid quick very short list: ", count, " - ", end_time-start_time)

count = 0
l = [5, 21, 14] # very short list
start_time = time.time()
quickSort(l, 0, 2) # quicksort on very short list
end_time = time.time()
print("quicksort very short list: ", count, " - ", end_time-start_time)

count = 0
l = [5, 21, 14] # very short list
start_time = time.time()
bubbleSort(l) # bubblesort on very short list
end_time = time.time()
print("bubblesort very short list: ", count,  " - ", end_time-start_time)

count = 0
l = [5, 21, 14] # very short list
start_time = time.time()
mergeSort(l, 0, 2) # quicksort on very short list
end_time = time.time()
print("mergesort very short list: ", count,  " - ", end_time-start_time)

# Comment Section here

# probably want to run at least 3 'tests' where 1 test uses
# bubblesort, quicksort, mergesort, and both hybrid sorts
# can compare comparison counter and time used for each method


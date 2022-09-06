from turtle import right

# Bubblesort function definition
def bubbleSort(L):
    # Scan through the list this many times
    for i in range(len(L)-1):
        # Scan through the list item by item
        for j in range(len(L)-i-1):
            # if the following item in the list is larger than the current item
            if L[j+1] < L[j]:
                # swap the two items in the list
                L[j], L[j+1] = L[j+1], L[j]


# quickSort Implementation
def quickSort(list, leftIndex, rightIndex):
    if (len(list) == 1):
        return list
    if leftIndex < rightIndex:
        pivotIndex = quickSortPartition(list, leftIndex, rightIndex) # find pivot
        quickSort(list, leftIndex, pivotIndex-1) # sort list to left of pivot
        quickSort(list, pivotIndex+1, rightIndex) # sort list to right of pivot

def quickSortPartition(list, leftIndex, rightIndex):
    pivot = list[rightIndex]
    pointer = leftIndex
    for i in range(leftIndex, rightIndex):
        if list[i] <= pivot:
            #swap the value to the front
            list[i], list[pointer] = list[pointer], list[i]
            pointer += 1
    list[pointer], list[rightIndex] = list[rightIndex], list[pointer]
    return pointer

# mergeSort implementation    
def mergeList(list, leftIndex, midIndex, rightIndex):
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
    if leftIndex < rightIndex:
        midIndex = leftIndex + (rightIndex - leftIndex) // 2

        mergeSort(list, leftIndex, midIndex)
        mergeSort(list, midIndex + 1, rightIndex)
        mergeList(list, leftIndex, midIndex, rightIndex)

def hybridSort(list, BIG, SMALL, THRESHOLD):

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

# Comment Section here
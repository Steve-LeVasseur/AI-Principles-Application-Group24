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

l = [0, 5, 4, 3, 2, 1]
quickSort(l, 0, 5)
print(l)
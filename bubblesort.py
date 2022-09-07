# Python program for implementation of Bubble Sort

# DO NOT SUMBIT THIS CODE

def bubbleSort(L):
    for i in range(len(L)-1):
        for j in range(len(L)-i-1):
            if L[j+1] < L[j]:
                swap = True
                L[j], L[j+1] = L[j+1], L[j]

# def bubbleSort(arr):
# 	n = len(arr)
# 	swapped = False
# 	for i in range(n-1):
# 		for j in range(0, n-i-1):
# 			if arr[j] > arr[j + 1]:
# 				swapped = True
# 				arr[j], arr[j + 1] = arr[j + 1], arr[j]
		
# 		if not swapped:
# 			return


# Driver code to test above
arr = [64, 34, 25, 12, 22, 11, 90]

bubbleSort(arr)

print("Sorted array is:")
for i in range(len(arr)):
	print("% d" % arr[i], end=" ")

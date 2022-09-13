import time

count = 0

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





l = [5, 21, 14, 6, 9, 13, 56, 79, 1003, 123, 432, 1, 1, 1, 1, 1, 1, 1, 1, 2, 34, 5, 4, 534, 5, 345, 345, 34, 5, 34, 53, 453, 45, 345, 3453, 45, 345, 3, 2] # very short list
start_time = time.time()
bubbleSort(l) # bubblesort on very short list
end_time = time.time()
print(l)
print("bubblesort very short list: ", count, " - ", (end_time-start_time)* 10**3)

def bubbleSort(array):
    n = len(array)

    # Traverse through all array elements
    for i in range(n-1):
    # range(n) also work but outer loop will
    # repeat one time more than needed.

        # Last i elements are already in place
        for j in range(0, n-i-1):

            # traverse the array from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element
            if array[j] > array[j + 1] :
                array[j], array[j + 1] = array[j + 1], array[j]

    return array
    
#==========================================================================#

def partition(start, end, array):

    # Initializing pivot's index to start
    pivot_index = start
    pivot = array[pivot_index]
    
    # This loop runs till start pointer crosses
    # end pointer, and when it does we swap the
    # pivot with element on end pointer
    while start < end:
        
        # Increment the start pointer till it finds an
        # element greater than pivot
        while start < len(array) and array[start] <= pivot:
            start += 1
            
        # Decrement the end pointer till it finds an
        # element less than pivot
        while array[end] > pivot:
            end -= 1
        
        # If start and end have not crossed each other,
        # swap the numbers on start and end
        if(start < end):
            array[start], array[end] = array[end], array[start]
    
    # Swap pivot element with element on end pointer.
    # This puts pivot on its correct sorted place.
    array[end], array[pivot_index] = array[pivot_index], array[end]
    
    # Returning end pointer to divide the array into 2
    return end
    
# The main function that implements QuickSort
def quickSort(array, start, end):

    if (start < end):
        
        # p is partitioning index, array[p]
        # is at right place
        p = partition(start, end, array)
        
        # Sort elements before partition
        # and after partition
        quickSort(array, start, p - 1)
        quickSort(array, p + 1, end)

    return array

#==========================================================================#
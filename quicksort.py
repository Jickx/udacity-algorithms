"""Implement quick sort in Python.
Input a list.
Output a sorted list."""
def quicksort(array):
    
    if len(array) < 1:
        return array
    
    pivot = array[0]    

    smaller = list(filter(lambda x: x < pivot, array))
    equal = [i for i in array if i == pivot]
    larger = list(filter(lambda x: x > pivot, array))

    return quicksort(smaller) + equal + quicksort(larger)

test = [21, 4, 1, 3, 9, 20, 25, 6, 21, 14]
print(quicksort(test))
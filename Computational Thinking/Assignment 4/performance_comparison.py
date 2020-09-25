import math

# Queick sort n^2
# Merge sort = n * log(n)

AMOUNT_OF_ELEMENTS = 500000

bigOQuickSort = AMOUNT_OF_ELEMENTS ** 2

bigOMergeSort = AMOUNT_OF_ELEMENTS * math.log(AMOUNT_OF_ELEMENTS)

print("Big O Quicksort: ", bigOQuickSort)
print("Big O Mergesort: ", bigOMergeSort)
print("The worst case for Merge-sort is ", bigOQuickSort / bigOMergeSort,
      " times faster than the worst case for Quick-sort")

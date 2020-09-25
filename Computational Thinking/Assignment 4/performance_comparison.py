# Module to access mathematical functions like log
import math

# So that we can also calculate for other sizes of arrays
AMOUNT_OF_ELEMENTS = 500000

# time complexity of QuickSort using worst case formula
bigOQuickSort = AMOUNT_OF_ELEMENTS ** 2

# time complexity of MergeSort using worst case formula
bigOMergeSort = AMOUNT_OF_ELEMENTS * math.log(AMOUNT_OF_ELEMENTS)

# print results
print("Big O QuickSort: ", bigOQuickSort)
print("Big O MergeSort: ", bigOMergeSort)
print("The worst case for MergeSort is ", bigOQuickSort / bigOMergeSort,
      " times faster than the worst case for QuickSort")

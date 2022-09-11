import random

def quickSort(array, start, end):
    if start >= end:
        return

    pivotIndex = random.randrange(start, end + 1)

    print(f"Pivot Index : {pivotIndex}")


    pivot = array[pivotIndex]

    array[start], array[pivotIndex] = pivot, array[start]

    print(array)

    p1 = start + 1

    p2 = end

    while p1 <= p2:

        if array[p1] > pivot and array[p2] <= pivot:
            array[p1], array[p2] = array[p2], array[p1]

            p1 += 1
            p2 -= 1

        elif array[p1] > pivot:
            p2 -= 1

        elif array[p2] <= pivot:
            p1 += 1

        else:
            p1 += 1
            p2 -= 1

    array[p2], array[start] = array[start], array[p2]


    quickSort(array, start, p2 - 1)
    quickSort(array, p2 + 1, end)

arr = [2,0,2,1,1,0]

quickSort(arr, 0, len(arr) - 1)

print(arr)
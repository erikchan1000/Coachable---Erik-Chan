import random

#Self Implementation

def quickSort(array, lo, hi):
    if lo >= hi:
        return

    pivotIndex = random.randint(lo, hi)

    pivot = array[pivotIndex]

    #Shifts pivot to front
    array[lo], array[pivotIndex] = pivot, array[lo]

    p1 = lo + 1

    p2 = hi

    while p1 <= p2:
        if array[p1] >= pivot and array[p2] < pivot:
            array[p1], array[p2] = array[p2], array[p1]
            p1 += 1
            p2 -= 1

        elif array[p1] >= pivot:
            p2 -= 1

        elif array[p2] < pivot:
            p1 += 1

        else:
            p1 += 1
            p2 -= 1

    array[0], array[p1 - 1] = array[p1 - 1], array[0]

    print("Pivot Index: " + str(pivot))

    print(array)

    quickSort(array, lo, p1 - 1)
    quickSort(array, p1, hi)




if __name__ == "__main__":
    arr = [2,1]

    quickSort(arr, 0, len(arr) - 1)



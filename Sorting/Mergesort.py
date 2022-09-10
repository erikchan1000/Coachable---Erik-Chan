import random

def divide(array, lo, hi):
    if lo >= hi:
        return

    mid = (hi + lo) // 2 + 1

    divide(array, lo, mid - 1)
    divide(array, mid, hi)

    array[lo : hi + 1] = merge(array, lo, mid, hi)

def merge(array, lo, mid, end):
    p1 = lo
    p2 = mid
    temp = []

    while p1 < mid and p2 <= end:
        if array[p1] > array[p2]:
            temp.append(array[p2])
            p2 += 1

        else:
            temp.append(array[p1])
            p1 += 1

    if p1 < mid:
        temp += array[p1 : mid]

    elif p2 <= end:
        temp += array[p2 : end + 1]

    return temp
    

def mergeSort(array):
    divide(array, 0, len(array) - 1)


if __name__ == "__main__":
    arr = [random.randrange(0, 101) for x in range(50)]

    print(arr)

    mergeSort(arr)

    print(arr)


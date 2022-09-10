def mergeSort(arr):
    divide(arr, 0, len(arr) - 1)


def divide(arr, lo, hi):
    if lo >= hi:
        return

    mid = (hi + lo) // 2 + 1

    divide(arr, lo, mid - 1)
    divide(arr, mid, hi)

    merge(arr, lo, mid, hi)

def merge(arr, lo, mid, hi):
    p1 = lo
    p2 = mid

    curr = lo

    copy = arr[:]

    while curr <= hi:
        if p1 < mid and p2 <= hi:
            if copy[p1] < copy[p2]:
                arr[curr] = copy[p1]

                p1 += 1

            else:
                arr[curr] = copy[p2]

                p2 += 1

        elif p1 < mid:
            arr[curr] = copy[p1]
            p1 += 1

        else:
            arr[curr] = copy[p2]
            p2 += 1

        curr += 1


if __name__ == "__main__":
    arr = [8,4,3,9,10,2,1,5,6,7]

    print(arr)

    mergeSort(arr)

    print(arr)
import sys

def merge(items, left, right):
    i = j = k = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            items[k] = left[i]
            i+=1
        else:
            items[k] = right[j]
            j+=1
        k+=1

    while i < len(left):
        items[k] = left[i]
        i+=1
        k+=1

    while j < len(right):
        items[k] = right[j]
        j+=1
        k+=1


def mergesort(items):
    if len(items) > 1:
        mid = len(items) // 2
        left = items[:mid]
        right = items[mid:]

        mergesort(left)
        mergesort(right)
        merge(items, left, right)


def main():
    items = sys.argv[1].split(",")
    items = list(map(lambda i : int(i), items))
    print("Given array is: ", items.__str__())
    mergesort(items)
    print("Sorted array is: ", items.__str__())

main()

import sys

'''
    In this implementation, I am using the last element as pivot.
'''

def partition(items, low, high):
    pivot = items[high]
    i = low - 1

    for j in range(low, high):
        if items[j] <= pivot:
            i+=1
            items[i], items[j] = items[j], items[i]

    items[i+1], items[high] = items[high], items[i+1]
    return i+1


def quicksort(items, low, high):
    if low < high:
        partition_index = partition(items, low, high)

        quicksort(items, low, partition_index - 1)
        quicksort(items, partition_index + 1, high)


def main():
    items = sys.argv[1].split(",")
    items = list(map(lambda i : int(i), items))
    print("Given array is: ", items.__str__())
    quicksort(items, 0, len(items) - 1)
    print("Sorted array is: ", items.__str__())

main()

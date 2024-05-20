# test_sorting_algorithms.py

from sorting_algorithms import bubble_sort, selection_sort, insertion_sort, merge_sort, quick_sort

def main():
    arr = [64, 25, 12, 22, 11]

    print("Original array:", arr)

    print("\nBubble Sort:")
    print(bubble_sort(arr.copy()))

    print("\nSelection Sort:")
    print(selection_sort(arr.copy()))

    print("\nInsertion Sort:")
    print(insertion_sort(arr.copy()))

    print("\nMerge Sort:")
    print(merge_sort(arr.copy()))

    print("\nQuick Sort:")
    print(quick_sort(arr.copy()))


if __name__ == "__main__":
    main()

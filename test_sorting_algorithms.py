# test_sorting_algorithms.py

from sorting_algorithms import bubble_sort, selection_sort, insertion_sort, merge_sort, quick_sort

def visualize_array(arr):
    print("Array visualization:")
    print("[" + ", ".join(map(str, arr)) + "]")

def get_user_array():
    arr = []
    while len(arr) < 20:
        try:
            num = input(f"Enter a number ({len(arr)+1}/20) or press Enter to finish: ")
            if num == "":
                break
            num = int(num)
            arr.append(num)
        except ValueError:
            print("Please enter a valid number.")
    return arr

def main():
    sorting_algorithms = {
        1: ("Bubble Sort", bubble_sort),
        2: ("Selection Sort", selection_sort),
        3: ("Insertion Sort", insertion_sort),
        4: ("Merge Sort", merge_sort),
        5: ("Quick Sort", quick_sort)
    }

    print("Select a sorting algorithm:")
    for key, (name, _) in sorting_algorithms.items():
        print(f"{key}. {name}")

    while True:
        try:
            choice = int(input("Enter the number corresponding to your choice: "))
            if choice in sorting_algorithms:
                break
            else:
                print("Invalid choice. Please select a valid number.")
        except ValueError:
            print("Please enter a valid number.")

    print(f"You have selected {sorting_algorithms[choice][0]}.")

    user_array = get_user_array()
    if not user_array:
        print("No elements entered. Exiting.")
        return

    print("Original array:")
    visualize_array(user_array)

    sorted_array = sorting_algorithms[choice][1](user_array.copy())

    print("\nSorted array using", sorting_algorithms[choice][0] + ":")
    visualize_array(sorted_array)

if __name__ == "__main__":
    main()

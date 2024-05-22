import time
from sorting_algorithms import bubble_sort, selection_sort, insertion_sort, merge_sort, quick_sort

def visualize_array(arr):
    print("Array visualization:")
    print("[" + ", ".join(map(str, arr)) + "]")

def get_user_array():
    arr = []
    while len(arr) < 50:
        try:
            num = input(f"Input numbers ({len(arr)+1}/50) or press Enter to start sorting now: ")
            if num == "":
                break
            num = int(num)
            arr.append(num)
            visualize_array(arr)
        except ValueError:
            print("Please enter a valid number.")
    return arr

def paste_array():
    while True:
        try:
            arr_str = input("Paste your array (up to 50 numbers separated by commas like so: 1,6,2,1 etc): ")
            arr = [int(x.strip()) for x in arr_str.split(",") if x.strip().isdigit()]
            if len(arr) > 50:
                print("Array exceeds 50 numbers. Please try again.")
            else:
                visualize_array(arr)
                return arr
        except ValueError:
            print("Please enter a valid sequence of numbers separated by commas.")

def main():
    while True:
        print("\nWelcome to kuriakos.ant Python sorting algorithms demonstration script!")
        print("Please select a sorting algorithm to start:")

        sorting_algorithms = {
            1: ("Bubble Sort", bubble_sort),
            2: ("Selection Sort", selection_sort),
            3: ("Insertion Sort", insertion_sort),
            4: ("Merge Sort", merge_sort),
            5: ("Quick Sort", quick_sort)
        }

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

        while True:
            input_method = input("Do you want to input an array manually cell by cell or paste an existing array? (m for manual, p for paste): ").lower()
            if input_method == 'm':
                print("You have selected manual array creation.")
                user_array = get_user_array()
                break
            elif input_method == 'p':
                print("You have selected paste an array option.")
                user_array = paste_array()
                break
            else:
                print("Invalid option. Please press 'm' for manual input or 'p' to paste an array.")

        if not user_array:
            print("No elements entered. Exiting.")
            return

        print("Original array:")
        visualize_array(user_array)

        start_time = time.time()
        sorted_array = sorting_algorithms[choice][1](user_array.copy())
        end_time = time.time()

        print("\nSorted array using", sorting_algorithms[choice][0] + ":")
        visualize_array(sorted_array)
        print(f"Sorting completed in {end_time - start_time:.6f} seconds.")

        while True:
            restart = input("Do you want to sort another array? (y/n): ").lower()
            if restart == 'y':
                break
            elif restart == 'n':
                print("Exiting the program. Goodbye!")
                return
            else:
                print("Invalid option. Please press 'y' to sort another array or 'n' to exit.")

if __name__ == "__main__":
    main()

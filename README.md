# Sorting Algorithms in Python

  
This repository contains implementations of the most common sorting algorithms in Python.

It is part of a project for a computer science class.

  
## Algorithms Implemented

  
- Bubble Sort

- Selection Sort

- Insertion Sort

- Merge Sort

- Quick Sort

## Example Use ( Image )

Here is a demonstration of using the terminal application to sort an array with bubble sort : 


## Prerequisites

Before you begin, ensure you have met the following requirements:


- **Python 3.x**: (Mandatory) Make sure Python 3 is installed on your system. You can check your Python version by running:

  `python3 --version` 
  
  or 
  
  `py -v`

If Python is not installed, you can download and install it from [python.org](https://www.python.org/).

-   **Git**: ( Optional) You should have Git installed to clone the repository. Check if Git is installed by running:
  
    
    `git --version` 
    
    If Git is not installed, follow the instructions on [git-scm.com](https://git-scm.com/) to install it.
    If you dont want to install git you can just download the zip file from this repository and extract it and proceed with the rest of the    instructions

## Installation

To install and run this project locally, follow these steps:

1.  **Clone the repository**:
    
    `git clone https://github.com/kuriakosant/sorting-algorithms-python` 
    
2.  **Navigate to the project directory**:
    
    `cd sorting-algorithms-python` 
    
3.  **Run the script**:
    
    `python3 test_sorting_algorithms.py` 
    

## How to Use

Once you run the script, you'll be presented with a menu and several options. Here's a step-by-step guide on how to use it:

### 1. Select a Sorting Algorithm

The script starts by asking you to select a sorting algorithm from the following list:

1.  **Bubble Sort**
2.  **Selection Sort**
3.  **Insertion Sort**
4.  **Merge Sort**
5.  **Quick Sort**

Simply enter the number corresponding to your choice.

### 2. Choose Input Method

After selecting the sorting algorithm, you'll be prompted to choose how you'd like to input your array:

-   **Manual Input**: Press `m` to input the array manually, cell by cell.
    
    -   The script will guide you to input up to 50 numbers, visualizing the array as you add each number.
    -   You can stop entering numbers at any time by pressing Enter without typing a number.
-   **Paste Array**: Press `p` to paste an existing array.
    
    -   You'll be asked to paste a sequence of up to 50 numbers, separated by commas (e.g., `1,3,4,51,65,62`).
    -   The array will be visualized immediately after you paste it.

### 3. Sorting and Output

Once the array is ready, the script will sort it using the selected algorithm:

-   The script will display the **original array** before sorting.
-   It will then sort the array and visualize the **sorted array**.
-   Finally, it will display the time taken to perform the sort in seconds.

### 4. Continue or Exit

After sorting, the script will ask if you want to sort another array:

-   Press `y` to input a new array and sort it again.
-   Press `n` to exit the script.


## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE.md) file for details.

## Contributions

Contributions are welcome! Please follow these steps to contribute:

1.  Clone/Fork this repository.
2.  Create a new branch (`git checkout -b feature-branch`).
3.  Make your changes and commit them (`git commit -m 'Add some feature'`).
4.  Push to the branch (`git push origin feature-branch`).
5.  Create a Pull Request.

## Contact

For any questions or suggestions, feel free to reach out to me:

**Email**: kuriakosant2003@gmail.com
**GitHub**: [https://github.com/kuriakosant](https://github.com/kuriakosant)
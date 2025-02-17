"""
    Create a program that finds (min,max,mean,mode,median,range,variance,STD,quartiles and IQR)
        - The program will take a list of numbers and find the above requirements 
        - it should contain 11 functions for each requirement
        - Do not use built in functions and make sure you handle Errors 
"""



def get_numbers():
    """Takes a list from the user and handles input errors."""
    try:
        nums = list(map(int, input("Enter numbers separated by spaces: ").split()))
        if not nums:
            raise ValueError("List cannot be empty 😡")
        return nums
    except ValueError as e:
        print(f"Invalid input: {e}")
        return get_numbers()


def find_min(numbers):
    """Returns min value in the list (without using built-in min)."""
    return numbers[0]


def find_max(numbers):
    """Returns max value in the list (without using built-in max)."""
    return numbers[-1]


def find_mean(numbers):
    """Returns the mean (average) of the list."""
    total = 0
    for num in numbers:
        total += num
    return total / len(numbers)


def find_mode(numbers):
    """Returns the mode (most frequent value)."""
    freq = {}
    mode_val, max_count = None, 0
    for num in numbers:
        freq[num] = freq.get(num, 0) + 1
        if freq[num] > max_count:
            max_count = freq[num]
            mode_val = num
    return mode_val


def find_median(numbers):
    """Returns the median of the list."""

    sz = len(numbers)
    mid = sz // 2

    if sz % 2 == 1:
        return numbers[mid]
    else:
        return (numbers[mid - 1] + numbers[mid]) / 2


def find_range(numbers):
    """Returns the range of the list."""
    return find_max(numbers) - find_min(numbers)


def find_variance(numbers):
    """Returns the variance of the list."""
    mean = find_mean(numbers)
    total = 0
    for num in numbers:
        total += (num - mean) ** 2
    return total / len(numbers)


def find_STD(numbers):
    """Returns the standard deviation."""
    return find_variance(numbers) ** 0.5


def find_Quartiles(numbers):
    """Returns Q1, Q2 and Q3 quartiles."""
    sz = len(numbers)

    def median(arr):
        mid = len(arr) // 2
        if len(arr) % 2 == 1:
            return arr[mid]
        else:
            return (arr[mid - 1] + arr[mid]) / 2

    Q1 = median(numbers[:sz // 2])
    Q2 = median(numbers)
    Q3 = median(numbers[(sz + 1) // 2:])
    return Q1, Q2, Q3


def find_IQR(numbers):
    """Returns the Interquartile Range (IQR)."""
    Q1, Q2, Q3 = find_Quartiles(numbers)
    return Q3 - Q1


# Get input numbers
nums = get_numbers()
sorted_nums = sorted(nums)

print(f"Etfdl 7agtk ya m3lm <3")
print(f"Min: {find_min(sorted_nums)}")
print(f"Max: {find_max(sorted_nums)}")
print(f"Mean: {find_mean(sorted_nums)}")
print(f"Mode: {find_mode(sorted_nums)}")
print(f"Median: {find_median(sorted_nums)}")
print(f"Range: {find_range(sorted_nums)}")
print(f"Variance: {find_variance(sorted_nums)}")
print(f"Standard Deviation: {find_STD(sorted_nums)}")
Q1, Q2, Q3 = find_Quartiles(sorted_nums)
print(f"Quartiles: (Q1={Q1}, Q2={Q2} Q3={Q3})")
print(f"Interquartile Range (IQR): {find_IQR(sorted_nums)}")

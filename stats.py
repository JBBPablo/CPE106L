from collections import Counter

def mean(numbers):
    """Returns the average (mean) of a list of numbers."""
    return sum(numbers) / len(numbers)

def median(numbers):
    """Returns the median value of a list of numbers."""
    numbers_sorted = sorted(numbers)
    n = len(numbers_sorted)
    mid = n // 2
    if n % 2 == 0:
        return (numbers_sorted[mid - 1] + numbers_sorted[mid]) / 2
    else:
        return numbers_sorted[mid]

def mode(numbers):
    """Returns the mode(s) of a list of numbers."""
    count = Counter(numbers)
    max_count = max(count.values())
    modes = [key for key, value in count.items() if value == max_count]
    return modes if len(modes) > 1 else modes[0]
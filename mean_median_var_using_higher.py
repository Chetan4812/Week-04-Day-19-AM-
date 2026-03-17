from functools import reduce

def compute_mean(numbers):
    return reduce(lambda x, y: x + y, numbers) / len(numbers)

def compute_median(numbers):
    sorted_nums = sorted(numbers)
    n = len(sorted_nums)
    mid = n // 2
    
    if n % 2 == 0:
        return (sorted_nums[mid - 1] + sorted_nums[mid]) / 2
    return sorted_nums[mid]

def compute_variance(numbers):
    mu = compute_mean(numbers)
    sq_diffs = map(lambda x: (x - mu) ** 2, numbers)
    return reduce(lambda x, y: x + y, sq_diffs) / len(numbers)

data = [10, 2, 38, 23, 38, 23, 21]
print(f"Mean: {compute_mean(data):.2f}")
print(f"Median: {compute_median(data)}")
print(f"Variance: {compute_variance(data):.2f}")

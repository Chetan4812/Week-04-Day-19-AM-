def compute_mean(numbers):
    total = 0.0
    for n in numbers:
        total += n
    return total / len(numbers)

def compute_median(numbers):
    sorted_nums = sorted(numbers)
    n = len(sorted_nums)
    mid = n // 2
    
    if n % 2 == 0:
        return (sorted_nums[mid - 1] + sorted_nums[mid]) / 2
    else:
        return sorted_nums[mid]

def compute_variance(numbers):
    mu = compute_mean(numbers)
    sum_sq_diff = 0.0
    for n in numbers:
        sum_sq_diff += (n - mu) ** 2
    return sum_sq_diff / len(numbers)

data = [10, 2, 38, 23, 38, 23, 21]
print(f"Mean: {compute_mean(data):.2f}")
print(f"Median: {compute_median(data)}")
print(f"Variance: {compute_variance(data):.2f}")

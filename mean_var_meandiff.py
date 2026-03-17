def get_stats(data):
    mean = sum(data) / len(data)
    variance = sum((x - mean) ** 2 for x in data) / len(data)
    return mean, variance

A = [12, 23, 3, 34, 45, 56, 5]
B = [12, 1, 3, 1, 1, 2, 3, 4, 5, 3, 4]

mean_a, var_a = get_stats(A)
mean_b, var_b = get_stats(B)
diff = abs(mean_a - mean_b)

print(f"Group A - Mean: {mean_a:.2f}, Variance: {var_a:.2f}")
print(f"Group B - Mean: {mean_b:.2f}, Variance: {var_b:.2f}")
print(f"Difference in Means: {diff:.2f}")

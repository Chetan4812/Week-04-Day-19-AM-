import numpy as np

def compute_std_deviation(numbers):
    if not numbers:
        return 0.0
    
    mu = sum(numbers) / len(numbers)
    
    variance = sum((x - mu) ** 2 for x in numbers) / len(numbers)
    
    return variance ** 0.5

data = [10, 20, 30, 40, 50]

manual_res = compute_std_deviation(data)
numpy_res = np.std(data)

print(f"Manual Result: {manual_res}")
print(f"NumPy Result:  {numpy_res}")
print(f"Match: {manual_res == numpy_res}")

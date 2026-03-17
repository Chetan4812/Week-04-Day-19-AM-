import numpy as np
from scipy import stats

def two_sample_t_test(sample1, sample2, alpha=0.05):
    m1, m2 = np.mean(sample1), np.mean(sample2)
    v1, v2 = np.var(sample1, ddof=1), np.var(sample2, ddof=1)
    

    t_stat, p_val = stats.ttest_ind(sample1, sample2, equal_var=False)
    
    is_significant = p_val < alpha
    
    return {
        "Mean 1": round(m1, 2), "Var 1": round(v1, 2),
        "Mean 2": round(m2, 2), "Var 2": round(v2, 2),
        "T-Statistic": round(t_stat, 3),
        "P-Value": round(p_val, 4),
        "Significant": is_significant
    }

# Sample Dataset
A = [12, 23, 3, 34, 45, 56, 5]
B = [12, 1, 3, 1, 1, 2, 3, 4, 5, 3, 4]

results = two_sample_t_test(A, B)
print(results)

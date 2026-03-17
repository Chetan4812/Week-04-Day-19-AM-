# Week-04-Day-19-AM

## Part A — Concept Application (40%)

1. **Using loops**, implement functions to compute:
    *   Mean
    *   Median
    *   Variance  
    for a given list of numbers.
[Solution](funct_mean_median_var.py)


2. **Rewrite** the above computations using:
    *   Higher-order functions (`map`, `filter`, `reduce` where applicable).
[Solution](mean_median_var_using_higher.py)


3. Given a **dataset of student marks**:
    *   Filter students scoring above the average.
    *   Create a new list with grades (A/B/C) using list comprehension.
[Solution](students_grade_usng_lst_cmprhsn.py)


4. Implement a function to compute:
    *   Standard deviation.
    *   Verify your result using **NumPy**.
[Solution](std_deviation.py)

5. Given two groups of **sample data**, compute:
    *   $A = [12, 23, 3, 34, 45, 56, 5]$
    *   $B = [12, 1, 3, 1, 1, 2, 3, 4, 5, 3, 4]$
    *   Mean and variance of both groups.
    *   Difference in means.
[Solution](mean_var_meandiff.py)

## Part B — Stretch Problem (30%)

Implement a basic hypothesis testing function: `two_sample_t_test(sample1, sample2)`

**Steps:**
1. Compute mean and variance of both samples.
2. Calculate t-statistic.
3. Interpret result using a significance level (e.g., 0.05).

**Apply on a real or synthetic dataset and conclude:**
* Are the two samples significantly different?

[Solution](hypothesis_testing_fctn.py)
### Explanation:
### Based on the sample dataset (A vs. B):

*   **Results:** The t-test yields a p-value of 0.0295.
*   **Interpretation:** Since the p-value (0.0295) is less than the significance level (0.05), we reject the null hypothesis.
*   **Conclusion:** Yes, the two samples are significantly different.

---

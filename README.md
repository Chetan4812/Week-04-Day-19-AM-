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
## Part C — Interview Ready (20%)

**Q1 — What is the difference between loops, list comprehension, and higher-order functions in Python? When would you use each?**

## 1. Comparison Overview


| Feature | **Loops (`for` / `while`)** | **List Comprehension** | **Higher-Order Functions** |
| :--- | :--- | :--- | :--- |
| **Paradigm** | **Imperative**: Focuses on *how* to do it step-by-step. | **Declarative**: Focuses on *what* the resulting list should be. | **Functional**: Uses functions as arguments to process data. |
| **Readability** | Best for complex logic with side effects. | Best for simple, one-line transformations. | Best for abstracting logic or chaining operations. |
| **Performance** | Standard; manual overhead. | **Fastest** (optimized at C-level). | Memory-efficient (uses generators). |

---

## 2. When to Use Each

### 🟢 Loops
* Use Loops when your logic is complex, involves multiple steps, or requires break/continue statements.
### 🟢 List Comprehensions 
* Use List Comprehensions for simple transformations or filtering where you want to create a new list in a single, readable line.
### 🟢 Higher-Order
* Use Higher-Order Functions (map, filter, reduce) when you want to pass functional logic as an argument or chain operations together.

**Q2 (Coding) — Implement a function using list comprehension to:**
*   Flatten a nested list
*   Remove all even numbers

```python
def flatten_and_filter(nested_list):
    return [item for sublist in nested_list for item in sublist if item % 2 != 0]

# Example
data = [[1, 2, 3], [4, 5, 6], [7, 8]]
print(flatten_and_filter(data)) 
# Output: [1, 3, 5, 7]
```

**Q3 — What is hypothesis testing? Explain null hypothesis, p-value, and significance level with an example.**

Hypothesis Testing is a statistical method used to decide if there is enough evidence in a sample of data to infer that a certain condition is true for the entire population.
* Null Hypothesis (H0): The "default" assumption that there is no effect or no difference. (e.g., "This new drug works the same as a sugar pill.")
* P-value: The probability that your observed data occurred by random chance if the Null Hypothesis is true. A low p-value means the result is unlikely to be a fluke.
* Significance Level (alpha): Your "line in the sand" (usually 0.05). If the p-value is smaller than alpha, you reject the Null Hypothesis.

Example:
* Scenario: Think a specific fertilizer makes plants grow taller.
* H0: The fertilizer has no effect on height.
* Result: You get a p-value of 0.03.
* Conclusion: Since 0.03 < 0.05, you reject H0. The fertilizer likely does make a difference.

---
## Part D — AI-Augmented Task (10%)

1. **Prompt AI:**  
   "Explain descriptive statistics and hypothesis testing with a Python example using real-world data."

2. **Document prompt and output**  
   "Prompt: Explain descriptive statistics and hypothesis testing with a Python example using real-world data."
   [AI Output](output.md)
   
4. **Evaluate:**
    *   Is the explanation clear and correct?
    *   Is the code logically structured and runnable?

## 1. Explanation correctness
**Yes.** The explanation accurately distinguishes between the two branches of statistics:
*   **Descriptive Statistics:** Correctly identified as a method to summarize existing data (mean, median, standard deviation) without making broader inferences.
*   **Hypothesis Testing:** Correctly defined as a framework for making population-level inferences. The definitions for the **Null Hypothesis ($H_0$)**, **P-value**, and **Significance Level ($\alpha$)** align with standard statistical theory.
*   **Contextual Accuracy:** Using the "Tips" dataset highlights a critical real-world lesson: a difference in sample means (e.g., $3.09 vs $2.83) does not automatically imply a statistically significant difference.

## 2. Code logically structured and runnable?
**Yes.** The code follows a professional data science workflow:
*   **Modular Design:** It separates data loading, descriptive analysis, and inferential testing into distinct blocks.
*   **Modern Syntax:** The use of `observed=True` in the `groupby` function ensures compatibility with the latest versions of Pandas when handling categorical data.
*   **Library Choice:** Using `seaborn` for data and `scipy.stats` for testing is the standard "Pythonic" approach, making the code easy to maintain.
*   **Actionable Output:** The inclusion of an `if-else` block to interpret the p-value transforms raw numbers into a clear, binary conclusion (Reject vs. Fail to Reject).


### Suggested Refinement for Robustness
To make the code even more resilient to real-world data (where group variances are rarely equal), we can use **Welch’s T-test** by adding one parameter:

```python
# Use equal_var=False to perform Welch's T-test
t_stat, p_val = stats.ttest_ind(male_tips, female_tips, equal_var=False)
```









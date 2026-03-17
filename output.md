# Statistics in Python: Descriptive vs. Inferential

This guide explains **Descriptive Statistics** and **Hypothesis Testing** using a real-world dataset (Tipping behavior).

## 1. Descriptive Statistics
Descriptive statistics summarize the characteristics of a data set. They answer "What does the data look like?"

*   **Mean**: The average value.
*   **Median**: The middle value when data is sorted.
*   **Standard Deviation**: How spread out the numbers are from the mean.
*   **Variance**: The square of the standard deviation.

## 2. Hypothesis Testing
Hypothesis testing uses sample data to make inferences about a population. It answers "Is this effect real or just a fluke?"

*   **Null Hypothesis ($H_0$)**: The assumption of **no effect** (e.g., "Men and women tip the same").
*   **P-value**: The probability that your result happened by chance. 
*   **Significance Level ($\alpha$)**: Usually **0.05**. If $P < 0.05$, we reject the Null Hypothesis.

---

## 3. Python Implementation (using `seaborn` & `scipy`)

```python
import seaborn as sns
import scipy.stats as stats

# Load real-world dataset
df = sns.load_dataset('tips')

# --- PART 1: Descriptive Statistics ---
print("--- Summary Statistics ---")
print(df.describe()) # Provides count, mean, std, min, max, and quartiles

# Specific comparison
avg_tip = df.groupby('sex', observed=True)['tip'].mean()
print(f"\nAverage Tip (Male):   ${avg_tip['Male']:.2f}")
print(f"Average Tip (Female): ${avg_tip['Female']:.2f}")

# --- PART 2: Hypothesis Testing (T-Test) ---
# Goal: Test if gender significantly affects tip amount
male_tips = df[df['sex'] == 'Male']['tip']
female_tips = df[df['sex'] == 'Female']['tip']

t_stat, p_val = stats.ttest_ind(male_tips, female_tips)

print(f"\nP-Value: {p_val:.4f}")

# Interpretation
if p_val < 0.05:
    print("Conclusion: Significant difference exists (Reject Null).")
else:
    print("Conclusion: No significant difference (Fail to Reject Null).")

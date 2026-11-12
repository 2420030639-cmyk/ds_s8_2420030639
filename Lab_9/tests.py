"""Use hypothesis tests to compare student marks."""

import numpy as np
from scipy.stats import ttest_ind
from statsmodels.stats.weightstats import ztest


def print_result(p, threshold=0.05):
    message = "Reject Null Hypothesis" if p < threshold else "Fail to Reject Null Hypothesis"
    print("\nResult:", message)


def run_tests():
    print("----- Z-Test -----")
    student_scores = np.array([78, 82, 85, 88, 90, 76, 95, 89, 84, 91])
    reference_average = 80

    z_value, z_probability = ztest(student_scores, value=reference_average)
    print("Sample Marks:")
    print(student_scores)
    print("\nPopulation Mean:", reference_average)
    print("\nZ-Statistic:", z_value)
    print("P-Value:", z_probability)
    print_result(z_probability)

    print("\n----- Independent t-Test -----")
    first_class = np.array([78, 82, 85, 88, 90])
    second_class = np.array([72, 75, 70, 68, 74])

    t_value, t_probability = ttest_ind(first_class, second_class)
    print("Class A Marks:")
    print(first_class)
    print("\nClass B Marks:")
    print(second_class)
    print("\nt-Statistic:", t_value)
    print("P-Value:", t_probability)
    print_result(t_probability)


if __name__ == "__main__":
    run_tests()

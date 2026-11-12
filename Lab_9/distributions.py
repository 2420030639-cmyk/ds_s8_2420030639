"""Explore Bernoulli and Binomial probabilities with exam results."""

from scipy.stats import bernoulli as bernoulli_dist
from scipy.stats import binom as binomial_dist


def run_distributions():
    probability_pass = 0.7

    print("----- Bernoulli Distribution -----")
    student_results = bernoulli_dist.rvs(probability_pass, size=10)
    print("Probability of Passing:", probability_pass)
    print("Student Outcomes (1=Pass, 0=Fail):")
    print(student_results)

    pass_chance = bernoulli_dist.pmf(1, probability_pass)
    fail_chance = bernoulli_dist.pmf(0, probability_pass)
    print("\nProbability of Pass:")
    print(pass_chance)
    print("Probability of Fail:")
    print(fail_chance)

    print("\n----- Binomial Distribution -----")
    class_size = 10
    target_passes = 8
    target_probability = binomial_dist.pmf(
        target_passes, class_size, probability_pass
    )

    print("Number of Students:", class_size)
    print("Probability of Passing:", probability_pass)
    print(f"Probability that exactly {target_passes} students pass:")
    print(target_probability)

    class_trials = binomial_dist.rvs(class_size, probability_pass, size=5)
    print("\nRandom Binomial Outcomes:")
    print(class_trials)


if __name__ == "__main__":
    run_distributions()

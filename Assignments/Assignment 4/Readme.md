# Comparison of Normal Distributions with Different Standard Deviations


# 1. Introduction

In probability theory and statistics, the Normal Distribution (also known as Gaussian Distribution) is one of the most fundamental continuous probability distributions. It plays a central role in statistical inference, hypothesis testing, quality control, economics, engineering, and data science.

A normal distribution is completely determined by two parameters:

Mean (μ) — Measure of central tendency

Standard Deviation (σ) — Measure of dispersion

In this assignment, we analyze and compare three normal distributions that share the same mean (μ = 55) but differ in standard deviation (σ = 4, 10, 15). The objective is to determine which distribution is more stable, consistent, and statistically preferable under different conditions.

Here, we compare three classes:

* Class 4A (σ = 4)
* Class 4B (σ = 10)
* Class 4C (σ = 15)

All three classes have the same mean score (μ = 55), but they differ in their standard deviation. Using the Normal Distribution and the Empirical Rule, we analyze which class performs better and why.


# 2. Given Data

## 2.1 Mean (μ)

Mean score for all classes:

μ = 55

This means the average marks scored by students in each class is 55.

## 2.2 Standard Deviation (σ)

Standard deviation measures how spread out the marks are from the mean.

* Class 4A → σ = 4
* Class 4B → σ = 10
* Class 4C → σ = 15

Although the average marks are the same, the variation in marks differs significantly.

# 3. Theory of Normal distribution

## 3.1 Definition

The Normal Distribution, also known as the Gaussian Distribution, is a fundamental concept in statistics and probability theory. It describes a continuous probability distribution characterized by a symmetric, bell-shaped curve where most of the observations cluster around the mean, and probabilities taper off equally on both sides.

## 3.2 Key Properties

Symmetry – The curve is symmetric about the mean (μ).

Mean, Median, Mode – All are equal and located at the center of the distribution.

Standard Deviation (σ) – Measures the spread or dispersion of the data around the mean.

Probability Density Function (PDF) – The mathematical expression of the normal distribution is:

Total area under the curve equals 1.

f(x) = 1 / (σ √(2π)) * e^(-(x - μ)^2 / (2σ^2))

Where:

𝑥 = variable

𝜇 = mean

𝜎 = standard deviation

𝑒 = Euler’s number (~2.71828)

68–95–99.7 Rule – Approximately 68% of data lies within 1σ, 95% within 2σ, and 99.7% within 3σ of the mean.

## 3.3 Mean (μ)

The **mean** is the average value of a dataset and represents the central point around which data values are distributed. It is calculated by:

Mean (μ) = Σxᵢ / n

Where:

* xᵢ = each data point
* n = total number of data points

**Importance:**

* Indicates the central tendency of data.
* Serves as a reference for variance and standard deviation.
* Helps predict expected outcomes, like average sales.

## 3.4 Standard Deviation (σ)

**Standard Deviation** measures the spread or dispersion of data values around the mean. It shows whether data points are close to the mean (low variability) or widely spread out (high variability).

Standard Deviation (σ) = √(Σ(xᵢ - μ)² / n)

Where:

* xᵢ = each data point
* μ = mean of the dataset
* n = total number of data points

**Importance:**

* Quantifies variability or risk.
* Supports the Empirical Rule for normal distributions.
* Essential for forecasting, decision-making, and detecting outliers.


# 4. Understanding Standard Deviation in Academic 

Standard deviation indicates consistency.

* Low standard deviation → Students perform similarly.
* High standard deviation → Marks vary widely among students.

In an academic environment, consistency is often preferred because it indicates uniform understanding of concepts across students.


# 5. Application of Empirical Rule (68–95–99.7 Rule)

The Empirical Rule states:

* 68% of data lies within 1σ of the mean.
* 95% lies within 2σ.
* 99.7% lies within 3σ.

Let us apply this to each class.


# 6. Comparison of Classes 4A, 4B, and 4C Using Mean and Standard Deviation

<img width="592" height="455" alt="ec71c0b5-b70e-4243-a444-74327db6b76f" src="https://github.com/user-attachments/assets/a882757c-1261-44bc-b526-4ab82e00dbae" />

## 1. Same Mean for All Classes

All three classes have the same mean value (μ = 55), indicating that the average performance of students in classes 4A, 4B, and 4C is equal. Therefore, the mean alone cannot be used to determine which class is better.

## 2. Standard Deviation (σ)

* Standard deviation quantifies the dispersion of data around the mean.
* Formula: (σ) = √(Σ(xᵢ - μ)² / n)
* Smaller σ indicates that data points are close to the mean, implying uniform performance.
* Larger σ indicates wider spread, suggesting inconsistent performance among students.


# 7. Performance Range of Classes

## 7.1 Class 4A (Blue)

**Range:** μ ± σ = 55 ± 4 = 51 to 59

**Interpretation:**

* Most students scored between 51 and 59.
* Narrow range → high consistency and uniform performance.

## 7.2 Class 4B (Orange)

**Range:** μ ± σ = 55 ± 10 = 45 to 65

**Interpretation:**

* Most students scored between 45 and 65.
* Moderate range → moderate variation in performance.

## 7.3 Class 4C (Green)

**Range:** μ ± σ = 55 ± 15 = 40 to 70

**Interpretation:**

* Students scored between 40 and 70.
* Wide range → high variation, inconsistent performance.

# 8. Comparison Based on Consistency

| Class | σ (Standard Deviation) | Range | Consistency |
| ----- | ---------------------- | ----- | ----------- |
| 4A    |           4            | 51–59 | High        |
| 4B    |          10            | 45–65 | Moderate    |
| 4C    |          15            | 40–70 | Low         |

**Explanation:**

* Class 4A has the smallest range (51–59) and the least variation.
* Class 4B has a moderate range (45–65).
* Class 4C has the widest range (40–70), showing maximum variation.

When the mean of all classes is the same, the class with the minimum standard deviation is considered the best. Hence, **Class 4A** is the best class because it shows maximum consistency and minimum variation around the mean value of 55.


# 9. Graphical Interpretation

In the above graph of normal distribution curves:

* Class 4A will have a tall and narrow bell curve.
* Class 4B will have a moderately wide curve.
* Class 4C will have a very wide and flat curve.

A narrow curve indicates high consistency.
A wider curve indicates high variability.


# 10. Which Class is Better?

Although all classes have the same mean score (55), the better class is the one with lower variability.

Class 4A (σ = 4) is better because:

* Student performance is consistent.
* Very few extreme low scores.
* Stable academic outcome.
* Better predictability of results.

Class 4B is average in terms of consistency.

Class 4C shows high inequality in student performance and therefore is less stable.


# 11. Conclusion

When comparing classes with the same mean but different standard deviations, the class with the smallest standard deviation is considered better in terms of consistency and stability.

Since:

* μ = 55 for all classes
* σ4A = 4
* σ4B = 10
* σ4C = 15

Class 4A performs better overall because student marks are closely concentrated around the mean.

This analysis demonstrates that mean alone is not sufficient to evaluate performance. Standard deviation plays a critical role in understanding data distribution and consistency.


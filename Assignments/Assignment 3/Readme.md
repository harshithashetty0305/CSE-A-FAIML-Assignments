# Normal Distribution and Empirical Rule

## Domain: Daily Sales in Supermarket


# 1. Introduction

The Normal Distribution is one of the most widely used statistical distributions in business analytics. It helps in understanding how values are spread around an average.In the context of daily sales in a supermarket, understanding this distribution helps stakeholders predict sales patterns, manage inventory, and optimize operations.

By modeling daily sales with a Normal Distribution, businesses can leverage statistical tools to forecast trends, assess risks, and make data-driven decisions.In this report, we analyze **Daily Sales in a Supermarket** using the Normal Distribution and explain the Empirical Rule (68–95–99.7 Rule).

The graphical representation shows how daily sales are distributed around the average sales value.


# 2. Domain Explanation: Daily Sales in Supermarket

## 2.1 Why Daily Sales?

Daily sales in a supermarket represent the total revenue generated from all products sold within a single day. This includes sales from groceries, vegetables, dairy products, packaged foods, household items, personal care products, and other consumer goods. Supermarket sales are influenced by multiple factors such as customer footfall, seasonal demand, discounts, festivals, holidays, weather conditions, and promotional campaigns.

In real-world retail business, daily sales do not remain constant. Most days generate sales close to an average value, while a few days may show extremely high sales (during festivals or special offers) or extremely low sales (due to unexpected closures or low demand). Because of this natural variation, daily sales data often forms a bell-shaped pattern when plotted over a long period.

Understanding the distribution of daily sales is important for:

- Revenue forecasting
- Inventory management
- Staff scheduling
- Profit analysis
- Business performance evaluation

When sales data is collected over many days and plotted on a graph, it tends to cluster around a central average value. This clustering with gradual decrease on both sides forms a Normal Distribution curve. Therefore, daily supermarket sales is a suitable and practical domain to explain the Normal Distribution and the Empirical Rule.

## 2.2 Assumed Parameters for Analysis

For this domain, we assume:

* Mean (μ) = ₹500,000 per day
* Standard Deviation (σ) = ₹50,000

These values help demonstrate the Empirical Rule clearly.


# 3. Understanding Normal Distribution

## 3.1 Definition

A Normal Distribution is a continuous probability distribution that describes how numerical data is spread around a central value (mean). It is symmetric in shape, meaning the left side and right side of the curve are mirror images of each other. Most of the observations cluster around the mean, and the frequency of values decreases gradually as we move away from the center.

It is defined using two important parameters:

Mean (μ) – The center of the distribution. It represents the average value of the dataset and determines where the peak of the bell-shaped curve lies.

Standard Deviation (σ) – The measure of dispersion or spread of the data. It indicates how far the values are distributed from the mean. A small standard deviation results in a narrow and tall curve, while a large standard deviation produces a wider and flatter curve.

In the context of daily supermarket sales, the mean represents the average daily revenue, and the standard deviation shows how much daily sales typically vary from that average.

## 3.2 Key Characteristics

* Bell-shaped curve
* Symmetrical around mean
* Mean = Median = Mode
* Total area under curve = 1


# 4. Empirical Rule (68–95–99.7 Rule)

The Empirical Rule explains how data is distributed within standard deviations from the mean.

<img width="584" height="455" alt="ea29866d-a70b-4aea-82af-4c131d656c89" src="https://github.com/user-attachments/assets/fc153cbf-fe51-417b-b9ca-df3670b00e1c" />

## 4.1 68% of Data (Within 1 Standard Deviation)

μ ± 1σ → ₹500,000 ± ₹50,000
Range: ₹450,000 to ₹550,000

Approximately 68% of daily sales fall within this range.


## 4.2 95% of Data (Within 2 Standard Deviations)

μ ± 2σ → ₹500,000 ± ₹100,000
Range: ₹400,000 to ₹600,000

About 95% of daily sales lie within this range.


## 4.3 99.7% of Data (Within 3 Standard Deviations)

μ ± 3σ → ₹500,000 ± ₹150,000
Range: ₹350,000 to ₹650,000

Almost all daily sales values fall within this range.


# 5. Graphical Representation

The above graph displays:

* A bell-shaped normal distribution curve
* Vertical lines at:

  * Mean (μ)
  * μ ± 1σ
  * μ ± 2σ
  * μ ± 3σ

The center peak represents the most frequent daily sales value. As we move away from the mean, the probability of occurrence decreases.


# 6. Business Interpretation

## 6.1 Performance Monitoring

Performance monitoring is one of the most important applications of the Normal Distribution in retail management. By comparing daily sales with the mean and standard deviation, management can quickly evaluate whether business performance is stable or unusual.

Normal (within 1σ): If daily sales fall within one standard deviation from the mean, it indicates stable and expected performance. These are regular business days where sales are operating within normal variation.

Slightly Unusual (within 2σ): If sales fall between 1σ and 2σ from the mean, the variation is noticeable but still acceptable. Management may review factors such as weekday patterns or minor promotions.

Highly Unusual (beyond 3σ): If sales lie beyond three standard deviations, it signals an abnormal event. Immediate investigation may be required to understand the cause.

Using this approach, managers can continuously track performance and ensure business operations remain under control.


## 6.2 Identifying Outliers

Outliers are values that significantly differ from the majority of data points. In the case of daily supermarket sales, any value below ₹350,000 or above ₹650,000 falls outside the 3σ range and is considered highly unusual.

Such extreme values may indicate:

Special promotional campaigns or discount offers

Seasonal demand during festivals or holidays

Supply chain disruptions

Store closures or operational issues

Identifying outliers helps management understand unexpected patterns and take corrective or strategic action.


## 6.3 Decision Making

Understanding how sales are distributed enables better strategic and operational decisions. When managers know the expected sales range, they can plan resources more effectively.

Inventory Planning: Stock levels can be adjusted according to expected sales variation.

Staffing Decisions: Workforce scheduling can match anticipated customer traffic.

Sales Forecasting: Historical distribution helps predict future revenue trends.

Risk Management: Businesses can prepare contingency plans for extreme sales scenarios.

Thus, the Normal Distribution and Empirical Rule provide a structured and data-driven framework for informed decision-making in supermarket management.


# 7. Mathematical Formula

The probability density function of the Normal Distribution is:

f(x) = (1 / (σ√2π)) e^(-(x - μ)^2 / 2σ^2)

μ (Mean) – Represents the average value of the dataset and determines the center of the distribution.

σ (Standard Deviation) – Measures the spread or dispersion of the data around the mean.

π (Pi) – A mathematical constant approximately equal to 3.14159.

e – Euler’s number, approximately equal to 2.718, which is the base of the natural logarithm.

x – The value of the random variable for which the probability density is calculated.


# 8. Advantages of Using Normal Distribution in Business

* Helps predict expected sales
* Identifies unusual sales patterns
* Supports forecasting models
* Improves strategic planning


# 9. Conclusion

The Normal Distribution provides a powerful statistical tool for analyzing supermarket daily sales. Using the Empirical Rule, we can clearly understand how sales are distributed around the average value.

The graph demonstrates:

✔ Symmetry around mean
✔ Predictable spread using standard deviation
✔ Majority of sales within expected range

This analysis helps businesses make data-driven decisions and improve operational efficiency.


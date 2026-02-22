# Variance and Bias in Machine Learning (Underfitting, Overfitting, and Best Fit Model)

## 1. Introduction

Machine Learning (ML) is a branch of Artificial Intelligence that enables computers to learn patterns from data and make predictions or decisions without being explicitly programmed. Instead of writing step-by-step rules, we train models using data so that they automatically learn relationships.

To build a successful ML system, it is important to understand:

* What ML models are
* What training and testing mean
* What underfitting and overfitting are
* The role of bias and variance
* Which combination of bias and variance gives the best fit model

# 2. Machine Learning Models

## 2.1 What is a Machine Learning Model?

A Machine Learning model is a mathematical representation of a real-world process. It learns patterns from input data and uses those patterns to make predictions.

For example:

* Predicting house prices
* Detecting spam emails
* Recommending movies
* Classifying images

The model takes input features (independent variables) and produces an output (dependent variable).

## 2.2 Types of Machine Learning Models

### Supervised Learning Models

* Linear Regression
* Logistic Regression
* Decision Trees
* Support Vector Machines
* Neural Networks

These models learn from labeled data.

### Unsupervised Learning Models

* K-Means Clustering
* Hierarchical Clustering
* PCA

These models find patterns in unlabeled data.

# 3. Training and Testing in Machine Learning

## 3.1 Training Phase

Training is the process where the model learns from historical data.

During training:

* The model is given input data
* The model predicts output
* The prediction is compared with actual output
* The error is calculated
* Model parameters are adjusted to reduce error

Goal: Minimize training error.

## 3.2 Testing Phase

Testing evaluates how well the model performs on unseen data.

* The model does not learn during testing
* It only makes predictions
* Performance is measured using accuracy, error rate, etc.

Goal: Measure generalization ability.


## 3.3 Why Separate Training and Testing?

If we evaluate only on training data, the model may appear very accurate but may fail on new data. This is why testing data is important.


# 4. Bias in Machine Learning

## 4.1 What is Bias?

Bias is the error caused by simplifying assumptions in the model.

High bias means:

* Model is too simple
* Cannot capture complexity
* Leads to underfitting

Low bias means:

* Model captures patterns well
* Better training performance


# 5. Variance in Machine Learning

## 5.1 What is Variance?

Variance measures how much model predictions change with different training data.

High variance means:

* Model is very sensitive
* Learns noise
* Leads to overfitting

Low variance means:

* Stable model
* Good generalization

# 6. Underfitting

## 6.1 Definition

Underfitting occurs when a model is too simple to capture the underlying pattern in data.

## 6.2 Characteristics

* High training error
* High testing error
* High bias
* Low variance

## 6.3 Causes

* Model too simple
* Insufficient features
* Not enough training

## 6.4 Example

Using a straight line to model curved data leads to underfitting.


# 7. Overfitting

## 7.1 Definition

Overfitting occurs when a model learns the training data too well, including noise.

## 7.2 Characteristics

* Very low training error
* High testing error
* Low bias
* High variance

## 7.3 Causes

* Model too complex
* Too many features
* Small dataset
* No regularization

## 7.4 Example

A very high-degree polynomial perfectly fitting all training points but failing on new data.

# 8. Combinations of Bias and Variance

## 8.1 Low Bias and High Variance

* Model captures training data well
* Overfits
* Low training error
* High testing error

Result: Overfitting

## 8.2 Low Bias and Low Variance

* Model captures true pattern
* Stable predictions
* Low training error
* Low testing error

Result: Best Fit Model

## 8.3 High Bias and High Variance

* Poor learning
* Unstable predictions
* High training error
* High testing error

Result: Very Poor Model

## 8.4 High Bias and Low Variance

* Too simple model
* Stable but inaccurate
* High training error
* High testing error

Result: Underfitting

# 9. Which is best fit model

### Answer:

Low Bias and Low Variance

Explanation:

* High bias causes underfitting
* High variance causes overfitting
* Best model balances both

Therefore, the best fit model must have:

* Low Bias
* Low Variance
* Good Generalization

# 10. Bias–Variance Tradeoff

There is a tradeoff between bias and variance.

* Increasing model complexity → Decreases bias, Increases variance
* Decreasing model complexity → Increases bias, Decreases variance

Total Error Formula:

Total Error = Bias² + Variance + Irreducible Error

Goal: Minimize Bias² + Variance.


# 11. Comparison Table

| Model Type   | Training Error | Testing Error | Bias | Variance |
| ------------ | -------------- | ------------- | ---- | -------- |
| Underfitting | High           | High          | High | Low      |
| Overfitting  | Low            | High          | Low  | High     |
| Best Fit     | Low            | Low           | Low  | Low      |

# 12. Methods to Control Bias and Variance

## To Reduce High Bias (Underfitting):

- Increase model complexity
- Add more relevant features
- Reduce excessive regularization
- Train the model properly

## To Reduce High Variance (Overfitting):

- Collect more training data
- Apply regularization (L1, L2)
- Use cross-validation
- Perform feature selection
- Apply early stopping

# 13. Real world Application

- Recommendation Systems (Netflix, Amazon)
- Stock Market Prediction
- Self-Driving Cars
- Medical Diagnosis Systems

# 14. Conclusion

Machine Learning models learn patterns from data through training and are evaluated using testing data. If a model is too simple, it underfits due to high bias. If a model is too complex, it overfits due to high variance.

The ideal situation is a balanced model with:

- Low Bias
- Low Variance
- Low Training Error
- Low Testing Error
- Strong Generalization Ability

Understanding bias and variance helps in selecting the correct model complexity and building efficient Machine Learning systems.



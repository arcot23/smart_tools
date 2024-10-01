## Machine Learning

A machine learning algorithm is the one that is able to learn from data. These algorithms can be categorized into following :

- Classification. E.g., Fish or Mammals
- Regression. E.g., Predicting price of an automobile based on make, model, engine, HP, etc.
- Clustering. E.g., Fit emails into technology, personnel, etc
- Rule-extraction. E.g., Recommendation systems.


These algorithms are classified into:

- Supervised learning
    - have labels. e.g., classification models
    - has two phases:
        - Training phase
        - Prediction phase
    - focusses on features (a.k.a. x variables, feature vectors)
    - predicts labels (a.k.a y variables). They can be categorical (classification) or continuous (regression)
- unsupervised learning
    - do not have labels (and only has features). e.g., clustering
    - find patterns or structures within data

Data falls into:
- Continous: can take infinite set of values
- Categorical: can take a finite set of values (like days of the week or binary variables like true/false)

**Standardized data:**

Standardizing the numeric data requires calculating $\frac {x - \bar{x}}{\sqrt\frac{\Sigma (x- \bar{x})^2}{n-1}\\}\ $ Understanding Mean and Variance:

- Mean (or average) i.e., $\bar{x}$: one number that represents all the data points ($n$).
- Range: Highest minus Smallest number
- Variance: This is based on this series of calculations
    - Mean Deviation: How far away is every data point from the average
    - Squared Mean Deviation: Square of the mean deviation.
    - Variance: Sum of the square of the every distance of the data points from the mean divided by the number of data points.
    - Variance (Bassel's Correction): Sum of the square of the every distance of the data points from the mean divided by the number of data points.
- Standard Deviation: Square root of variance

$$ Mean (\bar{x}) = \frac{x_1 + x_2 + ... + x_n}{n}\ $$
$$ Range = x_{max} - x_{min} $$
$$ Mean Deviation = (x- \bar{x}) $$
$$ Squared Mean Deviation =  (x- \bar{x})^2 $$
$$ Variance = \frac{\Sigma (x- \bar{x})^2}n $$
$$ Variance (Bassel's Correction) = \frac{\Sigma (x- \bar{x})^2}{n-1}\ $$
$$ Standard Deviation = \sqrt\frac{\Sigma (x- \bar{x})^2}{n-1}\\ $$

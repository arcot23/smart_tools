## Machine Learning

A machine learning algorithm is the one that is able to learn from data. These algorithms can be categorized into following :

**Classification:** Classification is a machine learning technique to predict correct label for a given input data. With an input training dataset, classification algorithms can identify categories and classify subsequent data accordingly.E.g., Fish or Mammals.

**Regression:** Regression is a supervised machine learning technique which is used to predict continuous values. The ultimate goal of the regression algorithm is to plot a best-fit line or a curve between the data. The three main metrics that are used for evaluating the trained regression model are variance, bias and error. E.g., Predicting price of an automobile based on make, model, engine, HP, etc.

**Clustering:** Clustering is an unsupervised machine learning technique designed to group unlabeled data based on their similarity to each other. If the data are labeled, then the grouping is *classification*. E.g., Fit emails into technology, personnel, etc

**Rule-extraction:** E.g., Recommendation systems.

These algorithms are classified into:

- Supervised learning: These algorithms have labels. e.g., classification models. There are two phases to the development of this model: Training phase and Prediction phase
    - focusses on features (a.k.a. x variables, feature vectors)
    - predicts labels (a.k.a y variables). They can be categorical (classification) or continuous (regression)
- Unsupervised learning
    - do not have labels (and only has features). e.g., clustering
    - find patterns or structures within data

## Data Standardization

Before running a machine learning algorithm, a given data must be cleansed and standardized. Any data to a model falls into two types:
- Continous data: In machine learning, "continuous data" refers to a type of numerical data that can take on any value within a given range, meaning it can be measured with infinite precision and can include decimals or fractions, unlike discrete data which is restricted to specific values; examples include height, weight, temperature, or the time taken to complete a task, where any value within a certain range is possible. 
- Categorical data: Categorical data in machine learning is non-numerical information that is organized into groups or categories. It can be used to represent qualitative or descriptive characteristics, such as the colors of house exteriors or the names of streets in a city. 

### Numeric data

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

## Scikit-learn

### Classification Algorithms

Scikit-learn provides a wide range of classification algorithms. Here are a few common ones:

Simple and Efficient:
- Logistic Regression: A linear model for binary classification problems.
- K-Nearest Neighbors (KNN): Classifies data points based on the majority class of their k nearest neighbors.
- Naive Bayes: A probabilistic classifier based on Bayes' theorem, particularly suitable for text classification.
- Decision Trees: Builds a tree-like model of decisions and their possible consequences.

Ensemble Methods (Combining Multiple Models):

Random Forest:
An ensemble of decision trees, often providing high accuracy and robustness.

AdaBoost:
Combines multiple weak classifiers into a strong classifier, iteratively adjusting weights to focus on misclassified samples.

Gradient Boosting Machines (GBM):
Builds an ensemble of trees sequentially, with each tree correcting the errors of the previous ones.

Support Vector Machines (SVMs):
- SVC (Support Vector Classifier): Finds a hyperplane that maximizes the margin between classes. Effective in high-dimensional spaces.
- LinearSVC: A faster implementation of SVC for linear kernels.

Neural Networks:
- MLPClassifier (Multi-layer Perceptron): A feedforward neural network for classification tasks.

### Regression Algorithms

Scikit-learn offers a variety of regression algorithms. Here are a few common ones:

Linear Models:
- Linear Regression: The simplest and most widely used.
- Ridge Regression: Adds L2 regularization to linear regression, useful when dealing with multicollinearity.
- Lasso Regression: Adds L1 regularization, which can lead to feature selection by shrinking some coefficients to zero.
- ElasticNet: Combines L1 and L2 regularization.

Tree-Based Models:

Decision Tree Regressor:
Builds a tree-like model to predict continuous values. Easy to interpret but prone to overfitting.

Random Forest Regressor:
An ensemble method that combines multiple decision trees, reducing overfitting and improving accuracy.

Gradient Boosting Regressor:
Another ensemble method that builds trees sequentially, with each tree correcting the errors of the previous ones.

Other Models:
- Support Vector Regression (SVR): Uses support vectors to find the best fit line, effective in high-dimensional spaces.
- KNeighborsRegressor: Predicts values based on the average of the k nearest neighbors.
- Bayesian Ridge Regression: Uses Bayesian inference to estimate the regression coefficients, providing uncertainty estimates for predictions.

### Clustering Algorithms

Scikit-learn provides a variety of clustering algorithms. Here are a few of the most common ones:

K-Means:
A simple and efficient algorithm that partitions data into K clusters based on their proximity to centroids.

Hierarchical Clustering:
Builds a hierarchy of clusters by either merging (agglomerative) or splitting (divisive) them based on their similarity.

DBSCAN:
Density-based clustering that identifies clusters based on the density of data points in a region.

Mean-Shift:
Finds clusters by iteratively shifting points towards the mode of their local density.

Spectral Clustering:
Uses the eigenvectors of a similarity matrix to perform clustering, often providing better results for non-convex clusters.

Gaussian Mixture Models (GMM):
A probabilistic model that assumes data points are generated from a mixture of Gaussian distributions.

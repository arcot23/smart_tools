## Machine Learning

A machine learning algorithm is the one that is able to learn from data. 

### Machine learning techniques

Machine language techniques can be broadly classified into:

**Classification:** Classification is a machine learning technique to predict correct label for a given input data. With an input training dataset, classification algorithms can identify categories and classify subsequent data accordingly.E.g., Fish or Mammals.

**Regression:** Regression is a supervised machine learning technique which is used to predict continuous values. The ultimate goal of the regression algorithm is to plot a best-fit line or a curve between the data. E.g., Predicting price of an automobile based on make, model, engine, HP, etc.

**Clustering:** Clustering is an unsupervised machine learning technique designed to group unlabeled data based on their similarity to each other. If the data are labeled, then the grouping is *classification*. E.g., Fit emails into technology, personnel, etc

**Rule-extraction:** E.g., Recommendation systems.

### Machine learning types

- Supervised learning: Supervised learning is a machine learning technique that uses labeled datasets to train algorithms to recognize patterns and predict outcomes. e.g., classification models. Features (X variables, or feature vectors) are the values that a supervised model uses to predict the label (Y variable).
- Unsupervised learning: Unsupervised learning technique uses algorithms to analyze unlabeled data sets without human intervention. The algorithms are able to identify patterns and relationships in the data on their own. Unsupervised machine learning is well-suited for complex processing tasks, such as: Clustering, Association, Dimensionality reduction.
- Semi-supervised learning: Uses unsupervised learning algorithms to automatically generate labels for data that can be used by supervised techniques. 
- Reinforcement learning: An agent learns to make decisions by interacting with its environment. The agent is rewarded or penalized for its actions, and its goal is to maximize the total reward. Reinforcement learning is often used to improve models after they have been deployed. 

The main difference between supervised and unsupervised machine learning is the type of data used. Supervised learning uses labeled training data, while unsupervised learning does not.

## Data Preprocessing

Data preprocessing is the process of preparing raw data for machine learning (ML) models by cleaning, transforming, and structuring it. It's a crucial step in the ML pipeline because it directly impacts the accuracy and performance of the models. Some common preprocessing techniques include:

**Handling missing values:** Some algorithms can't handle missing values, or they perform worse with them.

**Removing outliers:** This can help improve data quality.

**Scaling features:** This ensures all data fits a uniform scale. Scaling refers to the process of transforming the features of a dataset to a specific range or distribution. Common Scaling Techniques in Scikit-Learn are: StandardScaler, MinMaxScaler, RobustScaler, MaxAbsScaler.

Scaling, or feature scaling, is a vital pre-processing step in machine learning that involves transforming the values of features in a dataset to a common scale. The goal of scaling is to ensure that all features have a comparable impact on the model, and to reduce potential biases and inconsistencies. 

Scaling can help improve the performance and accuracy of a machine learning model by: 
- Increasing algorithm effectiveness: Scaling brings data points that are far apart closer together, which can help the model learn and understand the problem. 
- Preventing variables from dominating: Scaling can help prevent certain variables from dominating the model due to their larger magnitude. 
- Easing convergence: Scaling can help ease the convergence of certain algorithms, such as non-penalized logistic regression. 

Some common techniques for scaling data include:

- Normalization: Bounds the values of each feature between two numbers, typically between 0 and 1 or -1 and 1
- Standardization: Transforms the data to have zero mean and a variance of 1, making the data unitless
- Min-Max Scaling: Sets the minimum value of each feature to 0 and the maximum value to 1 

Tree-based algorithms, such as decision trees, random forest, and gradient boosting, are generally not affected by scaling and do not require it.

**Encoding categorical variables:** This converts categorical data into a numerical format so the model can understand it. Encoders are transformers that convert categorical variables into numeric values. Some types of encoders in scikit-learn include One-hot encoder, Label binarizer, Label encoder.

Encoders are transformers that convert categorical variables into numeric values. Some types of encoders in scikit-learn include: 

- One-hot encoder: Expands a table by creating a new column for each category. For example, if a table has a column for cities, the one-hot encoder will create a new column for each city, and set the value to 1 for that city and 0 for all other cities. 
- Label binarizer: Converts binary variables, which have only two classes, into numerical values of 0 and 1. 
- Label encoder: Generates a numerical value for each class within a categorical variable. 

**Splitting data into training and testing sets:** This helps avoid training test contamination, which can lead to an overly optimistic model evaluation.

**Reducing dimensionality:** Techniques like Principal Component Analysis (PCA) can help reduce data dimensionality.

**Applying mathematical transformations:** Log or square root transformations can help stabilize variances.

Data preprocessing helps machine learning algorithms understand the data, which can improve their performance.

## Types of data

### Continuous data

Continuous data refers to a type of numerical data that can take on any value (infinite) within a given range, meaning it can be measured with infinite precision and can include decimals or fractions, unlike discrete data which is restricted to specific values; examples include height, weight, temperature, or the time taken to complete a task, where any value within a certain range is possible. 

When working with continuous data, it is important to know certain basics. Standardizing the numeric data requires calculating $\frac {x - \bar{x}}{\sqrt\frac{\Sigma (x- \bar{x})^2}{N-1}\\}\ $ Understanding Mean and Variance:

Mean (or average) i.e., $\bar{x}$: The mean is the average value of a data set. To calculate the mean, you add all the numbers in the data set and divide by the total number of values. This is one number that represents all the data points ($n$).

$ Mean (\bar{x}) = \frac{x_1 + x_2 + ... + x_n}{N}\ $

Range: Range is the difference between the largest and smallest values in a set of numerical data. It's a simple measure of variation that can be used to describe how well the central tendency represents the data.

$ Range = x_{max} - x_{min} $

Variance: Variance is a statistical measurement of the spread between numbers in a data set. It measures how far each number in the set is from the mean (average), and thus from every other number in the set. This is based on a series of calculations. https://www.investopedia.com/terms/v/variance.asp

1. Mean Deviation: The mean deviation is defined as a statistical measure that is used to calculate the average deviation from the mean value of the given data set. This calculates how far away every data point is from the average,

    $ Mean Deviation = (x- \bar{x}) $

2. Squared Mean Deviation: Square of the mean deviation.

    $ Squared Mean Deviation =  (x- \bar{x})^2 $

3. Variance: Sum of the square of the every distance of the data points from the mean divided by the number of data points. 

    $ \sigma^2 = \frac{\Sigma (x- \bar{x})^2}N $

4. Variance (Bassel's Correction): Sum of the square of the every distance of the data points from the mean divided by the number of data points.

    $ \sigma^2 (Bassel's Correction) = \frac{\Sigma (x- \bar{x})^2}{N-1}\ $

5. Standard Deviation: Square root of variance

    $ \sigma = \sqrt\frac{\Sigma (x- \bar{x})^2}{N-1}\\ $


### Categorical data

Categorical data refers to non-numerical information that is organized into groups (finite) or categories. It can be used to represent qualitative or descriptive characteristics, such as the colors of house exteriors or the names of streets in a city. 

https://medium.com/@ranjanrgia/simplifying-encoder-choosing-for-categorical-variables-868bef970f13

## Measuring Results

1. A coefficient is a numerical value that determines the relationship between input and output variables in a model. Coefficients are learned during training and used to make predictions on new data. 
Here are some types of coefficients in machine learning: 
    - Correlation coefficient
        A measure of how well two variables are related. It ranges from -1 to +1, with -1 indicating a perfect negative correlation, 0 indicating no correlation, and 1 indicating a perfect positive correlation. 
    - R-squared
        Also known as the coefficient of determination, this metric measures how well a model fits data and can predict future outcomes. The closer the R-squared value is to one, the better the model fits the data. 
    - Learning coefficient
        A numerical value that defines the learning capability of a neural network during training. 
2. Covariance is a statistical measure that indicates the direction of the linear relationship between two variables. Covariance is a measure of how much two random variables vary together. It can range from negative infinity to positive infinity. 
    - Positive covariance
        A positive covariance indicates that one variable increases with the other. 
    - Negative covariance
        A negative covariance indicates that the variables change in opposite directions. 
    - Covariance matrix
        A covariance matrix is a square matrix that shows the covariance between multiple variables. 
    - Relationship to correlation
        Correlation is a normalized version of covariance that indicates both the direction and strength of the linear relationship between two variables

In linear models, coefficients represent the relationship between a feature and the target. However, machine learning models are generally unable to infer causal effects. 

Covariance is useful for defining the type of relationship between variables, but it's not as good for interpreting the magnitude. 

## Scikit-learn Algorithms

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

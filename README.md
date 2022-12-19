# Chronic-Kidney-Disease-Classification
As part of my academic Machine Learning module, I was part of a team of 5 colleagues where we had to read two scientific articles and recreate them using the various machine learning methods we learned.
The articles worked on a Chronic Kidney Disease dataset available on UCI. We made 3 Jupyter notebooks, one for each article and a final notebook that had our improvements in it.

For the first article:
- We performed an exploratory analysis of the dataset
- Checked for missing values and outliers
- Imputed missing values using two statistical methods: mean for quantitative variables and mode for qualitative (categorical) variables.
- Then we performed feature selection using Recursive Feature Elimination with Cross Validation (RFECV) which is a wrapper method for feature selection that fits a model on the dataset and determines how significant the features are. We used a Random Forest as an estimator.
- For the modelling we used Support Vector Machine, Random Forest Classifier, Decision Tree Classifier and K-Nearest Neighbors. All of the models were trained on a 75% of the data with a Stratified split due to the class imbalance.
- Finally, we evaluated the models with and without feature selection by looking at their Accuracy rates, Precision, Recall, and F1 Score.

For Article 2:
- Data Preparation was done in the same manner.
- We used Correlation-Based Feature Selection
- For modelling we used 3 classifiers: K-Nearest Neighbors, Support Vector Machine and Naïve Bayes. We fitted them on the original data, then on the data after feature selection and finally we used AdaBoost + CFS. For K-Nearest Neighbors, we couldn't use AdaBoost because KNN doesn't have weights, there for we had to introduce Weighted KNN.

Finally, for the improvements,
- We performed a thorough analysis for the missing values, and we ended up imputing each missing value in relation to values from other features. If someone had a missing value for Random Glucose and had diabetes, we imputed them with the mean of Random Glucose for observations that had diabetes. We hoped that this way we could get a more accurate dataset.
- For Feature Selection, we used RFECV.
- And for the modelling we used all the previously mentioned classifiers with hyperparameter tuning (as was the case for the articles as well) and we introduced XGBoost Classifier as well.
- To treat the case of imbalance, we used SMOTE oversampling to introduce more observations of the notckd weak class and refitted the models on this new augmented data.
- Finally we deployed a proof of concept dashboard using Streamlit Cloud which you can access using this link: https://lnkd.in/eBbEtpFY

In conclusion, this has been a fruitful academic activity in which I've learned so much. I'm glad to say that my team got the highest mark for this amazing work. I hope to continue growing my machine learning knowledge.

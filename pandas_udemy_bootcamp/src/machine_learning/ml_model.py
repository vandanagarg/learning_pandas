''' Training and Evaluating models '''
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error
from train_test_sets import X_train, y_train, X_test, y_test


# Training the ML Model (Random Forest Regressor)
''' We have created the training set and the test set,
and first of all, we have to train our machine
learning model with the training set.
And the question is always which model of its algorithm to use
And there are quite a few regression models available.
And actually, based on our extensive explanatory data analysis,
we have seen that there are important features that influence
house prices in a nonlinear way e.g: location in terms of
coordinates is a really important feature for house prices.
However, we have clearly seen that there's definitely no linear
relationship between latitude and longitude and house prices.
So we shouldn't use a linear regression model and therefore we
should select a model that can capture some non-linear relationships
and the random forest regressor is such a model.
We create a random forest regressor - And we define some hyper
parameters, to optimize the model and to improve the predictive power
by reducing overfitting '''

forest_reg = RandomForestRegressor(random_state=42, n_estimators=500,
                                   max_features="sqrt", max_depth=75,
                                   min_samples_split=2)

# fit the model with the training set by passing features and labels
print(forest_reg.fit(X_train, y_train))

''' Now, before we test our model with the test set to see whether
we can generalize to new cases, we can verify it how well our model
fits the training set, or in other words, how well we can predict the
house prices of our training set with the model.
And if the fit is too good, this can indicate overfitting.
And actually, there are two metrics to measure the fit;
first, we consider the coefficient of determination or short R-squared
which shows the values between 0 and 1; zero indicating no fit at all
and one indicating a perfect fit.
And we get the R squared with method score() and we have to pass
X train and the Y train '''
print(forest_reg.score(X_train, y_train))
# high value might indicate that our regressor is actually overfitting.

''' the second metric is the mean squared error and rules are simple
The lower the means squared error closer to zero the better fit '''
pred = forest_reg.predict(X_train)
print(pred)  # predicted house prices not actual

# compare the actual and predicted labels to calculate mean squared error
forest_mse = mean_squared_error(y_train, pred)
forest_rmse = np.sqrt(forest_mse)
print(forest_rmse)
''' So with R squared about .97 and root mean square error of 18000,
we could conclude that actually our model fits training data pretty well
But this doesn't indicate at all whether our model, can generalize to
new cases and predict house prices for new data '''

# Evaluating the Model on the Test Set
''' We are now evaluating our model on the test set and we try to measure
the generalization error or prediction error with the coefficient of
determination and also the root mean squared error.
And finally, we try to find some more intuitive metrics for the accuracy
of our model '''
print(forest_reg)  # fitted regressor object

# coefficient of determination, R-squared, pass test sets
print(forest_reg.score(X_test, y_test))  # lower value compared to train set

# predict labels for test set, pass features to predict method
pred = forest_reg.predict(X_test)
print(pred)

# based on predicted and actual values find root mean squared error
forest_mse = mean_squared_error(y_test, pred)
forest_rmse = np.sqrt(forest_mse)
print(forest_rmse)  # should be a higher value then train set

# Compare the predicted values with the true values
comp = pd.DataFrame(data={"True_V": y_test, "Pred": pred})
print(comp)  # new dataframe with true and predicted values

# absolute difference between the true and predicted values
ae = comp.True_V.sub(comp.Pred).abs()
print(ae)

# mean, absolute difference.
mae = ae.mean()
print(mae)
''' For some observations for some districts, difference is pretty high.
So on average, we can expect that there is a difference of over 30000
between the predicted value and the actual value '''

# Feature Importance
''' We have created a good, but of course not perfect model.
And let's get some more insights:
The conclusion of the explanatory data analysis was that the
income might be the most important factor, followed by the
location and actually good news this that the random forest
regressor could give us the relative importance of features
for the model using feature_importances_ '''

print(forest_reg.feature_importances_)
# we get a numpy array

# create a pandas series, add feature names that we can extract from X
# train, so we get the column labels and sort feature importances
feature_imp = pd.Series(data=forest_reg.feature_importances_,
                        index=X_train.columns).sort_values(ascending=False)
print(feature_imp)

# create horizontal bar plot, to see the importance
feature_imp.sort_values().plot.barh(figsize=(12, 8))
plt.show()
''' All features, sum up to one
median income is the feature with the highest importance.
Then inland or not - So that's the location.
Then we have two features indicating the size of the houses.
then again, we have the location - longitude and latitude.
so on..
So we can conclude that the question is whether the
district is in the inland or near the ocean.
And it doesn't really matter whether it is less than one
hour to the ocean near the ocean etc
And actually based on this outcome, we could drop some features and
rerun our model '''

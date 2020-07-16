''' Splitting the Data into Train and Test Set '''
from feature_engineering import label, features


''' Now, the time has come to split our dataset into a
training set and a test set, because the only way
to know how well our model will generalize to new cases
is to try it out on new cases. And we are going to train
our machine learning model using the training set,
and then we test the ability of our model to generalize and
to forecast house prices for data points that our model has
not seen before. Here we save 80 percent of the data for
training and 20 percent for testing, but this depends on the
size of the dataset. If we have millions of data points, that
might be enough to have a test set of 2 percent.
In our case, we have over 20000 observations and it makes sense
to have a test size of 20 percent.
Easiest way to split our data set is by drawing a random sample
and Pandas has a method for it. The sample method.
To random state we can pass any number to ensures the reproducibility
To create the features of the test: X stands for the features and
Y for the label.
By sampling we get the random rows,
Now, there's one drawback of a simple random sampling.
The risk of introducing a so called sampling bias, and that means that
the sample is not representative of the whole dataset
And we have seen before that the median income is probably the most
important feature. So having all the low income districts in the
training set and all high income districts in the test set;
that wouldn't be representative and this could lead to a poor model,
and therefore we should make sure that the five income categories
in training set and test set have the same ratios as in the whole
dataset. This is also called a stratified sampling.
Scikit Learn has a workflow for it, For now  simple random sampling
of pandas is good enough.
And the rule is that the larger the dataset to the more simple
random sampling approaches stratify to sampling.
And in our case, we should definitely double check whether we are
close to a perfectly stratified sample or not.
Hence we compare the relative frequencies of the income categories
in our test set '''
test_size = 0.2

# features
X_test = features.sample(frac=test_size, random_state=123)
print(X_test)

# comparing frequencies for income_cat
print(X_test.income_cat.value_counts(normalize=True))
print(features.income_cat.value_counts(normalize=True))

# row labels for the test set
print(X_test.index)

# creating training set
''' So we check for each and every row label in features whether the
row label is ready in the test set and if the row label is not in
test set, (~ symbol for not in test set) the row is in our training set '''
X_train = features.loc[~features.index.isin(X_test.index)].copy()
print(X_train)

# validating ratios
print(X_train.income_cat.value_counts(normalize=True))

''' There's a workflow that is actually not necessary for our case.
but we should definitely work with a SHEFFORD training set.
So that means that the rows here in the training set are randomly
ordered. And we can see here that the order is still the same as before
we can simply shuffle the training set again, using the sample method
And now we take the fraction one.
So we are drawing all the rows.
But in a random order and we overwrite X_train.
And now the order is actually random '''

X_train = X_train.sample(frac=1, random_state=123)
print(X_train)

''' Now we need to drop the categorical feature income categories
we actually do not require it for our model.
So we drop income category from X_train and X_test '''

X_train.drop(columns=["income_cat"], inplace=True)
X_test.drop(columns=["income_cat"], inplace=True)

''' And now we have the final features for the training and test set
and now we have to split the labels into training and test set.
labels = median house prices
We use row indexes from features test & training set and filter
label correspondingly.

'''
y_train = label.loc[X_train.index]
y_test = label.loc[X_test.index]

print(y_train)

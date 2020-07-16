''' Data Preprocessing & Feature Engineering for Machine Learning '''
import pandas as pd
import scipy.stats as stats
from data_analysis import housing_df


''' Before creating ML model we must transform some features and before
that separate features and labels. So we shouldn't transform the label
house price because we want to forecast the prices. Thus we select column
median house value and to create a separate object and save the object in
the variable label. We get the features by dropping the column median house
value from housing_df.
If we focus on numerical features and in most cases, it's not the best
solution to keep the numerical features as they are. So typically,
numerical features have very different scales. As we have different scales
in the columns, the population and median income. One we have in thousands
and other we have between one and 15. And actually, many machine learning
algorithms don't perform better with different scales.
And there are several methods how to scale or to normalize numerical features.
And all have pros and cons. And it depends on the machine learning model
which method to use.
And in our case, we standardize the numerical features by calculating z values.
In features dataframe we have all numerical columns & data type float '''

label = housing_df.median_house_value.copy()
print(label)

features = housing_df.drop(columns=["median_house_value"])
print(features)

features.info()

print(features.select_dtypes("float"))

# calculate z scores
feat1 = features.select_dtypes("float").apply(lambda x: stats.zscore(x))
print(feat1)

pd.options.display.float_format = '{:.2f}'.format
print(feat1)

print(feat1.agg(["mean", "std"]))
''' So here we have now standardized numerical features.
mean value in each and every column is zero and the standard deviation one
All features have, Now the very same scale

Typically, machine learning algorithms cannot handle text data,
and therefore we have to transform texts or categorical data into numbers
And then our dataset, we have two categorically features.
However, our final model, we only use the ocean proximity feature.
It has five different categories. We can transform this categorical feature
into number with so-called one hot encoding. And for each and every category
we create a new feature/column with binary values One or zero and called as
dummy variables/ Dummy Features.
idea behind this is for every district we have value one, one time and four
times is zero. And one dummy variable is redundant. As once we know the value
in four columns, then we automatically know also the value in the fifth column
Keeping all 5 dummy variable causes multi co-linearity problem.
Some algorithms are sensitive to it and can be harmed by multi co-linearity
like linear regression and there we should delete one feature and only use
K minus one.
However, when we use other models, like random forest regression,
It can be beneficial to keep all five or all K features in our dataset.
So we can merge our all features again into one feature dataframe.
So use PD dot concat and we horizontally concatenate feature one with our
standardized numerical features, dummies and income categories.
We can use Scikit learn for preprocessing pipelines and use Scikit
methods to engineer features. Still we can do most of the things
with Pandas and other libraries like scipy.stats'''

print(features.ocean_proximity)
print(features.ocean_proximity.value_counts())

dummies = pd.get_dummies(features.ocean_proximity)
print(dummies)

features = pd.concat([feat1, dummies, housing_df.income_cat], axis=1)
print(features)

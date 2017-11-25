import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv), data manipulation as in SQL
import matplotlib.pyplot as plt # this is used for the plot the graph
import seaborn as sns # used for plot interactive graph. I like it most for plot
from sklearn.linear_model import LogisticRegression # to apply the Logistic regression
from sklearn.model_selection import train_test_split # to split the data into two parts
from sklearn.cross_validation import KFold # use for cross validation
from sklearn.model_selection import GridSearchCV# for tuning parameter
from sklearn.ensemble import RandomForestClassifier # for random forest classifier
from sklearn.naive_bayes import GaussianNB
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn import svm # for Support Vector Machine
from sklearn import metrics # for the check the error and accuracy of the model
# Any results you write to the current directory are saved as output.
# dont worry about the error if its not working then insteda of model_selection we can use cross_validation

data = pd.read_csv("diabetes.csv")
features = list(data.columns[1:8])

train,test = train_test_split(data, test_size=0.25, random_state = 0, stratify = data['Outcome'])
train_x = train[train.columns[:8]]
test_x = test[test.columns[:8]]

test_y = test['Outcome']
train_y = train['Outcome']

model = DecisionTreeClassifier()
model.fit(train_x, train_y)
prediction = model.predict (test_x)
print "Accuracy = ", metrics.accuracy_score(prediction, test_y)


comparison_table = []
classifiers = ['Linear SVM', 'Radial SVM', 'Logistic Regression', 'K Nearest Neighbours', 'Decision Tree']
models = [svm.SVC(kernel = 'linear'), svm.SVC(kernel = 'rbf'), LogisticRegression(), K KNeighborsClassifier(n_neighbors=3), DecisionTreeClassifier()]

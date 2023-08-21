import sklearn.preprocessing
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report

import pandas as pd

def get_tree(train_X, val_X, train_y, val_y):
    # Instantiate the DecisionTreeClassifier as 'dt'
    dt = DecisionTreeClassifier(max_depth = 5, random_state=42)

    # Train the model
    dt.fit(train_X, train_y)

    # Calculate and print the accuracy on the training data
    train_score = dt.score(train_X, train_y)
    print("Decision Tree Model Accuracy on Training Data:", train_score)

    val_score = dt.score(val_X, val_y)
    print("Decision Tree Model Accuracy on Validation Data:", val_score)
    
def get_forest(train_X, val_X, train_y, val_y):
    '''get random forest accuracy on train and validate data'''

    # create model object and fit it to training data
    rf = RandomForestClassifier(max_depth=7, min_samples_leaf= 10, random_state=42)
    rf.fit(train_X,train_y)

    # print result
    print(f"Accuracy of Random Forest on train is {rf.score(train_X, train_y)}")
    print(f"Accuracy of Random Forest on validate is {rf.score(val_X, val_y)}")
    
def get_logreg(train_X, val_X, train_y, val_y):

    seed = 42

    logreg = LogisticRegression(random_state = seed, max_iter = 100, multi_class= 'multinomial')

    logreg.fit(train_X, train_y)

    # print result
    print(f"Accuracy of Logistic Regression on train is {logreg.score(train_X, train_y)}")
    print(f"Accuracy of Logistic Regression on validate is {logreg.score(val_X, val_y)}")


def get_knn(train_X, val_X, train_y, val_y):

    # create model object and fit it to the training data
    knn = KNeighborsClassifier(n_neighbors= 17, weights='uniform', p= 1)
    knn.fit(train_X, train_y)

    # print results
    print(f"Accuracy of K-Nearest Neighbors on train is {knn.score(train_X, train_y)}")
    print(f"Accuracy of K-Nearest Neighbors on validate is {knn.score(val_X, val_y)}")
    
def get_forest_test(train_X, test_X, train_y, test_y):
    '''get random forest accuracy on train and validate data'''

    # create model object and fit it to training data
    rf = RandomForestClassifier(max_depth=7, min_samples_leaf= 10, random_state=42)
    rf.fit(train_X,train_y)

    # print result
    print(f"Accuracy of Random Forest on train is {rf.score(train_X, train_y)}")
    print(f"Accuracy of Random Forest on validate is {rf.score(test_X, test_y)}")
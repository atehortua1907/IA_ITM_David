from sklearn.datasets import load_digits
import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import KFold


dataset = load_digits()
X, Y = dataset.data, dataset.target

n = np.shape(X)[0]
train_len = int(n*0.7)
indices = np.arange(0,1796,1)
perm_index = np.random.permutation(indices)
X_train, Y_train = X[perm_index[0:train_len]], Y[perm_index[0:train_len]]
X_test, Y_test = X[perm_index[train_len:]], Y[perm_index[train_len:]]

model = KNeighborsClassifier(n_neighbors=5)
model.fit(X_train, Y_train)
preds = model.predict(X_test)
print('Accuracy con K-nn 5: ', accuracy_score(preds, Y_test))

model.fit(X, Y)
preds = model.predict(X)
print('confusion k-nn = 5',confusion_matrix(Y,preds))

model = KNeighborsClassifier(n_neighbors=11)
model.fit(X_train, Y_train)
preds = model.predict(X_test)
print('Accuracy con K-nn 11: ', accuracy_score(preds, Y_test))

model.fit(X, Y)
preds = model.predict(X)
print('confusion k-nn = 11',confusion_matrix(Y,preds))

model = GaussianNB()
model.fit(X_train, Y_train)
preds = model.predict(X_test)
print('Accuracy con Naive bayes: ', accuracy_score(preds, Y_test))

model.fit(X, Y)
preds = model.predict(X)
print('confusion con Naive bayes',confusion_matrix(Y,preds))


n_neighbors = 11
splits = 10
kfolds = KFold(n_splits=splits)
kfolds.get_n_splits(X)

sum_accuracy = 0

for train_index, test_index in kfolds.split(X):
    X_train, X_test = X[train_index], X[test_index]
    Y_train, Y_test = Y[train_index], Y[test_index]

    model = model = GaussianNB()
    model.fit(X_train, Y_train)
    preds = model.predict(X_test)
    sum_accuracy += accuracy_score(preds, Y_test)

print('Kfolds modelo ',n_neighbors,' = ',sum_accuracy / splits)
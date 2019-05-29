# height,weight,shoe size

X = [[181, 80, 44], [177, 70, 43], [160, 60, 38], [154, 54, 37], [166, 65, 40],
     [190, 90, 47], [175, 64, 39],
     [177, 70, 40], [159, 55, 37], [171, 75, 42], [181, 85, 43]]
Y = ['male', 'male', 'female', 'female', 'male', 'male', 'female', 'female',
     'female', 'male', 'male']

# Decision Tree
from sklearn import tree
clf = tree.DecisionTreeClassifier()
clf = clf.fit(X,Y)
#pred1 = clf.predict([[190,70,43]])
pred1 = clf.predict(X)
print pred1

# SVM

from sklearn import svm
clf2 = svm.SVC(gamma='scale')
clf2.fit(X, Y)
pred2 = clf2.predict(X)
#pred2 = clf2.predict([[190,70,43]])
print pred2


# metrics
from sklearn.metrics import accuracy_score
y_pred1 = pred1
y_pred2 = pred2 
y_true = Y
print accuracy_score(y_true, y_pred1)
print accuracy_score(y_true, y_pred2)

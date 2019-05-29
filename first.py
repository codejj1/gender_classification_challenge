from sklearn import tree

# height,weight,shoe size

X = [ [181,80,44], [177,70,43], [160,60,38]]
Y = ['male', 'female','female']

clf = tree.DecisionTreeClassifier()

clf = clf.fit(X,Y)

prediciton = clf.predict([[190,70,43]])

print prediciton

# SVM

from sklearn import svm
clf2 = svm.SVC(gamma='scale')
clf2.fit(X, Y)  

pred2 = clf2.predict([[190,70,43]])

print pred2
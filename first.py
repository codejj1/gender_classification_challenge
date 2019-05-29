from sklearn import tree

# height,weight,shoe size

X = [[181, 80, 44], [177, 70, 43], [160, 60, 38], [154, 54, 37], [166, 65, 40],
     [190, 90, 47], [175, 64, 39],
     [177, 70, 40], [159, 55, 37], [171, 75, 42], [181, 85, 43]]

Y = ['male', 'male', 'female', 'female', 'male', 'male', 'female', 'female',
     'female', 'male', 'male']

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

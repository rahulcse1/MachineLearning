'''
Created on 05-Sep-2017

@author: techwalk
'''

from sklearn import tree

# more data better classifier.

features = [[140, 1], [130, 1], [150, 0], [170, 0]]
lables = [0, 0, 1, 1]
 
clf = tree.DecisionTreeClassifier()
clf = clf.fit(features, lables)

print(clf.predict([[150, 0]]))

# 0 for Apple and 1 for Orange
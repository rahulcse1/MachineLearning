'''
Created on 05-Sep-2017

@author: techwalk

will test classifier accuracy
Not part of training data

'''

import numpy as np
from sklearn.datasets import load_iris
from sklearn import tree

iris = load_iris()
test_ids = [0, 50, 100]
# training data
train_target = np.delete(iris.target, test_ids)
train_data = np.delete(iris.data, test_ids, axis=0)

# testing data
test_target = iris.target[test_ids]
test_data = iris.data[test_ids]

clf = tree.DecisionTreeClassifier()
clf = clf.fit(train_data, train_target)

print(test_target)  # match data
print(clf.predict(test_data))  # predit value

from sklearn.externals.six import StringIO
import pydotplus

dot_data = StringIO()
tree.export_graphviz(clf,
                     out_file=dot_data,
                     feature_names=iris.feature_names,
                     class_names=iris.target_names,
                     filled=True, rounded=True, impurity=False)

graph = pydotplus.graph_from_dot_data(dot_data.getvalue())
graph.write_pdf("iris.pdf")

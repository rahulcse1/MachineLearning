'''
Created on 05-Sep-2017

@author: techwalk
'''

from sklearn.datasets import load_iris

iris = load_iris()
print(iris.feature_names)
print(iris.target_names)
print(iris.data[0])

# ['setosa' 'versicolor' 'virginica']
# [0 , 1, 2]
print(iris.target[0])
for i in range(len(iris.target)):
    print("Example: %d labels: %s features: %s" % (i, iris.target[i], iris.data[i]))

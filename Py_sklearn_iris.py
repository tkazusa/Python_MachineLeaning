
# coding: utf-8

# In[1]:

import numpy as np
from sklearn import datasets
from sklearn import tree
from sklearn.grid_search import GridSearchCV
from sklearn import cross_validation
import pydot


# In[2]:

data = datasets.load_iris()
X = data.data
y = data.target


# In[3]:

max_score = 0
max_max_depth = 1

#GridResearch 
for max_depth in range(1,7):
    #Creating an instance of Decision Tree Crasification
    clf  = tree.DecisionTreeClassifier(max_depth=max_depth)
    
    #Cross Validation
    cv_scores = cross_validation.cross_val_score(clf,X,y,cv=5)
    #交差検定の各学習の平均値計算
    score = np.mean(cv_scores)
    
    print "max_deopth:{} score:{}".format(max_depth, score)
    
    if score > max_score:
            max_score = score
            max_max_depth = max_depth
    
    print "best_max_depth:{} best_score:{}".format(max_max_depth, max_score)

clf  = tree.DecisionTreeClassifier(max_depth=max_max_depth)

clf.fit(X,y)


# In[4]:

from sklearn.externals.six import StringIO  
dot_data = StringIO()
tree.export_graphviz(clf, out_file=dot_data) 
graph = pydot.graph_from_dot_data(dot_data.getvalue()) 
g = graph.write_pdf("iris.pdf")


# In[5]:

from sklearn import datasets,tree
import StringIO
import pydot
from sklearn.externals.six import StringIO  

iris = datasets.load_iris()

clf = tree.DecisionTreeClassifier()
clf = clf.fit(iris['data'],iris['target'])

dot_data = StringIO()
tree.export_graphviz(clf, out_file=dot_data)
graph = pydot.graph_from_dot_data(dot_data.getvalue())
graph.write_pdf("iris.pdf")


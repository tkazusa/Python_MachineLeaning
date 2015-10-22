
# coding: utf-8

# In[1]:

import numpy as np
import pandas as pd
from sklearn import datasets
from sklearn import tree
from sklearn.grid_search import GridSearchCV
from sklearn import cross_validation
import pydot


# In[2]:

df = pd.read_csv('iris_train.csv')

clf = tree.DecisionTreeClassifier()
#Assign an explanatory variable
data_array = ["SepalLength", "SepalWidth", "PetalLength", "PetalWidth"]
#Assign an objective variable
class_array = ["Name"]

clf = clf.fit(df[data_array], df[class_array])


# In[8]:

with open('iris.dot', 'w') as f:
    f = tree.export_graphviz(clf, out_file=f)
    
import os
os.unlink('iris.dot')

from sklearn.externals.six import StringIO  
import pydot 
dot_data = StringIO() 
tree.export_graphviz(clf, out_file=dot_data) 
graph = pydot.graph_from_dot_data(dot_data.getvalue()) 
graph.write_pdf("iris.pdf") 


# In[21]:

#Apply tree for test data
df_p = pd.read_csv('iris_test.csv')

result = clf.predict(df_p[data_array])


# In[27]:

print result


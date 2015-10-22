
# coding: utf-8

# In[1]:

import pulp


# In[2]:

#Creat variables
x = pulp.LpVariable("x", cat = "Integer")
y = pulp.LpVariable("y", cat = "Integer")

#Create object function
problem = pulp.LpProblem("Container", pulp.LpMaximize)
problem += 29*x + 45*y  #(6.6)

#constrained condition
problem += 2*x + 8*y <= 60 #(6.4)
problem += 4*x + 4*y <= 60 #(6.4)
problem += x >= 0 #(6.5)
problem += y >= 0 #(6.5)

status = problem.solve()
print "Status", pulp.LpStatus[status]

print problem

print "Result"
print "x", x.value()
print "y", y.value()


# In[3]:

#Creat variables
x = pulp.LpVariable("x", cat = "Continuous")
y = pulp.LpVariable("y", cat = "Continuous")

#Create object function
problem = pulp.LpProblem("Alloy", pulp.LpMaximize)
problem += 30*x + 25*y  #(6.9)

#constrained condition
problem += 0.5*x + 0.25*y <= 10 #(6.7)
problem += 0.5*x + 0.75*y <= 15 #(6.7)
problem += x >= 0 #(6.8)
problem += y >= 0 #(6.8)

status = problem.solve()
print "Status", pulp.LpStatus[status]

print problem

print "Result"
print "x", x.value()
print "y", y.value()


# In[4]:

#Creat variables
a = pulp.LpVariable("a", cat = "Continuous")
b = pulp.LpVariable("b", cat = "Continuous")

#Create object function
problem = pulp.LpProblem("Test", pulp.LpMaximize)
problem += a + b  #(6.16)

#constrained condition
problem += -a - b <= -2 #(6.14)
problem += -2*a + b <= 15 #(6.14)
problem += a - 2*b <= 15 #(6.14)
problem += a >= 0 #(6.15)
problem += b >= 0 #(6.15)

status = problem.solve()
print "Status", pulp.LpStatus[status]

print problem

print "Result"
print "a", a.value()
print "b", b.value()


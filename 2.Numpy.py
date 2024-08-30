#!/usr/bin/env python
# coding: utf-8

# # <font color='Blue'>Numpy.</font>

# <font color='black'>1.NumPy is a Python library, used for working with arrays.</font>

# <font color='black'>2.using of numpy we can make statical calculations.</font>

# In[ ]:


get_ipython().system(' pip install "numpy" #--------> Package Install')


# In[3]:


import numpy as np #----------> Importing Library


# In[47]:


a=(23,24,25,226) #------------> creating normal data
a


# In[48]:


a[1]


# In[4]:


b=np.array([23,24,25,226]) #----------> Using numpy creating data 
print(b)
c=np.array([24,22,21,223])
print(c)
d=np.array([26,27,28,299])
print(d)
e=np.vstack((b,c,d))  #---------------> in numpy library using (vstack) to combine three data sets in single
e


# In[50]:


# Accessing Variables


q=e[0,0]
print(q)

w=e[2,0]
print(w)

r=e[0,2]
print(r)

t=e[2,1]
print(t)

y=e[2,2]
print(y)


# In[51]:


# Calculating Statistical Calculations

x=np.array([23,24,25,226])
print(x)

z=np.mean(x)
v=np.median(x)
n=np.std(x)
m=np.var(x)
k=np.min(x)
j=np.max(x)
h=np.percentile(x,25)
g=np.percentile(x,50)
f=np.percentile(x,75)

print(z)
print(v)
print(n)
print(m)
print(k)
print(j)
print(h)
print(g)
print(f)



# In[5]:


# Creating Random Variables 

a1=np.random.randint(11,20,size=(5))
print(a1)

a2=np.random.randint(11,20,size=(3,4))
a2


# In[14]:


import numpy as np

np.random.randint(1.5,10.5)


# # <font color='red'>END.</font>

# In[ ]:





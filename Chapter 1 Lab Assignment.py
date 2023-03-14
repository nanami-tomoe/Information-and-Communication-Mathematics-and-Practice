#!/usr/bin/env python
# coding: utf-8

# In[22]:


pip install numpy


# In[25]:


pip install matplotlib


# ## 1-a
# Evaluate f(x) for x= -1, 0, 1

# In[10]:


import numpy as np

ppar = [5, -3, 1]
p = np.poly1d(ppar)
print(p(-1), p(0), p(1))


# ## 1-b
# Find the roots of f(x)

# In[11]:


import numpy as np

print(np.roots([5, -3, 1]))


# ## 1-c
# Factorize the f(x) manually using the solution of (b)

# 5(x-(0.3+0.33166248j))(x-((0.3-0.33166248j)))

# ## 1- d
# Express x whose values are between -1 and 1 and stepping interval of 0.1

# In[15]:


import numpy as np

xvals = np.arange(-1, 1, 0.1)
print(xvals)


# ## 1-e
# Evaluate f(x) for the x values defined in (d)

# In[18]:


import numpy as np

ppar = [5, -3, 1]
p = np.poly1d(ppar)
xvals = np.arange(-1, 1, 0.1)
yvals = np.polyval(ppar, xvals)
print((yvals))


# ## 1 - f
# Plot f(x) in (e).  Label the x-axis as “X” and the y-axis “F(x)”.  Turn the grid on.

# In[43]:


import numpy as np
import matplotlib.pyplot as plt

ppar = [5, -3, 1]
p = np.poly1d(ppar)
xvals = np.arange(-1, 1, 0.1)
yvals = np.polyval(ppar, xvals)

plt.plot(xvals, yvals, '-.k') ## plt.plot(xvals, yvals, 포맷 문자열)
plt.xlabel("X")
plt.ylabel("F(x)")
plt.axis([-1, 1, 0, 10]) ## plt.axis([xmin, xmax, ymin, ymax])
plt.grid()
plt.show


# ## 2-a
# Express f(x) and g(x) in Python

# In[59]:


import numpy as np
import matplotlib.pyplot as plt

f = np.poly1d([1, -5, 1])
fxvals = np.arange(-5, 5, 0.5)
fyvals = np.polyval(f, fxvals)


plt.plot(fxvals, fyvals, '-.k') 
plt.xlabel("X")
plt.ylabel("F(x)")
plt.axis() 
plt.grid()
plt.show


# In[58]:


import numpy as np
import matplotlib.pyplot as plt

g = np.poly1d([1, -3, 7])
gxvals = np.arange(-5, 5, 0.5)
gyvals = np.polyval(g, gxvals)

plt.plot(gxvals, gyvals, '-.k') 
plt.xlabel("X")
plt.ylabel("G(x)")
plt.axis()
plt.grid()
plt.show


# ## 2-b
# Compute h(x) = f(x)*g(x)

# In[61]:


import numpy as np

f = [1, -5, 1]
g = [1, -3, 7]

m = np.polymul(f, g)
print(m)


# ## 2-c
# Compute q, r = f(x)/g(x)

# In[62]:


import numpy as np

f = [1, -5, 1]
g = [1, -3, 7]

q, r = np.polydiv(f, g)
print(q, r)


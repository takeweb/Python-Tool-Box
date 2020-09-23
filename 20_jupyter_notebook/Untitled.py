#!/usr/bin/env python
# coding: utf-8

# In[1]:


n = 1 + 1


# In[2]:


print(n)


# In[5]:


get_ipython().run_line_magic('matplotlib', 'inline')
import matplotlib.pyplot as plt
import numpy as np
x = np.linspace(0, 3*np.pi, 500)
plt.plot(x, np.sin(x**2))


# In[ ]:





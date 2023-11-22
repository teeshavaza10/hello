#!/usr/bin/env python
# coding: utf-8

# import pandas as pd

# In[6]:


data=pd.read_csv("indian_restaurants.csv")
print(data)


# In[7]:


excel=pd.read_excel("indian_restaurants.xlsx")
print(excel)


# In[9]:


import matplotlib.image as nping
import matplotlib.pyplot as plt
img=nping.imread("edinburgh.jpg")
plt.imshow(img)


# In[ ]:





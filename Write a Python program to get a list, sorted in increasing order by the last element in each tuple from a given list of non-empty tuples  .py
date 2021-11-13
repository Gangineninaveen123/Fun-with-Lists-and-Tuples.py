#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Sample List : [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]

# Expected Result : [(2, 1), (1, 2), (2, 3), (4, 4), (2, 5)]



def call_tuple(tuple_arg):
    return tuple_arg[1]
tuple_list = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
tuple_list.sort(key = call_tuple)
print(tuple_list)


# In[ ]:





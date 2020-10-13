#!/usr/bin/env python
# coding: utf-8

# In[9]:



def positivo (lista):
    lista3=[]
    for elemento in lista:
        if elemento>=0:
            lista3.append(elemento)
        else:
            elemento *=-1
            lista3.append(elemento)
    return lista3
    


# In[7]:


lista=[1,-1,4,-15,9,7,6,-1,2,-20]


# In[10]:


print(positivo(lista))


# In[ ]:





# In[ ]:





# In[ ]:





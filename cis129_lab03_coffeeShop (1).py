#C is a var of coffee cost; 
#M is a var of muffin cost;
#X=number of coffee*cost;
#Y=number of muffin*cost;
#T=total tax,6%
#F=final price(tax+subtotal)

# In[1]:


C=5.00


# In[2]:


M=4.00


# In[1]:


coffees = int(input("How many coffees would you like?"))


# In[ ]:


muffins=int(input("How many muffins would you like?"))


# In[ ]:


X=float(coffees*C)


# In[ ]:


Y=float(muffins*M)


# In[ ]:


print('***************************************\nMy Coffee and Muffin Shop\nNumber of coffees bought?\n')


# In[ ]:


print(coffees)


# In[ ]:


print('Number of Muffins bought?\n')


# In[ ]:


print(muffins)


# In[ ]:


print('***************************************\n\n***************************************')


# In[ ]:


print('My Coffee and Muffin Shop Receipt')


# In[ ]:


print(coffees,'Coffee at $',int(C),'each: $',float(X))


# In[ ]:


print(muffins,'Muffin at $',int(M),'each: $',float(Y))


# In[ ]:


T=float(.06*(X+Y))


# In[ ]:


print('6% tax:%',float(T))


# In[ ]:


F=float(T+(X+Y))


# In[ ]:


print('---------\nTotal:$',float(F))


# In[ ]:


print('***************************************')


#Author: Nancy St Thomas
#CIS129 Lab 3 
#Coffee Shop
#C is a var of coffee cost; 
#M is a var of muffin cost;
#B is a var of Bagel cost;
#t is a var of Tea cost;
#X=number of coffee*cost;
#Y=number of muffin*cost;
#Z=number of Tea*cost;
#W=number of Bagel*cost;
#T=total tax,6%
#F=final price(tax+subtotal)

# In[1]:


C=5.00


# In[2]:


M=4.00


# In[3]:


B=4.00


# In[4]:


t=2.00


# In[1]:


coffees = int(input("How many coffees would you like?"))


# In[ ]:


muffins=int(input("How many muffins would you like?"))


# In[ ]:


teas=int(input("How many teas would you like?"))


# In[ ]:


bagels=int(input("How many bagels would you like?"))


# In[ ]:


X=float(coffees*C)


# In[ ]:


Y=float(muffins*M)


# In[ ]:


Z=float(teas*t)


# In[ ]:


W=float(bagels*B)


# In[ ]:


print('***************************************\nMy Coffee and Muffin Shop\n')


# In[ ]:


print('Number of coffees bought?\n')


# In[ ]:


print(coffees)


# In[ ]:


print('Number of Muffins bought?\n')


# In[ ]:


print(muffins)


# In[ ]:


print('Number of Teas bought?\n')


# In[ ]:


print(teas)


# In[ ]:


print('Number of Bagels bought?\n')


# In[ ]:


print(bagels)


# In[ ]:


print('***************************************\n\n***************************************')


# In[ ]:


print('My Coffee and Muffin Shop Receipt')


# In[ ]:


print(coffees,'Coffee at $',int(C),'each: ${:.2f}'.format(X))


# In[ ]:


print(muffins,'Muffin at $',int(M),'each: ${:.2f}'.format(Y))


# In[ ]:


print(teas,'Teas at $',int(t),'each: ${:.2f}'.format(Z))


# In[ ]:


print(bagels,'Bagel at $',int(B),'each: ${:.2f}'.format(W))


# In[ ]:


T=float(.06*(X+Y+Z+W))


# In[ ]:


print('6% tax:%{:.2f}'.format(T))


# In[ ]:


F=float(T+(X+Y+Z+W))


# In[ ]:


print('---------\nTotal:${:.2f}'.format(F))


# In[ ]:


print('*Thank you for your visit,*\n*Please come agian soon!*')


# In[ ]:


print('***************************************')


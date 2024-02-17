#!/usr/bin/env python
# coding: utf-8

# In[1]:


#module 4 lab4
#Nancy Stthomas
#2/17/34
#determines bonuses due to monthlysales and sales increase. 


# In[2]:


# declare local variables
monthlySales = 0 # monthly sales amount
storeAmount = 0  # store bonus amount
empAmount = 0 # employee bonus amount
salesIncrease= 0  # percent of sales increase
# prompt will be a string literal
prompt = monthlySales>=80000 or salesIncrease>=3/100


# In[ ]:


#This code get the montley sales
monthlySales=float(input("Enter the monthly sales"))


# In[ ]:


#this code determines the store bonus
if monthlySales>=110000:  
    storeAmount=6000
elif monthlySales>=100000:
    storeAmount=5000
elif monthlySales>=90000:
    storeAmoutn=4000
elif monthlySales>=80000:
    storeAmount=30000
else: 
    storeAmount=0


# In[ ]:


#this code gets the percent of increase in sales
salesIncrease=float(input("Enter the percent of sales increase in decimal format"))


# In[ ]:


if salesIncrease>=0.05:
    empAmount=75
elif salesIncrease>=0.04:
    empAmount=50
elif salesIncrease>=0.03:
    empAmount=40
else: 
    empAmount=0


# In[ ]:


#this code prints the bonus information
print("The store bonus amount is $",storeAmount)
print("The employee bonus amount is $",empAmount)
if(storeAmount==6000)and(empAmount==75):
    print('Congrats! You have reached the highest bonus amounts possible!')


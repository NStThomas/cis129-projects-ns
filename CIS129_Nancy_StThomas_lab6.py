#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Nancy StThomas
#hotdog cookout lab
#03/4/24
#CIS129
#code to figure out how many packages of hotdogs and buns needed for a cookout


# In[2]:


#gettotalHotDogs function
def getTotalHotDogs():
    totalHotDogs=0
    attendees=0 #number of poeple at cookout
    hotDogs=0 #hotdogs per person
    getTotalHotDogs=totalHotDogs
    attendees=int(input('How many people attending?'))
    hotDogs=int(input('How many Hotdogs per person?'))
    total=attendees*hotDogs
    return total   


# In[3]:


#showResults
def showResuts(total):
    BUNS=8 #amount in each pack
    DOGS=10 #amount in each pack
    dogsLeft=0 #extra
    BunsLeft=0 #extra
    minDogs=0 #minimun amount needed
    minBuns=0 #minimun amount needed
    #caluations fot minimun and extra
    dogsLeft=(DOGS-total%DOGS)%DOGS
    minDogs=(total//DOGS)+(0**(0**dogsLeft))
    BunsLeft=(BUNS-total%BUNS)%BUNS
    minBuns=(total//BUNS)+(0**(0**BunsLeft))
    #display 
    print("Minimun packages of hotdogs needed",minDogs)
    print("Minimun packages of hotdog buns needed",minBuns)
    print("Hotdogs remaining",dogsLeft)
    print("Hotdog buns remaining",BunsLeft)
    end=''


# In[ ]:


#call function for gettotalhotdogs
total=getTotalHotDogs() 


# In[ ]:


#call function for results
results=showResuts(total) 


# In[ ]:





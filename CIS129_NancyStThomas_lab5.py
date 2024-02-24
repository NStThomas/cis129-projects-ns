#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Nancy StThomas
#2/22/2024
#lab 5
#the Bottle Return Program
#totalBottles var the store bottle retured
#counter var control the loop
#todayBottles var amount of bottles retured in one day
#totalPayout var calc calue of totalBottle*.10
#keepGoing var run the program again.


# In[ ]:


keepGoing='y'
while keepGoing=='y':
    # loop
    totalBottles=0
    counter=1
    todayBottles=0
    totalPayout=0
    #getBottle code
    totalBottles=todayBottles
    #return total number of bottles for the week
    nbr_of_days=7
    for counter in range (1,8):
        print('Enter number of bottles returned for day #',counter,':')
        todayBottles=int(input())
        counter+=1
        totalBottles+=todayBottles
        #calc Payout code
        totalPayout=0
        payout_per_bottle=.10
        totalPayout=totalBottles*payout_per_bottle
        
    print('The total number of bottles collected is',(totalBottles))
    print('The total paid out is $',(totalPayout))
        
    print("Do you want to enter another week's worth of data?")
    keepGoing=input("Enter y or n") 
   


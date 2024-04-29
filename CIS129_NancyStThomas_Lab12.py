#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Nancy StThomas
#Pet Class lab 12
#4/28
#CIS129 


# In[2]:


class newPet(object):
#Declare input variables
    name=""
    type=""
    age=0
    #Constructor
    def __init__(self,name,type,age): 
        self.setName=name
        self.setType=type
        self.setAge=age
    #Mutators
    def setNames(self,setName):
        self.setName=name
    def setType(self,setType):
        self.setType=type
    def setAge(self,age):
        self.setAge=age
    
    #  Accessors
    def getName(self):
        return self.name
    def getType(self):
        return self.type
    def getAge(self):
        return self.age
    


# In[3]:


#main module
def main():
    # create a Pet object
    animal=newPet("","",0)
    #Get values for a pet
    animal.setName=input("Enter a pet name?:")
    animal.setType=input("Enter a pet type:") 
    animal.setAge=int(input("Enter a pet age?:"))
    # Show values for this pet
    print("The pet name is", animal.setName)
    print("The pet type is", animal.setType)
    print("The pet age is", animal.setAge)
    #end module
    end=''


# In[4]:


main()


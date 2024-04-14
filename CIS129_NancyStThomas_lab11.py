#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Nancy StThomas
#CIS129
#lab 11 exercises 9.1, 9.2, and 9.3
#4/13/2024


# In[2]:


#initialization 
total=0 #sum of grades
grade=0 # grade
grade_counter=0 #number of grades enterd
grades='grades.txt'


# In[3]:


#9.1
#Funtion to record grades and save to a file
def record_grades(filename):
    try:
        with open (filename, mode='w') as file:
            print("Enter grades (enter 'q' to quit):")
            while True:
                grade=input('Enter a grade:')
                if grade.lower()=='q':
                    break
                else:
                    file.writelines(grade +'\n')
            print('Grades saved to', filename)
    except IOError as e:
        print('Error:',e)     

#Determine filename where you want grades saved
filename='grades.txt'

#call funtion to record grades and save to file
record_grades(filename)


# In[4]:


#9.2
#class average
with open('grades.txt', mode='r') as file:
    #calls grade form grades.txt
    grades=file.readlines()
    #average action
    for grade in grades:  
        grade=int(grade.strip())
        print(grade)
        total+=int(grade)
#display        
print(f'Total: {total}')
print(f'Çount: {len(grades)}')
print(f'Class Average: {total/len(grades) : .2f}')
    


# In[7]:


#9.3
import csv 
#open and write csvfile
with open ('grades.csv', mode='w',newline='') as csvfile:
    writer = csv.writer(csvfile)
#enter information    
    while True:
        firstname = input("Enter student's first name (Enter 'q' to quit):")
        if firstname.lower() == 'q':
            break
        lastname = input("Enter student's last name:")
        exam1grade = int(input("Enter grade for Exam 1:"))
        exam2grade = int(input("Enter grade for Exam 2:"))
        exam3grade = int(input("Enter grade for Exam 3:"))
        data=[firstname,lastname,exam1grade,exam2grade,exam3grade]
        if len(data)==5:
            #writer.writeheader()
            writer.writerow(data)
            print("Saved to grades.csv")
        else:
            print("Invalid input")
#display  
print("Saved to grades.csv')


# In[ ]:





#!/usr/bin/env python
# coding: utf-8

# In[108]:


print("21k-4829 \n Danish \n Ai lab1")


# In[106]:


number = int(input("Enter any number :"))
result =(((number+3)*2)-4)+3
print(result)


# In[107]:


import math
R = float(input("Enter the value of Redius"))
area =math.pi *(R**2)
print(area)


# In[32]:


favorite_color = input("What is your favorite color: ")
output1 = favorite_color * 10
space_count=len(output1)-len(favorite_color)*2
output2 = favorite_color + " "*space_count+ favorite_color
print(output1)
print(output2)
print(output1)


# In[38]:


name ="\t\n Danish \t\n"
print("Name with whitespace",name)

print("Name using lstrip().",name.lstrip())
print("Name using rstrip().",name.rstrip())
print("Name using strip().",name.strip())


# In[44]:


def absolute_num(num):
    if num >= 0:
         return num
    else:
        return -num

number = int(input("Enter any number :"))
result=absolute_num(number)
print("Answer:",result)


# In[57]:


def isprime(num):
    if num < 2:
        return False
    for i in range(2, num):
        if num % i == 0:
            return false
    return True

number = int(input("Enter any number: "))
result = isprime(number)

if result:
    print(f"{number} is a prime number.")
else:
    print(f"{number} is not a prime number.")


# def sort_num(arr):
#     n = len(arr)
# 
#     # Ascending Order
#     for i in range(n):
#         for j in range(0, n-i-1):
#             if arr[j] > arr[j+1]:
#                 arr[j], arr[j+1] = arr[j+1], arr[j]
# 
#     print("Ascending Order.", arr)
#     # Descending Order
#     for i in range(n):
#         for j in range(0, n-i-1):
#             if arr[j] < arr[j+1]:
#                 arr[j], arr[j+1] = arr[j+1], arr[j]
# 
#     print("Descending Order:", arr)
# 
# input_list = [3,5,7,8,2,4,7]
# sort_num(input_list)
# 

# In[58]:


def sort_num(arr):
    n = len(arr)

    # Ascending Order
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

    print("Ascending Order:", arr)

    # Descending Order
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] < arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

    print("Descending Order:", arr)

# Example usage with the given list [3, 5, 2, 1, 7, 4]
input_list = [3, 5, 2, 1, 7, 4]
sort_num(input_list)


# In[69]:


number = int(input("Enter any number "))
for i in range (1, 11):
    table = number*i
    print(number,"*",i,"=",table)


# In[78]:


for i in range (0 , 6):
    if i%3==0:
        continue
    print("i =",i)


# In[105]:


age = float(input("Enter your age :"))
if age <2:
    print("person is baby")
elif 4 <= age <13:
        print("person is kid")
elif 13 <= age <20:
        print("person is teenager")
elif 20 <= age <65:
        print("person is adult")
else:
    print("person is elder")


# In[ ]:





# In[ ]:





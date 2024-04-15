#!/usr/bin/env python
# coding: utf-8

# In[2]:


pip install selenium


# In[3]:


from selenium import webdriver
from bs4 import BeautifulSoup
import time


# In[4]:


driver=webdriver.Chrome()


# In[5]:


driver.get("https://www.flipkart.com/search?q=laptops&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off")


# In[6]:


soup=BeautifulSoup(driver.page_source, 'html.parser')


# In[7]:


soup


# In[8]:


#names price and rating.


# In[13]:


# classes for name price and rating.

names = "_4rR01T"

prices = "_30jeq3 _1_WHN1"

ratings = "_3LWZlK"


# In[15]:


laptop_names_div = soup.find_all(class_= names)
laptop_prices_div = soup.find_all(class_= prices)
laptop_ratings_div = soup.find_all(class_= ratings)


# In[16]:


laptop_names=[]
for i in laptop_names_div:
    laptop_names.append(i.text)


# In[17]:


laptop_prices=[]
for i in laptop_prices_div:
    laptop_prices.append(i.text)


# In[18]:


laptop_ratings=[]
for i in laptop_ratings_div:
    laptop_ratings.append(i.text)


# In[19]:


laptop_names


# In[21]:


laptop_prices=[]
for i in laptop_prices_div:
    laptop_prices.append(i.text)


# In[22]:


laptop_prices


# In[23]:


laptop_ratings=[]
for i in laptop_ratings_div:
    laptop_ratings.append(i.text)


# In[24]:


laptop_ratings


# In[26]:


driver.quit()


# In[27]:


## user define searchbar and showing the product list in jupyter.


# In[31]:


user_input=input("Enter the name of device you want to scrap from Flipkart: ")


# In[33]:


driver=webdriver.Chrome()


# In[34]:


driver.get(f"https://www.flipkart.com/search?q={user_input}&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off")


# In[35]:


soup=BeautifulSoup(driver.page_source,'html.parser')


# In[36]:


soup


# In[38]:


soup.prettify()


# In[41]:


userinput_names_div = soup.find_all(class_= names)


# In[43]:


userinput_names_div


# In[44]:


userinput_names=[]
for i in userinput_names_div:
    userinput_names.append(i.text)


# In[45]:


userinput_names


# In[46]:


userinput_prices_div = soup.find_all(class_= prices)


# In[47]:


userinput_prices_div


# In[48]:


userinput_prices=[]
for i in userinput_prices_div:
    userinput_prices.append(i.text)


# In[49]:


userinput_prices


# In[50]:


userinput_ratings_div = soup.find_all(class_= ratings)

userinput_ratings=[]
for i in userinput_ratings_div:
    userinput_ratings.append(i.text)


# In[51]:


userinput_ratings


# In[52]:


driver.quit()


# In[57]:


## pages of website acc. to user need.

##output : showing the device according tp user need and automatically goes to next page of that website in provided time limit.

## for mobile


# In[55]:


user_input = input("Enter the name of device which you want to scrap from flipkart: ")
driver= webdriver.Chrome()

userinput_names=[]

for i in range(1,11):
    driver.get(f"https://www.flipkart.com/search?q={user_input}&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&page={i}")
    time.sleep(5)    #giving 5 sec to run the website else the website consider us a hacker, so for cting like a user, we use time.sleep
    soup=BeautifulSoup(driver.page_source,'html.parser')
    userinput_names_div=soup.find_all(class_=names)
    for j in userinput_names_div:
        userinput_names.append(j.text)
        
driver.quit()


# In[56]:


userinput_names


# In[59]:


#for laptop

user_input = input("Enter the name of device which you want to scrap from flipkart: ")
driver= webdriver.Chrome()

userinput_names=[]

for i in range(1,11):
    driver.get(f"https://www.flipkart.com/search?q={user_input}&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&page={i}")
    time.sleep(5)    #giving 5 sec to run the website else the website consider us a hacker, so for cting like a user, we use time.sleep
    soup=BeautifulSoup(driver.page_source,'html.parser')
    userinput_names_div=soup.find_all(class_=names)
    for j in userinput_names_div:
        userinput_names.append(j.text)
        
driver.quit()


# In[60]:


#for tv

user_input = input("Enter the name of device which you want to scrap from flipkart: ")
driver= webdriver.Chrome()

userinput_names=[]

for i in range(1,11):
    driver.get(f"https://www.flipkart.com/search?q={user_input}&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&page={i}")
    time.sleep(5)    #giving 5 sec to run the website else the website consider us a hacker, so for cting like a user, we use time.sleep
    soup=BeautifulSoup(driver.page_source,'html.parser')
    userinput_names_div=soup.find_all(class_=names)
    for j in userinput_names_div:
        userinput_names.append(j.text)
        
driver.quit()


# In[66]:


import pandas as pd

df = pd.DataFrame([user_input])

csv_file_path = 'usesr_input.csv'

df.to_csv(csv_file_path, index=False)


# In[ ]:





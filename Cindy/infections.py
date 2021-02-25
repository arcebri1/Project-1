#!/usr/bin/env python
# coding: utf-8

# In[77]:


import matplotlib.pyplot as plt
import pandas as pd
import scipy.stats as st
import numpy as np


# In[78]:


import csv


def sanitize(filename):
    new_filename = "project/cleanoutput.csv" 
    with open(filename, 'r') as input_file:
        reader = csv.reader(input_file, quotechar='"', delimiter=',', quoting=csv.QUOTE_ALL, skipinitialspace=True)
        with open(new_filename, 'w') as output_file:
            writer = csv.writer(output_file)
            for row in reader:
                clean_row = []
                for value in row:
                    clean_value = clean_input(value)
                    clean_row.append(clean_value)
               
                writer.writerow(clean_row)


def clean_input(input):
    try:
       
        return int(input.replace(',', ''))
    except:
        
        return input


sanitize("project/HotSpots.csv")


# In[79]:


Hot_Spots_file = "project/cleanoutput.csv"
Hot_Spots = pd.read_csv(Hot_Spots_file)
Hot_Spots


# In[71]:


Hot_Spots.plot(x='Metro_Area',y='CHANGE PER 100K', )


# In[72]:


Hot_Spots.plot(x='Metro_Area',y='CHANGE PER 100K', )


# In[80]:


Hot_Spots.plot.bar(x="Metro_Area", y="Percent_of_Increase") 


# In[41]:


Hot_Spots.plot(x='Metro_Area', y=['A WEEK AGO','NOW'])


#!/usr/bin/env python
# coding: utf-8

# In[139]:


import pandas as pd
import numpy as np
from scipy.stats import ttest_1samp
from scipy.stats import binom_test
df = pd.read_csv("/Users/Sunny/Desktop/heart.csv")
df.head()


# Dictionary
# 
# - age: The person's age in years
# - sex: The person's sex (1 = male, 0 = female)
# - cp: The chest pain experienced (Value 1: typical angina, Value 2: atypical angina, Value 3: non-anginal pain, Value 4: asymptomatic)
# - trestbps: The person's resting blood pressure (mm Hg on admission to the hospital)
# - chol: The person's cholesterol measurement in mg/dl
# - fbs: The person's fasting blood sugar (> 120 mg/dl, 1 = true; 0 = false)
# - restecg: Resting electrocardiographic measurement (0 = normal, 1 = having ST-T wave abnormality, 2 = showing probable or definite left ventricular hypertrophy by Estes' criteria)
# - thalach: The person's maximum heart rate achieved
# - exang: Exercise induced angina (1 = yes; 0 = no)
# - oldpeak: ST depression induced by exercise relative to rest
# - slope: the slope of the peak exercise ST segment (Value 1: upsloping, Value 2: flat, Value 3: downsloping)
# - ca: The number of major vessels (0-3)
# - thal: A blood disorder called thalassemia (3 = normal; 6 = fixed defect; 7 = reversable defect)
# 
# - target: Heart disease (0 = no, 1 = yes)

# In[140]:


#load data


# In[141]:


df = df.drop(columns=['ca', 'thal', 'oldpeak', 'slope', 'restecg'])


# In[142]:


yes_hd = df[df.target == 1]
no_hd = df[df.target == 0]


# In[143]:


chol_hd= yes_hd.chol
chol_no_hd= no_hd.chol


# In[144]:


healthy = np.average(yes_hd.chol)
unhealthy= np.average(no_hd.chol)


# In[145]:


print("The average Cholestrol level of patients with heart disease is : " + str(unhealthy))
print("The average Cholestrol level of patients with no heart disease is : " + str(healthy))


# In[146]:


tstat, pval = ttest_1samp(chol_hd, 240)


# In[147]:


(pval)/2


# In[148]:


tstat, pval = ttest_1samp(chol_no_hd, 240)
(pval)/2


# In[149]:


num_of_patients= len(df)
print(num_of_patients)


# In[150]:


#num_highfbs_patients= df[df.fbs == 1]
num_highfbs_patients = np.sum(df.fbs)
print(num_highfbs_patients)


# In[151]:


print(0.08*num_of_patients)


# In[154]:


p_value2 = binom_test(num_highfbs_patients, num_of_patients, 0.08, alternative = 'greater')
print("binom_test p-value: ", p_value2)


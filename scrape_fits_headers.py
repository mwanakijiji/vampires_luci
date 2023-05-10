#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# This notebook scrapes meta-data from LBTI FITS headers
# by E.S.

# The idea is 
# 1. Read in the FITS files and scrape the data from the FITS headers
# 2. Write out a machine-readable csv file containing the FITS header data.
# 3. Read the csv file back in as a pandas dataframe, which makes it easy to make visualizations
# 4. Add a column to the dataframe showing the frame number (this may be useful later)
# 5. Write out a final machine-readable csv file (which includes the column of frame numbers)


# In[37]:


## import stuff

import glob
import copy

'''
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.dates import DateFormatter
import numpy as np
import pandas as pd
import datetime
from astropy.io import fits
import asciitable
'''


# In[18]:


file_name_csv_write = 'test.txt'


# In[11]:


stem = '/Users/bandari/Documents/git.repos/vampires_luci/'


# In[12]:


file_names = glob.glob(stem + '*.fits')


# In[13]:


file_names


# In[47]:


## read in a file and extract a meta-data field from the FITS header

# loop over files and read in data
for f in range(0,len(file_names)):
    
    file_name_this = file_names[f]
        
    print('Reading in header info from frame '+str(file_name_this)+'...')
    image, header = fits.getdata(file_name_this,
                                 0,
                                 header=True)
    
    dict_header_this = {key:[header[key]] for key in header}
    print(dict_header_this.keys())
    
    if f==0:
        
        df_master = pd.DataFrame.from_dict(dict_header_this, orient='columns')
        
    else:
        
        df_this = pd.DataFrame.from_dict(dict_header_this, orient='columns')
        df_master = df_master.append(df_this, ignore_index=True)


# In[10]:


# write out final machine-readable csv table

df.to_csv(file_name_csv_write, sep="|")


# In[10]:


# parse the times

#times = [datetime.datetime.strptime(elem, '%H:%M:%S.%f') for elem in df['TIME-OBS']]


# In[11]:


# make manual plots (change this as needed)

'''
plt.plot(times,df['LBT_PARA'], 'o', markersize=2, mec='blue', mfc='blue')
plt.title('PARALLACTIC ANGLE')
plt.xlabel('UT TIME')
plt.ylabel('PA')
formatter = DateFormatter('%H:%M')
plt.gcf().axes[0].xaxis.set_major_formatter(formatter)
plt.show()
'''


# In[ ]:





#!/usr/bin/env python
# coding: utf-8

# This notebook scrapes meta-data from LBTI FITS headers
# by E.S.

# The idea is 
# 1. Read in the FITS files and scrape the data from the FITS headers
# 2. Write out a machine-readable csv file containing the FITS header data.
# 3. Read the csv file back in as a pandas dataframe, which makes it easy to make visualizations
# 4. Add a column to the dataframe showing the frame number (this may be useful later)
# 5. Write out a final machine-readable csv file (which includes the column of frame numbers)

## import stuff

import glob
import copy
from astropy.io import fits
import pandas as pd
import os

file_name_csv_write = 'test.txt'

#stem = '/Users/bandari/Documents/git.repos/vampires_luci/'
stem = '/import/morgana2/snert/VAMPIRESData/201810/20181023/'

file_names = glob.glob(stem + '*.fits')

# for merging 2 dictionaries
def Merge(dict1, dict2):
    res = dict1 | dict2
    return res

## read in a file and extract a meta-data field from the FITS header
# loop over files and read in data
for f in range(0,len(file_names)):
    
    file_name_this = file_names[f]
        
    print('Reading in header info from frame '+str(file_name_this)+'...')

    # assumes 2 headers
    header0 = fits.getheader(file_name_this,ext=0)
    header1 = fits.getheader(file_name_this,ext=1)
    
    dict_header_this0 = {key:[header0[key]] for key in header0}
    dict_header_this1 = {key:[header1[key]] for key in header1}
    dict_header_this = Merge(dict_header_this0, dict_header_this1)

    # append file name too
    dict_header_this['file_name'] = os.path.basename(file_name_this)
    
    if f==0:
        
        df_master = pd.DataFrame.from_dict(dict_header_this, orient='columns')
        
    else:
        
        df_this = pd.DataFrame.from_dict(dict_header_this, orient='columns')
        df_master = df_master.append(df_this, ignore_index=True)


# write out final machine-readable csv table
df_master.to_csv(file_name_csv_write, sep="|")


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





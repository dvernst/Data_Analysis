##importing packages:
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import math
import statsmodels.api as sm
import patsy
from patsy import dmatrices
import analysis_function as ana
import test_function as test


#Import dataset
dataset = pd.read_csv('car_crashes.csv')
dataset.head()

#Slicing the columns we need
fixed_df = dataset[['total', 'no_previous', 'ins_premium']]
fixed_df.head()

#Looking how many columns and row the data has
fixed_df.shape

#Looping to make histogram of each column in our dataset
for variable in fixed_df:
    plt.hist(fixed_df[variable], color='g', bins= 10)
    plt.figure()
    plt.show()
    

# looking for outlier through box plot
total_boxplot = plt.figure()
total_boxplot.suptitle('total_boxplot', fontsize=14, fontweight='bold')
total_boxplot = plt.boxplot(fixed_df['total'])
fig_handle = plt.figure()  

no_previous_boxplot = plt.figure()
no_previous_boxplot.suptitle('no_previous_boxplot', fontsize=14, fontweight='bold')
no_previous_boxplot = plt.boxplot(fixed_df['no_previous'])
fig_handle = plt.figure()  

Log_insurance = plt.figure()
Log_insurance.suptitle('insurance', fontsize=14, fontweight='bold')
Log_insurance = plt.boxplot(fixed_df['ins_premium'])
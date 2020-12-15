import pandas as pd


#Calculating mean
def get_mean(data_col):
    sum_row = 0
    for i in range(0, len(data_col)):
        
        sum_row += data_col[i]
    
    out =  sum_row/len(data_col)
    
    return out

#Calculating variance
def get_variance(data_col):
    sq_diff = 0
    for i in range(0, len(data_col)):
        
        difference = data_col[i] - get_mean(data_col)
        sq_diff += difference **2
    
    result =  sq_diff/len(data_col)
    
    return result


#Calculating standard deviation
def get_stdev(data_col):
    sq_diff = 0
    for i in range(0, len(data_col)):
        
        difference = data_col[i] - get_mean(data_col)
        sq_diff += difference **2
    
    result =  sq_diff/len(data_col)
    std_dev = result**(1/2)
    
    return std_dev
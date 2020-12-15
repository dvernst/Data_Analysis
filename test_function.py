import pandas as pd
import analysis_function as af
import numpy as np

#test get_mean function
def test_get_mean(data_col):
    assert callable(af.get_mean)
    assert isinstance(af.get_mean(data_col), float)
    assert af.get_mean(data_col) == np.mean(data_col)
    print('get mean function works!')
    
#test get_variance function
def test_get_variance(data_col):
    assert callable(af.get_variance)
    assert isinstance(af.get_variance(data_col), float)
    assert af.get_variance(data_col) == np.var(data_col)
    print('get variance function works!')

#test get_stdev function
def test_get_stdev(data_col):
    assert callable(af.get_stdev)
    assert isinstance(af.get_stdev(data_col), float)
    assert af.get_stdev(data_col) == np.std(data_col)
    print('get stdev function works!')

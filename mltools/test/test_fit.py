import nose
from nose.tools import assert_equal, assert_true

import pandas as pd
import numpy as np

from scipy import stats
from numpy import linspace
from mltools import fit 

df = pd.read_csv('data/fit.csv', sep='\t', names=['data'])
df = df.data


def test_get_cv():
    cv = fit.get_cv(df, 'Weibull')
    print(cv)

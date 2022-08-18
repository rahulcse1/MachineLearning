#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun  9 22:14:02 2022

@author: amar
"""


# lets call this file template

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


dataset = pd.read_csv('/home/amar/Desktop/ml/Machine Learning A-Z (Codes and Datasets)/Part 1 - Data Preprocessing/Section 2 -------------------- Part 1 - Data Preprocessing --------------------/Python/Data.csv')
X = dataset.iloc[:,:-1].values
Y = dataset.iloc[:, -1].values

from sklearn.impute import SimpleImputer

imputer = SimpleImputer(missing_values=np.nan, strategy='mean')
imputer.fit(X[:,1:3])
X[:,1:3] = imputer.transform(X[:,1:3])
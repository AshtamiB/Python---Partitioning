# -*- coding: utf-8 -*-
"""
Created on Sat Dec 15 15:36:07 2018

@author: Ashtami
"""
import os
os.chdir("C:/Users/Ashtami/Documents/Python/")

import pandas as pd
import numpy as np
from sklearn.datasets import load_diabetes
from sklearn.model_selection import train_test_split 

diabetes = load_diabetes(return_X_y=False) #load the diabetes dataset

X = diabetes.data
y = diabetes.target

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
print(X_train.shape, y_train.shape)
print(X_test.shape, y_test.shape)

X2 = np.sort(np.random.rand(200, 1), axis=0)



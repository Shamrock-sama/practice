# -*- coding:UTF-8 -*-
import pandas as pd
import xlrd
import numpy as np
import matplotlib as plt

data = pd.read_excel('data.xlsx')
print(data['风速'])

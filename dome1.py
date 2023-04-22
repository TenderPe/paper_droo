import numpy as np

import pandas as pd
data = pd.read_csv(r'../archive/AEP_hourly05.csv', sep='.')
print(data)
print(data.shape)
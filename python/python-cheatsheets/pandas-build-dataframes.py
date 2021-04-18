import pandas as pd
from numpy.random import randint

# 1. Directly add rows, one by one to the DataFrame (very slow)

df1 = pd.DataFrame(columns=['lib', 'qty1', 'qty2'])

for i in range(5):
    df1.loc[i] = ['name' + str(i)] + list(randint(10, size=2))


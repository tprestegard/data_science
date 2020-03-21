import pandas as pd
import matplotlib.pyplot as plt
import ipdb

data_file = 'raw_data/train.csv'

df = pd.read_csv(data_file)

fig = plt.figure()
df.plot()
plt.show()
ipdb.set_trace()

import matplotlib
from matplotlib import pyplot as plt
import pandas as pd
df=pd.read_excel('../Downloads/covid.xlsx')

plt.bar(df['Date'],df['Casesperday'])
plt.plot(df['Date'],df['Casesperday'])
plt.xlabel('dates')
plt.ylabel('Cases_per_day')
plt.tick_params(axis='x',which='major',labelsize=6)
plt.show()

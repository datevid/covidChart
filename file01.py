import pandas as pd
import matplotlib.pyplot as plt

confirmed=pd.read_csv('covid19_confirmed.csv.txt')
deaths=pd.read_csv('covid19_deaths.csv.txt')
recovered=pd.read_csv('covid19_recovered.csv.txt')

confirmed=confirmed.drop(['Province/State','Lat','Long'],axis=1)
deaths=deaths.drop(['Province/State','Lat','Long'],axis=1)
recovered=recovered.drop(['Province/State','Lat','Long'],axis=1)

confirmed=confirmed.groupby(confirmed['Country/Region']).aggregate('sum')
deaths=deaths.groupby(deaths['Country/Region']).aggregate('sum')
recovered=recovered.groupby(recovered['Country/Region']).aggregate('sum')

confirmed=confirmed.T
deaths=deaths.T
recovered=recovered.T

print(confirmed)
countries=['Peru','Brazil','Ecuador','Chile','Mexico'];

for country in countries:
    confirmed[country][60:].plot(label=country)

plt.legend(loc='upper left')
plt.show();
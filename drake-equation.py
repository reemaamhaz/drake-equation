#import necessary modules and libraries
import pandas as pd;
import numpy as np;
import matplotlib.pyplot as plt
import pandas as pd;
import plotly.offline as py

from astropy.table import Table
from fbprophet.plot import plot_plotly
from fbprophet import Prophet

#import necessary modules and libraries
def travelTime(x):
    time = (4.3 * 9500000000000)/ x
    return time
def timeConver(t):
    years = t/(24*365)
    return print (years, "years")

y = travelTime(343180)
timeConver(y)
#create a table with the data
data_rows = [('Voyager 1', 62136, 22248009321.487, 42, 1977),
('Galileo', 173736, 4600000000, 14, 1989),
('Mars Pathfinder', 27000, 497000000, .232, 1996),
('Cassini–Huygens', 122000, 7800000000, 20, 1997),
('New Horizons', 58536, 6600000000, 14, 2006),
('Juno', 209000, 628743036, 8, 2011),
('Parker Solar Probe', 343180, 497000000, 2, 2018)]

#format table
spaceCraftTable = Table(rows=data_rows, names=('Name', 'Fastest Speed Recorded (km/h)', 'Farthest Distance Travelled (km)', 'Years in Orbit', 'Date Launched'))
#prints the table
spaceCraftTable

#plots the data in the table on a line graph
year = [1977, 1989, 1996, 1997, 2006, 2011, 2018]
speed = [62136, 173736, 27000, 122000, 58536, 209000, 343180]
plt.plot(year, speed, color='red')
plt.xlabel('Year Launched')
plt.ylabel('Fastest Speed Recorded (km/h)')
plt.title('Fastest Spacecrafts Launched in the Last 50 Years')

#create a dataframe for manipulation
data = [['1977-09-05', 62136], ['1989-10-18', 173736], ['2011-08-05', 209000], ['2018-08-12', 343180]]
df = pd.DataFrame(data, columns = ['ds', 'y']) 

#use fbprophet to predict groth
m = Prophet()
m.fit(df)
future = m.make_future_dataframe(periods=365*243)
future.tail(n=10)

forecast = m.predict(future)
forecast.tail(n=3)

py.init_notebook_mode()
fig = plot_plotly(m, forecast)  # This returns a plotly Figure
py.iplot(fig)

m.plot_components(forecast)

y = travelTime(50034460)
timeConver(y)



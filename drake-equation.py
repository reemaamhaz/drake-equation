#import necessary modules and libraries
import pandas as pd;
import numpy as np;
import matplotlib.pyplot as plt
import statsmodels.api as sm
import statsmodels.formula.api as smf
import matplotlib.pyplot as plt
import seaborn as sns

#import necessary modules and libraries
from astropy.table import Table

def travelTime(x):
    time = (4.3 * 9500000000000)/ x
    return time
def timeConver(t):
    years = t/(24*365)
    return print (years, "years")

y = travelTime(343180)
timeConver(y)

from astropy.table import Table

data_rows = [('Voyager 1', 62136, 22248009321.487, 42, 1977),
('Galileo', 173736, 4600000000, 14, 1989),
('Mars Pathfinder', 27000, 497000000, .232, 1997),
('Cassini–Huygens', 122000, 7800000000, 20, 1997),
('New Horizons', 58536, 6600000000, 14, 2006),
('Juno', 209000, 628743036, 8, 2016),
('Parker Solar Probe', 343180, 497000000, 2, 2018)]

spaceCraftTable = Table(rows=data_rows, names=('Name', 'Fastest Speed Recorded (km/h)', 'Farthest Distance Travelled (km)', 'Years in Orbit', 'Year Launched'))

spaceCraftTable

year = [1977, 1989, 1997, 1997, 2006, 2016, 2018]
speed = [62136, 173736, 27000, 122000, 58536, 209000, 343180]
plt.plot(year, speed, color='red')
plt.xlabel('Year Launched')
plt.ylabel('Fastest Speed Recorded (km/h)')
plt.title('Fastest Spacecrafts Launched in the Last 50 Years')

import fbprophet
data = [['1977-07-23', 62136], ['1989-07-23', 173736], ['1997-07-23', 27000], ['1997-07-23', 122000], ['2006-07-23', 58536], ['2016-07-23', 209000], ['2018-07-23', 343180]]
df = pd.DataFrame(data, columns = ['ds', 'y']) 
predictYr = fbprophet.Prophet()
predictYr.fit(df)

forecast = predictYr.make_future_dataframe(periods=365 * 2, freq='D')
# Make predictions
forecast = predictYr.predict(gm_forecast)

predictYr.plot(forecast, xlabel = 'Date', ylabel = 'Fastest Speed (km/h)')
plt.title('Spacecraft Predictions');

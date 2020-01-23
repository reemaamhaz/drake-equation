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

spaceCraftTable = Table(names=('Name', 'Fastest Speed Recorded (km/h)', 'Farthest Distance Travelled (km)', 'Years in Orbit', 'Year Launched'))
spaceCraftTable.add_row(('Voyager 1', 62136, 22248009321.487, 42, 1977))
spaceCraftTable.add_row(('Galileo', 173736, 4600000000, 14, 1989))
spaceCraftTable.add_row(('Mars Pathfinder', 27000, 497000000, .232, 1997))
spaceCraftTable.add_row(('Cassini–Huygens', 122000, 7800000000, 20, 1997))
spaceCraftTable.add_row(('New Horizons', 58536, 6600000000, 14, 2006))
spaceCraftTable.add_row(('Juno', 209000, 628743036, 8, 2016))
spaceCraftTable.add_row(('Parker Solar Probe', 343180, 497000000, 2, 2018))

spaceCraftTable[:5]

spaceCraftTable.set_index('Year Launched')['Fastest Speed Recorded (km/h)'].plot.line();

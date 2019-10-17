"""
    Author: João Ventura <flatangleweb@gmail.com>
    
    
    This recipe shows sample code for computing 
    the temperament protocol.

"""

from flatlib_fr import const
from flatlib_fr.chart import Chart
from flatlib_fr.datetime import Datetime
from flatlib_fr.geopos import GeoPos
from flatlib_fr.protocols import behavior


# Build a chart for a date and location
date = Datetime('2015/03/13', '17:00', '+00:00')
pos = GeoPos('38n32', '8w54')
chart = Chart(date, pos)

# Behavior
factors = behavior.compute(chart)
for factor in factors:
    print(factor)
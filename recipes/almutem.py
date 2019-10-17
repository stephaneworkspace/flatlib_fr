"""
    Author: João Ventura <flatangleweb@gmail.com>
    
    
    This recipe shows sample code for computing 
    the almutem protocol.

"""

from flatlibfr import const
from flatlibfr.chart import Chart
from flatlibfr.datetime import Datetime
from flatlibfr.geopos import GeoPos
from flatlibfr.protocols import almutem


# Build a chart for a date and location
date = Datetime('2015/03/13', '17:00', '+00:00')
pos = GeoPos('38n32', '8w54')
chart = Chart(date, pos)

# Print almutem scores
alm = almutem.compute(chart)
for k, v in alm['Score'].items():
    print(k, v)  # Mercury scores 40
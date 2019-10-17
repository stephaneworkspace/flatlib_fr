"""
    Author: João Ventura <flatangleweb@gmail.com>
    
    
    This recipe shows sample code for handling 
    solar returns.

"""

from flatlib_fr import const
from flatlib_fr.chart import Chart
from flatlib_fr.datetime import Datetime
from flatlib_fr.geopos import GeoPos
from flatlib_fr.predictives import returns


# Build a chart for a date and location
date = Datetime('2013/06/13', '17:00', '+01:00')
pos = GeoPos('38n32', '8w54')
chart = Chart(date, pos)

# Get the next solar return Chart given a date
today = Datetime('2015/04/06', '10:40', '+01:00')
srChart = returns.nextSolarReturn(chart, today)

# Print the date and Asc
asc = srChart.get(const.ASC)
print(asc)           # <Asc Taurus +26:25:47>
print(srChart.date)  # <2015/06/14 04:38:37 01:00:00>

# Solar return of the year
srChart = chart.solarReturn(2015)
print(asc)           # <Asc Taurus +26:25:47>
print(srChart.date)  # <2015/06/14 04:38:37 01:00:00>
import matplotlib as mpl 
import matplotlib.pyplot as plt 
import numpy as np
from matplotlib import pyplot 
from matplotlib.collections import LineCollection 
import fastf1 as ff1 
from fastf1 import plotting 
from fastf1.core import Laps

#Set Parameters
year=2025
wknd='9'
sess='R'
driver='HAM' #Lewis Hamilton
colourmap =mpl.colormaps['plasma']

#Load Session Data session
session=ff1.get_session(year,wknd,sess) 
session.load()
weekend=session.event

#Pick Fastest Lap for the Driver 
lap=session.laps.pick_driver(driver).pick_fastest()

#Extract Telemetry Data and Convert to Numpy Arrays

x=lap.telemetry['X'].to_numpy()
y=lap.telemetry['Y'].to_numpy()
speed=lap.telemetry['Speed'].to_numpy() 

#Create Segments for Line Collection
points = np.array([x, y]).T.reshape(-1, 1, 2)
segments = np.concatenate([points[:-1], points[1:]], axis=1)

# Build the plot
fig, ax = plt.subplots(figsize=(10, 8))

# Create the line collection (coloured by speed)
lc = LineCollection(segments, cmap=colourmap, norm=plt.Normalize(speed.min(), speed.max()))
lc.set_array(speed)
lc.set_linewidth(3)

# Add to the axes
line = ax.add_collection(lc)

# Formatting
ax.set_title(f"{driver} Fastest Lap - {weekend.EventName} {year}")
ax.set_xlabel("X Coordinate")
ax.set_ylabel("Y Coordinate")
ax.autoscale()
ax.set_aspect('equal')

# Add colour bar to show speed scale
cbar = plt.colorbar(line, ax=ax)
cbar.set_label("Speed (km/h)")

# Show the plot
plt.show()
print(plt.get_backend())
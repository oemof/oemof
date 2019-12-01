#!/usr/bin/env python
# coding: utf-8
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import matplotlib.dates as mdates
from datetime import datetime
import textwrap

events = pd.read_csv('sorted_releases.csv')
events['date'] = pd.to_datetime(events['date'], format='%Y-%m-%d')
events = events.sort_values(by='date')
names = events['description']
dates = events['date']
levels = events['level']

fig, ax = plt.subplots(figsize=(12, 6))

# Create the base line
start = min(dates)
stop = max(dates + pd.DateOffset(50))

ax.plot((start, stop), (0, 0), 'k', alpha=1)
ax.scatter(stop, 0, s=70, marker='>', c='k')

# Iterate through releases annotating each one
for ii, (iname, idate, ilevel) in enumerate(zip(names, dates, levels)):
    level = ilevel
    vert = 'top' if level < 0 else 'bottom'

    ax.scatter(idate, 0, s=100, facecolor='w', edgecolor='k', zorder=9999)
    # Plot a line up to the text
    ax.plot((idate, idate), (0, level), c='#002E4F', alpha=.7)
    # Give the text a faint background and align it properly
    wrapped_name = textwrap.fill(iname, 14)
    ax.text(idate, level, wrapped_name,
            horizontalalignment='left', verticalalignment=vert, fontsize=14,
            backgroundcolor=(1., 1., 1., 1))

# Set the xticks formatting
# format xaxis with 3 month intervals
ax.get_xaxis().set_major_locator(mdates.MonthLocator(interval=6))
ax.get_xaxis().set_major_locator(mdates.MonthLocator(interval=6))
ax.get_xaxis().set_major_formatter(mdates.DateFormatter("%m/%Y"))
fig.autofmt_xdate()

# Space to avoid cutting off labels
ax.set_ylim(-4,3.2)
plt.gcf().subplots_adjust(right=0.15)
plt.gcf().subplots_adjust(bottom=0.2)
plt.tight_layout()

# Remove components for a cleaner look
plt.setp((ax.get_yticklabels() + ax.get_yticklines() +
          list(ax.spines.values())), visible=False)

plt.savefig('oemof_releases.pdf')
plt.show()




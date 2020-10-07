#!/usr/bin/env python
# coding: utf-8

# ## Twitch Part 2: Visualize Data with Matplotlib
# 
# Welcome to Part 2 of the Twitch Project. In this part of the project, you will be taking your findings from the SQL queries and visualize them using Python and Matplotlib, in the forms of:
# 
# Bar Graph: Featured Games
# Pie Chart: Stream Viewers’ Locations
# Line Graph: Time Series Analysis
# The Twitch Science Team provided this practice dataset. You can download the .csv files (800,000 rows) from GitHub.
# 
# Note: This is data is scrubbed and is meant for practice use only.

# ## Bar Graph: Featured Games
# 
# Twitch’s home page has a Featured Games section where it lists the “Games people are watching now”.
# 
# In the previous part of the project, you used SQL to find the top 10 trending games (on January 1st, 2015) and their number of viewers.
# 
# It looked something like this:
# 
# ![featured-sql.png](attachment:featured-sql.png)
# 
# Featured Games
# In the next few tasks, you are going to take this data and plot a bar graph using Matplotlib.
# 
# Let’s get started!
# 
# Now, use the plt.bar() to plot a bar graph using range(len(games)) and viewers as arguments.
# 
# Feel free to pick a color, too (using color='____').
# 
# Then, use plt.show() to visualize it.
# 
# Let’s make the graph more informative by doing the following:
# 
# Add a title
# Add a legend
# Add axis labels
# Add ticks
# Add tick labels (rotate if necessary)

# In[10]:


from matplotlib import pyplot as plt
import numpy as np
import pandas as pd


# In[11]:


games = ["LoL", "Dota 2", "CS:GO", "DayZ", "HOS", "Isaac", "Shows", "Hearth", "WoT", "Agar.io"]

viewers =  [1070, 472, 302, 239, 210, 171, 170, 90, 86, 71]

ax=plt.subplot()
plt.bar(range(len(games)),viewers, color = 'red')
ax.set_xticks(range(len(games)))
ax.set_xticklabels(games, rotation = 30)
plt.xlabel("Games")
plt.ylabel("Viewers")
plt.title("Viewers per game on Jan-01-2015")
plt.legend(["Twitch"])
plt.show()


# In[12]:


plt.clf()


# ## Pie Chart: League of Legends Viewers' Whereabouts
# 
# There are 1070 League of Legends viewers from this dataset. Where are they coming from?
# 
# When you performed the SQL query, you got this result:
# 
# ![countries-sql.png](attachment:countries-sql.png)
# 
# As well as other countries that accounted for another 279 stream viewers.
# 
# In the next few tasks, you are going to take this data and make a pie chart.
# 
# Let’s get started!

# Because there are 12 countries (including N/A and Others), let’s create an array called colors and add 12 color codes to it, like so:

# In[13]:


colors = ['lightskyblue', 'gold', 'lightcoral', 'gainsboro', 'royalblue', 'lightpink', 'darkseagreen', 'sienna', 'khaki', 'gold', 'violet', 'yellowgreen']


# Then, use plt.pie() to plot a pie chart.

# In[14]:


labels = ["US", "DE", "CA", "N/A", "GB", "TR", "BR", "DK", "PL", "BE", "NL", "Others"]

countries = [447, 66, 64, 49, 45, 28, 25, 20, 19, 17, 17, 279]

plt.pie(countries, colors = colors, labels = labels)
plt.axis("equal")
plt.show()


# Then, inside plt.pie(), we are going to:
# 
# -Add the explode
# -Add shadows
# -Turn the pie 345 degrees
# -Add percentages
# -Configure the percentages’ placement

# In[15]:


plt.clf()

explode = (0.1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)

plt.pie(countries, colors = colors, explode=explode, shadow=True, startangle=345, autopct="%1.0f%%", pctdistance=1.2)
plt.axis("equal")
plt.legend(labels, loc = "right")
plt.title("League of Legends Viewers' Whereabouts")
plt.show()


# In[16]:


plt.clf()


# ## Line Graph: Time Series Analysis
# 
# We were able to find the number of US viewers at different hours of the day on January 1st, 2015:
# 
# ![time.png](attachment:time.png)
# 
# Use plt.plot() to plot a line graph.
# 
# Don’t forget to throw in hour and viewers_hour.
# 
# Then, add the title, the axis labels, legend, and ticks.
# 
# Lastly, use plt.show() to visualize.

# In[17]:


hour = range(24)

viewers_hour = [30, 17, 34, 29, 19, 14, 3, 2, 4, 9, 5, 48, 62, 58, 40, 51, 69, 55, 76, 81, 102, 120, 71, 63]

ax=plt.subplot()
plt.plot(hour,viewers_hour, marker = "o")
ax.set_xticks(hour)
plt.xlabel("Hour")
plt.ylabel("Viewers")
plt.legend(["Jan-01-2015"])
plt.title("Time Series")
plt.show()


# There is some uncertainty in these numbers because some people leave their browsers open. Let’s account for a 15% error in the viewers_hour data.
# 
# First, create a list containing the upper bound of the viewers_hour and call it y_upper.
# 
# Then, create a list containing the lower bound of the viewers_hour and call it y_lower.
# 
# Lastly, use plt.fill_between() to shade the error, with an alpha of 0.2.

# In[20]:


y_upper = [i +  (i*0.15) for i in viewers_hour]
y_lower = [i - (i*0.15) for i in viewers_hour]

ax=plt.subplot()
plt.plot(hour,viewers_hour, marker = "o")
plt.fill_between(hour, y_lower, y_upper, alpha=0.2)
ax.set_xticks(hour)
plt.xlabel("Hour")
plt.ylabel("Viewers")
plt.legend(["Jan-01-2015"])
plt.title("Time Series")
plt.show()


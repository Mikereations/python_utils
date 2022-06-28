"""
This file contains functions that helpout with making decent graphs. From changing 
Colors and fonts to producing bestfit lines. 

Date    : Tuesday, 28th Jun, 2022
Author  : Mike Banabila
"""
import matplotlib
import matplotlib.pyplot as plt
import numpy as np

# Beautiful colors that can be used to plot. 
colors = ["royalblue","darkgoldenrod", "darkcyan","indigo","palevioletred","darkgreen","darkviolet","darkred","olive","gold","tomato","slategray","crimson","pink"]
linestyles = ['solid' , 'dashed', 'dashdot', 'dotted']


# Making graphs beautiful again. Call this function after y
def graph_settings(xlabel, ylable, title="", legend_location='upper right', walls=[1,1,1,1]):
    # Comment out the next line if you dont want a dark theme
    plt.style.use('dark_background')
    fig, ax = plt.subplots(nrows=1,ncols=1,figsize=(8,6.5))
    # Comment out the next four lines or adjust them depending on which walls 
    # you want visible in your final plot
    ax.spines["top"].set_visible(walls[0])
    ax.spines["right"].set_visible(walls[1])
    ax.spines["left"].set_visible(walls[2])
    ax.spines["bottom"].set_visible(walls[3])
    ax.minorticks_on()
    ax.set_xlabel(xlabel, fontsize=20, labelpad=4, fontfamily='monospace')
    ax.set_ylabel(ylable, fontsize=20, labelpad=4, fontfamily='monospace')
    plt.xticks(fontsize=15)
    plt.yticks(fontsize=15)
    ax.set_title(title, fontsize=16, fontfamily='monospace')
    ax.xaxis.set_tick_params(length=5, width=1)
    ax.yaxis.set_tick_params(length=5, width=1)
    plt.legend(fontsize=10, loc=legend_location)

# Read in a space-delimited text file, skipping header comments. Returns the data 
# as a 2D array.
def read_txtfile(filename):
    f = open(filename, 'r')
    data = np.genfromtxt(f, comments='#', dtype=float)
    f.close()
    return(data)

# Fits the data x and y through the best fit line. You can determine the degrees
# of freedom.
def best_fit(x,y,degrees) :
    coeff, sqres, _, _, _ = np.polyfit(x, y, degrees, full=True)
    x_made_up = np.linspace(-0.3,1.5,1000)
    y_made_up = np.zeros_like(x_made_up)
    for i in range(degrees) :
        y_made_up += coeff[i]*x_made_up**(degrees-i)
    y_made_up += coeff[-1]
    return x_made_up,y_made_up


# Example of how to use the grpah_setting function.
graph_settings("x", "y")
plt.plot([1,2,3,4,5,6,7], [1,4,9,16,25,36,49])
plt.show()
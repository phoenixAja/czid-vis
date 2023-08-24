import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np


def plot_czid_heatmap(
    df,
    title="",
    x_axis_title="",
    y_axis_title="",
    legend_label="",
    color_palette="YlOrRd",
    top_n=25, 
    figure_size=(8,8), 
    log=False, 
    sort_values = True, 
    ):
    '''
    Plot the final heatmap
    '''
    
    plot_df = df
    
    x = plot_df.unstack().groupby(level=0, group_keys=False).nlargest(top_n).to_frame()
    all_top_n_taxa = list(set([i[1] for i in x.index]))
    plot_df = plot_df.loc[all_top_n_taxa]  # filter the plot data to only include taxa in the top_n
    print(plot_df.shape)
    
    if sort_values:
        plot_df.sort_index(inplace=True)
    
    # apply log-scale to value
    if(log):
        plot_df = np.log(plot_df + 1)
        
    # set CZ ID color pallette - yellow to orange to red
    czid_colors = sns.color_palette(color_palette, as_cmap=True)  
    
    # plot heatmap
    fig, ax = plt.subplots(figsize=figure_size)
    ax = sns.heatmap(
        plot_df, 
        cmap=czid_colors, 
        linewidths=.1, 
        linecolor='grey', 
        square=True, 
        xticklabels=True, 
        yticklabels=True, 
        ax=ax, 
        cbar_kws={'shrink': 0.5}
    )
    
    # Add padding to axis tick marks
    ax.tick_params(axis='y', which='major', pad=10)  # pad on y-axis
    ax.tick_params(axis='x', which='major', pad=10)  # pad on x-axis

    # Adjust the legend (colorbar)
    cbar = ax.collections[0].colorbar
    cbar.ax.set_ylabel(legend_label, size=10)  # Adjust legend label
    cbar.ax.tick_params(labelsize=8)  # Adjust tick label size

    # Add title and axis labels
    plt.title(title, pad=20)
    
    if not x_axis_title:
        x_axis_title=plot_df.columns.name.replace("_", " ").title()

    if not y_axis_title:
        y_axis_title=plot_df.index.name.replace("_", " ").title()
        
    plt.xlabel(x_axis_title)
    plt.ylabel(y_axis_title)

    return plt
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np


def plot_czid_heatmap(df, plot_value = 'nt_bpm', top_n=10, figure_size=(8,8), 
                      log=False, sort_values = True, output_filename = 'output.pdf'):
    '''
    Plot the final heatmap
    '''
    
    # convert long df to wide df
    plot_df = df.pivot(index='name', columns='samplename', values=plot_value)
    
    x = plot_df.unstack().groupby(level=0, group_keys=False).nlargest(top_n).to_frame()
    all_top_n_taxa = set([i[1] for i in x.index])
    print(plot_df.shape)
    plot_df = plot_df.loc[all_top_n_taxa]  # filter the plot data to only include taxa in the top_n
    print(plot_df.shape)
    
    # sort the rownames alphabetically
    if sort_values:
        plot_df.sort_index(inplace=True)
    
    # apply log-scale to value
    if(log):
        plot_df = np.log(plot_df + 1)
        
    # set CZ ID color pallette - yellow to oranage to red
    czid_colors = sns.color_palette("YlOrRd", as_cmap=True)  
    
    # plot heatmap
    plt.figure(figsize=figure_size)
    sns.heatmap(plot_df, cmap=czid_colors, linewidths=.1, linecolor='grey', 
                square=True, xticklabels=True, yticklabels=True) 
    plt.tight_layout()
    plt.savefig(output_filename)
    plt.show()
import pandas as pd

def read_ont_czid_report(filename,
                     metric = 'nt_bpm',
                     tax_level = [], 
                     category_list = [],
                     min_nt_bpm = 1,
                     min_nr_bpm = 1,
                     min_nt_contigs = 0,
                     min_nr_contigs = 0):

    '''
    Read in the CZ ID Sample Taxon Reports by filename, applying filtering. 
    Conservative default filter values are provided, but filters may be adjusted when calling the function.
    '''
    
    df = pd.read_csv(filename)
    df.fillna(0, inplace=True)
    
    # filter on tax_level
    if(len(tax_level) > 0):
        df = df.loc[df['tax_level'].isin(tax_level)]
        
    # select only categories of interest
    if(len(category_list) > 0):
        df = df.loc[df['category'].isin(category_list)]
    
    # apply filters on specific data columns
    df = df[df['nt_bpm'] >= min_nt_bpm]           # min_nt_bpm
    df = df[df['nr_bpm'] >= min_nr_bpm]           # min_nr_bpm
    df = df[df['nt_contig_b'] >= min_nt_contigs]  # min_nt_contigs
    df = df[df['nr_contig_b'] >= min_nr_contigs]  # min_nr_contigs

    # add samplename column to enable concatenating dataframes to long format 
    df['samplename'] = ['_'.join(filename.split('/')[-1].split('_')[0:-3]) for i in range(len(df.index))]
    
    return(df)


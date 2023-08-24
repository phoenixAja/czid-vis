import pandas as pd

def read_amr_czid_report(filename, num_contigs_cutoff = 0, cutoff_list = ['Strict', 'Perfect', 0], 
                     contig_cov_breadth_cutoff = 0, contig_percent_id_cutoff = 0,
                     num_reads_cutoff = 0, read_coverage_breadth_cutoff = 0, read_coverage_depth_cutoff = 0, 
                     rpm_cutoff = 0, dpm_cutoff = 0, drug_class_list = [], 
                     split_drug_class = True):
    
    # read in the AMR data from the .csv file
    df = pd.read_csv(filename)
    df.fillna(0, inplace=True)

    # apply quality filters
    df = df[df.num_contigs >= num_contigs_cutoff]
    if('nan') in cutoff_list:
        df = df[df['cutoff'].isin(cutoff_list) | df['cutoff'].isnull()]
    else:
        df = df.loc[df['cutoff'].isin(cutoff_list)]
    df = df[df.contig_coverage_breadth >= contig_cov_breadth_cutoff]
    df = df[df.contig_percent_id >= contig_percent_id_cutoff]
    df = df[df.num_reads >= num_reads_cutoff]
    df = df[df.read_coverage_breadth >= read_coverage_breadth_cutoff]
    df = df[df.read_coverage_depth >= read_coverage_depth_cutoff]
    df = df[df.rpm >= rpm_cutoff] 
    df = df[df.dpm >= dpm_cutoff] 
    
    # filter by drug class
    if len(drug_class_list) > 0:
        print(df.shape)
        df = df.loc[[(sum([dclass in i for dclass in drug_class_list]) > 0) for i in df['drug_class']]]
        print(df.shape)
    
    # define a "max_breadth" field that combines information from reads and contigs
    df['max_breadth'] = df[["contig_coverage_breadth", "read_coverage_breadth"]].max(axis=1)
    
    return(df)

import pandas as pd

def format_drug_class(df):
    '''
    The drug_class output by CARD contains semicolon-delimited class names. This function will
    separate these out and duplicate lines of the matrix to properly format pivot tables.
    '''
    
    print(df.shape)
    tally_dc = 0
    new_df = []
    for i in df.index:
        drug_class_split = [this.strip() for this in df.loc[i,'drug_class'].split(';')]
        for dc in drug_class_split:
            tally_dc += 1
            df.loc[i,'drug_class_split'] = dc
            new_df.append(df.loc[i])

            
    final_df = pd.DataFrame(new_df)
    df = final_df
    print(tally_dc)
    print(df.shape)
    return(df)
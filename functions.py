import pandas as pd
import numpy as np
from functools import reduce


def fetch(player_list):
    df_pga = pd.DataFrame()
    for player in player_list:
        df1 = pd.read_csv(f'./Data/{player}/{player}_OT.csv', index_col = 'Tournament')
        df1.columns = [col.lower().replace(' ', '_') for col in df1.columns]
        df1['date'] = pd.to_datetime(df1['date'])
        df1.replace('-', np.nan, inplace = True)
        df1['finish'] = df1['finish_pos.']

        df2 = pd.read_csv(f'./Data/{player}/{player}_AG.csv', index_col = 'Tournament')
        df2.columns = [col.lower().replace(' ', '_') for col in df2.columns]
        df2['date'] = pd.to_datetime(df2['date'])
        df2.replace('-', np.nan, inplace = True)

        df3 = pd.read_csv(f'./Data/{player}/{player}_ArG.csv', index_col = 'Tournament')
        df3.columns = [col.lower().replace(' ', '_') for col in df3.columns]
        df3['date'] = pd.to_datetime(df3['date'])
        df3.replace('-', np.nan, inplace = True)

        df4 = pd.read_csv(f'./Data/{player}/{player}_P.csv', index_col = 'Tournament')
        df4.columns = [col.lower().replace(' ', '_') for col in df4.columns]
        df4['date'] = pd.to_datetime(df4['date'])
        df4.replace('-', np.nan, inplace = True)

        dfs = [df1, df2, df3, df4]
        df_total = reduce(lambda left,right: pd.merge(left,right,on='date', left_index = True), dfs)
        df_total['player'] = player

        df_pga = df_pga.append(df_total)
        
    return df_pga


def to_inches(distance):
    
    dist_ = distance.split("\' ")
    if len(dist_) == 1:
        dist_ = dist_[0].strip('"')
        ft_ = 0
        in_ = float(dist_)
    else: 
        ft_ = float(dist_[0])
        in_ = float(dist_[1].replace("\"",""))
        
    return (12*ft_) + in_
import pandas as pd
import config


def load_player_data():
    df = pd.read_excel(config.path + 'defense.xlsx')[config.dict_columns['defense']]

    for key in list(config.dict_dfs.keys())[1:]:
        df_key = config.dict_dfs[key][config.dict_columns[key]]
        df = df.merge(df_key, on=['Player', 'Pos', '90s', 'Age'], how='left')

    # file_path = 'C:/Users/Admin/Desktop/streamlit_ppi/stats_v1.csv'
    # df = pd.read_csv(file_path)
    df = df[df['Pos'] != 'GK']

    return df

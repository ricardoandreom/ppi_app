import pandas as pd

path = 'C:/Users/Admin/Desktop/streamlit_ppi/'

documentation_md_str = """
This tool allows you to calculate a Player Performance Index (PPI) based on various physical attributes of football players. 
The calculation takes into account the position of the player and applies different weights to each attribute based on the position. 
### How the PPI Calculation Works:
The PPI is calculated by:
1. **Age Adjustment**: The player's age influences the final score. Players younger than 23 have their score increased by 5%, while players over 30 see a 5% reduction.
2. **Attribute Normalization**: For each selected attribute (e.g., speed, strength), the player's value is compared to the maximum value in the dataset, normalizing it to a scale of 0 to 1.
3. **Position-Specific Weights**: For each position (FW, MF, DF), specific weights are assigned to the attributes. The sum of these weights must be equal to 1 for each position.
4. **PPI Calculation**: The final PPI for a player is the weighted sum of their normalized attributes, adjusted by age.

### How it works:
1. **Step 1: Select Physical Variables** - You can choose which physical attributes (e.g., speed, strength) to include in the PPI calculation.
2. **Step 2: Assign Weights by Position** - For each position (FW, MF, DF), assign specific weights to the selected attributes. The sum of weights for each position must be equal to 1.
3. **Step 3: Calculate PPI** - Once all weights are assigned correctly, you can calculate the PPI for each player.
4. **Additional Feature** - In the future, you can visualize selected player performance using a radar chart to compare them in percentile format. Stay tuned!
"""

dict_columns = {
    'defense': ['Player', 'Pos', '90s', 'Age', 'Tackles_Tkl', 'Tackles_TklW', 'Challenges_Tkl', 'Challenges_Att', 'Challenges_Tkl%'],
    'gsca': ['Player', 'Pos', '90s', 'Age', 'SCA_SCA'],
    'misc': ['Player', 'Pos', '90s', 'Age', 'Performance_CrdY', 'Performance_CrdR', 'Performance_Fls', 'Recoveries', 'Aerial Duels Won', 'Aerial Duels Lost'],
    'pass_types': ['Player', 'Pos', '90s', 'Age', 'Pass Types_Live', 'Pass Types_Dead', 'Outcomes_Cmp'],
    'passing': ['Player', 'Pos', '90s', 'Age', 'Passes completed', 'Passes attempted', 'Pass completion%', 'Short passes completion', 'Short passes attempted', 'Short passes completion%', 'Medium passes completion', 'Medium passes attempted', 'Medium passes completion%', 'Long passes completed', 'Long passes attempted', 'Long passes completion%', 'Assists', 'Key passes'],
    'shooting': ['Player', 'Pos', '90s', 'Age', 'Goals', 'Shots', 'Shots on target%', 'Shots on target', 'xG']
}

dict_dfs = {
    'defense': pd.read_excel(path + 'defense.xlsx'),
    'gsca':  pd.read_excel(path + 'gsca.xlsx'),
    'misc':  pd.read_excel(path + 'misc.xlsx'),
    'pass_types': pd.read_excel(path + 'pass_types.xlsx'),
    'passing': pd.read_excel(path + 'passing.xlsx'),
    'shooting': pd.read_excel(path + 'shooting.xlsx')
}

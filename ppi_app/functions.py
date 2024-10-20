import pandas as pd
from io import BytesIO


def calculate_ppi_with_context_v2(player_data, physical_weights, position_weights):
    def age_adjustment(age_value):
        if pd.isna(age_value):
            return 1.0
        try:
            age = int(str(age_value).split('-')[0])
            if age < 23:
                return 1.05
            elif age > 30:
                return 0.95
        except ValueError:
            return 1.0

        return 1.0

    player_ppi = {}
    for i, row in player_data.iterrows():
        ppi_score = 0
        position = row['Pos'].split(',')[0]
        position_adjust = position_weights.get(position, {})

        for stat, weight in physical_weights.items():
            stat_value = row.get(stat, 0)
            if pd.isna(stat_value) or stat_value == 0:
                normalized_value = 0.1
            else:
                normalized_value = min(stat_value / player_data[stat].max(), 1)

            stat_weight = position_adjust.get(stat, weight)
            ppi_score += normalized_value * stat_weight * 5

        ppi_score *= age_adjustment(row['Age'])

        player_ppi[row['Player']] = ppi_score

    return player_ppi


def convert_df_to_xlsx(df):
    output = BytesIO()
    writer = pd.ExcelWriter(output, engine='xlsxwriter')
    df.to_excel(writer, index=False, sheet_name='PPI Results')
    writer.close()
    processed_data = output.getvalue()
    return processed_data

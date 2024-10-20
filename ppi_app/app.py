import streamlit as st
import pandas as pd
from datetime import datetime
from functions import calculate_ppi_with_context_v2, convert_df_to_xlsx
from get_data import load_player_data
import config

df = load_player_data()
df = df[df['Pos'] != 'GK']

excluded_columns = ['Player', 'Age', 'Pos']

st.title("PPI Calculation Interface")

st.subheader("Documentation")

st.markdown(config.documentation_md_str)

st.subheader("Step 1: Select Physical Variables")
available_columns = [col for col in df.columns if col not in excluded_columns]
selected_columns = st.multiselect("Select columns for physical weights", available_columns)

if selected_columns:
    st.subheader("Step 2: Select Weights for Each Position")
    position_weights = {}
    positions = ['FW', 'MF', 'DF']

    for pos in positions:
        st.markdown(f"### Position: {pos}")
        pos_weights = {}
        for col in selected_columns:
            pos_weight = st.number_input(f"Weight for {col} ({pos})", min_value=0.0, max_value=1.0, value=0.1)
            pos_weights[col] = pos_weight

        sum_pos_weights = sum(pos_weights.values())
        if sum_pos_weights != 1.0:
            st.warning(f"Sum of position weights for {pos} is {sum_pos_weights:.2f}. It should equal 1.")
        if sum_pos_weights > 0:
            for col in pos_weights:
                pos_weights[col] = pos_weights[col] / sum_pos_weights
        position_weights[pos] = pos_weights

    st.subheader("Step 3: Calculate PPI")
    if st.button("Calculate PPI"):
        if all(sum(position_weights[pos].values()) == 1.0 for pos in positions):
            ppi_results_with_context_v2 = calculate_ppi_with_context_v2(df, {col: 1 for col in selected_columns},
                                                                        position_weights)
            ppi_df = pd.DataFrame.from_dict(ppi_results_with_context_v2, orient='index', columns=['PPI'])
            ppi_df = ppi_df.sort_values(by='PPI', ascending=False).reset_index().rename(columns={'index': 'Player'})

            st.write(ppi_df)

            date_today = datetime.today().strftime('%Y-%m-%d')

            xlsx_data = convert_df_to_xlsx(ppi_df)
            st.download_button(label="Download PPI Data as XLSX",
                               data=xlsx_data,
                               file_name=f"ppi_results_{date_today}.xlsx",
                               mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")
        else:
            st.error("The sum of weights for all positions must equal 1. Please adjust the values.")

    st.subheader("Step 4: Plot Selected Player Percentiles Radar Chart?")

    image = config.path + 'image_example.png'
    st.image(image, caption="Example Radar Chart for Nathan Aké", use_column_width=True)

    st.subheader("Step 5:??? Generate some comment about the selected player using a LLM.")

else:
    st.warning("Please select at least one physical variable.")

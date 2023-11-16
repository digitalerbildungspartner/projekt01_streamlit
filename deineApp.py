import streamlit as st
import pandas as pd

# Lade die CSV-Datei
csv_file = st.file_uploader("C:/Users/deinPfad/deineDatei.csv", type=["csv"])

if csv_file is not None:
    # Konvertiere die Datei in ein Pandas DataFrame
    csv_data = pd.read_csv(csv_file)

    # Zeige die ersten 10 Zeilen des DataFrames an
    st.write(csv_data.head(10))

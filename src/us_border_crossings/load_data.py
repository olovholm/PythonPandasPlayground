import pandas as pd
from common.paths import BORDER_CSV
from common.db_connection import DatabaseConnector



def load_data():

    df = pd.read_csv(BORDER_CSV)

    for col in df.columns:
        print(f"Distinct values in {col}:")
        print(df[col].unique())
        print()

    dim_port_df = df[['Port Name', 'Port Code', 'Latitude', 'Longitude', 'Border', 'State']].drop_duplicates()
    dim_port_df = dim_port_df.rename(columns={
        'Port Name': 'port_name',
        'Port Code': 'port_codes',
        'State': 'state',
        'Latitude': 'latitude',
        'Longitude': 'longitude',
        'Border': 'border',
    })

    dim_border_crossing_measure_df = df[['Measure']].drop_duplicates()




    db = DatabaseConnector()
    engine = db.get_engine()

    dim_port_df.to_sql('dim_port', con=engine, if_exists='replace', index=False)
    dim_border_crossing_measure_df.to_sql('dim_border_crossing_measure', con=engine, if_exists='replace', index=False)

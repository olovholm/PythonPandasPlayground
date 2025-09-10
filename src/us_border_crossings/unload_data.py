import os
import pandas as pd

def unload_data():

    """
    Unload data from the database tables to CSV files.
    """

    from common import DatabaseConnector
    from common import DATA_PROCESSED

    db = DatabaseConnector()
    engine = db.get_engine()

    # Unload dim_port table
    dim_port_df = pd.read_sql_table('dim_port', con=engine)
    dim_port_df.to_csv(os.path.join(DATA_PROCESSED, 'dim_port.csv'), index=False)

    # Unload dim_border_crossing_measure table
    dim_border_crossing_measure_df = pd.read_sql_table('dim_border_crossing_measure', con=engine)
    dim_border_crossing_measure_df.to_csv(os.path.join(DATA_PROCESSED, 'dim_border_crossing_measure.csv'), index=False)

    print("Data unloaded successfully to CSV files.")

import pandas as pd
from src.common.db_connection import DatabaseConnector
from sqlalchemy import text



db = DatabaseConnector()
engine = db.get_engine()

# Example: test connection
if db.test_connection():
    print("Connection successful")
else:
    print("Connection failed")

# Define date range
start_date = "2000-01-01"
end_date = "2030-12-31"
dates = pd.date_range(start=start_date, end=end_date, freq="D")

# Create DataFrame
date_dim = pd.DataFrame({"date": dates})
date_dim["year"] = date_dim["date"].dt.year
date_dim["month"] = date_dim["date"].dt.month
date_dim["day"] = date_dim["date"].dt.day
date_dim["quarter"] = date_dim["date"].dt.quarter
date_dim["week"] = date_dim["date"].dt.isocalendar().week
date_dim["day_of_week"] = date_dim["date"].dt.dayofweek
date_dim["day_name"] = date_dim["date"].dt.day_name()
date_dim["month_name"] = date_dim["date"].dt.month_name()

date_dim.to_sql('dim_dates', con=engine, if_exists='replace', index=False)

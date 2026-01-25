import pandas as pd
from sqlalchemy import create_engine

# 1. Setup Connection (matches your docker-compose)
engine = create_engine('postgresql://root:root@localhost:5432/ny_taxi')

# 2. Read the Parquet file you just downloaded
file_name = "green_tripdata_2025-11.parquet"
df = pd.read_parquet(file_name)

# 3. Fix datetimes (Parquet usually keeps these, but it's good practice)
df.lpep_pickup_datetime = pd.to_datetime(df.lpep_pickup_datetime)
df.lpep_dropoff_datetime = pd.to_datetime(df.lpep_dropoff_datetime)

# 4. Push to Postgres
# This creates a table called 'green_taxi_data'
df.to_sql(name='green_taxi_data', con=engine, if_exists='replace', index=False)

print(f"Finished! Loaded {len(df)} rows into Postgres.")
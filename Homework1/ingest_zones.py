import pandas as pd
from sqlalchemy import create_engine

# Connection string for your local Docker setup
engine = create_engine('postgresql://root:root@localhost:5432/ny_taxi')

# Load the CSV you downloaded with Invoke-WebRequest
df_zones = pd.read_csv('taxi_zone_lookup.csv')

# Write to the 'zones' table
df_zones.to_sql(name='zones', con=engine, if_exists='replace', index=False)

print("Zones table successfully created and loaded!")
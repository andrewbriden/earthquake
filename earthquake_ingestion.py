
import requests
import psycopg2
from datetime import datetime

# Database connection parameters
db_host = "YourActualDNS"
db_name = "YourActualDbName"
db_user = "YourActualDbUser"
db_password = "YourActualDbPassword"

# Connect to the PostgreSQL database
conn = psycopg2.connect(
    host=db_host,
    database=db_name,
    user=db_user,
    password=db_password
)
cur = conn.cursor()

# Create table if it doesn't exist
cur.execute("""
    CREATE TABLE IF NOT EXISTS earthquakes (
        id SERIAL PRIMARY KEY,
        time TIMESTAMP,
        latitude DOUBLE PRECISION,
        longitude DOUBLE PRECISION,
        depth DOUBLE PRECISION,
        mag DOUBLE PRECISION,
        place TEXT
    )
""")
conn.commit()

# Fetch earthquake data from the USGS API
response = requests.get("https://earthquake.usgs.gov/earthquakes/feed/v1.0/summ>
data = response.json()

# Insert data into the PostgreSQL database
for feature in data['features']:
    properties = feature['properties']
    geometry = feature['geometry']
    cur.execute("""
        INSERT INTO earthquakes (time, latitude, longitude, depth, mag, place)
        VALUES (%s, %s, %s, %s, %s, %s)
    """, (
        datetime.utcfromtimestamp(properties['time'] / 1000.0),
        geometry['coordinates'][1],
        geometry['coordinates'][0],
        geometry['coordinates'][2],
        properties['mag'],
        properties['place']
    ))
conn.commit()

# Close the database connection
cur.close()
conn.close()

print("Data ingestion complete.")


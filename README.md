# Earthquake Data Pipeline

## Introduction
The purpose of this project is to build an ETL pipeline that extracts earthquake data from the USGS Earthquake API and loads it into an AWS RDS instance running a PostgreSQL database. The data is then visualized using Tableau to provide insights into recent earthquake activities.

## Project Architecture
The project is divided into two stages:

1. Ingestion Stage: Retrieving data from the USGS Earthquake API into the PostgreSQL database.
2. Visualization Stage: Connecting Tableau to the PostgreSQL database and creating visualizations.

## Diagram
![Project Architecture Diagram](https://github.com/andrewbriden/earthquake/blob/main/diagram.png)

### Ingestion
The objective is to retrieve recent earthquake data from the USGS Earthquake API. The data includes information such as location, magnitude, depth, and time of occurrence. This script runs daily to ensure the database is updated with the latest data.

1. **Ingestion Script:**
   - `earthquake_data_ingestion.py`: A Python script that fetches data from the USGS Earthquake API and inserts it into the PostgreSQL database.
   
### ETL
The ingestion stage results in a dataset stored in the PostgreSQL database. This data can then be transformed and queried for analysis and visualization.

## Technologies
- **Python**: Used for writing the ingestion script.
- **AWS**: Provides the cloud infrastructure, including:
  - **EC2**: Hosts the ingestion script.
  - **RDS**: Hosts the PostgreSQL database.
- **PostgreSQL**: The RDBMS used to store earthquake data.
- **Tableau**: Used for data visualization.
- **USGS Earthquake API**: The source of earthquake data.

## Setup Instructions

### Set Up the Environment:

\`\`\`bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
\`\`\`

### Configure AWS and Database Credentials:
Update the \`config.py\` file with your AWS and PostgreSQL credentials.

### Run the Ingestion Script:

\`\`\`bash
python earthquake_data_ingestion.py
\`\`\`

### Set Up Scheduled Jobs:
Use \`cron\` or any scheduler to run the ingestion script daily.

### Tableau Visualization
Connect Tableau to the PostgreSQL database and use the data to create interactive visualizations. Example visualizations include:

- Map of recent earthquakes with color-coded magnitudes.
- Time-series plot of earthquake occurrences.
- Bar chart of earthquake frequencies by magnitude range.

## Future Directions
- **Data Enrichment**: Integrate additional data sources to provide more context (e.g., population density, building infrastructure) to the earthquake data.
- **Real-time Data Processing**: Implement a real-time data pipeline using AWS Lambda and Kinesis.
- **Advanced Analytics**: Apply machine learning models to predict earthquake occurrences and assess risks.
- **Enhanced Visualizations**: Create more detailed and interactive visualizations in Tableau or other BI tools.
- **Automated Reporting**: Set up automated reports and alerts based on earthquake data thresholds.



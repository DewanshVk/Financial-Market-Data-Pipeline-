# Real-Time Financial Market Data Pipeline

## Overview
Overview
This project builds a real-time financial market data pipeline to fetch, process, and analyze stock market data using Azure services and visualize it in Power BI.

This project is a real-time financial market data pipeline that fetches stock market data, processes it, and visualizes it in real-time. It uses Azure services for streaming and storage, Power BI for dashboards, and Apache Airflow to automate the workflow. I built it to explore stock market trends and sharpen my data engineering skills.

Key Features
* Live Data Streaming: Fetches stock market data using the Yahoo Finance API and streams it via Azure Event Hub.
* Real-Time Processing: Azure Stream Analytics processes incoming data for analysis.
* Cloud Storage & Querying: Processed data is stored in Azure Data Lake Storage (ADLS) and CosmosDB for structured querying.
* Insights & Visualization: Power BI provides real-time dashboards for financial market trends.
* Automation & Orchestration: Apache Airflow automates and schedules pipeline tasks.
* Containerized Deployment: The entire setup is Dockerized for easy deployment and scalability.

### Key Features
- **Live Data**: Pulls stock data from Yahoo Finance and streams it through Azure Event Hubs.
- **Real-Time Processing**: Azure Stream Analytics crunches the numbers (like 1-minute averages).
- **Storage**: Saves everything in Azure Cosmos DB for easy access.
- **Visualization**: Power BI shows live trends and insights.
- **Automation**: Apache Airflow keeps everything running on schedule.
- **Dockerized**: Wrapped it all in Docker for smooth deployment.

## Architecture

![Alt text](Architecture.png)


1. **Data Ingestion:** Stock data is fetched from Yahoo Finance using Python.
2. **Streaming:** Data is streamed using Azure Event Hub (Kafka not used in final implementation).
3. **Processing:** Azure Stream Analytics processes incoming data.
4. **Storage:** Processed data is stored in Azure Data Lake Storage (ADLS) and CosmosDB.
5. **Visualization:** Power BI is used for real-time insights.
6. **Orchestration:** Apache Airflow manages the data pipeline workflow.
7. **Containerization:** The entire setup is containerized using Docker.

## **Data Model**

### **Table: `stock_averages`**
This table stores the average stock prices along with the window end time.

| **Column Name**    | **Data Type**    | **Description**                     |
|---------------------|-----------------|-------------------------------------|
| `id`                | INT (PK)        | Unique ID (Primary Key)             |
| `ticker`            | VARCHAR(10)     | Stock symbol (e.g., GOOGL, AMZN)    |
| `avg_price`         | FLOAT           | Average price                       |
| `window_end`        | DATETIME        | Window end timestamp                |
| `created_at`        | TIMESTAMP       | Timestamp of data insertion         |

### **Sample Data**
| **id** | **ticker** | **avg_price**   | **window_end**           | **created_at**           |
|--------|-----------|-----------------|--------------------------|--------------------------|
| 1      | GOOGL     | 171.91          | 2025-03-06 18:44:00       | 2025-03-06 18:45:00       |
| 2      | AMZN      | 200.24          | 2025-03-06 18:44:00       | 2025-03-06 18:45:00       |
| 3      | TSLA      | 260.37          | 2025-03-06 18:44:00       | 2025-03-06 18:45:00       |
| 4      | NVDA      | 118.66          | 2025-03-06 18:44:00       | 2025-03-06 18:45:00       |
| 5      | AMD       | 105.73          | 2025-03-06 18:44:00       | 2025-03-06 18:45:00       |

## Tech Stack
- Python
- Azure Event Hub
- Azure Stream Analytics
- Azure Data Lake Storage (ADLS)
- CosmosDB
- Power BI
- Apache Airflow
- Docker
- Git

## Setup Instructions
### Prerequisites
- Docker installed
- Azure account with Event Hub, Stream Analytics, ADLS, and CosmosDB configured

## Setup Instructions

### Prerequisites
- Docker installed
- Azure account with Event Hub, Stream Analytics, ADLS, and CosmosDB configured
- Python 3.8+ 

### Steps

1. Clone the repository:
   ```sh
   gh repo clone DewanshVk/Financial-Market-Data-Pipeline-
   cd Financial-Market-Data-Pipeline-
   ```
2. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
3. Start Event Hub setup (modify config as needed).
4. Deploy the Stream Analytics job in Azure.
5. Run the producer to fetch and stream stock data:
   ```sh
   python src/producer/producer.py
   ```
6. Run the consumer to receive and store data:
   ```sh
   python src/test_consumer/consumer.py
   ```
7. Use Power BI to connect to CosmosDB and visualize data.

## Screenshots
Visual representations of key components are located in the `screenshots/` directory:
- Azure Event Hubs
   
   ![Alt text](screenshots/eventhub.png)

- Azure Stream Analytics
   
   ![Alt text](screenshots/Azure_Stream_Analytics_job_topology.png )

- Azure Cosmos 

   ![Alt text](screenshots/Cosmos-Db-data-explorer.png)

- Power BI Dashboard
  ![Alt text](screenshots/PowerBI_Dashboard.png)

- Apache Airflow UI

 ![Alt text](screenshots/Airflow%20UI%20-%20DAGs%20List.png)

## Usage
- **Start the Pipeline**: Run the producer to stream stock data to Event Hubs.
- **Process Data**: Stream Analytics handles the real-time calculations.
- **Visualize**: Open Power BI to check out the dashboards.
- **Automate**: Use Airflow to schedule and monitor everything.

## Challenges and Learnings
One big hurdle was getting the Stream Analytics query right for 1-minute averages. It took some trial and error, but figuring out the `TumblingWindow` function was super satisfying! Here’s the query I ended up with:

```sql
SELECT
    ticker,
    AVG(price) as avg_price,
    System.Timestamp() as window_end
INTO
    CosmosDB
FROM
    EventHub
GROUP BY
    ticker,
    TumblingWindow(minute, 1)
```

Also, hooking up Power BI to Cosmos DB was a bit of a headache at first—connection strings are picky!—but I got it sorted eventually.

## Future Improvements
- **ML Predictions**: Add a machine learning model to forecast stock prices.
- **More Data**: Pull in extra sources like news or economic data for better insights.
- **Fancier Dashboards**: Upgrade the Power BI visuals with more metrics.


## Contribution
Feel free to fork the repo and submit a PR with improvements!

## License
MIT License

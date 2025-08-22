# Dockerized Stock Data Pipeline with Airflow

![Pipeline](https://img.shields.io/badge/pipeline-airflow-blue)
![Docker Compose](https://img.shields.io/badge/docker--compose-enabled-blue?logo=docker)
![Python](https://img.shields.io/badge/python-3.8%2B-blue)

---

## Overview

This project implements a **Dockerized data pipeline** that automatically fetches, parses, and stores daily stock market data from the Alpha Vantage API into a PostgreSQL database. The pipeline is fully orchestrated using **Apache Airflow** running within Docker containers and follows best practices for robustness, security, and scalability.

---

## Features

- **Automated Data Fetching**  
  Retrieves JSON stock data from the Alpha Vantage API on a scheduled daily basis.

- **Data Processing & Storage**  
  Extracts relevant fields and updates/inserts the data into a persistent PostgreSQL database table.

- **Error Handling**  
  Incorporates comprehensive try-except blocks and conditional checks to gracefully manage API rate limits, missing data, and database exceptions.

- **Security**  
  Manages sensitive information such as API keys and database credentials through environment variables, keeping secrets out of source code.

- **Scalability & Resilience**  
  Designed leveraging container orchestration and Airflow scheduling with retries to handle increased frequency or data volume.

---

## Project Structure

```
├── dags/ 
│ ├── stock_data_pipeline.py # Core Airflow DAG
│ └── fetch_data.py # Fetch and save stock data script
├── init-db/ 
│ └── 01-create-stock-table.sql
├── logs/ 
├── plugins/
├── .env # Environment variables (API keys, DB creds)
└── docker-compose.yml # Docker Compose configuration for all services
```

---

## Prerequisites

- Docker installed (supporting Docker Compose)
- Alpha Vantage API Key (free to obtain at [https://www.alphavantage.co/support/#api-key](https://www.alphavantage.co/support/#api-key))
- Basic understanding of Airflow, Docker, and PostgreSQL

---

## Setup Instructions

1. **Clone this repository**
```
git clone <repository_url>
cd <repository_folder>
```

2. **Configure Environment Variables**

Create a `.env` file in the root directory with the following contents:
```
ALPHAVANTAGE_API_KEY=YOUR_ALPHA_VANTAGE_KEY_HERE
POSTGRES_HOST=postgres
POSTGRES_USER=postgres
POSTGRES_PASSWORD=YOUR_DB_PASSWORD
POSTGRES_DB=postgres
POSTGRES_PORT=5432
AIRFLOW_PORT=8080
```
Replace `YOUR_ALPHA_VANTAGE_KEY_HERE` and `YOUR_DB_PASSWORD` with your real credentials.


3. **Database Initialization**

The PostgreSQL service initializes the `stock_data` table on container startup using the SQL script at `init-db/01-create-stock-table.sql`.

4. **Start Services**

Run the following command to start Postgres, Airflow scheduler, and webserver containers:
```
docker-compose up airflow-init
```
This will initialize the Airflow metadata database and create the admin user.

Then start all services in detached mode:
```
docker-compose up -d
```
5. **Access the Airflow UI**

Open your browser and navigate to:
```
http://localhost:8080
```

Login credentials (default from init step):
```
- Username: `admin`
- Password: `admin`
```

6. **Enable and Trigger the DAG**

- Locate the DAG named `stock_pipeline`.
- Turn it ON (toggle switch).
- Trigger it manually or wait for the scheduled daily run.

---

## Usage

- The DAG automatically fetches daily stock data for configured stock symbols (default `"IBM"`).
- It stores or updates stock prices in the `stock_data` table in PostgreSQL.
- Logs for each task can be viewed in the Airflow UI for debugging.
- Modify DAG or `.env` to add custom symbols or change schedule frequency.

---

## Error Handling & Monitoring

- API connection and rate limit errors are handled gracefully with retries.
- Database connection issues cause task retries as configured.
- Logs capture detailed exceptions for root cause analysis.
- Airflow’s built-in retry and alerting mechanisms improve resilience.

---

## Scalability & Extensibility

- Easily extend DAG to multiple symbols with TaskGroups or dynamic task creation.
- Supports adding new data sources or processing steps in Airflow.
- Containerization ensures easy deployment and scalability on any Docker-supported platform.

---

## Technologies Used
```
- Python 3.8+
- Apache Airflow 2.8.1
- PostgreSQL 13
- Docker & Docker Compose
- Alpha Vantage API
- Psycopg2 (PostgreSQL driver)
- Requests (HTTP client)
```
---

## Contact & Support

For issues or questions, please open an issue on the GitHub repository or contact the author.

---

*This project fulfills the requirements for a Dockerized data pipeline assignment, combining best practices in orchestration, containerization, and data engineering.*  
*Last updated: August 2025*

*All API secrets and DB credentials have been set to empty in the uploaded .env file to ensure no data breach occurs*

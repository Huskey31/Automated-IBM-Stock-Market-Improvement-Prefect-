Yahoo Finance ETL Project
Project Overview

This project automates the extraction, transformation, and loading (ETL) of stock market data from Yahoo Finance using Python, Prefect, and PostgreSQL. It focuses on providing clean, structured data that can be further analyzed and visualized, for example in Power BI dashboards.

The ETL pipeline handles:

Automated extraction of historical stock data

Data cleaning and transformation

Loading data into a PostgreSQL database

Features

Data Extraction: Fetches stock data (e.g., IBM) from Yahoo Finance.

Data Transformation: Cleans the data, removes duplicates, and formats dates.

Data Loading: Loads the transformed data into a PostgreSQL database.

Retry Logic: Tasks and flows retry automatically on failure.

Power BI Integration: Connects to the PostgreSQL database to create dashboards for visualization.

Technologies Used

Python Libraries: yfinance, pandas, sqlalchemy, prefect, logging

Database: PostgreSQL

Workflow Orchestration: Prefect

Data Visualization: Power BI

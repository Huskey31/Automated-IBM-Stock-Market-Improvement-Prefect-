import yfinance as yf
import pandas as pd
import logging
import sqlalchemy
from prefect import task,flow
from prefect.blocks.system import Secret

logging.basicConfig(
    filename= r"C:\Users\khany\OneDrive\Desktop\Stuff\Richfield studies\DE_projects\PipeLines\Yahoo_Finance\yfinance.log",
    level = logging.INFO,
    format = '%(asctime)s-%(levelname)s-%(message)s',
    filemode = 'a'
)
    
@task(retries = 4, retry_delay_seconds = 10)
def extract():
    #Starting the yfinance data extraction process
    logging.info("Stating the yfinance data extraction process")
    df = yf.download("IBM", start="2024-11-01", end = None)
    logging.info("Data extraction completed successfully")
    return df
    
@task(retries = 4, retry_delay_seconds = 10)
def transform(df):
    #Starting the data transformation process
    logging.info("Starting the data transformation process")
    df.reset_index(inplace=True)
    df["Date"] = pd.to_datetime(df["Date"]).dt.date
    df.columns = (["Date","Close","High","Low","Open","Volume"])
    df.drop_duplicates(subset=["Date"], inplace=True)
    return df

@task(retries = 4, retry_delay_seconds = 10)
def load(df):
    #Starting the data loading process
    my_secret_block = Secret.load("yfinance-password")
    my_password = my_secret_block.get()
    logging.info("Starting the data loading process")
    engine = sqlalchemy.create_engine(
        f"postgresql+psycopg2://postgres:{my_password}@Localhost:5432/ETL_Database"
        ) 
    df.to_sql("yfinance", engine, if_exists="replace",index=False)
    logging.info("Data loading completed successfully")
    return df
    
@flow(retries = 4, retry_delay_seconds = 10)
def y_finance_flow():
        data = extract()
        df = transform(data)
        load(df)
if __name__=="__main__":
    y_finance_flow()






   

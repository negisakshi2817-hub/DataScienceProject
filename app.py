from src.DataScienceproject.logger import logging
from src.DataScienceproject.exception import CustomException
from src.DataScienceproject.data_ingestion import DataIngestion
from src.DataScienceproject.data_ingestion import DataIngestionConfig
import sys
if __name__ == "__main__":
    logging.info("Logging has started")

try:
    #data_ingestionConfig = data_ingestionConfig()
    Data_Ingestion = DataIngestion()
    Data_Ingestion.initiate_data_ingestion()
except Exception as e:
    logging.info("Divide by zero error")
    raise CustomException(e, sys.exc_info())
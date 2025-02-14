from house_project.Pipeline.Stages_of_pipeline import DataIngestionPipeline,DataValidationPipeline
from house_project import logging

try:
    logging.info(">>>>>>>Data Ingestion>>>>>>>")
    data_ingestion = DataIngestionPipeline()
    data_ingestion.Main()
    logging.info(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
except Exception as e:
    #logging.exception(e)
    raise e 


try:
    logging.info(">>>>>>>Data Validation>>>>>>>")
    data_validaion = DataValidationPipeline()
    data_validaion.Main()
    logging.info(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
except Exception as e:
    #logging.exception(e)
    raise e 
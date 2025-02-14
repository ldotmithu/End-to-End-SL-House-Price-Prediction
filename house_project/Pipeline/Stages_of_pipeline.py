from house_project.components.data_ingestion import DataIngestion


class DataIngestionPipeline:
    def __init__(self):
        pass
    
    def Main(self):
        data_ingestion = DataIngestion()
        data_ingestion.Download_ZipFile()
        data_ingestion.Unzip_operation()
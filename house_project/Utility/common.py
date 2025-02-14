from house_project import logging
from pathlib import Path
import os 

def Create_Dir(file_path):
    try:
        os.makedirs(file_path,exist_ok=True)
        logging.info(f"{file_path} Created Succesfully")
    except:
        logging.info("Invalid Dir Path")    
        
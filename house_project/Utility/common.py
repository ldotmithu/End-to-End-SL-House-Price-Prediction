from house_project import logging
from pathlib import Path
import os 
import yaml
from yaml import safe_load

def Create_Dir(file_path):
    try:
        os.makedirs(file_path,exist_ok=True)
        logging.info(f"{file_path} Created Succesfully")
    except:
        logging.info("Invalid Dir Path")    
        
def Read_Yaml(file_path):
    try:
        with open(file_path,'r') as f:
            file = yaml.safe_load(f)
            logging.info(f"Read the {file_path} Yaml file")
            return file
    except yaml.YAMLError as e:
        logging.error("YAML file is empty")
        raise e 
        
        
from house_project.Config.config_entity import ModelTrainerConfig
from house_project import logging
from sklearn.ensemble import RandomForestRegressor
from house_project.Utility.common import Create_Dir,Read_Yaml
import numpy as np 
import joblib
import os

class ModelTrainer:
    def __init__(self):
        self.model_trainer = ModelTrainerConfig()
        self.params = Read_Yaml(self.model_trainer.params_path)
        
        Create_Dir(self.model_trainer.root_dir)
    
    def Model_building(self):
            train_data = np.load(self.model_trainer.train_path)
            
            train_data_input_features = train_data[:,:-1]
            train_data_target_feature = train_data[:,-1]
            
            
            rf=RandomForestRegressor()
            rf.fit(train_data_input_features,train_data_target_feature)
            print(rf.score(train_data_input_features,train_data_target_feature))
            
            joblib.dump(rf,os.path.join(self.model_trainer.root_dir,self.model_trainer.model_name))
            logging.info("save the model.pkl")
            

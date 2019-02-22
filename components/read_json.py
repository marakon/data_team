import os, json, logging
import pandas as pd

logger = logging.getLogger(__name__)

class JsonOperations:
    def categorize_json(self, folder_name):
        self.data = folder_name
        logging.getLogger(__name__).info(f"Dividing data between raw_fse and raw_dd.")
        json_fse = [folder_name + json for json in os.listdir(self.data)
                    if json.endswith('.json') and json.startswith('fse_data')]
        json_dd = [folder_name + json for json in os.listdir(self.data)
                    if json.endswith('.json') and json.startswith('domain_data')]
        return json_fse, json_dd


    def read_json(self, file):
        logging.getLogger(__name__).info(f"Feating data from raw {file}.")
        data = pd.read_json(file, lines=True, orient='columns')
        return data
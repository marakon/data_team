import os, json
import pandas as pd

class JsonOperations:
    def categorize_json(self, folder_name):
        self.data = folder_name
        print("Dividing data between fse_data and domain_data...\n")
        json_fse = [folder_name + json for json in os.listdir(self.data) if json.endswith('.json') and json.startswith('fse_data')]
        json_dd = [folder_name + json for json in os.listdir(self.data) if json.endswith('.json') and json.startswith('domain_data')]
        return json_fse, json_dd

    def read_json(self, file):
        print(f"Reading file: {file}...")
        data = pd.read_json(file, lines=True, orient='columns')
        return data
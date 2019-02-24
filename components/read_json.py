#!/usr/bin/env python
import os, json, logging
import pandas as pd

__author__ = "Mateusz Osinski"

log = logging.getLogger(__name__)

class JsonOperations:
    def categorize_json(self, folder_name):
        log.info(f"Dividing data between raw_fse and raw_dd.")
        json_fse = [folder_name + json for json in os.listdir(folder_name)
                    if json.endswith('.json') and json.startswith('fse_data')]

        json_dd = [folder_name + json for json in os.listdir(folder_name)
                    if json.endswith('.json') and json.startswith('domain_data')]
        return json_fse, json_dd


    def read_json(self, file):
        log.info(f"Feating data from raw {file}.")
        data = pd.read_json(file, lines=True, orient='columns')
        return data
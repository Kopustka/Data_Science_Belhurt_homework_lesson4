"""DATA_LOADER (csv, json)"""

# Import the libraries
import pandas as pd

def json_loader(path):
    data = pd.read_json(path)
    return data

def csv_loader(path):
    data = pd.read_csv(path)
    return data









import os, pickle
DATA_DIR = 'data'
OUTPUT_DIR = 'outputs'
LXMX_FILENAME = 'lxmx_data_for_code.xls' #note that I modified the .xls file to fix some inconsistencies. 
SPECIES_COL = 4

def load_pickle(filename):
    with open(filename, 'rb') as f:
        return pickle.load(f)
    
def save_pickle(a, filename):
    with open(filename, 'wb') as f:
        pickle.dump(a, f)
        
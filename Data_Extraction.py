import pandas as pd
import os

class DataExtraction:

    def extract_data(source, output_path):
        """This function extracts data from db and writes the same in csv file"""
        print("Started writing Data in csv.,")
        file_nm = 'Data_extract.csv'
        file_path = os.path.join(output_path, file_nm)
        source.to_csv(file_path)
        print("Completed writing Data in csv.,")

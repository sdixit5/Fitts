
import pandas as pd
from sqlalchemy import create_engine
import os

def find_and_delete_file(search_path, target_file):
    # Walk through the search_path and its subdirectories
    for root, dirs, files in os.walk(search_path):
        if target_file in files:
            file_path = os.path.join(root, target_file)
            try:
                # Attempt to delete the file
                os.remove(file_path)
                print(f"File '{target_file}' found and deleted at: {file_path}")
            except Exception as e:
                print(f"Error deleting file '{target_file}': {str(e)}")

start_directory = "C:/Users/dixit/Downloads/"  # Replace with the directory you want to start the search from
target_file_to_delete = "Fitts_Application.xlsx" 


excel = pd.read_excel('C:/Users/dixit/Downloads/Fitts_Application.xlsx')



engine = create_engine('mysql+mysqlconnector://sql3645243:BZdTWgiheG@sql3.freesqldatabase.com:3306/sql3645243')
table_name = 'Login_data'
excel.to_sql(table_name, con=engine, if_exists='replace', index=False)
engine.dispose()

find_and_delete_file(start_directory, target_file_to_delete)

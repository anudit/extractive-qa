import os
import pandas as pd
import concurrent.futures
from tqdm import tqdm

# specify the path to the directory containing the Excel files
excel_directory = '../census/census_data_new'

# specify the path to the directory where you want to save the CSV files
csv_directory = '../census/census_csvs'

# define a function to convert a single Excel file to CSV
def convert_excel_to_csv(filename):
    if filename.endswith('.xls') or filename.endswith('.xlsx'):
        # read the Excel file into a pandas dataframe
        filepath = os.path.join(excel_directory, filename)
        df = pd.read_excel(filepath)
        
        # write the dataframe to a CSV file in the CSV directory
        csv_filename = os.path.splitext(filename)[0] + '.csv'
        csv_filepath = os.path.join(csv_directory, csv_filename)
        df.to_csv(csv_filepath, index=False)

# create a list of filenames in the Excel directory
filenames = os.listdir(excel_directory)

# create a thread pool with the number of workers equal to the number of CPU cores
with concurrent.futures.ThreadPoolExecutor(max_workers=os.cpu_count()) as executor:
    # submit each filename to the thread pool for processing and use tqdm to show a progress bar
    futures = [executor.submit(convert_excel_to_csv, filename) for filename in tqdm(filenames)]

    # wait for all the futures to complete and use tqdm to show a progress bar
    for future, filename in tqdm(zip(concurrent.futures.as_completed(futures), filenames), total=len(futures)):
        try:
            # get the result of the future (if any)
            result = future.result()
        except Exception as exc:
            # handle any exceptions that occurred during processing
            print(f'{filename} generated an exception: {exc}')
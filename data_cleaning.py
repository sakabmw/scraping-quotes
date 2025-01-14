import pandas as pd
import re

def data_cleaner(csv_input, csv_output):
    # Load the raw data
    df = pd.read_csv(csv_input)

    # Clean the values in column `quote`
    print("=== Remove special characters in column `quote`. ===")
    df['quote'] = df['quote'].apply(lambda x: re.sub(r'[“”.,]', '', x))

    # Save the cleaned data into a new CSV
    print("=== Cleaning done. Now storing the cleaned data in a new CSV file. ===")
    df.to_csv(csv_output, index=False)
    print("=== The new CSV file has been created, named as {filename} ===".format(filename=csv_output))
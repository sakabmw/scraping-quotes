import pandas as pd
import re

def data_cleaner(csv_input, csv_output):
    # Load the raw data
    df = pd.read_csv(csv_input)

    # Clean the values in column `quote`
    df['quote'] = [re.sub(r'[“”.,]', '', quote) for quote in df['quote']]
    # df['quote'] = df['quote'].apply(lambda x: re.sub(r'[“”.,]', '', x))

    # Save the cleaned data into a new CSV
    df.to_csv(csv_output, index=False)
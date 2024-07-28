import pandas as pd

# Step 1: Read the CSV file into a DataFrame
df = pd.read_csv('/home/sivadam/SahaYaatri/stations_mapping.csv')

# Step 2: Remove duplicate rows
df_cleaned = df.drop_duplicates()

# Step 3: Save the cleaned DataFrame to a new CSV file
df_cleaned.to_csv('cleaned_file.csv', index=False)

import pandas as pd

# Load the dataset
df = pd.read_csv('employee_raw_dataset.csv')

# Convert 'joining_date' to datetime format and back to string in a consistent format
df['joining_date'] = pd.to_datetime(df['joining_date'], format='mixed', errors='coerce')
df['joining_date'] = df['joining_date'].dt.strftime('%Y-%m-%d')

# Ensure all required columns are present
required_columns = ['employee_id', 'name', 'salary', 'department', 'job_role', 'joining_date']
for col in required_columns:
    if col not in df.columns:
        df[col] = ''

# Reorder columns to match desired output
df = df[required_columns]

# Display the cleaned DataFrame
print(df.head(10))

# Save the cleaned DataFrame to a new CSV file
df.to_csv('cleaned_employee_dataset.csv', index=False)
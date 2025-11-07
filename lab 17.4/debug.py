import sys
import traceback
try:
    import pandas as pd
    print("Pandas imported successfully")
    
    print("Attempting to read CSV...")
    df = pd.read_csv('employee_raw_dataset.csv')
    print("CSV read successfully")
    print("DataFrame head:")
    print(df.head())
    
    print("\nProcessing dates...")
    df['joining_date'] = pd.to_datetime(df['joining_date'], format='mixed', errors='coerce')
    df['joining_date'] = df['joining_date'].dt.strftime('%Y-%m-%d')
    print("Dates processed successfully")
    
    required_columns = ['employee_id', 'name', 'salary', 'department', 'job_role', 'joining_date']
    for col in required_columns:
        if col not in df.columns:
            df[col] = ''
    print("\nColumns verified")
    
    df = df[required_columns]
    print("\nColumns reordered")
    
    print("\nFinal DataFrame head:")
    print(df.head())
    
    df.to_csv('cleaned_employee_dataset.csv', index=False)
    print("\nFile saved successfully")
    
except Exception as e:
    print("An error occurred:", str(e), file=sys.stderr)
    print("\nFull traceback:", file=sys.stderr)
    traceback.print_exc()
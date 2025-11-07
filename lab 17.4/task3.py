import io
import pandas as pd

# task3.py
# GitHub Copilot
# Script to create example healthcare dataset, clean it, and write cleaned CSV.


def main():
    csv_data = """patient_id,name,age,gender,height_cm,weight_kg,blood_pressure,heart_rate,diagnosis
P001,John Doe,45,M,175,80,120,72,Hypertension
P002,Jane Smith,38,Female,160,65,NaN,80,Healthy
P003,Robert Brown,50,male,170,90,140,,Diabetes
P004,Emily Davis,29,F,165,55,110,75,Healthy
P005,Michael Johnson,60,Male,180,95,150,88,Hypertension
P006,Linda Wilson,NaN,f,158,62,115,70,Healthy
P007,David Lee,52,M,172,,135,85,Heart Disease
P008,Sarah Kim,33,Female,NaN,58,118,78,Healthy
P009,James White,47,m,169,85,,82,Diabetes
P010,Olivia Green,41,F,162,60,125,NaN,Healthy
"""

    # Read dataset (treat literal "NaN" and empty strings as missing)
    df = pd.read_csv(io.StringIO(csv_data), na_values=['NaN', ''], keep_default_na=True)

    # Ensure numeric columns are numeric
    for col in ['age', 'height_cm', 'weight_kg', 'blood_pressure', 'heart_rate']:
        df[col] = pd.to_numeric(df[col], errors='coerce')

    # Standardize gender labels
    gender_map = {
        'M': 'Male', 'm': 'Male', 'male': 'Male', 'Male': 'Male',
        'F': 'Female', 'f': 'Female', 'female': 'Female', 'Female': 'Female'
    }
    df['gender'] = df['gender'].astype(str).str.strip().replace(gender_map)
    # Convert string "nan" back to actual NaN
    df.loc[df['gender'].isin(['nan', 'None']), 'gender'] = pd.NA

    # Convert height from cm to meters (new column), then drop the original cm column
    df['height_m'] = df['height_cm'] / 100.0

    # Fill missing numeric values with column mean (applies to age, height_m, weight_kg, blood_pressure, heart_rate)
    numeric_cols = ['age', 'height_m', 'weight_kg', 'blood_pressure', 'heart_rate']
    for col in numeric_cols:
        mean_val = df[col].mean(skipna=True)
        df[col] = df[col].fillna(mean_val)

    # Drop irrelevant columns after cleaning
    df = df.drop(columns=['patient_id', 'height_cm'])

    # Reorder columns nicely
    cols = ['name', 'age', 'gender', 'height_m', 'weight_kg', 'blood_pressure', 'heart_rate', 'diagnosis']
    df = df[cols]

    # Write cleaned dataset to CSV
    output_filename = 'healthcare_patient_record.csv'
    df.to_csv(output_filename, index=False)
    print(f"\nCleaned dataset written to: {output_filename}")
    
    # Display the cleaned dataset
    print("\nCleaned Dataset:")
    print(df.to_string(index=False))

if __name__ == '__main__':
    main()
import sys
from pathlib import Path
import pandas as pd

# task2.py
"""
Preprocess sales transaction data:
- Load sales_transaction_raw.csv
- Convert transaction date to datetime
- Create 'Month-Year' column (e.g. Jan-2020)
- Remove rows with transaction_amount <= 0
- Normalize transaction_amount with Min-Max scaling to [0,1]
- Save preprocessed output to sales_transaction_preprocessed.csv
"""


INPUT_CSV = Path("sales_transaction_raw.csv")
OUTPUT_CSV = Path("sales_transaction_preprocessed.csv")


def load_csv(path: Path) -> pd.DataFrame:
    if not path.exists():
        print(f"Error: {path!s} not found.", file=sys.stderr)
        sys.exit(2)
    return pd.read_csv(path)


def preprocess(df: pd.DataFrame) -> pd.DataFrame:
    # Ensure transaction_date exists and convert to datetime (coerce invalids to NaT)
    if "transaction_date" not in df.columns:
        raise KeyError("Expected column 'transaction_date' in input CSV.")
    df["transaction_date"] = pd.to_datetime(df["transaction_date"], errors="coerce", infer_datetime_format=True)
    # Drop rows with invalid dates
    df = df.dropna(subset=["transaction_date"]).copy()

    # Create Month-Year column like 'Jan-2020'
    df["Month-Year"] = df["transaction_date"].dt.strftime("%b-%Y")

    # Ensure transaction_amount exists and is numeric
    if "transaction_amount" not in df.columns:
        raise KeyError("Expected column 'transaction_amount' in input CSV.")
    df["transaction_amount"] = pd.to_numeric(df["transaction_amount"], errors="coerce")

    # Drop rows with NaN transaction_amount
    df = df.dropna(subset=["transaction_amount"])

    # Remove rows with transaction_amount <= 0
    df = df[df["transaction_amount"] > 0].copy()

    # Min-Max normalize transaction_amount to [0,1]
    min_val = df["transaction_amount"].min()
    max_val = df["transaction_amount"].max()
    if max_val == min_val:
        # All values identical -> set normalized to 0.0
        df["transaction_amount_normalized"] = 0.0
    else:
        df["transaction_amount_normalized"] = (df["transaction_amount"] - min_val) / (max_val - min_val)

    # Optional: reorder columns to show normalized amount next to original
    cols = list(df.columns)
    # ensure normalized column right after original if both present
    if "transaction_amount" in cols and "transaction_amount_normalized" in cols:
        cols.remove("transaction_amount_normalized")
        idx = cols.index("transaction_amount") + 1
        cols.insert(idx, "transaction_amount_normalized")
        df = df[cols]

    return df


def main():
    # Load and display the original data first
    df = load_csv(INPUT_CSV)
    print("Original Data:")
    print(df.to_string(index=False))
    
    # Process the data
    processed = preprocess(df)
    
    # Save to output file
    processed.to_csv(OUTPUT_CSV, index=False)
    
    print("\nProcessed Data:")
    print(processed.to_string(index=False))


if __name__ == "__main__":
    main()
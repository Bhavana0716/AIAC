import csv
import re

def analyze_csv_file(file_path):
    """
    Analyzes a CSV file and returns:
    - Total number of rows
    - Number of empty rows  
    - Total number of words across the file
    """
    total_rows = 0
    empty_rows = 0
    total_words = 0
    
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            reader = csv.reader(f)
            for row in reader:
                total_rows += 1
                # Check if row is empty (all cells are empty or whitespace)
                if not row or all(cell.strip() == "" for cell in row):
                    empty_rows += 1
                    continue
                # Count words in each cell
                for cell in row:
                    words = re.findall(r'\w+', cell)
                    total_words += len(words)
                    
        return total_rows, empty_rows, total_words
        
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found")
        return None
    except Exception as e:
        print(f"Error reading file: {e}")
        return None

# Example usage
if __name__ == "__main__":
    file_path = input("Enter CSV file path: ")
    result = analyze_csv_file(file_path)
    
    if result:
        total_rows, empty_rows, total_words = result
        print(f"Total rows: {total_rows}")
        print(f"Empty rows: {empty_rows}")
        print(f"Total words: {total_words}")

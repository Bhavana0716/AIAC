import csv
import re

def analyze_csv(path):
    total_rows = 0
    empty_rows = 0
    total_words = 0
    try:
        with open(path, newline='', encoding='utf-8') as f:
            reader = csv.reader(f)
            for row in reader:
                total_rows += 1
                cells = [c.strip() for c in row]
                if not cells or all(c == "" for c in cells):
                    empty_rows += 1
                    continue
                for cell in cells:
                    total_words += len(re.findall(r"\w+", cell))
    except FileNotFoundError:
        return ("Error: file not found", 0, 0)
    except Exception as e:
        return (f"Error: {e}", 0, 0)
    return total_rows, empty_rows, total_words

if __name__ == "__main__":
    path = input("Enter CSV file path: ").strip()
    result = analyze_csv(path)
    if isinstance(result[0], str):
        print(result[0])
    else:
        total_rows, empty_rows, total_words = result
        print(f"Total rows: {total_rows}")
        print(f"Empty rows: {empty_rows}")
        print(f"Total words: {total_words}")
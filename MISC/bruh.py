import csv

csv_path = r"C:/Users/dej72/Desktop/smitetracker/cleaned.csv"
with open(csv_path, newline="", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    print(reader.fieldnames)  # <-- see exactly what the header row is
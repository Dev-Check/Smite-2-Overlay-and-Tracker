input_file = "smitestats.csv"
output_file = r"C:/Users/dej72/Desktop/smitetracker/cleaned.csv"

with open(input_file, "r", encoding="utf-8") as infile, open(output_file, "w", encoding="utf-8") as outfile:
    for line in infile:
        # Split by comma, take only first 10 columns, then join back
        columns = line.strip().split(",")[:10]
        outfile.write(",".join(columns) + "\n")

print("CSV cleaned! Saved as gods_clean.csv")
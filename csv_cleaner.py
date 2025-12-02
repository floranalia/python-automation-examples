import csv

def clean_csv(input_file, output_file):
    cleaned_rows = []

    with open(input_file, "r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            if row.get("email"):
                cleaned_rows.append(row)

    with open(output_file, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=reader.fieldnames)
        writer.writeheader()
        writer.writerows(cleaned_rows)

clean_csv("input.csv", "output_clean.csv")

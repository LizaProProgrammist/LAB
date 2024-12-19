import csv

def read_csv(file_path):
    with open(file_path, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        data = [row for row in reader]
    return data

def display_data(data):
    for row in data:
        print(" | ".join([f"{key} -> {value}" for key, value in row.items()]))

def get_min_max(data, column):
    try:
        values = [float(row[column]) for row in data if row[column]]
        return min(values), max(values)
    except ValueError:
        print(f"Column '{column}' contains non-numeric values.")
        return None, None

def calculate_sum(data, column):
    try:
        return sum(float(row[column]) for row in data if row[column])
    except ValueError:
        print(f"Column '{column}' contains non-numeric values.")
        return None

def calculate_average(data, column):
    try:
        values = [float(row[column]) for row in data if row[column]]
        return sum(values) / len(values) if values else None
    except ValueError:
        print(f"Column '{column}' contains non-numeric values.")
        return None

if name == "main":
    file_path = "your_file.csv"  
    data = read_csv(file_path)

    print("Data from CSV:")
    display_data(data)

    column = "YourColumnName"  
    min_val, max_val = get_min_max(data, column)
    if min_val is not None:
        print(f"Minimum value in column '{column}': {min_val}")
        print(f"Maximum value in column '{column}': {max_val}")

    total = calculate_sum(data, column)
    if total is not None:
        print(f"Sum of values in column '{column}': {total}")

    average = calculate_average(data, column)
    if average is not None:
        print(f"Average value in column '{column}': {average}")
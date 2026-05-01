import pandas as pd

print("Excel / CSV Data Cleaner")
print("------------------------")

file_name = input("Enter your file name (.csv or .xlsx): ")

try:
    if file_name.endswith(".csv"):
        df = pd.read_csv(file_name)
    elif file_name.endswith(".xlsx"):
        df = pd.read_excel(file_name)
    else:
        print("Error: Please use a CSV or Excel file.")
        exit()

    print("\nOriginal data shape:")
    print(f"Rows: {df.shape[0]}, Columns: {df.shape[1]}")

    df = df.dropna()
    df = df.drop_duplicates()

    if file_name.endswith(".csv"):
        output_file = "cleaned_" + file_name
        df.to_csv(output_file, index=False)
    else:
        output_file = "cleaned_" + file_name
        df.to_excel(output_file, index=False)

    print("\nCleaning completed successfully.")
    print(f"Cleaned file saved as: {output_file}")
    print(f"Rows after cleaning: {df.shape[0]}")

except Exception as e:
    print("Something went wrong:", e)
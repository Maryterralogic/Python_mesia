import pandas as pd

# Create a DataFrame with the specified column names
data = {
    "Emp ID": range(1, 11),
    "Aug 23": ["WFO", "WFH", "WFO", "WFO", "", "WFH", "", "WFH", "", "WFO"],
    "Aug 24": ["WFO", "", "WFO", "WFH", "WFO", "", "WFH", "WFO", "", "WFH"],
    "Aug 25": ["", "WFO", "WFH", "WFH", "", "WFO", "WFO", "", "WFH", "WFO"],
    "Aug 28": ["WFH", "WFO", "WFH", "WFH", "", "WFO", "WFH", "", "WFO", "WFH"],
    "Aug 29": ["WFH", "WFH", "WFO", "WFO", "WFH", "WFH", "WFH", "", "WFH", ""],
    "Aug 30": ["WFH", "WFH", "", "WFO", "WFO", "WFO", "", "WFO", "WFH", "WFH"]
}

# Create a DataFrame from the data
df = pd.DataFrame(data)

# Save the DataFrame to an Excel file
excel_file = 'attendance.xlsx'
df.to_excel(excel_file, index=False)

# Alternatively, you can save it as a CSV file:
# csv_file = 'attendance.csv'
# df.to_csv(csv_file, index=False)

print(f"Excel sheet saved as '{excel_file}'")

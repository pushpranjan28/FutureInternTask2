import pandas as pd

# Load the Titanic data
df = pd.read_csv(r"C:\Users\LENOVO\Downloads\train.csv")

# Display the first few rows to understand the dataset structure
print(df.head())

# Calculate mean, median, mode, and standard deviation for numerical columns
mean_values = df.mean(numeric_only=True)
median_values = df.median(numeric_only=True)
mode_values = df.mode(numeric_only=True).iloc[0]  # .iloc[0] to get the first mode
std_dev_values = df.std(numeric_only=True)

# Displaying the calculated statistics
print("\nMean values:\n", mean_values)
print("\nMedian values:\n", median_values)
print("\nMode values:\n", mode_values)
print("\nStandard Deviation values:\n", std_dev_values)

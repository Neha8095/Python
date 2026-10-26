import pandas as pd

# Create a Series
s = pd.Series([10, 20, 30, 40, 50])

# Display Series
print("Series:")
print(s)

# Save Series to a CSV file
s.to_csv("series.csv", index=False)

# Read data from CSV file
data = pd.read_csv("series.csv", header=None)

print("\nData read from file:")
print(data)


# using dataframe

import pandas as pd

# Create a DataFrame
data = {
    "Name": ["Amit", "Neha", "Rahul"],
    "Marks": [85, 90, 78]
}

df = pd.DataFrame(data)

# Display DataFrame
print("Student Data:")
print(df)

# Save DataFrame to CSV file
df.to_csv("student.csv", index=False)

# Read data from CSV file
df2 = pd.read_csv("student.csv")

print("\nData read from file:")
print(df2)
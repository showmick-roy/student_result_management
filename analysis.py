import pandas as pd
from main import (
    fill_missing_english,
    calculate_total,
    calculate_average,
    assign_grades,
    assign_result,
    assign_rank
)


# 1. Load Data

df = pd.read_csv(
    "G:\\first_data_cleaning_project\\student_project\\students.csv",
    encoding="latin1"
)



# Check initial info
print("Before Cleaning:\n")
print(df.info())
print("\nMissing values:\n", df.isnull().sum())


# 2. Data Cleaning

df = fill_missing_english(df)


# 3. Academic Calculations

df = calculate_total(df)
df = calculate_average(df)


# 4. Grades and Results

df = assign_grades(df)
df = assign_result(df)


# 5. Ranking

df = assign_rank(df)


# 6. Final Output

print("\nFinal Student Results:\n")
print(df)

# Save final results
df.to_csv("final_result.csv", index=False)
print("\nSaved final results to 'final_result.csv'")

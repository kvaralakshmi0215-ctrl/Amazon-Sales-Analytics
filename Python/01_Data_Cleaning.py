# ==========================================================
# AMAZON SALES ANALYTICS PROJECT
# FILE NAME : 01_Data_Cleaning.py
# ==========================================================

import pandas as pd


print("="*60)
print(" AMAZON SALES ANALYTICS - DATA CLEANING ")
print("="*60)

# ----------------------------------------------------------
# LOAD DATASET
# ----------------------------------------------------------

# Change the path to your CSV file
file_path = r"C:\Users\kanav\OneDrive\ドキュメント\Amazon-Sales-Analytics-Dashboard\Dataset\Amazon_Sales_data.csv"

# Try UTF-8 first, then Latin-1 if needed
try:
    df = pd.read_csv(r"C:\Users\kanav\OneDrive\ドキュメント\Amazon-Sales-Analytics-Dashboard\Dataset\Amazon_Sales_data.csv")
except UnicodeDecodeError:
    df = pd.read_csv(r"C:\Users\kanav\OneDrive\ドキュメント\Amazon-Sales-Analytics-Dashboard\Dataset\Amazon_Sales_data.csv", encoding="latin1")

print("\nDataset Loaded Successfully!")

# ----------------------------------------------------------
# FIRST 5 ROWS
# ----------------------------------------------------------

print("\nFIRST 5 ROWS")
print(df.head())

# ----------------------------------------------------------
# LAST 5 ROWS
# ----------------------------------------------------------

print("\nLAST 5 ROWS")
print(df.tail())

# ----------------------------------------------------------
# SHAPE
# ----------------------------------------------------------

print("\nDATASET SHAPE")
print(df.shape)

# ----------------------------------------------------------
# COLUMNS
# ----------------------------------------------------------

print("\nCOLUMN NAMES")
print(df.columns.tolist())

# ----------------------------------------------------------
# DATA TYPES
# ----------------------------------------------------------

print("\nDATA TYPES")
print(df.dtypes)

# ----------------------------------------------------------
# DATASET INFO
# ----------------------------------------------------------

print("\nDATASET INFO")
df.info()

# ----------------------------------------------------------
# MISSING VALUES
# ----------------------------------------------------------

print("\nMISSING VALUES")
print(df.isnull().sum())

print("\nTOTAL MISSING VALUES")
print(df.isnull().sum().sum())

# ----------------------------------------------------------
# DUPLICATES
# ----------------------------------------------------------

print("\nDUPLICATE ROWS")
print(df.duplicated().sum())

df = df.drop_duplicates()

print("\nDUPLICATES AFTER REMOVAL")
print(df.duplicated().sum())

# ----------------------------------------------------------
# DATE CONVERSION
# ----------------------------------------------------------

# Convert Date Columns
# Automatically detect mixed date formats
df["Order Date"] = pd.to_datetime(df["Order Date"], format="mixed", errors="coerce")
df["Ship Date"] = pd.to_datetime(df["Ship Date"], format="mixed", errors="coerce")

# ----------------------------------------------------------
# NEW COLUMNS
# ----------------------------------------------------------

df["Year"] = df["Order Date"].dt.year
df["Month"] = df["Order Date"].dt.month_name()
df["Month Number"] = df["Order Date"].dt.month
df["Quarter"] = df["Order Date"].dt.quarter

# ----------------------------------------------------------
# NUMERICAL STATISTICS
# ----------------------------------------------------------

print("\nNUMERICAL STATISTICS")
print(df.describe())

# ----------------------------------------------------------
# CATEGORICAL STATISTICS
# ----------------------------------------------------------

print("\nCATEGORICAL STATISTICS")
print(df.describe(include="object"))

# ----------------------------------------------------------
# UNIQUE VALUES
# ----------------------------------------------------------

print("\nUNIQUE VALUES")
print(df.nunique())

# ----------------------------------------------------------
# CATEGORY VALUES
# ----------------------------------------------------------

print("\nCATEGORY")
print(df["Category"].unique())

print("\nSUB CATEGORY")
print(df["Sub-Category"].unique())

print("\nSEGMENT")
print(df["Segment"].unique())

print("\nSHIP MODE")
print(df["Ship Mode"].unique())

print("\nREGION")
print(df["Region"].unique())

print("\nSTATE")
print(df["State"].unique())

# ----------------------------------------------------------
# FINAL SHAPE
# ----------------------------------------------------------

print("\nFINAL DATASET SHAPE")
print(df.shape)

# ----------------------------------------------------------
# SAVE CLEANED DATASET
# ----------------------------------------------------------

output_csv = r"C:\Users\kanav\OneDrive\ドキュメント\Amazon-Sales-Analytics-Dashboard\Dataset\Amazon_Sales_Cleaned.csv"

output_excel = r"C:\Users\kanav\OneDrive\ドキュメント\Amazon-Sales-Analytics-Dashboard\Dataset\Amazon_Sales_Cleaned.xlsx"

df.to_csv(output_csv, index=False)
df.to_excel(output_excel, index=False)

print("\nFILES CREATED")
print(output_csv)
print(output_excel)

print("\nDATA CLEANING COMPLETED SUCCESSFULLY!")
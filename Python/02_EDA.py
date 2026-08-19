# ==========================================================
# AMAZON SALES ANALYTICS PROJECT
# FILE NAME : 02_EDA.py
# ==========================================================

import pandas as pd

print("="*60)
print(" AMAZON SALES ANALYTICS - EXPLORATORY DATA ANALYSIS ")
print("="*60)

# ----------------------------------------------------------
# LOAD CLEANED DATASET
# ----------------------------------------------------------

file_path = r"C:\Users\kanav\OneDrive\ドキュメント\Amazon-Sales-Analytics-Dashboard\Dataset\Amazon_Sales_Cleaned.csv"

df = pd.read_csv(file_path)

print("\nDataset Loaded Successfully!")

# ----------------------------------------------------------
# DATASET OVERVIEW
# ----------------------------------------------------------

print("\nShape of Dataset")
print(df.shape)

print("\nColumns")
print(df.columns.tolist())

# ----------------------------------------------------------
# TOTAL SALES
# ----------------------------------------------------------

print("\nTOTAL SALES")
print(round(df["Sales"].sum(),2))

# ----------------------------------------------------------
# TOTAL PROFIT
# ----------------------------------------------------------

print("\nTOTAL PROFIT")
print(round(df["Profit"].sum(),2))

# ----------------------------------------------------------
# TOTAL ORDERS
# ----------------------------------------------------------

print("\nTOTAL ORDERS")
print(df["Order ID"].nunique())

# ----------------------------------------------------------
# TOTAL CUSTOMERS
# ----------------------------------------------------------

print("\nTOTAL CUSTOMERS")
print(df["Customer ID"].nunique())

# ----------------------------------------------------------
# TOTAL PRODUCTS
# ----------------------------------------------------------

print("\nTOTAL PRODUCTS")
print(df["Product ID"].nunique())

# ----------------------------------------------------------
# SALES BY CATEGORY
# ----------------------------------------------------------

print("\nSALES BY CATEGORY")
print(df.groupby("Category")["Sales"].sum().sort_values(ascending=False))

# ----------------------------------------------------------
# PROFIT BY CATEGORY
# ----------------------------------------------------------

print("\nPROFIT BY CATEGORY")
print(df.groupby("Category")["Profit"].sum().sort_values(ascending=False))

# ----------------------------------------------------------
# SALES BY SUB-CATEGORY
# ----------------------------------------------------------

print("\nTOP 10 SUB-CATEGORIES")
print(df.groupby("Sub-Category")["Sales"].sum().sort_values(ascending=False).head(10))

# ----------------------------------------------------------
# SALES BY REGION
# ----------------------------------------------------------

print("\nSALES BY REGION")
print(df.groupby("Region")["Sales"].sum().sort_values(ascending=False))

# ----------------------------------------------------------
# PROFIT BY REGION
# ----------------------------------------------------------

print("\nPROFIT BY REGION")
print(df.groupby("Region")["Profit"].sum().sort_values(ascending=False))

# ----------------------------------------------------------
# SALES BY SEGMENT
# ----------------------------------------------------------

print("\nSALES BY SEGMENT")
print(df.groupby("Segment")["Sales"].sum().sort_values(ascending=False))

# ----------------------------------------------------------
# PROFIT BY SEGMENT
# ----------------------------------------------------------

print("\nPROFIT BY SEGMENT")
print(df.groupby("Segment")["Profit"].sum().sort_values(ascending=False))

# ----------------------------------------------------------
# SALES BY SHIP MODE
# ----------------------------------------------------------

print("\nSALES BY SHIP MODE")
print(df.groupby("Ship Mode")["Sales"].sum().sort_values(ascending=False))

# ----------------------------------------------------------
# TOP 10 STATES
# ----------------------------------------------------------

print("\nTOP 10 STATES")
print(df.groupby("State")["Sales"].sum().sort_values(ascending=False).head(10))

# ----------------------------------------------------------
# TOP 10 CITIES
# ----------------------------------------------------------

print("\nTOP 10 CITIES")
print(df.groupby("City")["Sales"].sum().sort_values(ascending=False).head(10))

# ----------------------------------------------------------
# TOP 10 CUSTOMERS
# ----------------------------------------------------------

print("\nTOP 10 CUSTOMERS")
print(df.groupby("Customer Name")["Sales"].sum().sort_values(ascending=False).head(10))

# ----------------------------------------------------------
# TOP 10 PRODUCTS
# ----------------------------------------------------------

print("\nTOP 10 PRODUCTS")
print(df.groupby("Product Name")["Sales"].sum().sort_values(ascending=False).head(10))

# ----------------------------------------------------------
# MOST PROFITABLE PRODUCTS
# ----------------------------------------------------------

print("\nTOP 10 PROFITABLE PRODUCTS")
print(df.groupby("Product Name")["Profit"].sum().sort_values(ascending=False).head(10))

# ----------------------------------------------------------
# LEAST PROFITABLE PRODUCTS
# ----------------------------------------------------------

print("\nTOP 10 LOSS MAKING PRODUCTS")
print(df.groupby("Product Name")["Profit"].sum().sort_values().head(10))

# ----------------------------------------------------------
# AVERAGE DISCOUNT
# ----------------------------------------------------------

print("\nAVERAGE DISCOUNT")
print(round(df["Discount"].mean(),2))

# ----------------------------------------------------------
# AVERAGE SALES
# ----------------------------------------------------------

print("\nAVERAGE SALES")
print(round(df["Sales"].mean(),2))

# ----------------------------------------------------------
# AVERAGE PROFIT
# ----------------------------------------------------------

print("\nAVERAGE PROFIT")
print(round(df["Profit"].mean(),2))

# ----------------------------------------------------------
# HIGHEST SALE
# ----------------------------------------------------------

print("\nHIGHEST SALE")
print(df["Sales"].max())

# ----------------------------------------------------------
# HIGHEST PROFIT
# ----------------------------------------------------------

print("\nHIGHEST PROFIT")
print(df["Profit"].max())

# ----------------------------------------------------------
# LOWEST PROFIT
# ----------------------------------------------------------

print("\nLOWEST PROFIT")
print(df["Profit"].min())

# ----------------------------------------------------------
# MONTHLY SALES
# ----------------------------------------------------------

monthly_sales = df.groupby("Month")["Sales"].sum()

print("\nMONTHLY SALES")
print(monthly_sales)

# ----------------------------------------------------------
# YEARLY SALES
# ----------------------------------------------------------

yearly_sales = df.groupby("Year")["Sales"].sum()

print("\nYEARLY SALES")
print(yearly_sales)

# ----------------------------------------------------------
# BUSINESS INSIGHTS
# ----------------------------------------------------------

print("\nBUSINESS INSIGHTS")
print("-----------------------------------------")

print("Highest Sales Category :",
      df.groupby("Category")["Sales"].sum().idxmax())

print("Highest Profit Region :",
      df.groupby("Region")["Profit"].sum().idxmax())

print("Best Customer :",
      df.groupby("Customer Name")["Sales"].sum().idxmax())

print("Best Product :",
      df.groupby("Product Name")["Sales"].sum().idxmax())

print("Most Used Ship Mode :",
      df["Ship Mode"].mode()[0])

print("-----------------------------------------")

print("\nEDA COMPLETED SUCCESSFULLY!")
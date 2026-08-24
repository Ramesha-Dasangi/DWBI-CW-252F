import pandas as pd
import numpy as np
from ydata_profiling import ProfileReport

# ============================================================
# FILE CONFIGURATION
# ============================================================

file_name = "2020_al_data_kaggle_upload_new_old_syllabi.csv"

print("=" * 60)
print("1. LOADING AND CLEANING DATASET")
print("=" * 60)

# ============================================================
# LOAD DATASET
# Treat "-", blank values, spaces, and "Absent" as missing
# ============================================================

df = pd.read_csv(
    file_name,
    na_values=["-", "", " ", "Absent"]
)

# ============================================================
# CONVERT Z-SCORE TO NUMERIC
# ============================================================

if "Zscore" in df.columns:
    df["Zscore"] = pd.to_numeric(
        df["Zscore"],
        errors="coerce"
    )

# ============================================================
# EXTRACT NUMERIC VALUES FROM RANK COLUMNS
# Example:
# "4336 (NEW)" -> 4336
# ============================================================

for rank_col in ["district_rank", "island_rank"]:

    if rank_col in df.columns:

        df[f"{rank_col}_num"] = (
            df[rank_col]
            .astype(str)
            .str.extract(r"(\d+)")
            .astype(float)
        )

# ============================================================
# BASIC DATASET INFORMATION
# ============================================================

print(f"Total Records (Rows): {df.shape[0]:,}")
print(f"Total Columns:        {df.shape[1]}")
print(f"Duplicate Rows:       {df.duplicated().sum():,}")

# ============================================================
# COLUMN HEALTH & MISSING VALUES
# ============================================================

print("\n" + "=" * 60)
print("2. COLUMN HEALTH & MISSING VALUES")
print("=" * 60)

overview = pd.DataFrame({
    "Data Type": df.dtypes.astype(str),
    "Missing Count": df.isnull().sum(),
    "Missing (%)": (df.isnull().mean() * 100).round(2),
    "Unique Values": df.nunique()
})

print(overview.to_string())

# ============================================================
# NUMERIC SUMMARY STATISTICS
# ============================================================

print("\n" + "=" * 60)
print("3. NUMERIC SUMMARY STATISTICS")
print("=" * 60)

numeric_summary = df.describe().T

print(numeric_summary.to_string())

# ============================================================
# CATEGORICAL DISTRIBUTIONS
# TOP 5 VALUES PER COLUMN
# ============================================================

print("\n" + "=" * 60)
print("4. CATEGORICAL DISTRIBUTIONS (TOP 5 VALUES PER COLUMN)")
print("=" * 60)

categorical_cols = df.select_dtypes(
    include=["object", "category"]
).columns

for col in categorical_cols:

    print(f"\n--- Distribution: {col} ---")

    val_counts = (
        df[col]
        .value_counts(dropna=False)
        .head(5)
    )

    percentages = (
        df[col]
        .value_counts(
            normalize=True,
            dropna=False
        )
        .mul(100)
        .round(2)
        .head(5)
    )

    dist_df = pd.DataFrame({
        "Count": val_counts,
        "Percentage (%)": percentages
    })

    print(dist_df.to_string())

# ============================================================
# EXPORT SUMMARY TABLES
# ============================================================

overview.to_csv(
    "profile_column_health.csv",
    index=True
)

numeric_summary.to_csv(
    "profile_numeric_summary.csv",
    index=True
)

print("\n[Done] Summary tables exported:")
print(" - profile_column_health.csv")
print(" - profile_numeric_summary.csv")

# ============================================================
# 5. GENERATE AUTOMATED YDATA PROFILING REPORT
# ============================================================

print("\n" + "=" * 60)
print("5. GENERATING AUTOMATED HTML PROFILING REPORT")
print("=" * 60)

profile = ProfileReport(
    df,
    title="2020 A/L Dataset Profiling Report",
    explorative=True,
    minimal=False
)

# ============================================================
# EXPORT HTML REPORT
# ============================================================

output_file = "dataset_profiling_report.html"

profile.to_file(output_file)

# ============================================================
# FINAL MESSAGE
# ============================================================

print("\n" + "=" * 60)
print("DATA PROFILING COMPLETED SUCCESSFULLY")
print("=" * 60)

print(f"HTML Report : {output_file}")
print("Column Health: profile_column_health.csv")
print("Numeric Summary: profile_numeric_summary.csv")

print("\nOpen 'dataset_profiling_report.html' in your browser.")
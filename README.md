# 2020 A/L Dataset Profiling

This project focuses on profiling and analyzing the **2020 G.C.E. Advanced Level Examination Dataset** using Python. The project evaluates the dataset structure, data quality, missing values, duplicates, numerical statistics, and categorical distributions.

## Student Information

- **Student Index:** GAHDSE252F-024

## Technologies Used

- Python 3.13
- Pandas
- NumPy
- YData Profiling

## Key Features

- Dataset loading and preprocessing
- Missing value analysis
- Duplicate record detection
- Data type and unique value analysis
- Numerical statistical analysis
- Categorical data distribution
- Rank data extraction and conversion
- Automated HTML profiling report
- Export of profiling summary files

## Project Progress

### 1. ETL - Extraction
- Dataset `2020_al_data_kaggle_upload_new_old_syllabi.csv` successfully loaded into a pandas DataFrame (`df_extracted`).

### 2. ETL - Transformation
- Rows with null values in the crucial **Zscore** column removed.
- **Zscore** column converted from object type to numeric (`float64`) for accurate mathematical operations.

### 3. Initial Data Analysis
- Column overview completed.
- Average **Zscore** calculated and visualized by academic **stream** using a bar plot.
- Descriptive statistics generated for **Zscore** (count, mean, standard deviation, min, max, quartiles).

## Project Files

- `profile_data.py` – Main Python profiling script
- `profile_column_health.csv` – Column health and missing-value summary
- `profile_numeric_summary.csv` – Numerical statistical summary
- `dataset_profiling_report.html` – Interactive profiling report
- `requirements.txt` – Required Python packages
- `.gitignore` – Files excluded from GitHub

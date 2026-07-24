# Day 1 Data Quality Summary Report

## 1. Executive Overview
- **Total CSV Datasets Loaded**: 10
- **Status**: Ingestion and Data Quality Inspection Complete

## 2. Dataset Shapes, Null Counts & Duplicate Rows Summary

| Dataset Variable | File Name | Shape (Rows x Cols) | Duplicates | Null Counts per Column | Suspicious Data Types |
| --- | --- | --- | --- | --- | --- |
| `fund_master` | `01_fund_master.csv` | 7 x 7 | 0 | None | None |
| `nav_history` | `02_nav_history.csv` | 7 x 5 | 0 | None | None |
| `aum_by_fund_house` | `03_aum_by_fund_house.csv` | 6 x 4 | 0 | None | None |
| `monthly_sip` | `04_monthly_sip.csv` | 6 x 4 | 0 | None | None |
| `category_inflows` | `05_category_inflows.csv` | 5 x 4 | 0 | None | None |
| `folio_count` | `06_folio_count.csv` | 6 x 6 | 0 | None | None |
| `scheme_performance` | `07_scheme_performance.csv` | 6 x 7 | 0 | None | None |
| `transactions` | `08_transactions.csv` | 5 x 8 | 0 | None | None |
| `holdings` | `09_holdings.csv` | 5 x 5 | 0 | None | None |
| `benchmark` | `10_benchmark.csv` | 5 x 6 | 0 | None | None |

## 3. AMFI Scheme Code Validation
- **Scheme Codes in `fund_master` missing from `nav_history`**: `[140001]`
- **Scheme Codes in `nav_history` missing from `fund_master`**: `[199999]`

## 4. Key Observations & Next Steps
1. **Date Types**: All date fields are ingested as string/object dtypes and will be parsed into `datetime64` in the data cleaning phase.
2. **Integrity**: No duplicate rows or missing values were found across the datasets.
3. **Cross-Validation**: AMFI scheme code mismatches were cataloged for further alignment during data transformations.

---
*Report generated automatically by `data_ingestion.py`*
# Day 1 Data Quality & Ingestion Summary Report

## Overview
- **Total Datasets Ingested**: 10
- **Ingestion Status**: Completed successfully

## Dataset Summary & Metrics

| Dataset Variable Name | Rows | Columns | Duplicate Rows | Null Value Columns | Data Type Anomalies |
| --- | --- | --- | --- | --- | --- |
| `df_axis_bluechip_nav_raw` | 3602 | 2 | 0 | None | None |
| `df_hdfc_top_100_direct_nav_raw` | 3128 | 2 | 0 | None | None |
| `df_icici_bluechip_nav_raw` | 3344 | 2 | 0 | None | None |
| `df_kotak_bluechip_nav_raw` | 3338 | 2 | 0 | None | None |
| `df_nippon_large_cap_nav_raw` | 3335 | 2 | 0 | None | None |
| `df_sbi_bluechip_nav_raw` | 3273 | 2 | 0 | None | None |
| `df_fund_master` | 7 | 7 | 0 | None | None |
| `df_nav_history` | 7 | 5 | 0 | None | None |
| `df_scheme_categories` | 5 | 4 | 0 | None | None |
| `df_amc_details` | 6 | 4 | 0 | None | None |

## AMFI Scheme Code Validation
- **Scheme Codes in Fund Master missing from NAV History**: `[140001]`
- **Scheme Codes in NAV History missing from Fund Master**: `[199999]`

## Key Observations & Findings
1. **Live NAV Data**: Successfully retrieved historical daily NAV records for 6 primary benchmark schemes from `mfapi.in`.
2. **Data Types**: Date fields in raw CSVs are represented as strings (`object` type) and will require parsing to `datetime64` in subsequent preprocessing steps.
3. **Completeness**: No missing critical values or duplicate records detected in the primary raw datasets.

---
*Report generated automatically by data_ingestion.py*
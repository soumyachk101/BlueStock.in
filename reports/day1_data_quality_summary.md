# Day 1 Data Quality Summary Report

## Overview
Completed initial data ingestion and quality checks on all 10 raw CSV datasets.

## Dataset Summary

| Dataset | Rows | Columns | Duplicate Rows | Null Columns |
| --- | --- | --- | --- | --- |
| `fund_master` | 7 | 7 | 0 | 0 |
| `nav_history` | 7 | 5 | 0 | 0 |
| `aum_by_fund_house` | 6 | 4 | 0 | 0 |
| `monthly_sip` | 6 | 4 | 0 | 0 |
| `category_inflows` | 5 | 4 | 0 | 0 |
| `folio_count` | 6 | 6 | 0 | 0 |
| `scheme_performance` | 6 | 7 | 0 | 0 |
| `transactions` | 5 | 8 | 0 | 0 |
| `holdings` | 5 | 5 | 0 | 0 |
| `benchmark` | 5 | 6 | 0 | 0 |

## AMFI Code Validation Results
- Codes in fund_master missing in nav_history: `[140001]`
- Codes in nav_history missing in fund_master: `[199999]`

## Initial Findings
1. Data is clean with no missing values or duplicate records.
2. Date columns are imported as strings/objects and will be cast to datetime format in Day 2 preprocessing.

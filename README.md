# PnL Analysis for Client Company

This repository contains a Python script to perform a Profit and Loss (PnL) analysis for a client company. The script includes deep statistical analysis and visualization of the results.

## Inputs
1. A CSV file containing the following columns:
   - `Date`: The date of the transaction or period.
   - `Revenue`: The revenue generated.
   - `Cost`: The cost incurred.

2. The script assumes the CSV file is located at `data/financial_data.csv`.

## Outputs
1. A statistical summary of the PnL data, including mean, median, standard deviation, skewness, kurtosis, min, max, and total profit.
2. Visualizations of:
   - PnL trend over time.
   - PnL distribution.
   - Boxplot of PnL.
   - Cumulative PnL over time.

## How to Run
1. Clone the repository.
2. Install the required dependencies using `pip install -r requirements.txt`.
3. Place your financial data CSV file in the `data` folder and ensure it has the correct column names.
4. Run the script using `python pnl_analysis.py`.

## Dependencies
- pandas
- numpy
- matplotlib
- seaborn
- scipy

## Folder Structure
pnl-analysis/
│
├── data/
│   └── financial_data.csv
│
├── pnl_analysis.py
├── README.md
└── requirements.txt

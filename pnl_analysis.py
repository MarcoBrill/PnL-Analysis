import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats

# Inputs
# 1. Path to the CSV file containing revenue and cost data
# 2. Date column name
# 3. Revenue column name
# 4. Cost column name

# Outputs
# 1. PnL DataFrame with statistical analysis
# 2. Visualizations of PnL trends and distributions

def load_data(file_path, date_col, revenue_col, cost_col):
    """
    Load the dataset and calculate Profit and Loss (PnL).
    """
    data = pd.read_csv(file_path)
    data[date_col] = pd.to_datetime(data[date_col])  # Ensure date is in datetime format
    data['PnL'] = data[revenue_col] - data[cost_col]  # Calculate PnL
    return data

def perform_statistical_analysis(data, pnl_col):
    """
    Perform statistical analysis on the PnL data.
    """
    stats_summary = {
        'mean': np.mean(data[pnl_col]),
        'median': np.median(data[pnl_col]),
        'std_dev': np.std(data[pnl_col]),
        'skewness': stats.skew(data[pnl_col]),
        'kurtosis': stats.kurtosis(data[pnl_col]),
        'min': np.min(data[pnl_col]),
        'max': np.max(data[pnl_col]),
        'total_profit': np.sum(data[pnl_col])
    }
    return stats_summary

def plot_results(data, date_col, pnl_col):
    """
    Plot PnL trends and distributions.
    """
    plt.figure(figsize=(14, 8))

    # PnL Trend Over Time
    plt.subplot(2, 2, 1)
    sns.lineplot(x=data[date_col], y=data[pnl_col])
    plt.title('PnL Trend Over Time')
    plt.xlabel('Date')
    plt.ylabel('PnL')

    # PnL Distribution
    plt.subplot(2, 2, 2)
    sns.histplot(data[pnl_col], kde=True)
    plt.title('PnL Distribution')
    plt.xlabel('PnL')
    plt.ylabel('Frequency')

    # Boxplot of PnL
    plt.subplot(2, 2, 3)
    sns.boxplot(y=data[pnl_col])
    plt.title('PnL Boxplot')
    plt.ylabel('PnL')

    # Cumulative PnL
    plt.subplot(2, 2, 4)
    data['Cumulative_PnL'] = data[pnl_col].cumsum()
    sns.lineplot(x=data[date_col], y=data['Cumulative_PnL'])
    plt.title('Cumulative PnL Over Time')
    plt.xlabel('Date')
    plt.ylabel('Cumulative PnL')

    plt.tight_layout()
    plt.show()

def main():
    # Define inputs
    file_path = 'data/financial_data.csv'  # Path to your CSV file
    date_col = 'Date'  # Column name for date
    revenue_col = 'Revenue'  # Column name for revenue
    cost_col = 'Cost'  # Column name for cost

    # Load data and calculate PnL
    data = load_data(file_path, date_col, revenue_col, cost_col)

    # Perform statistical analysis
    stats_summary = perform_statistical_analysis(data, 'PnL')
    print("Statistical Summary of PnL:")
    for key, value in stats_summary.items():
        print(f"{key}: {value:.2f}")

    # Plot results
    plot_results(data, date_col, 'PnL')

if __name__ == "__main__":
    main()

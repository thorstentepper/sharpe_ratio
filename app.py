from functions import read_data, daily_returns, calculate_excess_returns, \
    average_excess_return, standard_deviation_excess_return, \
    daily_sharpe_ratio, annualise_sharpe_ratio, pick_best_stock

stock_data_path = "data/stock_data.csv"
benchmark_data_path = "data/benchmark_data.csv"
benchmark_column = "S&P 500"


def main():
    # Read data
    stock_data = read_data(stock_data_path)
    benchmark_data = read_data(benchmark_data_path)

    # Compute daily returns
    daily_stock_returns = daily_returns(stock_data)
    daily_benchmark_returns = daily_returns(benchmark_data[benchmark_column])

    # Compute excess returns
    excess_returns = calculate_excess_returns(daily_stock_returns,
                                              daily_benchmark_returns)

    # Compute average excess return
    avg_excess_return = average_excess_return(excess_returns)

    # Compute standard deviation of excess return
    sd_excess_return = standard_deviation_excess_return(excess_returns)

    # Compute daily Sharpe ratio
    daily_ratio = daily_sharpe_ratio(avg_excess_return, sd_excess_return)

    # Compute annualized Sharpe ratio
    annualised_ratio = annualise_sharpe_ratio(daily_ratio)

    # Choose the best stock
    best_stock = pick_best_stock(annualised_ratio)

    # Print the result
    print("Annualised Sharpe Ratio:\n", annualised_ratio)
    print("\nIn this dataset, {} has the best Sharpe Ratio at {}.".format(
        best_stock, annualised_ratio.loc[best_stock]))


if __name__ == "__main__":
    main()

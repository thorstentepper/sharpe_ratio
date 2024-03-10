import numpy as np
import pandas as pd


def read_data(file):
    """
    Read data from a CSV file and return a pandas DataFrame.

    Parameters
    ----------
    file : str
        The file path of the CSV file containing the data.

    Returns
    -------
    pandas.DataFrame
        A DataFrame containing the data read from the CSV file. The DataFrame
        has the 'Date' column parsed as datetime and set as the index.
    """

    data = pd.read_csv(
        file,
        parse_dates=["Date"],
        index_col="Date"
    ).dropna()

    return data


def daily_returns(data):
    """
    Calculate the daily returns of a given dataset.

    Parameters
    ----------
    data : pandas.DataFrame
        A pandas DataFrame containing the data for which daily returns are to
        be calculated. It is assumed that the DataFrame has a datetime index.

    Returns
    -------
    pandas.DataFrame
        A DataFrame containing the daily returns calculated based on the
        provided data. Each column represents the daily return series of the
        corresponding column in the input DataFrame.
    """

    daily_returns = data.pct_change()
    return daily_returns


def calculate_excess_returns(stock_returns, benchmark_returns):
    """
    Calculate excess returns by subtracting benchmark returns from
    stock returns.

    Parameters
    ----------
    stock_returns : pandas.DataFrame
        A pandas DataFrame containing the returns of the stock or
        portfolio.
        It is assumed that the DataFrame has a datetime index.

    benchmark_returns : pandas.DataFrame
        A pandas DataFrame containing the returns of the benchmark or
        market index.
        It is assumed that the DataFrame has a datetime index.

    Returns
    -------
    pandas.DataFrame
        A DataFrame containing the excess returns calculated by subtracting
        the benchmark returns from the stock returns. Each column represents
        the excess return series of the corresponding column in the
        input DataFrames.
    """

    excess_returns = stock_returns.sub(benchmark_returns, axis=0)
    return excess_returns


def average_excess_return(excess_returns):
    """
    Calculate the average excess return from a series of excess returns.

    Parameters
    ----------
    excess_returns : pandas.DataFrame
        A pandas DataFrame containing the excess returns. Each column
        represents the excess return series of the corresponding asset.

    Returns
    -------
    pandas.Series
        A pandas Series containing the average excess return for each
        asset represented in the input DataFrame.
    """

    avg_excess_return = excess_returns.mean()
    return avg_excess_return


def standard_deviation_excess_return(excess_returns):
    """
    Calculate the standard deviation of excess returns.

    Parameters
    ----------
    excess_returns : pandas.DataFrame
        A pandas DataFrame containing the excess returns. Each column
        represents the excess return series of the corresponding asset.

    Returns
    -------
    pandas.Series
        A pandas Series containing the standard deviation of
        excess returns for each asset represented in the input DataFrame.
    """

    sd_excess_return = excess_returns.std()
    return sd_excess_return


def daily_sharpe_ratio(avg_excess_return, sd_excess_return):
    """
    Calculate the daily Sharpe ratio.

    Parameters
    ----------
    avg_excess_return : pandas.Series
        A pandas Series containing the average excess return for
        each asset.

    sd_excess_return : pandas.Series
        A pandas Series containing the standard deviation of
        excess returns for each asset.

    Returns
    -------
    pandas.Series
        A pandas Series containing the daily Sharpe Ratio for each asset
        represented in the input Series.
    """

    daily_sharpe_ratio = avg_excess_return.div(sd_excess_return)
    return daily_sharpe_ratio


def annualise_sharpe_ratio(daily_sharpe_ratio):
    """
    Annualise the daily Sharpe Ratio.

    Parameters
    ----------
    daily_sharpe_ratio : pandas.Series
        A pandas Series containing the daily Sharpe ratio for each asset.

    Returns
    -------
    pandas.Series
        A pandas Series containing the annualised Sharpe Ratio for each asset
        represented in the input Series, rounded to two decimal places.
    """

    annual_factor = np.sqrt(252)
    annual_sharpe_ratio = daily_sharpe_ratio.mul(annual_factor)
    return annual_sharpe_ratio.round(2)


def pick_best_stock(annualised_ratios):
    """
    Pick the stock with the highest annualised Sharpe Ratio.

    Parameters
    ----------
    annualised_ratios : pandas.Series
        A pandas Series containing the annualised Sharpe Ratio for each asset.

    Returns
    -------
    str
        The name of the stock with the highest annualised Sharpe Ratio.
    """

    best_stock = annualised_ratios.idxmax()
    return best_stock

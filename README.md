# Project Title
Risk and Returns: The Sharpe Ratio


## Description
This project calculates the Sharpe Ratio, which is a measure of assessing the return of an investment against a benchmark. The underlying data consists of Amazon and Facebook stocks which are compared against the S&P 500 for the time period from 04.01.2016 to 30.12.2016. After initial exploratory data analysis, the inputs for the Sharpe formula are calculated via average excess returns to arrive at an annualised measure.


## Date created
The project was completed on 01.01.2022.


## Usage
Point app.py to the correct file paths for stock and benchmark data and execute the script. The files should have a "Date" column that can serve as the index. Also make sure that both data sets have the same number of rows.


## Files used
The project uses two csv-files available via DataCamp: 'stock_data.csv' and 'benchmark_data.csv'


## Credits
Stefan Jansen created the project tasks for DataCamp.

The Python code in sharpe_ratio.ipynb was accepted as my solution to the project. In order to improve reusability, the code has been refactored into functions that are used by app.py.

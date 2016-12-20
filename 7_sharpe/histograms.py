#!/usr/bin/env python
# Plot a histogram
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

from util import get_data, plot_data, compute_daily_returns

def test_run():
    # Read data and plot
    dates = pd.date_range('2009-01-01', '2012-12-31')
    symbols = ['SPY', 'XOM', 'GLD', 'GOOG']
    initialize = 'n' # toggles whether or not to initialize with SPY data (must be 'n' if SPY is in symbols)
    df = get_data(symbols, dates, initialize)
    plot_data(df)

    # Compute daily returns
    daily_returns = compute_daily_returns(df)
    plot_data(daily_returns, title='Daily Returns', xlabel='Date', ylabel='Daily Returns')

    # Plot a histogram
    daily_returns.hist(bins=20)

    # Get mean and stdev
    mean = daily_returns['SPY'].mean()
    print 'mean=', mean
    std = daily_returns['SPY'].std()
    print 'stdev=', std

    # Scatterplot SPY vs GOOG
    daily_returns.plot(kind='scatter', title='Correlation SPY vs GOOG', x='SPY', y='GOOG')
    # beta is the slope of the line in the scatterplot, and alpha is the intercept
    beta_GOOG, alpha_GOOG = np.polyfit(daily_returns['SPY'], daily_returns['GOOG'], 1) # this returns the alpha and beta for GOOG
    # below '-' indicates a line should be drawn
    plt.plot(daily_returns['SPY'], beta_GOOG*daily_returns['SPY'] + alpha_GOOG, '-', color='r') # plots a regression curve using y = mx + b
    print '\nGOOG beta = ', beta_GOOG
    print 'GOOG alpha = ', alpha_GOOG # higher alpha would mean the stock performed better than the SPY
    plt.show()

    # Scatterplot SPY vs XOM
    daily_returns.plot(kind='scatter', title='Correlation SPY vs XOM', x='SPY', y='XOM')
    # beta is the slope of the line in the scatterplot, and alpha is the intercept
    beta_XOM, alpha_XOM = np.polyfit(daily_returns['SPY'], daily_returns['XOM'], 1) # this returns the alpha and beta for XOM
    # below '-' indicates a line should be drawn
    plt.plot(daily_returns['SPY'], beta_GOOG*daily_returns['SPY'] + alpha_XOM, '-', color='r') # plots a regression curve using y = mx + b
    print '\nXOM beta = ', beta_XOM
    print 'XOM alpha = ', alpha_XOM # higher alpha would mean the stock performed better than the SPY
    plt.show()

    # Calculate Correlation Coefficient
    # this uses pearson correlation coeff method to estimate how closely the data points fit the regression line
    print '\nCorrelation Coefficients:\n', daily_returns.corr(method='pearson')

    # plot separate plots for each stock
    plt.axvline(mean, color='w', linestyle='dashed', linewidth=2) # adds vertical dashed line at the mean
    plt.axvline(std, color='r', linestyle='dashed', linewidth=2)
    plt.axvline(-std, color='r', linestyle='dashed', linewidth=2)
    plt.show()

    # plot overlayed plots
    daily_returns['SPY'].hist(bins=20, label='SPY')
    daily_returns['XOM'].hist(bins=20, label='XOM')
    daily_returns['GLD'].hist(bins=20, label='GLD')
    plt.legend(loc='upper right')
    plt.show()

    # Compute kurtosis
    # This is how closely a dataset fits a gaussian normal distribution +num has longer tails, -num shorter tails
    print '\nKurtosis:\n', daily_returns.kurtosis()

if __name__ == '__main__':
    test_run()

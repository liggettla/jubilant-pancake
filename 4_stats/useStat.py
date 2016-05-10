import pandas as pd
import matplotlib.pyplot as plt

def get_data(symbols, dates):

    df = pd.DataFrame(index=dates)

    # Read in more stocks
    for symbol in symbols:
        #df_temp=pd.read_csv('data/{}.csv'.format(symbol), index_col='Date',
        df_temp=pd.read_csv('data/' + symbol + '.csv'.format(symbol), index_col='Date',
                            parse_dates=True, usecols=['Date', 'Adj Close'],
                            na_values=['nan'])

        df_temp = df_temp.rename(columns={'Adj Close': symbol})

        # just calling this will cause a columns overlap error, because 'Adj Close' is the title in each data set
        # each set of data must have unique column names
        df = df.join(df_temp, how='left') # use default how ='left' to keep all indices already in dataframe
        df = df.dropna()

    return df

def global_stats(df):
# computes global stats on all data in range
    print 'Mean: '
    print df.mean()
    print '\nMedian: '
    print df.median()
    print '\nStdDev: '
    print df.std()

# Plot stock prices
def plot_data(df,title='Stock Prices'):
    # ax here is a plot object
    ax = df.plot(title=title, fontsize=2)
    ax.set_xlabel("Date")
    ax.set_ylabel("Price")
    plt.show()

def get_rolling_mean(values, window):
    # compute rolling mean using a specified window
    rm = pd.rolling_mean(values, window=window)
    return rm

def get_rolling_std(values, window):
    pass

def get_bollinger_bands(rm, rstd):
# computing and plotting bollinger bands which are 2 stddev above/below rolling avg
# the idea behind bollinger bands is to buy after price dips below mvavg and then comes back up above it
    return upper_band, lower_band

def test_run():
# computing global statistics
    start_date = '2010-01-01'
    end_date = '2013-12-31'
    dates = pd.date_range(start_date, end_date)
    symbols = ['SPY', 'XOM', 'GOOG', 'IBM', 'GLD']
    df = get_data(symbols, dates)
    # compute global stats
    global_stats(df)
    # plot out the data
    # plot_data(df)

    # plot SPY data, retain matplotlib axis object
    ax = df['SPY'].plot(title="SPY Rolling Mean", label='SPY')
    # get rolling mean
    rm = get_rolling_mean(df['SPY'], 50)
    # add rolling mean to the same plot
    rm.plot(label='Rolling mean', ax=ax)
    plt.show()














if __name__ == '__main__':
    test_run()

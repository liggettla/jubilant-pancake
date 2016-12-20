import pandas as pd
import matplotlib.pyplot as plt

def get_data(symbols, dates, initialize):

    # create empty dataframe with dates as indices
    df = pd.DataFrame(index=dates)

    # initialize gives the option of initializing the dataframe with SPY data
    if initialize == 'Y':
        # read in SPY data
        dfSPY = pd.read_csv('data/SPY.csv', index_col="Date",
                            parse_dates=True, usecols=['Date', 'Adj Close'],
                            na_values = ['nan']) # reads just Date and Adj Close and sets NaN to strings

        # using DataFrame.join() the data from SPY is joined to df1
        # it is important to note that all the rows from df1 will be kept
        # and only rows with matching date indices from SPY will be joined
        # if instead dfSPY.join(df1) were used, the vice versa would be true
        df = df.join(dfSPY)

        # dropping NaN values
        df = df.dropna()

        # renames the 'Adj Close' column to 'SPY' to prevent column name overlap problem
        df = df.rename(columns={'Adj Close':'SPY'})

    elif initialize == 'n':
        # Read in more stocks
        for symbol in symbols:
            df_temp=pd.read_csv('data/' + symbol + '.csv'.format(symbol), index_col='Date',
                                parse_dates=True, usecols=['Date', 'Adj Close'],
                                na_values=['nan'])

            df_temp = df_temp.rename(columns={'Adj Close': symbol})

            # just calling this will cause a columns overlap error, because 'Adj Close' is the title in each data set
            # each set of data must have unique column names
            df = df.join(df_temp, how='left') # use default how ='left' to keep all indices already in dataframe
            df = df.dropna()

        return df

# Plot stock prices
def plot_data(df, title='Stock Prices', xlabel='Date', ylabel='Price'):
    # ax here is a plot object
    ax = df.plot(title=title, fontsize=12)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    plt.show()

def compute_daily_returns(df):
# computes daily return values
# manually calculating:
    daily_returns = df.copy() # copy the dataFrame so that values can be altered
    daily_returns[1:] = (df[1:] / df[:-1].values) - 1 # compute for row 1 onwards
    daily_returns.ix[0, :] = 0 # set daily returns for row 0 to 0
    return daily_returns

# using pandas:
    daily_returns = (df /df.shift(1)) - 1 # easier when just using pandas
    daily_returns.ix[0, :] = 0 # by default pandas leaves the 0th row full of NaNs

def get_rolling_mean(values, window):
    # compute rolling mean using a specified window
    rm = pd.rolling_mean(values, window=window)
    return rm

def get_rolling_std(values, window):
    rstd = pd.rolling_std(values, window=window)
    return rstd

def get_bollinger_bands(rm, rstd):
# computing and plotting bollinger bands which are 2 stddev above/below rolling avg
# the idea behind bollinger bands is to buy after price dips below mvavg and then comes back up above it
    upper_band = rstd * 2 + rm
    lower_band = rm - rstd * 2
    return upper_band, lower_band

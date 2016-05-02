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

# Plot stock prices
def plot_data(df,title='Stock Prices'):
    # ax here is a plot object
    ax = df.plot(title=title, fontsize=2)
    ax.set_xlabel("Date")
    ax.set_ylabel("Price")
    plt.show()

def test_run():
# computing global statistics
    start_date = '2010-01-01'
    end_date = '2013-12-31'
    dates = pd.date_range(start_date, end_date)
    symbols = ['XOM', 'GOOG', 'IBM', 'GLD']
    df = get_data(symbols, dates)
    #plot_data(df)

    # these would be global stats on all data in range
    #print df.mean()
    df.median()
    df.std()

# computing and plotting bollinger bands which are 2 stddev above/below rolling avg
    symbols = ['SPY']
    df = get_data(symbols, dates)

    # plot SPY data, retain matplotlib axis object
    ax = df['SPY'].plot(title="SPY Rolling Mean", label='SPY')

    # compute rolling mean using a 20-day window
    rm_SPY = pd.rolling_mean(df['SPY'], window=20)

    # add rolling mean to the same plot
    rm_SPY.plot(label='Rolling mean', ax=ax)

    # add axis labels and legen
    ax.set_xlabel("Date")
    ax.set_ylabel("Price")
    ax.legend(loc='upper left')
    plt.show()



if __name__ == '__main__':
    test_run()

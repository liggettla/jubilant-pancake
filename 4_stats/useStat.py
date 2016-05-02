import pandas as pd
import matplotlib.pyplot as plt

def get_data(symbols, dates):

    df = pd.DataFrame(index=dates)

    # read SPY data into temp dataframe
    # using index_col uses the Date column as the index
    # parse_dates converts the Dates into index objects
    dfSPY = pd.read_csv('data/SPY.csv', index_col="Date",
                        parse_dates=True, usecols=['Date', 'Adj Close'],
                        na_values = ['nan']) # reads just Date and Adj Close and sets NaN to strings

    # renames the 'Adj Close' column to 'SPY' to prevent column name overlap problem
    dfSPY = dfSPY.rename(columns={'Adj Close':'SPY'})

    # joining with inner paramter joins only data that has intersecting indices between df1 and dfSPY
    # this then does the same thing as first joining and then dropping NaN values
    # could also use how='left' to include all dates then use df1.dropna() to remove NaN values
    df = df.join(dfSPY, how='inner')

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

    return df


# Plot stock prices
def plot_data(df,title='Stock Prices'):
    # ax here is a plot object
    ax = df.plot(title=title, fontsize=2)
    ax.set_xlabel("Date")
    ax.set_ylabel("Price")
    plt.show()

def test_run():
# Define a date range
    start_date = '2010-01-01'
    end_date = '2013-12-31'
    dates = pd.date_range(start_date, end_date)
    symbols = ['XOM', 'GOOG', 'IBM', 'GLD']
    df = get_data(symbols, dates)
    plot_data(df)






if __name__ == '__main__':
    test_run()

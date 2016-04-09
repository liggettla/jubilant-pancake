import pandas as pd

def test_run():
# Define a date range
    start_date = '2010-01-01'
    end_date = '2010-12-31'

    # print '\nCreating a list with dates as indices'
    dates = pd.date_range(start_date, end_date)

    # print '\nCreating a dataframe with dates as indices'
    # a list could be used as the indices here
    df1 = pd.DataFrame(index=dates)

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
    df1 = df1.join(dfSPY, how='inner')

    # Read in more stocks
    symbols = ['GOOG', 'IBM', 'GLD']
    for symbol in symbols:
        #df_temp=pd.read_csv('data/{}.csv'.format(symbol), index_col='Date',
        df_temp=pd.read_csv('data/' + symbol + '.csv'.format(symbol), index_col='Date',
                            parse_dates=True, usecols=['Date', 'Adj Close'],
                            na_values=['nan'])

        df_temp = df_temp.rename(columns={'Adj Close': symbol})

        # just calling this will cause a columns overlap error, because 'Adj Close' is the title in each data set
        # each set of data must have unique column names
        df1 = df1.join(df_temp, how='left') # use default how ='left' to keep all indices already in dataframe
    # slice by row range using date indices and the DataFrame.ix[] selector
    print df1.ix['2010-01-01':'2010-01-21']

if __name__ == '__main__':
    test_run()
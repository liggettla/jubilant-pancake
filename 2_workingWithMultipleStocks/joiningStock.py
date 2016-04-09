# this script builds a dataframe in pandas containing multiple stocks
# SPY is a good control because it should be open on all market open days
import pandas as pd

def test_run():
    start_date = '2010-01-22'
    end_date = '2010-01-26'

    #print '\nCreating a list with dates as indices'
    dates = pd.date_range(start_date, end_date)
    print dates
    #print dates[0]

    #print '\nCreating a dataframe with dates as indices'
    df1 = pd.DataFrame(index=dates)
    #print df1

    # read SPY data into temp dataframe
    # using index_col uses the Date column as the index
    # parse_dates converts the Dates into index objects
    dfSPY = pd.read_csv('data/SPY.csv', index_col="Date", parse_dates=True) # reads all data
    dfSPY = pd.read_csv('data/SPY.csv', index_col="Date",
                        parse_dates=True, usecols=['Date', 'Adj Close'],
                        na_values = ['nan']) # reads just Date and Adj Close and sets NaN to strings

    print '\nJoining two dataframes'
    # using DataFrame.join() the data from SPY is joined to df1
    # it is important to note that all the rows from df1 will be kept
    # and only rows with matching date indices from SPY will be joined
    # if instead dfSPY.join(df1) were used, the vice versa would be true
    df1 = df1.join(dfSPY)
    #print df1

    # dropping NaN values
    df1 = df1.dropna()
    #print df1

    # renames the 'Adj Close' column to 'SPY' to prevent column name overlap problem
    dfSPY = dfSPY.rename(columns={'Adj Close':'SPY'})

    # joining with inner paramter joins only data that has intersecting indices between df1 and dfSPY
    # this then does the same thing as first joining and then dropping NaN values
    df1 = df1.join(dfSPY, how='inner')

    # Read in more stocks
    symbols = ['GOOG', 'IBM', 'GLD']
    for symbol in symbols:
        df_temp=pd.read_csv('data/{}.csv'.format(symbol), index_col='Date',
                            parse_dates=True, usecols=['Date', 'Adj Close'],
                            na_values=['nan'])

        df_temp = df_temp.rename(columns={'Adj Close': symbol})

        # just calling this will cause a columns overlap error, because 'Adj Close' is the title in each data set
        # each set of data must have unique column names
        df1 = df1.join(df_temp) # use default how ='left' to keep all indices already in dataframe

        df1 = df1.dropna(subset=["SPY"]) # this drops only the nan values for the ref SPY data

    print df1

if __name__ == '__main__':
    test_run()

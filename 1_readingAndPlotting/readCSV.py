#this script reads in data from AAPL.csv into a pandas dataframe
import pandas as pd
import matplotlib.pyplot as plt

def test_run():
    df = pd.read_csv('data/AAPL.csv')
    print df.head(5)
    print df.tail(5)
    print df[10:21] #print data between indices 10 and 20
    print 'Max Close'
    print 'AAPL'
    print get_max_close('AAPL')
    print 'Mean Volume'
    print 'AAPL'
    print get_mean_volume('AAPL')

#plotting data
    df['Adj Close'].plot()
    plt.show()
    df['High'].plot()
    plt.show()
    df[['Close', 'Adj Close']].plot()
    plt.show()


def get_max_close(symbol):
#returns the max closing value for stock
    df = pd.read_csv('data/AAPL.csv'.format(symbol)) #read in the data
    return df['Close'].max() #compute max from Close column

def get_mean_volume(symbol):
    df = pd.read_csv('data/AAPL.csv'.format(symbol)) #read in the data
    return df['Volume'].mean() #compute mean from Volume column

if __name__ == '__main__':
    test_run()

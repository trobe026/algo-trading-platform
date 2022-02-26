import yfinance

df = yfinance.download('AAPL', start='2021-12-30', end='2022-02-02')
df.to_csv('AAPL.csv')
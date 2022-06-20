import pandas as pd

#webpage url
url =  'https://en.wikipedia.org/wiki/History_of_Python'
#Extract tables
dfs = pd.read_html(url)
#Get firts table
df = dfs[0]
#Extract columns
df2 = df[['Version','Release date']]

print(df2)
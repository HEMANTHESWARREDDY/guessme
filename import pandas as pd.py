import pandas as pd
pd.options.display.max_rows = 99992
a=pd.read_csv("pokemon.csv")
print(a)
print(pd.options.display.max_rows)
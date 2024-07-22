import csv
import pandas as pd
aliens = pd.read_csv("aliens.csv",).to_dict('records')

# for i in aliens:
#  print(i['Power'])
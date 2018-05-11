# reminder of main code for pandas user

import pandas as pd

# Load and check data
data = pd.read_csv('sample.csv', header = 0, delimiter = ",", encoding = 'utf-8')

for i in range(0, len(data[data.columns[0]])-1):
    for col in data.columns:
        print data[col][i]


# Output a new dataframe
new_col_1 = ['3', '4']
new_col_2 = ['c', 'd']

output = pd.DataFrame(data = {"number":new_col_1,
                              "letter":new_col_2})

output.to_csv('sample_2.csv', sep=",", encoding = 'utf-8')

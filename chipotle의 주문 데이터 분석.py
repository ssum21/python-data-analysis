import pandas as pd

file_path = '/config/workspace/python-data-analysis/data/chipotle.tsv'
chipo = pd.read_csv(file_path, sep = '\t')

print(chipo.shape)
print('--------------------------------')
print(chipo.info())
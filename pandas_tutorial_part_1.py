import pandas
import numpy

def print_data(data, text = ""):
  print(text)
  print(data)

print('# Series')
series = pandas.Series(numpy.arange(1, 6), ['I', 'II', 'III', 'IV', 'V'])

print(series['III'])
print(series[0])

print(series['II':'V'])
print(series[1:5])

series = pandas.Series((50, 7, 88, 9))
print(series)

series1 = pandas.Series(dict(a = 1, b = 2, c = 3))
series2 = pandas.Series(dict(a = 4, b = 5, c = 6, d = 7))

print(series1 + series2)
print(series1[1:] * series2[:-1])

data_frame = pandas.DataFrame(dict(a = [1, 2, 3],
                                   b = [4, 5, 6],
                                   c = pandas.Timestamp('20170902'),
                                   d = pandas.Categorical(['red', 'green', 'blue'])))
print(data_frame)

data_frame.index = ('I II III'.split())
print(data_frame)

data_frame_csv = pandas.read_csv('pandas_tutorial_part_1.csv')
print(data_frame_csv)

data_frame_json = data_frame.to_json()
print(data_frame_json)

print()
print('# Metadata and Stats')
print_data(data_frame.index, '## Index')

print_data(data_frame.columns, '## Columns')

print_data(data_frame.describe(), '## Describe')

print()
print('# Selecting Data')

print_data(data_frame.loc['II'], '## Single row')

print_data(data_frame[:2], '## Multiple rows using integer index (no \'loc\')')

print_data(data_frame['b'], '## Single column')

print_data(data_frame.loc[:, 'b':'c'], '## Multiple columns')

print_data(data_frame.loc[:'II', 'b':'c'], '## Rectangular section')

print_data(data_frame.iloc[:2, 1:3], '## Using integer index (when actual index is not integer)')

print_data(data_frame[data_frame.b % 2 == 0], '## Select only rows with even values in column b')

print()
print('# Sorting Data')
index = ['one', 'two', 'three', 'four', 'five']
data_frame = pandas.DataFrame(numpy.random.randn(5, 2),
                              index = index,
                              columns = ['a', 'b'])

print_data(data_frame.sort_index(ascending = False), '## Sort by index (alphabetically and descending)')

print_data(data_frame.sort_values(by = 'a'), '## Sort by column')

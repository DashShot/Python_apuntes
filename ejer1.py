#Histórico de las acciones de Facebook en formato csv (comma-separated values)

facebook_stocks = """Date,Open,High,Low,Close,Volume,Adj Close
2012-05-18,42.05,45.0,38.0,38.23,573576400,38.23
2012-05-21,36.53,36.66,33.0,34.03,168192700,34.03
2012-05-22,32.61,33.59,30.94,31.0,101786600,31.0
2012-05-23,31.37,32.5,31.36,32.0,73600000,32.0
2012-05-24,32.95,33.21,31.77,33.03,50237200,33.03
2012-05-25,32.9,32.95,31.11,31.91,37149800,31.91
2012-05-29,31.48,31.69,28.65,28.84,78063400,28.84
2012-05-30,28.7,29.55,27.86,28.19,57267900,28.19
2012-05-31,28.55,29.67,26.83,29.6,111639200,29.6
2012-06-01,28.89,29.15,27.39,27.72,41855500,27.72
2012-06-04,27.2,27.65,26.44,26.9,35230300,26.9
2012-06-05,26.7,27.76,25.75,25.87,42473400,25.87
"""

#Separa el texto cambaindo cada , por un salto de linea y separando en las comas
split_text = facebook_stocks.replace("\n", ",").split(",")
print(split_text)

close_values = split_text[11::7]
print(close_values)

query_name = "Close"
column_names = facebook_stocks.splitlines()[0].split(',')
close_index = column_names.index(query_name)

step = len(column_names)
begin = close_index + step

split_text = facebook_stocks.replace("\n", ",").split(',')
close_values = split_text[begin::step]

max_value = max(map(float, close_values))
print(max_value)




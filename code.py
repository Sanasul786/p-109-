import pandas as pd
import csv
import statistics
import plotly.figure_factory as ff
import plotly.graph_objects as go
df = pd.read_csv("StudentsPerformance.csv")
data = df["reading score"].tolist()
mean = sum(data)/len(data)
data_median = statistics.median(data)
data_mode = statistics.mode(data)
data_std_deviation = statistics.stdev(data)
first_std_deviation_start,first_std_deviation_end = mean - data_std_deviation , mean + data_std_deviation
second_std_deviation_start,second_std_deviation_end = mean - (2*data_std_deviation) , mean + (2*data_std_deviation)
third_std_deviation_start,third_std_deviation_end = mean - (3*data_std_deviation) , mean + (3*data_std_deviation)
fig = ff.create_distplot([data],["reading scores"],show_hist=False)
fig.add_trace(go.Scatter(x=[mean,mean],y=[0,0.17],mode="lines",name="MEAN"))
fig.add_trace(go.Scatter(x=[first_std_deviation_start,first_std_deviation_start],y=[0,0.17],mode="lines",name="STANDARD DEVIATION 1"))
fig.add_trace(go.Scatter(x=[first_std_deviation_end,first_std_deviation_end],y=[0,0.17],mode="lines",name="STANDARD DEVIATION 1"))
fig.add_trace(go.Scatter(x=[second_std_deviation_start,second_std_deviation_start],y=[0,0.17],mode="lines",name="STANDARD DEVIATION 2"))
fig.add_trace(go.Scatter(x=[second_std_deviation_end,second_std_deviation_end],y=[0,0.17],mode="lines",name="STANDARD DEVIATION 2"))
fig.show()
list_of_data_within_1_std_deviation = [result for result in data if result > first_std_deviation_start and result < first_std_deviation_end]
list_of_data_within_2_std_deviation = [result for result in data if result > second_std_deviation_start and result < second_std_deviation_end]
list_of_data_within_3_std_deviation = [result for result in data if result > third_std_deviation_start and result < third_std_deviation_end]
print("Mean of this data is {}".format(mean))
print("Median of this data is {}".format(data_median))
print("Mode of this data is {}".format(data_mode))

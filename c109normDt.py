#properties of normal distribution
import pandas as pd 
import plotly.figure_factory as pff
import statistics as stt
import plotly.graph_objects as pgo

df = pd.read_csv("StudentsMarks.csv")

HL = df["math score"].to_list()


H_mean = stt.mean(HL)
print("The Mean of math marks is =", str(H_mean))

H_median = stt.median(HL)
print ( "The median of the dada is = " , str(H_median))

H_mode = stt.mode(HL)
print("The Mode of the data is =" , str(H_mode))

H_standard_deviation = stt.stdev(HL)
print("The Standard deviation of the data is = " , str(H_standard_deviation))


first_std_dev_start = H_mean - H_standard_deviation
first_std_dev_end = H_mean + H_standard_deviation

second_std_dev_start = H_mean - (2*H_standard_deviation)
second_std_dev_end = H_mean + (2*H_standard_deviation)

Third_std_dev_start = H_mean - (3*H_standard_deviation)
Third_std_dev_end = H_mean + (3*H_standard_deviation)

list_of_data_within_1_std_deviation = [result for result in HL if result>first_std_dev_start and result <first_std_dev_end]
list_of_data_within_2_std_deviation = [result for result in HL if result>second_std_dev_start and result <second_std_dev_end]
print ("{}% of data that lies within 1 standard deviation ". format(len(list_of_data_within_1_std_deviation)*100/len(HL)))
print ("{}% of data that lies within 2 standard deviation". format(len(list_of_data_within_2_std_deviation)*100/len(HL)))
list_of_data_within_3_std_deviation = [result for result in HL if result>Third_std_dev_start and result <Third_std_dev_end]
print ("{}% of data that lies within 3 standard deviation". format(len(list_of_data_within_3_std_deviation)*100/len(HL)))

fig = pff.create_distplot([HL],["Bell Curve"], show_hist=False)
fig.add_trace(pgo.Scatter(x = [H_mean, H_mean], y=[0, 0.17], mode= "lines", name = "MEAN"))
fig.add_trace(pgo.Scatter(x=[first_std_dev_start, first_std_dev_start], y=[0, 0.17], mode="lines", name = "1st Std Dev"))
fig.add_trace(pgo.Scatter(x=[first_std_dev_end, first_std_dev_end], y=[0, 0.17], mode="lines", name = "1st Std Dev"))
fig.add_trace(pgo.Scatter(x=[second_std_dev_start, second_std_dev_start], y=[0, 0.17], mode="lines", name = "2nd Std Dev"))
fig.add_trace(pgo.Scatter(x=[second_std_dev_end, second_std_dev_end], y=[0, 0.17], mode="lines", name = "2nd Std Dev"))
fig.show()
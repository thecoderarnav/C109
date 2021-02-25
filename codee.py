import random
import statistics
import csv

import pandas as pd 
import plotly.figure_factory as ff


df = pd.read_csv("data.csv")
height_list = df ["Height(Inches)"].tolist()
weight_list = df ["Weight(Pounds)"].tolist()

height_mean = statistics.mean(height_list)
weight_mean = statistics.mean(weight_list)

height_median = statistics.median(height_list)
weight_median = statistics.median(weight_list)

height_mode = statistics.mode(height_list)
weight_mode = statistics.mode(weight_list)

height_sd = statistics.stdev(height_list)
weight_sd = statistics.stdev(weight_list)

print("Mean, Median, Mode  & Standard Deviation of Height is {}, {}, {},{} respectively".format(height_mean, height_median ,height_mode,height_sd ))
print("Mean, Median, Mode  & Standard Deviation of Weight is {}, {}, {},{} respectively".format(weight_mean, weight_median ,weight_mode,weight_sd ))

height_first_sd_start , height_first_sd_end = height_mean - height_sd, height_mean+height_sd

height_second_sd_start , height_second_sd_end = height_mean -(  2 * height_sd), height_mean+(2*height_sd)

height_third_sd_start , height_third_sd_end = height_mean -( 3*height_sd), height_mean+( 3*height_sd)

weight_first_sd_start , weight_first_sd_end = weight_mean - weight_sd, weight_mean+weight_sd

weight_second_sd_start , weight_second_sd_end = weight_mean -(  2 * weight_sd), weight_mean+(2*weight_sd)

weight_third_sd_start , weight_third_sd_end = weight_mean - ( 3*weight_sd), weight_mean+( 3*weight_sd)



height_list_of_data_within_1_sd = [result for result in height_list if result > height_first_sd_start and result < height_first_sd_end]
height_list_of_data_within_2_sd = [result for result in height_list if result > height_second_sd_start and result < height_second_sd_end]
height_list_of_data_within_3_sd = [result for result in height_list if result > height_third_sd_start and result < height_third_sd_end]

print("{}% for data of height lies within one standard deviation".format(len(height_list_of_data_within_1_sd )* 100.0/len(height_list)))
print("{}% for data of height lies within two standard deviation".format(len(height_list_of_data_within_2_sd )* 100.0/len(height_list)))
print("{}% for data of height lies within three standard deviation".format(len(height_list_of_data_within_3_sd )* 100.0/len(height_list)))

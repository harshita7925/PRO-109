import pandas as pd
import statistics
import csv

df=pd.read_csv("students_performance.csv")
reading_marks_list=df["reading score"].to_list()
writing_marks_list = df["writing score"].to_list()

reading_marks_mean=statistics.mean(reading_marks_list)
writing_marks_mean=statistics.mean(writing_marks_list)

reading_marks_median=statistics.median(reading_marks_list)
writing_marks_median=statistics.median(writing_marks_list)

reading_marks_mode=statistics.mode(reading_marks_list)
writing_marks_mode=statistics.mode(writing_marks_list)

reading_std_deviation = statistics.stdev(reading_marks_list)
writing_std_deviation = statistics.stdev(writing_marks_list)

print("Mean, Median and Mode of Reading marks is {}, {} and {} respectively".format(reading_marks_mean,reading_marks_median,reading_marks_mode))
print("Mean, Median and Mode of Writing marks is {}, {} and {} respectively".format(writing_marks_mean,writing_marks_median,writing_marks_mode))
print("Standard deviation of Reading marks is:",reading_std_deviation)
print("Standard deviation of Writing marks is:",writing_std_deviation)

reading_first_std_deviation_start, reading_first_std_deviation_end = reading_marks_mean-reading_std_deviation, reading_marks_mean+reading_std_deviation
reading_second_std_deviation_start, reading_second_std_deviation_end = reading_marks_mean-(2*reading_std_deviation), reading_marks_mean+(2*reading_std_deviation)
reading_third_std_deviation_start, reading_third_std_deviation_end = reading_marks_mean-(3*reading_std_deviation), reading_marks_mean+(3*reading_std_deviation)

writing_first_std_deviation_start, writing_first_std_deviation_end = writing_marks_mean-writing_std_deviation, writing_marks_mean+writing_std_deviation
writing_second_std_deviation_start, writing_second_std_deviation_end = writing_marks_mean-(2*writing_std_deviation), writing_marks_mean+(2*writing_std_deviation)
writing_third_std_deviation_start, writing_third_std_deviation_end = writing_marks_mean-(3*writing_std_deviation), writing_marks_mean+(3*writing_std_deviation)

reading_list_of_data_within_1_std_deviation = [result for result in reading_marks_list if result > reading_first_std_deviation_start and result < reading_first_std_deviation_end]
reading_list_of_data_within_2_std_deviation = [result for result in reading_marks_list if result > reading_second_std_deviation_start and result < reading_second_std_deviation_end]
reading_list_of_data_within_3_std_deviation = [result for result in reading_marks_list if result > reading_third_std_deviation_start and result < reading_third_std_deviation_end]

writing_list_of_data_within_1_std_deviation = [result for result in writing_marks_list if result > writing_first_std_deviation_start and result < writing_first_std_deviation_end]
writing_list_of_data_within_2_std_deviation = [result for result in writing_marks_list if result > writing_second_std_deviation_start and result < writing_second_std_deviation_end]
writing_list_of_data_within_3_std_deviation = [result for result in writing_marks_list if result > writing_third_std_deviation_start and result < writing_third_std_deviation_end]

print("{}% of data for reading marks lies within 1 standard deviation".format(len(reading_list_of_data_within_1_std_deviation)*100.0/len(reading_marks_list)))
print("{}% of data for reading marks lies within 2 standard deviations".format(len(reading_list_of_data_within_2_std_deviation)*100.0/len(reading_marks_list)))
print("{}% of data for reading marks lies within 3 standard deviations".format(len(reading_list_of_data_within_3_std_deviation)*100.0/len(reading_marks_list)))
print("{}% of data for writing marks lies within 1 standard deviation".format(len(writing_list_of_data_within_1_std_deviation)*100.0/len(writing_marks_list)))
print("{}% of data for writing marks lies within 2 standard deviations".format(len(writing_list_of_data_within_2_std_deviation)*100.0/len(writing_marks_list)))
print("{}% of data for writing marks lies within 3 standard deviations".format(len(writing_list_of_data_within_3_std_deviation)*100.0/len(writing_marks_list)))
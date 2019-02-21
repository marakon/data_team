import json
import pandas as pd

from components.count import Count
from components.ploter import Plot
from components.read_json import JsonOperations
from components.un_tar import Tar

file_name = input('Enter file name: ')
folder_name = file_name + "/"
file = open("values.txt", "w")

def present_data(dd, fse):
    print("Domain data files: ")
    for data in dd:
        print(data)
    print("FSE data files: ")
    for data in fse:
        print(data)
    print('')

def read(dd, fse):
    dd_data = [json.read_json(dd_data) for dd_data in dd]
    fse_data = [json.read_json(fse_data) for fse_data in fse]
    return dd_data, fse_data

def txt_file_calculation(dd_data, fse_data):
    for data in dd_data:
        mean_dc = "Mean domain count per dc: " + count_data.mean_dc(data)
        sum_storage = "\nStorage used in MB: " + count_data.sum_storage(data)
        file.write(mean_dc)
        file.write(sum_storage)

    # for data in fse_data:
    #     mean_dc = "Mean domain actions per dc: " + count_data.mean_dc(data)
    #     sum_storage = "\nStorage used in MB: " + count_data.sum_storage(data)
    #     file.write(mean_dc)
    #     file.write(sum_storage)

def bar_plot(dd_data, fse_data):
    for data in dd_data:
        count_data.dd_data_center(data)
        val, leb, both=count_data.val_leb()
        plot = Plot(val, leb, both)
        plot.save_bar()

def pie_plot(dd_data, fse_data):
    for data in fse_data:
        count_data.fse_data_center(data)
        val, leb, both=count_data.val_leb()
        plot = Plot(val, leb, both)
        plot.save_pie()

Tar(file_name).un_tar_file()
json = JsonOperations()
count_data = Count()
fse, dd = json.categorize_json(folder_name)
# fse are file system events
# dd are domain data's
present_data(dd, fse)
dd_data, fse_data = read(dd, fse)

txt_file_calculation(dd_data, fse_data)
bar_plot(dd_data, fse_data)
pie_plot(dd_data, fse_data)

file.close()
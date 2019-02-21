import json
import pandas as pd

from components.count import Count
from components.ploter import Plot
from components.read_json import JsonOperations
from components.un_tar import Tar

file_name = input('Enter file name: ')
folder_name = file_name + "/"
file = open("values.txt", "w")
json = JsonOperations()
count_data = Count()

def present_data(raw_dd, raw_fse):
    print("Domain data files: ")
    for data in raw_dd:
        print(data)
    print("FSE data files: ")
    for data in raw_fse:
        print(data)
    print('')

def read(raw_dd, raw_fse):
    dd_data = [json.read_json(dd_data) for dd_data in raw_dd]
    fse_data = [json.read_json(fse_data) for fse_data in raw_fse]
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

raw_fse, raw_dd = json.categorize_json(folder_name)
# FSE - File System Event
# DD - Domain Data
present_data(raw_dd, raw_fse)
dd_data, fse_data = read(raw_dd, raw_fse)

txt_file_calculation(dd_data, fse_data)
bar_plot(dd_data, fse_data)
pie_plot(dd_data, fse_data)

file.close()
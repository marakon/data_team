import json, logging
import pandas as pd

from components.count import Count
from components.ploter import Plot
from components.read_json import JsonOperations
from components.un_tar import Tar


logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
                    datefmt='%m-%d %H:%M',
                    filename="run.log",
                    filemode='w')
console = logging.StreamHandler()
console.setLevel(logging.INFO)
formatter = logging.Formatter('%(name)-12s: %(levelname)-8s %(message)s')
console.setFormatter(formatter)
logging.getLogger('').addHandler(console)
log = logging.getLogger("main_core")


def present_data(raw_dd, raw_fse):
    log.info('Domain data:')
    for data in raw_dd:
        log.info(f'{data}')
    log.info('File System Event data:')
    for data in raw_fse:
        log.info(f'{data}')

def read(raw_dd, raw_fse):
    dd_data = [json.read_json(dd_data) for dd_data in raw_dd]
    fse_data = [json.read_json(fse_data) for fse_data in raw_fse]
    return dd_data, fse_data

def txt_file_calculation(dd_data):
    file = open("values.txt", "w")
    for data in dd_data:
        mean_dc = "\nMean domain count per dc: " \
                    + count_data.dd_mean_dc(data)
        sum_storage = "\nStorage used in MB: " \
                    + count_data.sum_storage(data)
        file.write(mean_dc)
        file.write(sum_storage)
    file.close()

def bar_plot(dd_data, fse_data):
    for data in dd_data:
        count_data.dd_data_center(data)
        val, leb, both = count_data.val_leb()
        plot = Plot(val, leb, both)
        plot.save_bar()

def pie_plot(dd_data, fse_data):
    for data in fse_data:
        count_data.fse_data_center(data)
        val, leb, both = count_data.val_leb()
        plot = Plot(val, leb, both)
        plot.save_pie()

        count_data.continent(data)
        val, leb, both = count_data.val_leb()
        plot = Plot(val, leb, both)
        plot.save_bar()


file_name = input('Enter file name: ')
folder_name = file_name + "/"
json = JsonOperations()
count_data = Count()

Tar(file_name).un_tar_file()
raw_fse, raw_dd = json.categorize_json(folder_name)

""" 
        FSE - File System Event
        DD - Domain Data
"""

present_data(raw_dd, raw_fse)
dd_data, fse_data = read(raw_dd, raw_fse)

txt_file_calculation(dd_data)
bar_plot(dd_data, fse_data)
pie_plot(dd_data, fse_data)
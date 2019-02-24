#!/usr/bin/env python
import json, logging, tarfile
import pandas as pd

from components.count import Count
from components.ploter import Plot
from components.read_json import JsonOperations

__author__ = "Mateusz Osinski"


logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
                    datefmt='%d-%m-%y %H:%M:%S',
                    filename="run.log",
                    filemode='w')
console = logging.StreamHandler()
console.setLevel(logging.INFO)
formatter = logging.Formatter('%(name)-12s: %(levelname)-8s %(message)s')
console.setFormatter(formatter)
logging.getLogger('').addHandler(console)
log = logging.getLogger("main_core")


def un_tar_file(file_name):
    log.info(f"Opening file: {file_name}.tar.gz")
    tar = tarfile.open(file_name + ".tar.gz")
    tar.extractall()
    tar.close()
    log.info(f"{file_name} opened.")

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
        mean_dc = "\nMean domain count per dc: " + count_data.dd_mean_dc(data)
        sum_storage = "\nStorage used in MB: " + count_data.sum_storage(data)
        file.write(mean_dc)
        file.write(sum_storage)
    file.close()

def bar_plot(dd_data, fse_data):
    for data in dd_data:
        count_data.dd_data_center(data)
        val, leb, both = count_data.val_leb()
        plot = Plot(val, leb, both)
        plot.save_bar()

    for data in fse_data:
        count_data.continent(data)
        val, leb, both = count_data.val_leb()
        plot = Plot(val, leb, both)
        plot.save_bar()

        count_data.hours(data)
        val, leb, both = count_data.val_leb()
        plot = Plot(val, leb, both)
        plot.save_bar()

        count_data.app_inferred(data)
        val, leb, both = count_data.val_leb()
        plot = Plot(val, leb, both)
        plot.save_bar()

        count_data.top_active_domains(data)
        val, leb, both = count_data.val_leb()
        plot = Plot(val, leb, both)
        plot.save_bar()

def pie_plot(dd_data, fse_data):
    for data in dd_data:
        count_data.dd_domain_status(data)
        val, leb, both = count_data.val_leb()
        plot = Plot(val, leb, both)
        plot.save_pie()

    for data in fse_data:
        count_data.fse_data_center(data)
        val, leb, both = count_data.val_leb()
        plot = Plot(val, leb, both)
        plot.save_pie()

        count_data.top_action(data)
        val, leb, both = count_data.val_leb()
        plot = Plot(val, leb, both)
        plot.save_pie()


file_name = input('Enter file name: ')
folder_name = file_name + "/"
json = JsonOperations()
count_data = Count()

un_tar_file(file_name)
raw_fse, raw_dd = json.categorize_json(folder_name)

present_data(raw_dd, raw_fse)
dd_data, fse_data = read(raw_dd, raw_fse)

txt_file_calculation(dd_data)
bar_plot(dd_data, fse_data)
pie_plot(dd_data, fse_data)
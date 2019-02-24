#!/usr/bin/env python
import matplotlib.pyplot as plt
import logging

__author__ = "Mateusz Osinski"

log = logging.getLogger(__name__)

class Plot:
    def __init__(self, values, label, both):
        self.values = values
        self.label = label
        self.both = both

    def save_pie(self):
        log.info("Plotting pie plot of given data.")
        plt.pie(self.values, counterclock=True)
        plt.legend(self.label, loc=3)
        fig1 = plt.gcf()
        fig1.savefig("pie_plot.png", dpi=700)
        print("Time for you to rename the saved plot file!\n")
        plt.show()

    def save_bar(self):
        log.info("Plotting bar plot of given data.")
        plt.style.use('ggplot')
        plt.bar(self.both, self.values, color='olive', width=0.2)
        plt.xticks(self.both, self.label, rotation=15)
        fig1 = plt.gcf()
        fig1.set_size_inches(8, 6)

        fig1.savefig("bar_plot.png", dpi=200)
        print("Time for you to rename the saved plot file!\n")
        plt.show()
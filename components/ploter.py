import matplotlib as mpl
import matplotlib.pyplot as plt
import shutil

mpl.rcParams['font.size'] = 6.0

class Plot:
    def __init__(self, values, label, both):
        self.values = values
        self.label = label
        self.both = both

    def save_pie(self):
        plt.pie(self.values, counterclock=True)
        plt.legend(self.label, loc=3)
        fig1 = plt.gcf()
        fig1.savefig("pie_plot.png", dpi=700)
        print("Time for you to rename the saved plot file!\n")
        plt.show()

    def save_bar(self):
        plt.style.use('ggplot')
        plt.bar(self.both, self.values, color='green')
        plt.xticks(self.both, self.label)
        fig1 = plt.gcf()
        fig1.savefig("bar_plot.png", dpi=700)
        print("Time for you to rename the saved plot file!\n")
        plt.show()
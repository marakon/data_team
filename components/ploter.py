import matplotlib as mpl
import matplotlib.pyplot as plt
import shutil

mpl.rcParams['font.size'] = 6.0

class Plot:
    def __init__(self, values, label):
        self.values = values
        self.label = label

    def save_pie(self):
        plt.pie(self.values, counterclock=True)
        plt.legend(self.label,loc=3)
        fig1 = plt.gcf()
        name = "plot.png"
        fig1.savefig(name, dpi=700)
        plt.show()
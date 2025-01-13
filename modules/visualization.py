"""
VISUALISATION
"""


# Import the libraries

import pandas as pd
import numpy as np

import seaborn as sns

import matplotlib as plt
import matplotlib as mpl
import matplotlib.cm as cm
import matplotlib.pyplot as plt
from matplotlib import pyplot



class VisualizationManager:
    def __init__(self):
        """Visualisation manager initialization"""
        self.visualizations = []

    def add_histogram(self, data, x, hue=None, palette='coolwarm', **kwargs):
        """Adding histogram """
        def plot_histogram():
            plt.figure(figsize=(10,6))
            sns.histplot(data=data, x=x, hue=hue, palette=palette, **kwargs)
            plt.title(f'Histogram for {x}')
            plt.xlabel(x)
            plt.ylabel('Frequency')
            plt.show()

        self.visualizations.append(plot_histogram)

    def add_line_plot(self, data, x, y, hue=None, **kwargs):
        """Adding a Line Graph"""
        def plot_line():
            plt.figure(figsize=(10, 6))
            sns.lineplot(data=data, x=x, y=y, hue=hue, **kwargs)
            plt.title(f'Line Graph:{y} vs {x}')
            plt.xlabel(x)
            plt.ylabel(y)
            plt.show()

        self.visualizations.append(plot_line)

    def add_pair_plot(self, data, vars=None, hue=None, palette='coolwarm', **kwargs):
        """Adding pairplot (scatterplot matrix)"""
        def plot_pair():
            sns.pairplot(data=data, vars=vars, hue=hue, palette=palette, **kwargs)
            plt.suptitle('Scatterplot matrix', y=1.02)
            plt.show()

        self.visualizations.append(plot_pair)



    def remove_visualisation(self, index):
        """Removing visualization by index."""
        if 0 <= index < len(self.visualizations):
            del self.visualizations[index]
            print(f"Visualization under index {index} removed.")
        else:
            print(f"Индекс {index} вне диапазона.")

    def show_all(self):
        """Show visualisations"""
        for i, plot_func in enumerate(self.visualizations):
            # print(viz_manager.visualizations)
            print(f"Display visualization {i + 1}")
            plot_func()


# data = pd.read_csv('../data/data.csv')

# # Create object visualization manager
# viz_manager = VisualizationManager()
#
# # Add types of visualisations
# viz_manager.add_histogram(data, x='Age', hue=data['Survived'].map({0: 'Died', 1: 'Survived'}), multiple='stack')
# viz_manager.add_pair_plot(data, vars=['Age', 'Fare'], hue='Survived')
# viz_manager.add_line_plot(data, x='Age', y='Fare', hue='Pclass')
#
# viz_manager.show_all()
#
# # Remove the first visualization (histogram)
# viz_manager.remove_visualisation(0)
#
# # We show the remaining visualizations again
# viz_manager.show_all()
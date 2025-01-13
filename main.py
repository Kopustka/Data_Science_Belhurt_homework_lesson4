from modules import (csv_loader,
                     empty_values_finding, empty_values_report,
                     filling_missing_values ,
                     VisualizationManager)


def main():
    # Загрузка данных
    path = 'data/data.csv'
    data = csv_loader(path)

    # Визуализация пропущенных значений
    # Create object visualization manager
    viz_manager = VisualizationManager()

    # Add types of visualisations
    viz_manager.add_histogram(data, x='Age', hue=data['Survived'].map({0: 'Died', 1: 'Survived'}), multiple='stack')
    viz_manager.add_pair_plot(data, vars=['Age', 'Fare'], hue='Survived')
    viz_manager.add_line_plot(data, x='Age', y='Fare', hue='Pclass')

    viz_manager.show_all()

    # Remove the first visualization (histogram)
    viz_manager.remove_visualisation(0)

    # We show the remaining visualizations again
    viz_manager.show_all()


    # Отчет о пропущенных значениях
    missing_values = empty_values_finding(data)
    print('Пропущенные значения:')
    print(missing_values)

    missing_report = empty_values_report(data)


    # Заполнение пропущенных значений
    filling_missing_values(data, column='Age', method='mean', create_new_data =True)


if __name__ == "__main__":
    main()

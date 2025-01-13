"""
EMPTY VALUES FINDING
"""

# Import the libraries
import pandas as pd



def empty_values_finding(data):
    #Count missing values in each column
    missing_data = data.isnull().sum()
    return missing_data



# print(empty_values_finding(data))

def empty_values_report(data):
    missing_data = data.isnull().sum()

    missing_percentage =(missing_data / len(data) * 100)

    report = pd.DataFrame({
    'Missing Values Count': missing_data,
    'Percentage of Missing Values': missing_percentage})

    report = report[report['Missing Values Count'] > 0].sort_values(by='Missing Values Count', ascending=False)

    total_missing = missing_data.sum()
    total_cells = data.size
    total_missing_percentage = (total_missing / total_cells) * 100

    print(f"Общее количество пропущенных значений: {total_missing} ({total_missing_percentage:.2f}% от всех значений)")
    print("\nОтчет по пропущенным значениям:")
    print(report)

# print(empty_values_report(data))
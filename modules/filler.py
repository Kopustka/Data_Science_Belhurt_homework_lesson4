"""
EMPTY VALUES FILLING
"""
# Import the libraries




def filling_missing_values(data, method = 'median', column = 'Age', create_new_data =True): #By default, the age column is filled in.
    if column not in data.columns:
        raise ValueError(f'Column is not in data')

    df_filled = data.copy()

    if method == 'median':
        fill_value = df_filled[column].median()
    elif method == 'mean':
        fill_value = df_filled[column].mean()
    else:
        raise ValueError('Incorrect method. Either median or mean.')

    df_filled[column] = df_filled[column].fillna(fill_value)

    output_csv = 'output.csv'
    if create_new_data is True:
        df_filled.to_csv(output_csv, index=False)
        print(f"Файл с заполненными значениями сохранен как: {output_csv}")

    return data


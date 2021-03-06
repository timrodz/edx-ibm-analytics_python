import pandas as pd
import numpy as np


def create_df():
    """ Generates the DataFrame for the course

     Returns:
             DataFrame: Contains information about vehicles
     """
    url = 'https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/DA0101EN/auto.csv'

    # 'https://archive.ics.uci.edu/ml/machine-learning-databases/autos/imports-85.names'
    column_names = [
        'symboling',
        'normalized-losses',
        'make',
        'fuel',
        'aspiration',
        'num-of-doors',
        'body-style',
        'drive-wheels',
        'engine-location',
        'wheel-base',
        'length',
        'width',
        'height',
        'curb-weight',
        'engine',
        'num-of-cylinders',
        'engine-size',
        'fuel-system',
        'bore',
        'stroke',
        'compression-ratio',
        'horsepower',
        'peak-rpm',
        'city-mpg',
        'highway-mpg',
        'price'
    ]

    df = pd.read_csv(url, header=None)
    df.columns = column_names

    df.replace('?', np.nan, inplace=True)
    count_missing_data(df)

    cols_to_convert = [
        'symboling',
        'bore',
        'stroke',
        'normalized-losses',
        'horsepower',
        'price',
        'peak-rpm',
        'wheel-base',
        'length',
        'width',
        'height',
        'curb-weight',
        'engine-size',
        'stroke',
        'compression-ratio',
    ]

    for c in cols_to_convert:
        replace_nan_with_mean(df[c])

    df[cols_to_convert] = df[cols_to_convert].apply(pd.to_numeric)

    return df


def count_missing_data(df: pd.DataFrame, show_missing=False):
    """
    Displays all missing data for a given DataFrame
    """
    missing_data = df.isnull()
    for column in missing_data:
        missing_values = (missing_data[column] == True).sum()

        if missing_values == 0:
            continue

        if show_missing:
            print('Column: {} | Missing values count: ({})'.format(
                column,
                missing_values
            ))
    return missing_data


def replace_nan_with_mean(column, type_to_check: type = float):
    mean = column.astype(type_to_check).mean(axis=0)
    column.fillna(mean, inplace=True)


if __name__ == "__main__":
    example_df = create_df()
    
    # Print head/tail
    example_df.head(5)
    example_df.tail(5)

    # Provide a statistical summary of everything
    example_df.describe()

    # Include non-numerical objects
    example_df.describe(include='all')

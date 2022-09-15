import pandas as pd
import geopandas as gpd
import json
import os


def read_file(input_file: str, nb_rows=None, sep=","):
    """Documentation:
    this function reads files from different format geojson,shp,xlsx,xsl,Xslx,csv
    """
    fileformat = input_file.split(".")[-1]
    if fileformat in ("geojson", "shp"):
        gdf = gpd.read_file(input_file, rows=nb_rows)
        return pd.DataFrame(gdf)
    if fileformat in ("xlsx", "xls", "Xlsx"):
        return pd.read_excel(input_file, sep=sep, nrows=nb_rows)
    if fileformat in ("csv"):
        return pd.read_csv(input_file, sep=sep, nrows=nb_rows)
    else:
        raise KeyError(f"{input_file} this file cannot be processed....")


def select_params(path_columns: str):
    """Documentation:
    this function selects the columns to delete or keep, specified in the
    corresponding json.
    """
    with open(path_columns) as d:
        columns = json.load(d)
    return columns


def select_column_by_values(data_frame: pd.DataFrame, columns_values: dict):
    """Documentation:
    this function selects the data to be kept in the corresponding columns,
    specified in the json.
    """
    df_res: pd.DataFrame = pd.DataFrame()
    for column in columns_values.keys():
        df_temp = data_frame[data_frame[column].isin(columns_values[column])]
        df_res = pd.concat([df_res, df_temp]).drop_duplicates().reset_index(drop=True)
    return df_res


def to_csv(df: pd.DataFrame, out_file: str, overwrite: bool):
    """Documentation:
    this function saves the Dataframe in the directory.
    """
    out_file = f"{out_file}.csv"
    if overwrite or not os.path.exists(out_file):
        df.to_csv(out_file, index=False)
    else:
        raise ValueError(f"{out_file} already exists")


def select_data(
    input_file: str,
    out_file: str,
    overwrite: bool,
    file_sep:str,
    nb_rows=None,
    path_columns_to_keep=None,
    path_columns_to_delete=None,
    path_to_values_to_keep=None,
):
    """Documentation:
    This function truncate data files.
    """
    data_frame = read_file(input_file, nb_rows=nb_rows, sep=file_sep)
    if path_to_values_to_keep is not None:
        columns_values = select_params(path_to_values_to_keep)
        check = set(columns_values.keys()).difference(data_frame.columns)
        if len(check) != 0:
            raise KeyError(f"{check} not found in columns")
        else:
            data_frame = select_column_by_values(data_frame, columns_values)
    if (path_columns_to_keep is not None) and (path_columns_to_delete is not None):
        columns_to_keep = select_params(path_columns_to_keep)
        columns_to_delete = select_params(path_columns_to_delete)
        check = set(columns_to_delete).intersection(columns_to_keep)
        if len(check) != 0:
            raise KeyError(f"{check} are in both files to be deleted and kept")
    if path_columns_to_keep is not None:
        columns_to_keep = select_params(path_columns_to_keep)
        check = set(columns_to_keep).difference(data_frame.columns)
        if len(check) != 0:
            raise KeyError(f"{check} not found in columns")
        else:
            data_frame = data_frame[columns_to_keep]
    if path_columns_to_delete is not None:
        columns_to_delete = select_params(path_columns_to_delete)
        check = set(columns_to_delete).difference(data_frame.columns)
        if len(check) != 0:
            raise KeyError(f"{check} not found in columns")
        else:
            data_frame = data_frame.drop(columns=columns_to_delete)
    to_csv(data_frame, out_file, overwrite)

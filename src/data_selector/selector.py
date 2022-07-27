import pandas as pd
from pandas import DataFrame as df
import os
import json
import warnings
warnings.simplefilter("ignore")


def select(
    input_file: str,
    output_file: str,
    overwrite: bool,
    input_format: str,
    format_choice: str,
    path_columns_to_keep=None,
    path_columns_to_delete=None,
    path_to_data_and_columns=None,
    data_frame=None
) -> None:
    """Documentation:
        inputs:
            input_file:

    This function handles the interaction with the
    user for the choices.
    """
    if data_frame is None:
        data_frame = pd.read_csv(input_file)

    if path_columns_to_keep is not None:

        with open(path_columns_to_keep) as d:
            param_dict = json.load(d)
            list_col_names: list[str] = [value for value in param_dict['column_names'].values()]
            data_frame = data_frame.reindex(columns=list_col_names)

    if path_columns_to_delete is not None:

        with open(path_columns_to_delete) as d:
            param_dict = json.load(d)
            list_col_names = [value for value in param_dict['column_names'].values()]
            for col_name in list_col_names:
                data_frame = data_frame.drop(columns=[col_name], axis=1)

    if path_to_data_and_columns is not None:

        with open(path_to_data_and_columns) as d:
            param_dict = json.load(d)
            data_frame = select_data_and_column(data_frame, param_dict)

    save(
        data_frame,
        output_file,
        overwrite,
        format_choice,
        input_format
    )


def save(
    data_frame: df,
    output_file: str,
    overwrite: bool,
    format_choice=None,
    input_format=None
) -> None:
    """Documentation:
        inputs:
            output_file: path to the output_file
            overwrite: boolean to overwrite existing file

    This function saves the file to the specified path.
    """
    if overwrite or not os.path.exists(output_file):
        if format_choice is None :
            format_choice = input_format

        if format_choice == "csv":
            data_frame.to_csv(output_file, index=False, sep=";")
            print("File has been saved. End of the service.")

        elif format_choice == "json":
            data_frame.to_json(output_file)
            print("File has been saved. End of the service.")

        elif format_choice == "x":
            try:
                data_frame.to_excel(output_file, index=False)
                print("File has been saved. End of the service.")
            except TypeError as e:
                raise TypeError("TypeError : " + str(e) + " Wrong output_file. New input path with file : ")

        else:
            raise ValueError("\nError in the choice of the format. Try again.")

    elif os.path.exists(output_file):
        raise ValueError(f"{output_file} already exists. Overwrite option set to False. "
                         + "Service failed.")


def delete_column(
    data_frame: df,
    List_of_columns: list[str],
) -> df:
    """Documentation:
        inputs:
            data_frame: DataFrame of the data to modify.
            column_name: name of the column to delete.

    This function deletes a column from a DataFrame and
    returns the new DataFrame.
    """

    df_res: df = data_frame.drop(columns=List_of_columns)
    return df_res


def select_column(
    data_frame: df,
    list_of_column_name: list[str],
) -> df:
    """Documentation:
        inputs:
            data_frame: DataFrame of the data to modify.
            column_name: name of the column to return.

    This function selects a column from a DataFrame and
    returns it.
    """

    try:
        df_res: df = data_frame.reindex(columns=list_of_column_name)
        return df_res
    except ValueError as ve:
        raise ValueError("Value Error : " + str(ve))


def select_data_and_column(
    data_frame: df,
    param_dict: dict
) -> df:
    """Documentation:
        inputs:
            data_frame: DataFrame of the data to truncate.
            column_names: name of the column to truncate from.

    This function selects rows from one or more column in a DataFrame and
    returns the truncated DataFrame.
    """

    data_frame = data_frame.reindex(columns=param_dict["column_names"].keys())
    try:
        df_res: df = pd.DataFrame()
        list_inter_value = []
        list_inter_column = []
        for column in param_dict['column_names'].keys():
            for val in param_dict["column_names"][column]['value']:
                list_inter_value.append(data_frame[data_frame[column] == val])
            list_inter_column.append(pd.concat(list_inter_value))
            list_inter_value = []

        df_res = pd.concat(list_inter_column)
        return df_res
    except KeyError as e:
        raise KeyError("KeyError : " + str(e))


def check_name_okay(
    name: str,
    data_frame: df
) -> bool:
    """Documentation:
        inputs:
            name: name to check
            data_frame: reference dataframe to iterate through

    This function verifies if a name is a DataFrame column name.
    """

    for col_name in data_frame:
        if str(col_name) == name:
            return True
    return False


def get_name_index(
    data_frame: df,
    name: str,
) -> int:
    """Documentation:
        inputs:
            data_frame: DataFrame to analyse.
            column_name: name of the column we want the index of.

    This function gets the index of the column in the DataFrame.
    """

    for i in range(len(data_frame.columns)):
        if str(data_frame.columns[i]) == str(name):
            return i
        elif i == len(data_frame.columns) - 1:
            return -1
    return -1


def check_name_valid(data_frame: df, name: str, accept_empty: bool) -> bool:
    """Documentation:UU
        inputs:
            name: name to check
            data_frame: reference dataframe to iterate through

    This function verifies if a name is a DataFrame column name.
    """

    for col_name in data_frame:
        if accept_empty:
            if (str(col_name) == name) or (name == ""):
                return True
        else:
            if str(col_name) == name:
                return True
    return False


def handle_name_error(
    data_frame: df,
    name: str,
    accept_empty: bool,
):
    """Documentation:
        inputs:
            data_frame: DataFrame to analyse.
            column_name: name of the column we want the index of.

    This function handles the "wrong column name" error.
    """

    if not check_name_valid(data_frame, name, accept_empty):
        raise ValueError("Column name argument not found.")
    return name

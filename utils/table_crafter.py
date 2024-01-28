"""
Helper function for craft_table.py

by Stephane Vujasinovic
"""

# -IMPORTS ---
from typing import Callable
import pandas as pd
from icecream import ic
from tabulate import tabulate


# - FUNCTIONS ---
def get_file_extension(
    file: str
) -> str:
    """
    Extract file extension.

    Args:
        filename (str): Location to the file

    Returns:
        file_extension (str): File extension
    """
    file_extension = file.split('.')[-1]
    ic(file_extension)

    return file_extension


def new_file_extension(
    table_format: str
) -> str:
    """
    Set extension to save the table.

    Args:
        table_format (str): Format to generate the table

    Returns:
        new_ext (str): New file extension
    """
    if table_format == "markdown":
        new_ext = "md"
    elif table_format == "latex":
        new_ext = "tex"
    elif table_format == "string":
        new_ext = "txt"
    else:
        raise ValueError("Unsupported format: " + table_format)
    ic(new_ext)

    return new_ext


def new_file_name(
    file: str,
    table_format: str
) -> str:
    """
    Create new file name

    Args:
        file (str): _description_
        table_format (str): _description_

    Returns:
        str: _description_
    """
    new_extension = new_file_extension(table_format)
    new_file = file.split(".")[0] + f'.{new_extension}'
    ic(new_file)

    return new_file


def read_function(
    file_ext: str
) -> Callable:
    """
    Return the appropriate pandas read function.

    Args:
        file_ext (str): File extension

    Returns:
        read_file_function (Callable): Function
    """
    if "csv" == file_ext:
        read_file_function = pd.read_csv
    elif "json" == file_ext:
        read_file_function = pd.read_json
    elif "xlsx" == file_ext:
        read_file_function = pd.read_excel
    else:
        raise ValueError("Unsupported format: " + file_ext)

    return read_file_function


def convert_file_to_dataframe(
    file: str
) -> pd.DataFrame:
    """
    Convert the file to a dataframe.

    Args:
        file (str): file location

    Returns:
        pd.DataFrame: _description_
    """
    file_extension = get_file_extension(file)
    func = read_function(file_extension)

    return func(file)


def convert_dataframe_to_table(
    dataframe: pd.DataFrame,
    table_format: str
) -> str:
    """
    Convert dataframe to string.

    Args:
        dataframe (pd.DataFrame): _description_
        table_format (str): _description_

    Returns:
        str: _description_
    """
    if "markdown" == table_format:
        tabular = tabulate(dataframe, headers="keys",
                           tablefmt="pipe", showindex=False)
    elif "latex" == table_format:
        tabular = dataframe.to_latex(index=False)
    elif "string" == table_format:
        tabular = dataframe.to_string(index=False)
    else:
        raise ValueError("Unsupported format: " + table_format)

    return tabular


def craft_table(
    file: str,
    table_format: str
) -> str:
    """
    Craft the table.

    Args:
        file (str): File location
        table_format (str): Format for the table

    Returns:
        tabular (str): Table in string format
    """
    dataframe = convert_file_to_dataframe(file)
    table = convert_dataframe_to_table(dataframe, table_format)

    return table


def save_table(
    file: str,
    table: str,
    table_format: str
):
    """
    Save the table.

    Args:
        file (str): Filename location
        tab (str): Table in string format
        table_format (str): Format to save the table
    """
    new_file_path = new_file_name(file, table_format)
    with open(new_file_path, 'w', encoding='utf-8') as f:
        f.write(table)

    print(f"{table_format.title()} table saved to {new_file_path}")

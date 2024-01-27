"""
Simple script to read files.

by Stéphane Vujasinovic
"""

import os
import pandas as pd
import argparse
from icecream import ic
from tabulate import tabulate
from typing import Callable


def get_file_extension(
    file: str
) -> str:
    """
    Extract file extension

    Args:
        filename (str): Location to the file

    Returns:
        file_extension (str): File extension
    """
    file_extension = file.split('.')[-1]
    ic(file_extension)

    return file_extension


def new_file_extension(
    format: str
) -> str:
    """
    Find extension to save the table

    Args:
        format (str): Format for generating the table

    Returns:
        new_ext (str): New file extension
    """
    if format == "markdown":
        new_ext = "md"
    elif format == "latex":
        new_ext = "text"
    elif format == "string":
        new_ext == "txt"
    else:
        raise ("This format is not supported")

    return new_ext


def get_appropriate_read_function(
    file_ext: str
) -> Callable:
    """
    Returns the appropriate pandas read function based on file extension.

    Args:
        file_ext (str): File extension

    Returns:
        read_file_function (Callable): Appropriate function to call for reading the file
    """
    # Find function for reading the file
    if "csv" == file_ext:
        read_file_function = pd.read_csv
    elif "json" == file_ext:
        read_file_function = pd.read_json,
    elif "xlsx" == file_ext:
        read_file_function = pd.read_excel
    else:
        raise ("Type of extension not supported")

    return read_file_function


def read_file(
    file: str
) -> pd.DataFrame:
    """
    Read file to a DataFrame

    Args:
        file (str): File location

    Returns:
        dataframe (pd.DataFrame): DataFrame
    """
    file_extension = get_file_extension(file)
    func = get_appropriate_read_function(file_extension)
    dataframe = func(file)

    return dataframe


def craft_table(
    dataframe: pd.DataFrame,
    format: str
) -> str:
    """
    Create the table in the desired format

    Args:
        format (str): Format for the table

    Returns:
        tabular (str): Table in string format
    """
    # Find appropriate function for saving in the wanted format
    if "markdown" == format:
        tabular = tabulate(dataframe, headers="keys",
                           tablefmt="pipe", showindex=False)
    elif "latex" == format:
        tabular = dataframe.to_latex(index=False)
    elif "string" == format:
        tabular = dataframe.to_string(index=False)
    else:
        raise ("This format is not supported")

    return tabular


def save_table(
    file: str,
    data: str,
    format: str
):
    """
    Save the table in the desired format

    Args:
        file (str): Filename location
        tab (str): Table in string format
        format (str): Format to save the table
    """
    new_extension = new_file_extension(format)
    file_path = file.split(".")[0] + f'.{new_extension}'

    with open(file_path, 'w') as file:
        file.write(data)

    print(f"LaTeX table saved to {file_path}")


if __name__ == "__main__":
    parser = \
        argparse.ArgumentParser(
            description="*Save csv file to markdown or latex*"
        )
    parser.add_argument(
        "--file", type=str, default="example.csv",
        help="file name to convert to table"
    )
    parser.add_argument(
        "--format", type=str, default="markdown", 
        help="format to create the table [markdown/latex]"
    )
    parser.add_argument(
        "--no_save", action="store_true",
        help="don't save the table"
    )
    parser.add_argument(
        "--verbose", action="store_false",
        help="show icecream prints"
    )

    # Load/Set arguments
    args = parser.parse_args()
    file_location = args.file
    format = args.format
    if args.verbose:
        ic.disable()

    # Read file in dataframe
    df = read_file(file_location)
    ic(df)

    table = craft_table(df, format)
    ic(table)

    if args.no_save:
        print(table)
        quit()

save_table(file_location, table, format)

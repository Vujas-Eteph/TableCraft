"""
Deal with arguments

by Stephane Vujasinovic
"""

# - IMPORTS ---
import argparse


# - FUNCTIONS ---
def arguments():
    """_summary_

    Returns:
        _type_: _description_
    """
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

    return parser.parse_args()

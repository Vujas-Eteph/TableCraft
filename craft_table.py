"""
Simple script to create tables.

by Stephane Vujasinovic
"""

# - IMPORTS ---
from icecream import ic
from utils.table_crafter import craft_table, save_table
from utils.arguments import arguments


# - MAIN ---
if __name__ == "__main__":
    # Call arguments
    args = arguments()
    if args.verbose:
        ic.disable()

    # Load arguments
    file_location = args.file
    table_format = args.format

    # Craft table
    table = craft_table(file_location, table_format)

    # Save table or print at least
    if args.no_save:
        print(table)
    else:
        save_table(file_location, table, table_format)

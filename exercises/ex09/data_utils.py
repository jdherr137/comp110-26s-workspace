"""Data related utility functions."""

__author__ = ["", ""]

from csv import DictReader


def get_keys(
    input_dict: (
        dict[str, list[str]]
        | dict[str, list[int]]
        | dict[str, list[str | int]]
        | dict[str, int]
        | dict[str, str]
    ),
) -> list[str]:
    result: list[str] = []
    for key in input_dict:
        result.append(key)

    return result


def convert_columns_to_int(
    data: dict[str, list[str]], columns_conv: list[str]
) -> dict[str, list[str | int]]:
    """Convert the data in the selected columns to be of type int."""
    # Create new table to store converted data
    data_converted: dict[str, list[int | str]] = {}

    # Iterate through column names (keys of the dictionary)
    for col_name in data:
        # Create new list to append converted values to
        data_converted[col_name] = []

        # Declare the converted value with a type of either int or str
        converted_value: int | str

        # Iterate through data values in the column
        for value in data[col_name]:
            # If this column is in the list of columns to be converted,
            # cast it to an int
            if col_name in columns_conv:
                converted_value = int(value)
            else:
                converted_value = value

            # Add it to the new column of values, the list we created
            # that we have a reference to at data_converted[col_name]
            data_converted[col_name].append(converted_value)

    return data_converted


"""These are the functions we wrote/will write in class!"""


def read_csv_rows(filename: str) -> list[dict[str, str]]:
    """Read the rows of a CSV into a 'table'."""
    result: list[dict[str, str]] = []

    # Open a handle to the data file
    file_handle = open(filename, "r", encoding="utf8")

    # Prepare to read the data file as a CSV rather than just strings.
    csv_reader = DictReader(file_handle)

    # Read each row of the CSV line-by-line
    for row in csv_reader:
        result.append(row)

    # Close the file when done, to free its resources.
    file_handle.close()

    return result


def column_values(table: list[dict[str, str]], column: str) -> list[str]:
    """Produce a list[str] of all values in a single column."""
    result: list[str] = []

    for row in table:
        item: str = row[column]
        result.append(item)

    return result


def columnar(row_table: list[dict[str, str]]) -> dict[str, list[str]]:
    """Transform a row-oriented table to a column-oriented table."""
    result: dict[str, list[str]] = {}

    first_row: dict[str, str] = row_table[0]
    for column in first_row:
        result[column] = column_values(row_table, column)

    return result


def head(table: dict[str, list[str]], rows: int) -> dict[str, list[str]]:
    result: dict[str, list[str]] = {}

    for column in table:
        values: list[str] = []
        i: int = 0
        while i < rows and i < len(table[column]):
            values.append(table[column][i])
            i += 1

        result[column] = values
    return result


def select(table: dict[str, list[str]], columns: list[str]) -> dict[str, list[str]]:
    result: dict[str, list[str]] = {}

    for column in columns:
        result[column] = table[column]

    return result


def concat(
    table1: dict[str, list[str]], table2: dict[str, list[str]]
) -> dict[str, list[str]]:
    result: dict[str, list[str]] = {}

    for column in table1:
        result[column] = table1[column]

    for column in table2:
        if column in result:
            result[column] += table2[column]
        else:
            result[column] = table2[column]

    return result


def count(values: list[str]) -> dict[str, int]:
    result: dict[str, int] = {}

    for item in values:
        if item in result:
            result[item] += 1
        else:
            result[item] = 1

    return result


# not used
def filter_experience(data: list[str], value_of_intrest: str):
    result: list[str] = []
    for val in data:
        if val == value_of_intrest:
            result.append(value_of_intrest)
        else:
            result.append("null")

    return result


# not used
def filter_effective(data: list[str], val1: str, val2: str, val3: str):
    result: list[str] = []
    for val in data:
        if val == val1:
            result.append(val1)
        elif val == val2:
            result.append(val2)
        elif val == val3:
            result.append(val3)
        else:
            result.append("null")

    return result


# combines two previous functions
def filter_and_pair(
    exp_data: list[str],
    eff_data: list[str],
    exp_value: str,
    val1: str,
    val2: str,
    val3: str,
):

    result: list[tuple[str, str]] = []

    for i in range(len(exp_data)):
        exp = exp_data[i]
        eff = eff_data[i]

        if exp == exp_value and eff in [val1, val2, val3]:
            result.append((exp, eff))

    return result

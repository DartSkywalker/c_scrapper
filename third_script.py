"""
Script which replace text in a files from file_list.xtx based on the pattern_list.txt
Where the pattern_list.txt is a list of patterns to be replaced. Format is as follows:
first item in csv - line number, second - file name, third - pattern to be replaced
"""
import re


def lookup_for_file_index():
    decoded_dec_list = parse_replacement_text_file("replacement_test_file.txt")

    # Read patter_list.csv file and create a list of patterns to be replaced
    pattern_list_csv = []
    with open("pattern_list.csv", "r") as f:
        for line in f:
            pattern_list_csv.append(line.strip().split(","))

    new_list_for_file = []
    found_file_index = []
    # Iterate through the decoded_hex_list
    for decoded_ints in decoded_dec_list:
        for pattern in pattern_list_csv:
            if pattern[2] == "_1MMDDHHMMI_FILE_INDEX_":
                if int(decoded_ints[0]) == int(pattern[3]):
                    if pattern not in found_file_index:
                        found_file_index.append(pattern)

    print(f"Found file index: {found_file_index}")

    for found_index in found_file_index:
        for decoded_hex in decoded_dec_list:
            if int(found_index[3]) == int(decoded_hex[0]):

                # Navigate to line and append values to new_list_for_file
                with open(found_index[1], "r") as f:
                    lines = f.readlines()
                    for i, line in enumerate(lines):
                        if i == int(decoded_hex[1]) - 1:
                            find_string_re = re.compile(r'"(.+?)"')
                            try:
                                found_string = re.search(find_string_re, line).group(0)
                                new_list_for_file.append([decoded_hex[0], decoded_hex[1], found_string])
                            except AttributeError:
                                continue

    print(f"New list for file: {new_list_for_file}")

    # Write new_list_for_file to file
    with open("updated_replacements.txt", "w") as f:
        for line in new_list_for_file:
            f.write(f"{line[0]},{line[1]},{line[2]}\n")



def parse_replacement_text_file(file_name):
    """
    Function which parse the replacement_text.txt file
    :return:
    """
    hex_to_be_replaced = []
    decoded_hex_list = []

    with open(file_name, 'r') as f:
        for line in f:
            if (line.startswith("I[") or line.startswith("D[") or line.startswith("W[") or line.startswith("E[")) and line[2].isnumeric():
                if line.strip()[-1].isdigit():
                    hex_to_be_replaced.append(line.strip() + ' printf')
                else:
                    hex_to_be_replaced.append(line.strip())

    # Decode data from hex to dec
    for hexed in hex_to_be_replaced:
        integer = hexed[2:10]
        line_number = hexed[11:15]
        if "printf" in hexed:
            decoded_hex_list.append([int(integer, 16), int(line_number, 16), 'printf'])
        else:
            decoded_hex_list.append([int(integer, 16), int(line_number, 16)])
    print(f"Decoded hex list: {decoded_hex_list}")
    return decoded_hex_list


def replace_text(pattern_list, new_text):
    """
    Function which replace text in a files from file_list.txt based on the pattern_list.txt
    :param pattern_list: each line has format - line[0] - line number, line[1] - file name, line[2] - line text
    :param new_text: str
    :return:
    """
    for line in pattern_list:
        with open(line[1], "r") as f:
            lines = f.readlines()
            # Update the line
            lines[int(line[0]) - 1] = lines[int(line[0]) - 1].replace(line[2], new_text)
            print(f"Line {line[0]} in file {line[1]} was replaced with {new_text}")
        with open(line[1], "w") as f:
            f.writelines(lines)


def main():
    new_text = "new_printf"
    pattern_list = []
    with open("pattern_list.csv", "r") as f:
        for line in f:
            pattern_list.append(line.strip().split(","))
    replace_text(pattern_list, new_text)


if __name__ == "__main__":
    # main()
    lookup_for_file_index()

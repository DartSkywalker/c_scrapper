"""
Write a python script which search from a set of files, extract texts by matching some text pattern.
Input is the above file (file_list.txt).
Output is a csv file (pattern_list.csv) related to the text pattern and its extraction.
"""
import re

patterns_list = ['_1MMDDHHMMI_FILE_INDEX_',
                 'LOGGER_DEBUG',
                 'LOGGER_INFO',
                 'LOGGER_WARNING',
                 'LOGGER_ERROR']

def extract_text_updated(file_list):
    pattern_found_list = []
    for file in file_list:
        for pattern in patterns_list:
            with open(file, "r") as f:
                for line_num, line in enumerate(f, 1):
                    if pattern in line:
                        if pattern == '_1MMDDHHMMI_FILE_INDEX_':
                            find_integer_re = re.compile(r'\d{10}')
                            integer = re.search(find_integer_re, line).group(0)
                            print(f"A new match found in {file} at line {line_num} for pattern {pattern}")
                            pattern_found_list.append([line_num, file, pattern, integer])
                        elif pattern.startswith("LOGGER"):
                            find_string_re = re.compile(r'"(.+?)"')
                            found_string = re.search(find_string_re, line).group(0)

                            # Find file index in the file
                            find_file_index_re = re.compile(r'\d{10}')
                            with open(file, "r") as f:
                                for line_num, line in enumerate(f, 1):
                                    if "_1MMDDHHMMI_FILE_INDEX_" in line:
                                        file_index = re.search(find_file_index_re, line).group(0)
                                        break

                            print(f"A new match found in {file} at line {line_num} for pattern {pattern} in file {file_index}")
                            pattern_found_list.append([line_num, file, pattern, found_string, file_index])

    return pattern_found_list



def extract_text_by_regular_expression(file_list, pattern):
    """
    Extract text by regular expression
    :param file_list:
    :param pattern:
    :return:
    """

    pattern = re.compile(pattern)
    pattern_list = []
    for file in file_list:
        with open(file, "r") as f:
            for line_num, line in enumerate(f, 1):
                if re.search(pattern, line):
                    print(f"A new match found in {file} at line {line_num}")
                    pattern_list.append([line_num, file, re.search(pattern, line).group(0)])
    return pattern_list


def extract_text_simple(file_list, pattern):
    """
    Extract text by simple method - finding a word in a line
    :param pattern: - word to find/change
    :param file_list: - input file_list.txt file
    :return:
    """
    pattern_found_list = []
    for file in file_list:
        with open(file, "r") as f:
            for line_num, line in enumerate(f, 1):
                if pattern in line:
                    print(f"A new match found in {file} at line {line_num}")
                    pattern_found_list.append([line_num, file, pattern])
    return pattern_found_list


def write_file(pattern_list):
    """
    Writing the pattern_list with found lines to a csv file
    Format: line number, path to file, line's text
    :param pattern_list:
    :return:
    """
    with open("pattern_list.csv", "w") as f:
        for line in pattern_list:
            f.write(f"{str(line[0])},{str(line[1])},{str(line[2])},{str(line[3])}\n")
        print("File pattern_list.csv was created")


def main():
    file_list = []
    with open("file_list.txt", "r") as f:
        for line in f:
            file_list.append(line.strip())

    # pattern = "printf"
    # pattern_list = extract_text_simple(file_list, pattern)

    pattern_list = extract_text_updated(file_list)

    write_file(pattern_list)


if __name__ == "__main__":
    main()

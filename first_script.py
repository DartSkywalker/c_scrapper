"""
 Search .c file under a folder and its subfolder tree and save paths.
 Input is the start folder location.
 Output a txt file (file_list.txt) of the search result
"""
import os


def search_file(start_path):
    """
    Search .c file under a folder and its subfolder tree and save paths.
    :param start_path: - Start path allocated via os.getcwd().
    :return:
    """
    file_list = []
    for root, dirs, files in os.walk(start_path):
        for file in files:
            if file.endswith(".c"):
                file_list.append(os.path.join(root, file))
                print(f"Found '*.c' file: {os.path.join(root, file)}")
    return file_list


def write_file(file_list):
    """
    Write search results to a txt file
    :param file_list: - List of file paths
    :return:
    """
    with open("file_list.txt", "w") as f:
        for file in file_list:
            f.write(file + "\n")
        print("File list saved to file_list.txt")


def main():
    # Start searching from the current folder
    start_path = os.getcwd()
    file_list = search_file(start_path)
    write_file(file_list)


if __name__ == "__main__":
    main()

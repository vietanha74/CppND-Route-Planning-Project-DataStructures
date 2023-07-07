import os

def find_files(suffix, path):
    """
    Find all files beneath path with file name suffix.

    Note that a path may contain further subdirectories
    and those subdirectories may also contain further subdirectories.

    There are no limits to the depth of the subdirectories.

    Args:
      suffix(str): suffix of the file name to be found
      path(str): path of the file system

    Returns:
       a list of paths
    """
    result = []
    if os.path.isfile(path):  # Base case: path is a file
        if path.endswith(suffix):
            result.append(path.replace("\\", "/"))
    elif os.path.isdir(path):  # Recursive case: path is a directory
        for item in os.listdir(path):
            item_path = os.path.join(path, item)
            result.extend(find_files(suffix, item_path))
    return result

#Test Case 1:
#suffix = ".txt"
#path = "path/to/directory"#

#Directory Structure:
#- path/
#  - to/
#    - directory/
#      - file1.txt
#      - file2.txt
#      - subdir/
#        - file3.txt
#        - file4.jpg
#        - subdir2/
#          - file5.txt#

#Expected Output:
#["path/to/directory/file1.txt", "path/to/directory/file2.txt", "path/to/directory/subdir/file3.txt", "path/to/directory/subdir/subdir2/file5.txt"]

#Test Case 2:
#suffix = ".jpg"
#path = "path/to/directory"
#
#Directory Structure:
#- path/
#  - to/
#    - directory/
#      - file1.txt
#      - file2.txt
#      - subdir/
#        - file3.txt
#        - file4.jpg
#        - subdir2/
#          - file5.txt
#
#Expected Output:
#["path/to/directory/subdir/file4.jpg"]

#Test Case 3:
#suffix = ".py"
#path = "path/to/directory"#

#Directory Structure:
#- path/
#  - to/
#    - directory/
#      - file1.txt
#      - file2.txt
#      - subdir/
#        - file3.txt
#        - file4.jpg
#        - subdir2/
#          - file5.txt#

#Expected Output:
#[]

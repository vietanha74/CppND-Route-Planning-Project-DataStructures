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


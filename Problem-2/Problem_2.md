## FILE RECURSION ##
The find_files function will take suffix and path as argument. This function recursive searching for a file end with the desired "suffix" in parent path and sub path.

### Run time complexity ###
1. Checking if path is a file: operation has a time complexity of O(1).
2. Checking if file end with the desired "suffix": operation has a time complexity of O(1).
3. Iterating over the items in the directory: The os.listdir(path) operation has a time complexity of O(k)
    k : number of items in the directory
4. Recursive calls it self  n times. 
    n : items in directory

=> All operation take : O(k + n)

### Space complexity ###
1. The result list has a space complexity is O(m). Where m is number of matching file
2. The space complexity of the recursive call  is O(d). Where d is the depth of the directory.

=> All operation take : O(m + d)
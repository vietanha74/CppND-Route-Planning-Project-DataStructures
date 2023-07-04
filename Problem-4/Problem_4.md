## ACTIVE DIRECTORY ##
The function user_exists will take user as argument. This function recursive searching for check if user exist in group if not, it will check all the sub groups until user found out user in any group return TRUE otherwise return FALSE.

### Run time complexity ###
1. Checking if the user exists in the current group's users list takes O(U) time since it performs a linear search through the list.
2. Recursively calling user_exists() on each subgroup takes O(G) .

=> All operation take : O(U*G)

### Space complexity ###
1. The space complexity of the groups list is O(G).Where G is number of groups in the group hierarchy.
2. The space complexity of the users list is O(U). Where U is number of users in the group hierarchy.
3. The space complexity of user_exists() method makes recursive calls O(D) . Where D is the depth of recursive calls.

=> All operation take : O((U + G)*D)

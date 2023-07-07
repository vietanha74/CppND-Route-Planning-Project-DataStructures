class Group(object):
    def __init__(self, _name):
        self.name = _name
        self.groups = []
        self.users = []

    def add_group(self, group):
        self.groups.append(group)

    def add_user(self, user):
        self.users.append(user)

    def get_groups(self):
        return self.groups

    def get_users(self):
        return self.users

    def get_name(self):
        return self.name


parent = Group("parent")
child = Group("child")
sub_child = Group("subchild")

sub_child_user = "sub_child_user"
sub_child.add_user(sub_child_user)

child.add_group(sub_child)
parent.add_group(child)

class Group(object):
    def __init__(self, _name):
        self.name = _name
        self.groups = []
        self.users = []

    def add_group(self, group):
        self.groups.append(group)

    def add_user(self, user):
        self.users.append(user)

    def get_groups(self):
        return self.groups

    def get_users(self):
        return self.users

    def get_name(self):
        return self.name
    
    def user_exists(self,user):
        if user in self.users:
            return True
        for group in self.groups:
            if group.user_exists(user):
                return True
        return False


parent = Group("parent")
child = Group("child")
sub_child = Group("subchild")

sub_child_user = "sub_child_user"
sub_child.add_user(sub_child_user)

child.add_group(sub_child)
parent.add_group(child)

print(parent.user_exists(sub_child_user))

#Test Case 1:
# Create groups
parent = Group("parent")
child = Group("child")
sub_child = Group("subchild")

# Add users
parent.add_user("user1")
child.add_user("user2")
sub_child.add_user("user3")

# Add groups
child.add_group(sub_child)
parent.add_group(child)

# Check if user exists
print(parent.user_exists("user3"))  # Expected output: True

#Test Case 2:
# Create group
group = Group("group")

# Check if user exists in an empty group
print(group.user_exists("user1"))  # Expected output: False

#Test Case 3:
# Create group
group = Group("group")

# Add users
group.add_user("user1")
group.add_user("user2")
group.add_user("user3")

# Check if user exists
print(group.user_exists("user2"))  # Expected output: True

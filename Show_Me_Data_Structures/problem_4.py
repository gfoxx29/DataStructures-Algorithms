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

def is_user_in_group(user, group):
    """
    Return True if user is in the group, False otherwise.

    Args:
      user(str): user name/id
      group(class:Group): group to check user membership against
    """

    def search(self):
        if user in self.users:
            return True

        for sub_group in self.groups:
            if search(sub_group):
                return True

        return False

    return search(group)


parent = Group("parent")
child = Group("child")
sub_child = Group("subchild")
unknown = Group("unknown")

sub_child_user = "sub_child_user"
sub_child.add_user(sub_child_user)

child.add_group(sub_child)
parent.add_group(child)

# Test Cases
print("Pass" if (is_user_in_group(sub_child_user, sub_child) == True) else "Fail")

print("Pass" if (is_user_in_group(sub_child_user, child) == True) else "Fail")

print("Pass" if (is_user_in_group(sub_child_user, parent) == True) else "Fail")

print("Pass" if (is_user_in_group(sub_child_user, unknown) == False) else "Fail")

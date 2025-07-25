def role_decorator(func):
    def wrapper(self, user ):

        if user.user_role != "manager":
            raise PermissionError("Access Denied.")
        return func(self, user)
    return wrapper



class Users:
    def __init__(self, username, user_role):
        self.username = username
        self.user_role = user_role


class ProjecSystem:
    # def __init__(self, role, project):
    #     self.role = role
    #     self.project = project

    @role_decorator
    def delete_project(self, user):

        print("Project has been deleted.")

    def view_project(self):
        pass


user1 = Users("sysadmin", "manager")
# user2 = Users("Ariyan", "manager")

project1 = ProjecSystem()

print(project1.delete_project(user1))

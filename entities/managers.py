class Manager:

    def __init__(self, manager_id, manager_username, manager_password):
        self.manager_id = manager_id
        self.manager_username = manager_username
        self.manager_password = manager_password

    def make_manager_dictionary(self):
        return {
                "managerID": self.manager_id,
                "userName": self.manager_username,
                "passWord": self.manager_password

            }


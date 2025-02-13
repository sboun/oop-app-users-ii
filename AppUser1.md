# Create User Class
class User:

    # add specified instance attributes
    def __init__(self, name, email=None, drivers_license=None):
        self.name = name
        self.email = email
        self.drivers_license = drivers_license

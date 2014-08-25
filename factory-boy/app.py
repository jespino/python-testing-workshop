class User:
    first_name = ""
    last_name = ""
    email = ""
    profile = None

    def __init__(self, first_name, last_name, email, profile):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.profile = profile

class Profile:
    age = None
    sex = None
    baby = None

    def __init__(self, age, sex):
        self.age = age
        self.sex = sex
        self.baby = age < 3

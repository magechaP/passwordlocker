class User:
    """
    Class that generates new instances of contacts.
    """

    user_list = [] # empty user list

    def __init__(self,name,username,password):
        self.name = name
        self.username = username
        self.password = password
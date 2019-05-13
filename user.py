class User:
    """
    Class that generates new instances of contacts.
    """

    user_list = [] # empty user list

    def __init__(self,name,username,password):
        self.name = name
        self.username = username
         self.password = password

        """
        __init__ method that helps us define properties for our objects.
        """    
    def save_user(self):
        '''
        save_user method saves user objects into user_list
        '''
        User.user_list.append(self)
    def delete_user(self):
        '''
        delete_user_method deletes a saved user from the user_list
        '''
        User.user_list.remove(self)
    @classmethod
    def find_by_username(cls,username):
        '''
        method that takes in a username and returns a user that matches that username
        '''
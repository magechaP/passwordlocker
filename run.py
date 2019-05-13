#!/usr/bin/env python3.6
#!/bin/python3.6
from user import User
import random
import pyperclip
def create_user(p_name,u_name,ps):
    '''
    function to create a new user
    '''
    new_user = User(p_name,u_name,ps)
    return new_user
def save_user(user):
    '''
    function to save user
    '''
    user.save_user()
def del_user(user):
    '''
    function to delete a user
    '''
    user.del_user()
def find_user(username):
    '''
    function that finds a user by platform_name and returns the user
    '''
    return User.find_by_username(username)
def check_existing_user(username):
    '''
    function that check if a user exists with that platform_name and return a boolean
    '''
    return User.user_exists(username)
def display_user():
    '''
    function that returns all the saved users
    '''
    return User.display_users()
def copy_password(username):
     '''
     function to copy password to the clipboard
    '''
     my_password = UserData.show_user_data(username)
     pyperclip.copy(my_password.password)

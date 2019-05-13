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
#!/usr/local/bin/python3.8
"""Written by nognut"""
import os
import subprocess
"""this script is to be used in an interactive python shell"""
"""some minimal git hub commands for day today use"""


"""initial command git init"""
def git_init():
    cmd = subprocess.call("git init", shell=True)
    return cmd

"""login to github account"""
def login(username, email):
    user_name = subprocess.call(f"git config --global user.name {username}", shell=True)
    user_email = subprocess.call(f"git config --global user.email {email}", shell=True)
    return user_name and user_email 

"""add function"""
def add():
    file_name = input("Enter file name: ")
    if file_name == ".":
        file_list = os.listdir(os.getcwd())#listing all the files in current working directory
        for i in range(len(file_list)):
            if i == ".git":#can be improved using regex
                continue#skipping the files
            subprocess.call(f"git add {file_list[i]}", shell=True)
    else:
         cmd = subprocess.call(f"git add {file_name}", shell=True)
    return cmd
"""git status function"""
def git_status():
    return subprocess.call("git status", shell=True)

"""commit function"""
def commit():
    cmt_message = " "
    inputs = input("Enter commit message: ").split(' ')
    for i in range(len(inputs)):
        cmt_message += inputs[i]
    cmd = subprocess.call(f"git commit -m {cmt_message}", shell=True)
    return cmd
"""push function"""
def push():
    return subprocess.call(f"git push", shell=True)


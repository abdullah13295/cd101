
# #class
class user:
    def __init__(self,first_name,last_name,birth,sex): # this is the main class's (attribute)function , self is the main v 
        self.first_name=first_name
        self.last_name=last_name
        self.birth=birth
        self.sex=sex
    def grit(self):
        print (f"name: {self.first_name},{self.last_name},  year: {self.birth}")
    def calc_age (self, curr_year):
       return 2021-self.birth
    def calc_avg(self,other): #static
        z=(self.calc_age(2021)+other.calc_age(2021))/2
        return z
user_data=input(" Enter Ur name , last name , birth year, sex separated by pint: ").split(".")
user1=user("paul" ,"yo" ,1991 ,"male")
# user1.grit()
# print(user1.calc_age(2021))
user2=user("mariam","khoury",1993,"female")
# user2.grit()
# a= user.calc_avg (user1,user2)
# print(a)
user3=user(user_data[0],user_data[1],user_data[2],user_data[3])
user3.grit()
# import math as m # here we call it as new name (m)
# import os #???????
# import antigravity
# # pypi.org
# import random
# import cos
# x=10
# y=m.pow(x,2) #math.cos()
# print(y)
# __name__=="__main__" 
# side file
# def printing(name):
#     print(f"I am afraid {name}")
# if __name__=="__main__":
#     print("wubba lubba DbDub")
# main file 
# import my_file
# n=input("enter your friend's name: ")
# my_file.printing(n)
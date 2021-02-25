# lst=[1,3,4,5.3,'ali']

# for idx,val in enumerate(lst):
#     print(idx,val)

# for val in lst:
#     print(val)

# #if

# x=10 # >,<,=<,=>,==,!=,and,or,not
# print(bool(x>0 and x<12))  



# even or not 
# x=10
# if x%2==0:
#     print("x is even")
# print("bye bye")

# x=10
# if x%2==0:
#      print("x is even")
# else:
#     print("x is not even")



# lst=[1,3,4,5.3,15]
# for val in lst:
#     if val%2==0:
#         print(f"{val} is even")
#     else:
#         print(f"{val} is not even")


# lst=[1,3,4,5.3,15]
# for val in lst:
#     if val%2==0:
#         print(f"{val} is even")
#     elif val%3==0:
#         print(f"{val}%3 is true")
#     else:
#         print(f"{val} is not even")

# lst=[1,-30,4,52,15]
# for val in lst:
#     if val%2==0 and val>=0:
#         print(f"{val} is even and positive")
#     else:
#         print("ERROR")

# print(bool(lst))
# a=[]
# x=5
# v=0
# l=[None]
# n=None
# print(bool(a))
# print(bool(x))
# print(bool(v))
# print(bool(l))
# print(bool(n))


# lst=[35,63,73,36,85,47,57,47,33,73,23,7,8,3,8,0]
# even=[]
# n_even=[]
# for x in lst:
#     if x%2==0:
#         even.append(x)
#     else:
#         n_even.append(x)
# print(lst)
# print(even)
# print(n_even)

# print(sum(lst))

# continue & break 


# names=[]
# ages=[]

# x=input(" would you like to add name? if yes press 'Y', if NO press 'N': " )
# if x=="Y":
#     while True:
#         data=input("Enter the name and the age separated by pint:").split(".")
#         names.append(data[0])
#         ages.append(int(data[1]))
#         y=input("press 'Y' if you want to add another name , otherwise press 'N' :")
#         if y=="Y":
#             print("okey")
#             continue
#         else:
#             break
#     print(names)
#     print(ages)
#     m=(sum(ages)/len(ages))
#     print(f"the mean of ages is : {m}")
# else:
#     print("you are welcome when ever you want)")


# data={"a":33,"b":44,"c":35}
# print(data["a"])
# for key,val in data.items():
#     print(key,val)
# data["b"]=55
# data["z"]=12
# print(data)

# full_data={""}   #val could be a list of data



#functions
def first_foo(x,y):
    a=x+y
    print(a)   #no element saved
first_foo(7,8)

def first_fooo(x,y):
    a=x+y
    return a #save result in mamory 


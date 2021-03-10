# lst=[1,3,4,5.3,'ali'] #List definition

# for a,b in enumerate(lst): #To write items with index numbers inside the list     # enumerate is useful for obtaining an indexed list:
#     print(a,b)

# for val in lst:  #To write items inside the list
#      print(val)

# if    #If the condition is met, the program will execute the instructions within the condition once, and if the condition is not met, it will ignore those instructions


# >,<,=<,=>,==,!=,and,or,not   #Operations used within the condition context

# x=10
# print(bool(x>0 and x<12))   #Here it is required to write (True) if the two conditions are met: before (and) and after (and) together. And writing (False) in case at least one of the two conditions is not met



# even or not 

# x=10  #Define or enter the variable (x)
# if x%2==0:   #Condition text (do the following if the remainder of dividing (x) by 2 equals zero)
#     print("x is even") #Print a message that the number (x) is an even number
# print("bye bye")


#Example of using (if) and (else)
# x=10
# if x%2==0:
#      print("x is even")
# else: #The program executes the instructions inside (else) ONLY in case the (if) condition, is not met and it does not need condetion
#     print("x is not even")


# this programe is for find which element of list is even and which not
# lst=[1,3,4,5.3,15]
# for val in lst: # we need (for )loop to try all elements in list
#     if val%2==0:
#         print(f"{val} is even")
#     else:
#         print(f"{val} is not even")



#here we use more than 2condition so we need (if,elif,else)
# lst=[1,3,4,5.3,15] 
# for val in lst:
#      if val%2==0: 
#          print(f"{val} is even")
#     elif val%3==0: #if(if condition) did not met ,the program will see if (elif condition)will met , if not the programe will move to (else)
#          print(f"{val}%3 is true")
#     else: 
#          print(f"{val} is not even") # the program will print it ONLY if (if,elif)will not met 




# lst=[1,-30,4,52,15]
# for val in lst:
#     if val%2==0 and val>=0:
#         print(f"{val} is even and positive")
#     else:
#         print("ERROR")

# print(bool(lst)) #(True) because there are elements in this list
# a=[] 
# x=5
# v=0
# l=[None]
# n=None
# print(bool(a)) #(False) because there are no elements in this list
# print(bool(x)) #(True) because this element not 0
# print(bool(v))
# print(bool(l)) #(True) because there are elements in this list
# print(bool(n))


# lst=[35,63,73,36,85,47,57,47,33,73,23,7,8,3,8,0] #This program is to divide the group into two groups (even and not even numbers) and then print these lists
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

# print(sum(lst)) #(sum) is to find(The sum of the numbers in the list)






# continue & break #(Continue) and (break) are only used in loops
#(Continue)is to ignore the next lines in the loop and return to the first line of loop 
#(break)is to stop the loop 

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




                            #(Dictionary) The dictionary works like a list, but with the addition that an item can be called with a specific name
# data={"a":33,"b":44,"c":35}
# print(data["a"]) #HERE WE CALLED THE FIRST ELEMENT BY ("a")
# for key,val in data.items(): #here we called all element with there names
#     print(key,val)
# print(data)
# data["b"]=55
# print(data)
# data["z"]=12
# print(data)

# full_data={""}   #(val) could be a list of data



#functions 
# def first_foo(x,y):
#     a=x+y
#     print(a)   #no element saved
# first_foo(7,8) #here I want to do the opperations in(first_foo) on (7,8)

# def first_fooo(x,y):
#     a=[x,y]
#     return a #save result in mamory 
# q=first_fooo(2,4)
# print(q)

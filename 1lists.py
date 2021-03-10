# users=['sam','rami','fadi',13,12,15,True,False,True]
# print(users)
# num=len(users)
# print(num)
# new_student="abod"
# new_number=19
# users.append(new_student)
# users.append(new_number)
# print(users)
# print (len(users))







# list=[1,585,37,3974,159,482]
# print(list)
# list.sort()
# print(list)
# list.sort(reverse=True)
# print(list)
# list[4]=5
# print(list)
# list[len(list)-1]=13
# print(list)





# a=[1,4,7,0,3,8]
# b=['t',True]

# print(a,b)
# print(a+b)
# a.pop() #delet the last element
# print(a)
# a.pop(1) # delet the 3d element
# print(a)
# a.remove(7) # delet element(7) should call element
# print(a)
# # sort, remove, pop , append


# x=[652,651,6541,894,741,651,21,646,4646,54416,54,8965,144,94,9,84,984,9,84,96,84,8,4,698,4]
# for i in x:
#     print(i**2)
# y=[1,3,5,7,9]
# sq_y=[]
# for i in y:
     sq_y.append(i**2)
# print(sq_y)
# s=0
# for i in y:
#     s+=(i**2)
# print(s)

a=[1,2,3,4,5,6]
b=a #in lists (=) keep the link between a and b
print(b)
c=a[:] # just copy once
print(c)
d=a[1:3] # cpy the scound and the theird
print(d)
a.pop()
print(a,b,c)
s=[]
for i in range(2):
    s.append(i)
print(s)
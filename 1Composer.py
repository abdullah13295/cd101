n=int(input("please Enter number of composers: "))
f_names=[]
l_names=[]
b_years=[]
d_years=[]
ages=[]
sum=0
for i in range(n) :
    print(f"composer num {i+1}")
    full_data=input(" Enter first name , last name , birth year , death year separated by space: ").split(" ")
    f_names.append(full_data[0])
    l_names.append(full_data[1])
    b_years.append(int(full_data[2]))
    d_years.append(int(full_data[3]))
    ages.append(d_years[i]-b_years[i])
    sum+=ages[i]
mean=sum/n
for i in range(n):
    print(f"{i+1}- First Name: {f_names[i]}, Last Name: {l_names[i]}, Age: {ages[i]}")
print(f"Average age of composers: {mean}")
print("Please send me your notes on this code)")

def in_composers(x):
    print(f"composer num {x}")
    full_data=input(" Enter first name , last name , birth year , death year separated by space: ").split(" ")
    return(full_data)
def ages_composers(b,d):
    ages=[]
    for n in range(len(b)):
        ages.append(d[n]-b[n])
    avg_ages=sum(ages)/len(ages)
    return(ages,avg_ages)



i=1
user=input("Please enter your name: ")
welcome=input(f"hello {user}!, would you like to use me?, if yes enter 1 , if not enter 2:  ")
if welcome == "1":
    f_names=[]
    l_names=[]
    b_years=[]
    d_years=[]
    print("great!, let's begin")
    while True:
        full_data=in_composers(i)
        f_names.append(full_data[0])
        l_names.append(full_data[1])
        b_years.append(int(full_data[2]))
        d_years.append(int(full_data[3]))
        q1=input("would you like to add more? , if yes enter 1 , if not enter 2:  ")
        if q1=="1":
            print("okey")
            i+=1
            continue
        else:
            print("as you want)")
            break
    q2=input("would you like to calculate ages?, if yes enter 1 , if not inter 2:  ")
    if q2=="1":
        ages,avg_ages=ages_composers(b_years,d_years)
        print("ages have been calculated")
        result={"f":f_names,"l":l_names,"ages":ages,"av":avg_ages}
        print("now it's time to print what we have got")
        print("first names: " ,result["f"] )
        print("last names: " ,result["l"] )
        print("ages: " ,result["ages"] )
        print("average ages: " ,result["av"] )
    else:
        print("as you want)")
        print("now it's time to print what we have got")
        print("first names: " ,f_names )
        print("last names: " ,l_names )
    print("thank you for useing me)")
else:
    print("as you wish, I am here when ever you need)")


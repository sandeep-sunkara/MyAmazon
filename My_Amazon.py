import csv
import auth_for_myamazon
import products_for_myamazon

obj=auth_for_myamazon.register()
obj1=products_for_myamazon.avalprod()

print("1.existing_user"'\n'"2.new_user")
ut=input()
if(ut=="2" or ut=="new_user"):
    if obj.reg()=="hai":
        ut="1"
        print('exe')
if(ut=="1"or ut=="existing_user"):
    uname=input("Enter username:")
    password=input("Enter password:")
    if obj.login(uname,password):
        print("Login Successful")
        print()
        print("Type of Products Avaliable:")
        print("1.Electronics"'\n'"2.Fashion"'\n'"3.stationary")
        print("Select type of product:")
        top=input()
        if(top=="1" or top=="electronics"):
            obj1.electronics()


        elif(top=="2" or top=="fashion"):
            obj1.fashion()

        elif(top=="3" or top=="stationary"):
            obj1.stationary()

        else:
            print(top,"type of product not avaliable")
    else:
        print("Invalid Credentials")
else:
    print("Invalid Selection")

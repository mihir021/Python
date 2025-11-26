def cust_data():
    name = input("Enter Name :")
    age = input("Enter Age :")
    f = open('customer.txt','w+')
    f.write(f"name is {name}\nage is {age}")
    f.close()

cust_data()

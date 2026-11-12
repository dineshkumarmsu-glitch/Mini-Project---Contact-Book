headline="contact"
print(headline.center(72))
print("1. add contact\n2.view all contact\n3.delete\n4.update contact\n5.exit")
a={}
def add():
    while True:
        number=input("enter the number")
        if len(number)==10 and number.isdigit():
            print("ok")
            name=input("enter the name")
            a[name]=number
            print("contact saved")
            break
def view_contact():
    for i in a:
        print(i,'-',a[i])
def delete_contact():
    contact=input("enter the name")
    if contact in a:
        a.pop(contact)
        print("contact deleted")
    else:
        print("INVALID CONTACT")
def update():
    name=input("enter the name")
    if name in a :
        number=int(input("enter the number"))
        a[name]=number
        print("contact updated")
    else:
        print("Invalid contact")

        

while True:
    contact_open=int(input("enter the option"))
    if contact_open==1:
        add()
    elif contact_open==2:
        view_contact()
    elif  contact_open==3:
       delete_contact()
    elif  contact_open==4:
        update()
    else:
        print("exit")
        break

    
##print(b['a'])



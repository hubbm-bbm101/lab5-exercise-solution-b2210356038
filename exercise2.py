def valid_mail(m):
    return ("@" not in m) or ("." not in m)
mail=input("please enter your mail: ")
if valid_mail(mail):
    print("it is not a valid mail ")
else:
    print("it is a valid mail")
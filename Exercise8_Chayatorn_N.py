userInput = input("User : ")
passwordInput = input("Password : ")
if userInput == "Boss" and passwordInput == "1234" :
    print("welcome to EShop")
    print("----Select the menu----")
    print("1.Apple  15 Bath/each")
    print("2.Banana  10 Bath/each")
    print("3.Grape  30 Bath/each")
    userSelected = int(input("___"))
    if userSelected == 1 :
        print("Apple")
        x = int(input("How many : "))
        y = 15 * x
        print("Total : ", y)
    elif userSelected == 2 :
        print("Banana")
        x = int(input("How many : "))
        y = 10 * x
        print("Total : ", y)
    elif userSelected == 3 :
        print("Grape")
        x = int(input("How many : "))
        y = 30 * x
        print("Total : ", y)
else :
    print("Username or Password incorrect")

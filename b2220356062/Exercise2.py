def mailcheck(mail):
    musthave1 = "@"
    musthave2 = "."
    for element in musthave1 and musthave2:
        if element in mail:
            print("This is a valid e-mail address.")
        else:
            print("This address is invalid!")


mailcheck(input("Enter your e-mail address:"))

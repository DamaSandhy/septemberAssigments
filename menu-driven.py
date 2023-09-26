while True:
    print("Menu")
    print("1.Calculate area")
    print("2.Calculate perimeter")
    print("3.exit")
    choice = int(input("Enter your choice:"))
    if choice == 1:
        print("calculating area")
    elif choice ==2:
        print("calculating perimeter")
    elif choice ==3:
        print("exiting")
        break
    else:
        print("invalid choice.please try again")
    
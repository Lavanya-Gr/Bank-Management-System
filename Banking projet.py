
CustomerNames = ['Vamshi Sagar', 'Saritha', 'Jessy Veronica', 'Krishna', 'Ravali', 'Thanmay']
customerPins = ['0100', '1101', '1123', '1251', '0009', '1211']
customerBalances = [10000, 20000, 33000, 40700, 38000, 42000]
Deposition = 0
Withdrawal = 0
Balance = 0
Counter_1 = 1
Counter_2= 6
i = 0
while True:
    # os.system("cls")
    print("*"*60)
    print("========== WELCOME TO Overseas BANKING SYSTEM ==============")
    print("************************************************************")
    print("==========     (1). Open New Account     ===================")
    print("==========     (2). Withdraw Money =========================")
    print("==========     (3). Deposit  Money  ========================")
    print("==========     (4). Check Customers & Balance   ============")
    print("==========     (5). Exit/Quit                   ============")
    print("*"*60)

    choice = input("Select your choice from the Above Box menu : ")
    if choice == "1":
        print(" choice number 1 is Selected by the Customer")
        NOC = eval(input("Number of Customers : "))
        i = i + NOC

        if i > 6:
            print("\n")
            print("Customer registration exceed reached or Client registration too low")
            i = i - NOC
        else:
            while Counter_1 <= i:
                name = input("Write Your Fullname : ")
                CustomerNames.append(name)
                pin = str(input("Please input a Pin to Secure your Account : "))
                customerPins.append(pin)
                Balance = 0
                Deposition = eval(input("Please Input a value to Deposit to Start an Account : "))
                Balance = Balance + Deposition
                customerBalances.append(Balance)
                print("\nName=", end=" ")
                print(CustomerNames[Counter_2])
                print("Pin=", end=" ")
                print(customerPins[Counter_2])
                print("Balance=", "P", end=" ")
                print(customerBalances[Counter_2], end=" ")
                Counter_1 = Counter_1 + 1
                Counter_2 = Counter_2 + 1
                print("\nYour name is added to Customer Table")
                print("Your pin is added to Customer Table")
                print("Your balance is added to Customer Table")
                print("----New Customer account created successfully !----")
                print("\n")
                print("Your Name is Available on the Customer list now : ")
                print(CustomerNames)
                print("\n")
                print("Note! Please remember the Name and Pin")
                print("========================================")

        mainMenu = input(" Press Enter Key to go Back to Main Menu to Conduct Another Transaction or Quit_")
    elif choice == "2":
        j = 0
        print(" choice number 2 is Selected by the Customer")
        while j < 1:
            k = -1
            name = input("Please Input a name : ")
            pin = input("Please Input a pin : ")
            while k < len(CustomerNames) - 1:
                k = k + 1
                if name == CustomerNames[k]:
                    if pin == customerPins[k]:
                        j = j + 1
                        print("Your Current Balance:", end=" ")
                        print(customerBalances[k], end=" ")
                        print("-/Rs\n")
                        Balance = (customerBalances[k])
                        Withdrawal = eval(input("Input value to Withdraw : "))
                        if Withdrawal > Balance:
                            deposition = eval(input(
                                "Please Deposit a higher Value because your Balance mentioned above is not enough : "))
                            Balance = Balance + deposition
                            print("Your Current Balance:", end=" ")
                            print(Balance, end=" ")
                            print('-/Rs\n')
                            Balance = Balance - Withdrawal
                            print("-\n")
                            print("----Withdraw Successfully!----")
                            customerBalances[k] = Balance
                            print("Your New Balance: ", "P", Balance, end=" ")
                            print("\n\n")
                        else:
                            Balance = Balance - Withdrawal
                            print("\n")
                            print("----Withdraw Successfully!----")
                            customerBalances[k] = Balance
                            print("Your New Balance: ", "P", Balance, end=" ")
                            print("\n")
            if j < 1:
                print("Your name and pin does not match!\n")
                break
        mainMenu = input(" Press Enter Key to go Back to Main Menu to Conduct Another Transaction or Quit_")
    elif choice == "3":
        print("choice number 3 is selected by the Customer")
        n = 0
        while n < 1:
            k = -1
            name = input("Please Input  name : ")
            pin = input("Please Input pin : ")
            while k < len(CustomerNames) - 1:
                k = k + 1
                if name == CustomerNames[k]:
                    if pin == customerPins[k]:
                        n = n + 1
                        print("Your Current Balance: ", "P", end=" ")
                        print(customerBalances[k], end=" ")
                        print('-/Rs')
                        Balance = (customerBalances[k])
                        Deposition = eval(input("Enter the value you want to deposit : "))
                        Balance = Balance + Deposition
                        customerBalances[k] = Balance
                        print("\n")
                        print("----Deposition successful!----")
                        print("Your New Balance: ", Balance, end=" ")
                        print("-/Rs\n\n")
            if n < 1:
                print("Your name and pin does not match!\n")
                break
        mainMenu = input(" Press Enter Key to go Back to Main Menu to Conduct Another Transaction or Quit_")
    elif choice == "4":
        print("choice number 4 is selected by the Customer")
        k = 0
        print("Customer name list and balances mentioned below : ")
        print("\n")
        while k <= len(CustomerNames) - 1:
            print("->.Customer =", CustomerNames[k])
            print("->.Balance =", customerBalances[k], end=" ")
            print('-/Rs\n')
            print("\n")
            k = k + 1
        mainMenu = input(" Press Enter Key to go Back to Main Menu to Conduct Another Transaction or Quit_ ")
    elif choice == "5":
        print("choice number 5 is selected by the customer")
        print("Thank you for using our banking system!")
        print("\n")
        print("Thank You and Come again")
        break
    else:
        print("Invalid option selected by the Customer")
        print("Please Try again!")

        mainMenu = input("Press Enter Key to go Back to Main Menu to Conduct Another Transaction or Quit_")

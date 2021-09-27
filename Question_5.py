#5. Design a software for bank system. There should be options like cash withdraw, cash credit and change password.
# According to user input, the software should provide required output.
# Hint: Use if else statements and functions
from datetime import datetime

PIN_NUMBER = "1234"
CASH_BALANCE = 10000
print("********** DS BANK ATM **********")
print("********** Welcome **********")
pin = input(print("Enter your 4-digit pin number."))
if PIN_NUMBER != pin:
    print("PIN Entered is wrong. Session will end now")
else:
    print("\n")
    print("Please select your option from below")
    print("1. Check your balance")
    print("2. Withdraw cash")
    print("3. Cash Credit")
    print("4. Change your PIN")
    print("\n")
    k_press = input(">>> ")
    if k_press == "1":
        print("Your Account balance is:- ", CASH_BALANCE)
    elif k_press == "2":
        c_out = int(input("Enter the amount to be withdrawn"))
        if c_out <= CASH_BALANCE:
            CASH_BALANCE = CASH_BALANCE - c_out
            print("Cash out", c_out, " remaining balance ", CASH_BALANCE)
    elif k_press == "3":
        c_in = int(input("Enter the amount to credit and place Money in deposit location"))
        CASH_BALANCE = CASH_BALANCE + c_in
        print(c_in, " Rupees has been into your account, Current Balance is :- ", CASH_BALANCE)
    elif k_press == "4":
        temp = (input("Enter your current PIN:-"))
        newpin = (input("Enter your new PIN:-"))
        newpin_temp = (input("Renter your new PIN:-"))
        if temp == PIN_NUMBER and newpin == newpin_temp:
            PIN_NUMBER = newpin
            print("Pin Changed Successfully")
        else:
            print("Either old pin is wrong or new pin is not correct")
    else:
        print("Wrong input. Session will End now")

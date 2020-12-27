typeOfInterest = input("Do you want to calculate compound or simple interest?(c/s) ")

if typeOfInterest.lower() == "s" or "simple":
    principalamount = float(input("What is the principal amount in dollars? "))
    interestrate = float(input ("What is your interest rate per annum in percentage? "))
    time = float(input ("What is your interest timeframe in years? "))

    interest = principalamount * (interestrate/100) * time
    total = principalamount + interest

    print(f"Here is your total interest in dollars: ${interest}")
    print(f"Here is your total in dollars: ${total}")

elif typeOfInterest.lower() == "c" or "compund":
    principalamount = float(input("What is the principal amount in dollars? "))
    interestrate = float(input ("What is your interest rate per annum in percentage? "))
    time = float(input ("What is your interest timeframe in years? "))

    total = principalamount * (1+(interestrate/100) ** time)
    interest = total-principalamount

    print(f"Here is your total interest in dollars: ${interest}")
    print(f"Here is your total in dollars: ${total}")

else:
    print ("Please check your input again!")


print ("Thank you for using the interest calculator!")

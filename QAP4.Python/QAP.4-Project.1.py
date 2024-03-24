# Description: Program for "One Stop Insurance Company" to enter and calculate
# new insurance policy information for its customers.
# Author: Angela Flynn
 
# Import libraries
from datetime import datetime, timedelta
import datetime
import FormatValues as FV
import Validations as Val
import Calculations as Calc
import ASCIIArt as Art
import sys
import time

# Define program constants.
# Open the defaults file and read the values into variables
f = open('Defaults.dat','r')
POLICY_NUM            = int(f.readline())
BASIC_PREMIUM         = float(f.readline())
ADD_CAR_DISCOUNT      = float(f.readline())
EXTRA_LIABILITY_RATE  = float(f.readline())
GLASS_COV_RATE        = float(f.readline())
LOAN_CAR_RATE         = float(f.readline())
HST_RATE              = float(f.readline())
PROCESS_FEE           = float(f.readline())
f.close()

CURR_DATE = datetime.datetime.now()



# Define program functions.
# Functions imported: FormatValues, Validations, Calculations, and ASCIIArt.

# Main program.

while True:
    # Gather user input.
    print()
    print()
    print("ONE STOP INSURANCE COMPANY - Gather Customer Information:")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print()
    while True:
        custFName = input("Enter the customer's first name: ").title()
        if Val.isNameValid(custFName) == True:
            break
          
    while True:
        custLName = input("Enter the customer's last name: ").title()
        if Val.isNameValid(custLName) == True:
            break
            

    while True:
        custStAdd = input("Enter the customer's street address: ").title()
        if custStAdd == "":
            print("Data Entry Error - Customer's street address cannot be blank.")
        else:
            break

    while True:
        custCity = input("Enter the customer's city: ").title()
        if custCity == "":
            print("Data Entry Error - Customer's city cannot be blank.")
        else:
            break

    while True:
        custProv = input("Enter the customer's province (XX): ").upper()
        if Val.isProvValid(custProv) == True:
            break
        
    while True:
        custPostal = input("Enter the customer's postal code (X9X9X9): ").upper()
        if Val.isPostalValid(custPostal) == True:
            break
    
      
    while True:    
        custPhoneNum = input("Enter the customer's phone number (999-999-9999): ")
        if Val.isPhoneNumValid(custPhoneNum) == True:
            break
    
    print()
    while True:
        numCars = input("Enter the number of vehicles being insured: ")
        if Val.isNumCarsValid(numCars) == True:
            break

    numCars = int(numCars)

    while True:
        extraLiability = input("Does the customer require extra liability up to $1,000,000? (Y or N):  ").upper()
        if Val.isLiabilityValid(extraLiability) == True:
            break

    while True:
        glassCoverage = input("Does the customer require glass coverage? (Y or N): ").upper()
        if Val.isGlassCovValid(glassCoverage) == True:
            break

    while True:
        loanerCar = input("Does the customer require a loaner car? (Y or N): ").upper()
        if Val.isLoanerCarValid(loanerCar) == True:
            break

    
    while True:
        paymentType = input("How would the customer prefer to pay? (Full, Monthly or Down Pay): ").title()
        if Val.isPayTypeValid(paymentType) == True:
            break
             
    amtDown = 0
    if paymentType == "Down Pay":
        while True:
            amtDown = input("Enter the customer's down payment amount: ")
            if Val.isAmtDownValid(amtDown):
                break
    
    amtDown = float(amtDown)

    print()
    print()
    print("ONE STOP INSURANCE COMPANY - Process Customer Claim(s):")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print()
   
    claimAmtTotal = 0  # Initializes the total claim amount outside the loop

    while True:
        while True:
            claimNum = input("Enter the customer's claim number: ")
            if claimNum == "":
                print("Data Entry Error - Cannot be blank")
                continue
            elif not claimNum.isdigit():
                print("Data Entry Error - Invalid characters, must be digits only.")
            else:
                break

        while True:
            try:
                claimDate = input("Enter the customer's claim date (YYYY-MM-DD): ")
                claimDate = datetime.datetime.strptime(claimDate, "%Y-%m-%d")
            except ValueError:
                print("Data Entry Error - Invalid format, date must be entered as YYYY-MM-DD only.")
                continue
            else:
                break

        while True:
            try:
                claimAmt = float(input("Enter the customer's claim amount: "))
                claimAmtTotal += claimAmt  # This adds up the claim amounts for total.
            except ValueError:
                print("Data Entry Error - Must be entered as a float only.")
                continue
            else:
                break

        claimDate = datetime.datetime.strftime(claimDate, "%Y-%m-%d")
        custName = custFName + " " + custLName
        custAddress = custStAdd + "-" + custCity + "-" + custProv + "-" + custPostal

        print()
        for _ in range(5): 
            print('Saving claim data ...', end='\r')
            time.sleep(.3) 
            sys.stdout.write('\033[2K\r') 
            time.sleep(.3)
        
        f = open("Claims.dat", "a")

        f.write("{},".format(str(claimNum)))
        f.write("{},".format(str(claimDate)))
        f.write("{}\n".format(str(FV.FDollar2(claimAmtTotal))))

        f.close()

        print()
        Art.printCar()
        print()
        print("Claim data successfully saved ...",end='\r')
        time.sleep(2) 
        sys.stdout.write('\033[2K\r')  
        print()

        while True:
            addClaim = input("Would you like to enter another claim? (Y or N): ").upper()
            if addClaim != "Y" and addClaim != "N":
                print("Data Entry Error - Enter either Y or N only.")
            elif addClaim == "N":
                break
            else:
                break

        if addClaim == "N":
            break
    

    # Perform calculations.
    
    premium = Calc.calcBasicPremium(numCars)
    premium = float(premium)

    costExtraLiability = EXTRA_LIABILITY_RATE * numCars
    costGlassCoverage  = GLASS_COV_RATE * numCars
    costLoanCar        = LOAN_CAR_RATE * numCars

    totalExtraCosts = costExtraLiability + costGlassCoverage + costLoanCar

    totalPremium = premium + totalExtraCosts

    HST = HST_RATE * totalPremium

    totalCost = totalPremium + HST

    monthlyPay = Calc.calcMonthlyPay(paymentType, PROCESS_FEE, totalCost, amtDown)

    invoiceDate = CURR_DATE

    firstPayDate = Calc.FirstOfNextMonth(CURR_DATE)

 
    # Display results

    extraLiabilityDsp = FV.FYesOrNo(extraLiability)
    glassCoverageDsp  = FV.FYesOrNo(glassCoverage)
    loanerCarDsp      = FV.FYesOrNo(loanerCar)


    print()
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("       ONE STOP INSURANCE COMPANY")
    print("            Customer Receipt")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print()
    print(f" Invoice Date:   {FV.FDateMonthDayYear(invoiceDate):<}")
    print(f" Customer Name:   {custName:<}")
    print(f" Customer Address:")
    print(f"                  {custStAdd:>}")
    print(f"                  {custCity:>},{custProv:>}")
    print(f"                  {custPostal:>}")
    print()
    print(f" Customer Phone Number: {custPhoneNum:<} ")
    print()
    print("******************************************")
    print()
    print(f" Number of Vehicles Insured: {numCars:<}")
    print()
    print(f" Optional Extra Liability:   {extraLiabilityDsp:<3s}")
    print(f" Optional Glass Coverage:    {glassCoverageDsp:<3s}")
    print(f" Optional Loaner Car:        {loanerCarDsp:<3s}")
    print()
    print("******************************************")
    print()
    print(f" Payment Type: {paymentType:<s} ")
    print()
    print(f" Down Payment Amount:        {FV.FDollar2(amtDown):>10s}")
    print(f" Insurance Premium:          {FV.FDollar2(premium):>10s}")
    print(f" Extra Liability Cost:       {FV.FDollar2(costExtraLiability):>10s}")
    print(f" Glass Coverage Cost:        {FV.FDollar2(costGlassCoverage):>10s}")
    print(f" Loan Car Cost:              {FV.FDollar2(costLoanCar):>10s}")
    print()
    print(f" Extra Costs Total:          {FV.FDollar2(totalExtraCosts):>10s}")
    print(f" Insuranse Premium Total:    {FV.FDollar2(totalPremium):>10s}")
    print()
    print(f" HST:                        {FV.FDollar2(HST):>10s}")
    print(f" Total Cost:                 {FV.FDollar2(totalCost):>10s}")
    print(f" Monthly Payment:            {FV.FDollar2(monthlyPay):>10s}")
    print()
    if paymentType != "Full":
        print(f" First Payment Date: {FV.FDateMonthDayYear(firstPayDate)} ")

    print("******************************************")
    print()
    print(f" Claim #      Claim Date         Amount")
    print(" -----------------------------------------")

    
    f = open("Claims.dat", "r")

    for claimRecords in f:

        claimLst  = claimRecords.split(",")

        claimNums  = claimLst[0].strip()
        claimDates = claimLst[1].strip()
        claimAmts  = claimLst[2].strip()

        print(f"   {claimNums:<5s}      {claimDates:<10s}      {claimAmts:>9s}  ")
    print(" -----------------------------------------")


    for _ in range(5): 
        print('Saving policy data ...', end='\r')
        time.sleep(.3) 
        sys.stdout.write('\033[2K\r') 
        time.sleep(.3)
 
   
    f = open("Policy.dat", "a")

    f.write("Policy Number: {}, ".format(str(POLICY_NUM)))
    f.write("Customer Name: {}, ".format(custName))
    f.write("Customer Address: {}, ".format(custAddress))
    f.write("Customer Phone Number:{}, ".format(str(custPhoneNum)))
    f.write("Number of Vehicles Insured: {}, ".format(str(numCars)))
    f.write("Optional Extra Liability: {}, ".format(str(extraLiabilityDsp)))
    f.write("Optional Glass Coverage: {}, ".format(str(glassCoverageDsp)))
    f.write("Optional Loaner Car: {}, ".format(str(loanerCarDsp)))
    f.write("Payment Type: {}, ".format(paymentType))
    f.write("Down Payment Amount: {}, ".format(str(amtDown)))
    f.write("Total Insurance Premium: {}\n ".format(str(totalPremium)))

    f.close()
    
    Art.printTrafficLight()
   
    print()
    print("Policy data successfully saved ...", end='\r')
    time.sleep(1)  
    sys.stdout.write('\033[2K\r')  
    
    print()
    while True:
        addCustomer = input("Would you like to enter another customer? (Y or N): ").upper()
        if addCustomer != "Y" and addCustomer != "N":
            print("Data Entry Error - Enter Y or N only.")
        else:
            break

    POLICY_NUM += 1

    if addCustomer == "N":
        break
    
    
# Housekeeping
print()
print(f" THANK YOU FOR CHOOSING 'ONE STOP INSURANCE COMPANY'!")
print(" ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print()
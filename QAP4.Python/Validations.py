# Functions used to validate inputs.

def isNameValid(Name):
    allowed_char = set("ABCDEFGHIJKLMNOPQRSTUVWXYZ abcdefghijklmnopqrstuvwxyz-',.")
    if Name == "":
        print("Data Entry Error - cannot be blank.")
        return False
    elif set(Name).issubset(allowed_char) == False:
        print("Data Entry Error - invalid characters.")
        return False
    else:
        return True
    
def isProvValid(Prov):
    ProvLst = ["NL", "NS", "NB", "PE", "PQ", "ON", "MB", "SK", "AB", "BC", "NT", "YT", "NV"]  
    if Prov == "":
        print("Data Entry Error - cannot be blank.")
        return False
    elif len(Prov) != 2:
        print("Data Entry Error - province must be 2 letter format only.")
        return False
    elif Prov not in ProvLst:
        print("Data Entry Error - not a valid province.")
        return False
    else:
        return True
    

def isPostalValid(Postal):
    allowed_char = set("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    allowed_num =  set("1234567890")
    if Postal == "":
        print("Data Entry Error - customer's postal code cannot be blank.")
        return False
    elif len(Postal) != 6:
        print("Data Entry Error - customer's postal code must be 6 characters only.")
        return False
    elif set(Postal[0] and Postal[2] and Postal[4]).issubset(allowed_char) == False or set(Postal[1] and Postal[3] and Postal[5]).issubset(allowed_num) == False:
        print("Data Entry Error - customer's postal code must be in the format X9X9X9 only.")
        return False
    else:
        return True
    

def isPhoneNumValid(PhoneNum):
    if PhoneNum == "":
        print("Data Entry Error - Phone number cannot be blank.")
        return False
    elif len(PhoneNum) != 12:
        print("Data Entry Error - Phone number must be 12 characters only.")
        return False
    elif PhoneNum != PhoneNum[0:3] + "-" + PhoneNum[4:7] + "-" + PhoneNum[8:12]:
        print("Data Entry Error - Phone number must be in this format only (999-999-9999).")
        return False
    else:
        return True
   
   
def isNumCarsValid(NumCars):
    if NumCars == "":
        print("Data Entry Error - Cannot be blank.")
        return False
    elif NumCars.isdigit() != True:
        print("Data Entry Error - Contains invalid character(s).")
        return False
    else:
        return True
    

def isLiabilityValid(Liability):
    if Liability == "":
        print("Data Entry Error - Cannot be blank.")
        return False
    elif Liability != "Y" and Liability != "N":
        print("Data Entry Error - Must be either Y or N.")
        return False
    else:
        return True
    

def isGlassCovValid(GlassCov):
    if GlassCov == "":
        print("Data Entry Error - Cannot be blank.")
        return False
    elif GlassCov != "Y" and GlassCov != "N":
        print("Data Entry Error - Must be either Y or N.")
        return False
    else:
        return True
    

def isLoanerCarValid(LoanerCar):
    if LoanerCar == "":
        print("Data Entry Error - Cannot be blank.")
        return False
    elif LoanerCar != "Y" and LoanerCar != "N":
        print("Data Entry Error - Must be either Y or N.")
        return False
    else:
        return True
    

def isPayTypeValid(PayType):
    PayTypeLst = ["Full", "Monthly", "Down Pay"]
    if PayType == "":
        print("Data Entry Error - Cannot be blank.")
        return False
    elif PayType not in PayTypeLst:
        print("Data Entry Error - Must be either: Full, Monthly, or Down Pay.")
        return False
    else:
        return True
    

def isAmtDownValid(AmtDown):
    if AmtDown == "":
        print("Data Entry Error - Cannot be blank.")
        return False
    elif AmtDown.isalpha() == True:
        print("Data Entry Error - Invalid characters, must be digits only.")
        return False
    else:
        return True
    



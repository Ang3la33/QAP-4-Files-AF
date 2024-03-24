# Functions used to calculate values.

def calcBasicPremium(numCars):
    BASIC_PREMIUM = 869.00
    ADD_CAR_DISCOUNT = .25
    if numCars == 1:
        premium = BASIC_PREMIUM
    else:
        premium = (numCars - 1) * (BASIC_PREMIUM - (ADD_CAR_DISCOUNT * BASIC_PREMIUM)) + BASIC_PREMIUM

    return premium



def calcMonthlyPay(paymentType, PROCESS_FEE, totalCost, amtDownPay):

    if paymentType == "Full":
        monthlyPay = 0
    elif paymentType == "Monthly":
        monthlyPay = (PROCESS_FEE + totalCost) / 8
    elif paymentType == "Down Pay":
        monthlyPay = (PROCESS_FEE + totalCost - amtDownPay) / 8

    return monthlyPay


def FirstOfNextMonth(today):
    from datetime import datetime, timedelta
    firstNextMonth = today.replace(day=1) + timedelta(days=32)
    firstNextMonth = firstNextMonth.replace(day=1)
    
    return firstNextMonth


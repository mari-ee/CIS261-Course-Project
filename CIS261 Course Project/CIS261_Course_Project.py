# Name
# CIS___
# Course Project Phase 1


def employeeName():
    name = input("Employee Name: ")
    return name


def totalHours():
    t_hours = float(input("Total Hours: "))
    return t_hours


def hourlyRate():
    hRate = float(input("Hourly Rate: "))
    return hRate


def incomeTaxRate():
    it_rate = float(input("Income Tax Rate: "))
    return it_rate



def grossPay_incomeTax_netPay(totalHrs, hrlyRate, txRate):
    grossPay = totalHrs * hrlyRate
    incomeTax = grossPay * txRate
    netPay = grossPay - incomeTax
    return grossPay, incomeTax, netPay


def display_info():
    print()

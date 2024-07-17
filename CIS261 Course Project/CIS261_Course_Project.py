# Name
# CIS___
# Course Project Phase 1

# Counters
totalEmployees = 0
totalHours = 0
totalGrossPay = 0
totalIncomeTax = 0
totalNetPay = 0


# All functions to be defined
def employeeName():
    name = input("Employee Name or press end to quit: ")
    return name


def hoursWorked():
    t_hours = float(input("Hours Worked: "))
    return t_hours


def hourlyRate():
    hRate = float(input("Hourly Rate: "))
    return hRate


def incomeTaxRate():
    it_rate = float(input("Income Tax Rate: "))
    it_rate = it_rate/100
    return it_rate


def grossPay_incomeTax_netPay(totalHrs, hrlyRate, txRate):
    grossPay = totalHrs * hrlyRate
    incomeTax = grossPay * txRate
    netPay = grossPay - incomeTax
    return grossPay, incomeTax, netPay


def display_info(empName, hr_work, hr_rate, it_rate, grpay, inctax, netpay):
    print("\nEmployee Name: " + empName)
    print("Hours Worked: " + f"{hr_work: ,.2f}")
    print("Hourly Rate: $" + f"{hr_rate: ,.2f}")
    print("Income Tax Rate: $" + f"{it_rate: ,.2f}")
    print("Gross Pay: $" + f"{grpay: ,.2f}")
    print("Income Tax: $" + f"{inctax: ,.2f}")
    print("Net Pay: $" + f"{netpay: ,.2f}")


def info_summary(t_emp, t_hours, t_gpay, t_tax, t_netPay):
    print("\nTotal Number of Employees: " + str(t_emp))
    print("Total Hours: " + f"{t_hours: ,.2f}")
    print("Total Gross Pay: $" + f"{t_gpay: ,.2f}")
    print("Total Tax: $" + f"{t_tax: ,.2f}")
    print("Total Net Pay: $" + f"{t_netPay: ,.2f}")


if __name__ == "__main__":
    e_name = employeeName()
    while e_name.lower() != "end":
        hours_worked = hoursWorked()
        hourly_rate = hourlyRate()
        income_taxrate = incomeTaxRate()
        gin = grossPay_incomeTax_netPay(hours_worked, hourly_rate, income_taxrate)
        gross_Pay = gin[0]
        income_tax = gin[1]
        netPay = gin[2]

        display_info(e_name, hours_worked, hourly_rate, income_taxrate,gross_Pay, income_tax, netPay)

        totalEmployees += 1
        totalNetPay += netPay
        totalGrossPay += gross_Pay
        totalIncomeTax += income_tax
        totalHours += hours_worked
        print("\n")

        e_name = employeeName()

    info_summary(totalEmployees, totalHours, totalGrossPay, totalIncomeTax, totalNetPay)

"""
Assignment-2 - Paying Debt off in a Year
"""
def paying_debt_off_in_a_year(inp_balance, annual_interest_rate):
    """# Assume that the interest is compounded monthly according to the balance
    #at the end of the month (after the payment for that month is made).
    #The monthly payment must be a multiple of $10 and is the same for all months. Notice that it is
    # possible for the balance to become
    # negative using this payment scheme, which is okay.
    # A summary of the required math is found below:
    # Monthly interest rate = (Annual interest rate) / 12.0
    # Monthly unpaid balance = (Previous balance) - (Minimum fixed monthly payment)
    # Updated balance each month = (Monthly unpaid balance) + (Monthly interest rate
     x Monthly unpaid balance)"""
    monthly_payment = 0
    balance = inp_balance
    while balance > 0:
        balance = inp_balance
        monthly_payment = monthly_payment + 10
        month = 1
        while month <= 12:
            monthly_interest_rate = (annual_interest_rate) / 12.0
            monthly_unpaid_balance = (balance) - (monthly_payment)
            updated_balance_each_month = (monthly_unpaid_balance) + \
            (monthly_interest_rate * monthly_unpaid_balance)
            balance = updated_balance_each_month
            month += 1
    return monthy_payment
def main():
    """ main function"""
    data = input()
    data = data.split(' ')
    data = list(map(float, data))
    print("Lowest Payment: " + str(paying_debt_off_in_a_year(data[0], data[1]))
if __name__ == "__main__":
    main()



# Account.py
class Account:
    #Initialize the Account class with a blanace and interest
    def __init__(self, balance, interest):
        self.balance = balance #Initial balance
        self.interest = interest #Interest earned

    # Method to set a new balance
    def set_balance(self, balance):
        self.balance = balance

    #Method to set the interest earned
    def set_interest(self, interest):
        self.interest = interest


# savings_account.py
def create_savings_account(balance, interest_rate, months):
    # Create an instance of the Account class
    account = Account(balance, 0) #Start with zero interest

    # Calculate the interest earned
    interest_earned = (balance * (interest_rate / 100) * (months / 12))

    # Update the balance by adding the interest earned
    updated_balance = balance + interest_earned

    # Use the Account class methods to set the new balance and interest
    account.set_balance(updated_balance)
    account.set_interest(interest_earned)

    # Return both the updated balance and interest earned
    return updated_balance, interest_earned


# cd_account.py
def create_cd_account(balance, interest_rate, months):
    # Similar to the savings account function, but for CDs
    account = Account(balance, 0) #Initial balance, no interest yet

    # Calculate the interest earned over the specified months
    interest_earned = (balance * (interest_rate / 100) * (months / 12))

    # Update the balance by adding the calculated interest
    updated_balance = balance + interest_earned

    # Set the updated balance and interest earned in the Account object
    account.set_balance(updated_balance)
    account.set_interest(interest_earned)

    # Return the updated balance and the interest earned
    return updated_balance, interest_earned


# customer_banking.py
def main():
    # Prompt the user for savings account details
    print("Savings Account:")
    savings_balance = float(input("Enter the savings account balance: "))
    savings_interest = float(input("Enter the annual interest rate (in %): "))
    savings_maturity = int(input("Enter the number of months: "))

    # Call the create_savings_account function to calculate updated balance and interest
    updated_savings_balance, savings_interest_earned = create_savings_account(
        savings_balance, savings_interest, savings_maturity
    )

    # Print out the interest earned and updated balance, formatted nicely
    print(
        f"Interest earned: ${savings_interest_earned:,.2f}. Updated balance: ${updated_savings_balance:,.2f}"
    )

    # Now handle CD account details
    print("\nCD Account:")
    cd_balance = float(input("Enter the CD account balance: "))
    cd_interest = float(input("Enter the annual interest rate (in %): "))
    cd_maturity = int(input("Enter the number of months: "))

    # Call the create_cd_account function for CD calculations
    updated_cd_balance, cd_interest_earned = create_cd_account(
        cd_balance, cd_interest, cd_maturity
    )

    # Print out the results for the CD account
    print(
        f"Interest earned: ${cd_interest_earned:,.2f}. Updated balance: ${updated_cd_balance:,.2f}"
    )
    
    
# Standard Python convention to run the main function
if __name__ == "__main__":
    main()
import time

# Customer registered details
saved_password = 1234
saved_balance = 10000
customer_phone = '09090021112'
date_of_birth = "1990-01-15"  # Customer's date of birth in YYYY-MM-DD format

# Global variables
list_of_banks = ['Gtbank', 'UBA', 'First Bank', 'Wema Bank', 'Heritage', 'Ecobank', 'Zenith Bank']
bar = 5  # Number of attempts allowed for entering the correct password

print(' Wave Bank '.center(30, '*'))
            
# Loop to ensure correct USSD code
while True:
    ussd = input('Enter *101# to access Wave Bank USSD Service: ')
    if ussd == '*101#':
        break
    else:
        print('Invalid MMI code. Please enter *101#.')
        
        
        
# Function to get a valid integer input within a specific range
def get_valid_int(prompt, min_val=None, max_val=None):
    while True:
        try:
            val = int(input(prompt))
            if (min_val is not None and val < min_val) or (max_val is not None and val > max_val):
                print("Invalid choice. Please try again.")
                continue
            return val
        except ValueError:
            print("Invalid input. Please enter a number.")
            
        
def get_valid_string(prompt):
    while True:
        val = input(prompt).strip()
        if val:
            return val
        print("This field cannot be empty. Please your number.")
        
        
def get_valid_phone_number(prompt):
    while True:
        phone_number = get_valid_string(prompt)
        if phone_number.isdigit() and len(phone_number) == 11:
            return phone_number
        print("Invalid phone number. It must be 11 digits.")

# Function to simulate a password check with a limited number of attempts
def password_check():
    incorrect_attempts = 0
    while incorrect_attempts < bar:
        customer_password = get_valid_int("Enter your password: ")
        if customer_password == saved_password:
            return True
        else:
            incorrect_attempts += 1
            remaining_attempts = bar - incorrect_attempts
            print(f'Wrong password! You have {remaining_attempts} attempts left.')
            if incorrect_attempts == bar:
                print('You have been barred. Visit the nearest branch to unblock your account.')
                return False

# Function to change the saved password
def change_password():
    global saved_password
    attempts = 3  # Attempts allowed to enter the correct current password

    for _ in range(attempts):
        current_password = get_valid_int("Enter your current password: ")
        if current_password == saved_password:
            dob_input = input("Enter your date of birth (YYYY-MM-DD): ")
            if dob_input == date_of_birth:
                new_password = get_valid_int("Enter your new 4-digit password: ", 1000, 9999)
                saved_password = new_password
                print("Your password has been changed successfully.")
                return
            else:
                print("Incorrect date of birth.")
        else:
            print("Wrong current password.")

    print("Too many incorrect attempts. Visit the nearest branch for assistance.")

# Main program loop
ussd_service = True
while ussd_service:
    print("\nChoose a transaction:\n"
          "1. Check Balance\n"
          "2. Send Money\n"
          "3. Purchase Airtime\n"
          "4. Purchase Data\n"
          "5. Change Password\n"
          "6. Cancel")

    customer_choice = get_valid_int("Enter: ", 1, 6)

    if customer_choice == 1:  # Check Balance
        if password_check():
            print('Balance:', saved_balance)

    elif customer_choice == 2:  # Send Money
        bank_choice = get_valid_int("1. Wave Bank\n2. Other Banks\nEnter: ", 1, 2)
        if bank_choice == 1:
            print("Transferring within Wave Bank")
        elif bank_choice == 2:
            print("Select bank:")
            for idx, bank in enumerate(list_of_banks, start=1):
                print(f"{idx}. {bank}")
            bank_name = get_valid_int("Enter bank choice: ", 1, len(list_of_banks))
            
            if bank_name > len(list_of_banks):
                print("Invalid bank selection.")
                continue

        # Get transfer details
        account_number = get_valid_int("Enter account number: ")
        amount_to_transfer = get_valid_int("Enter amount: ")

        # Check if the balance is sufficient
        if amount_to_transfer > saved_balance:
            print("Insufficient balance. Cannot process this transaction.")
            continue

        # Password check and process transfer
        if password_check():
            # Mimic loading
            print("Processing", end="")
            for _ in range(5):
                print(".", end="", flush=True)
                time.sleep(0.25)
            print()

            # Deduct from balance
            saved_balance -= amount_to_transfer
            print(f"{amount_to_transfer} sent to account {account_number}")
            print("Balance:", saved_balance)

    elif customer_choice == 3:  # Purchase Airtime
        card_purchase = get_valid_int("1. Buy airtime for yourself\n2. Buy for others\nEnter: ", 1, 2)

        if card_purchase == 2:  # Buy airtime for others
            print("\nSelect network:\n"
                  "1. MTN\n"
                  "2. 9mobile\n"
                  "3. Glo\n"
                  "4. Airtel")
            network_choice = get_valid_int("Enter (1-4): ", 1, 4)

            phone_number = get_valid_phone_number("Enter phone number: ")
        else:
            phone_number = customer_phone
        
        card_amount = get_valid_int("Enter amount: ")

        if card_amount > saved_balance:
            print("Insufficient balance. Cannot process this transaction.")
            continue

        if password_check():
            # Processing simulation
            print('Processing', end='')
            for _ in range(5):
                print('.', end='', flush=True)
                time.sleep(0.25)
            print()

            saved_balance -= card_amount
            print(f'{phone_number} has been credited with {card_amount}')
            print('Balance:', saved_balance)

    elif customer_choice == 4:  # Purchase Data
        data_purchase = get_valid_int("1. Buy data for yourself\n2. Buy for others\nEnter: ", 1, 2)

        if data_purchase == 1:
            phone_number = customer_phone
        else:
            # Get the network and phone number
            print("\nSelect network:\n"
                "1. MTN\n"
                "2. 9mobile\n"
                "3. Glo\n"
                "4. Airtel")

            network_choice = get_valid_int("Enter (1-4): ", 1, 4)
            phone_number = get_valid_phone_number("Enter phone number: ")
            

        print("\nChoose a data plan:\n"
              "1. 100MB - 1000 NGN\n"
              "2. 200MB - 2000 NGN\n"
              "3. 1GB - 5000 NGN\n"
              "4. 2GB - 8000 NGN\n"
              "5. 5GB - 15000 NGN")

        data_choice = get_valid_int("Enter (1-5): ", 1, 5)

        data_cost = {1: 1000, 2: 2000, 3: 5000, 4: 8000, 5: 15000}
        selected_data_cost = data_cost[data_choice]

        if selected_data_cost > saved_balance:
            print("Insufficient balance. Cannot process this transaction.")
            continue

        if password_check():
            # Processing simulation
            print('Processing', end='')
            for _ in range(5):
                print('.', end='', flush=True)
                time.sleep(0.25)
            print()

            saved_balance -= selected_data_cost
            print(f'{phone_number} has been credited with the selected data plan.')
            print('Balance:', saved_balance)

    elif customer_choice == 5:  # Change Password
        change_password()

    elif customer_choice == 6:  # Cancel
        print('Goodbye!')
        ussd_service = False
        continue

    # Ask if they would like to perform another transaction
    print("\nWould you like to perform another transaction?\n"
          "1. Yes\n"
          "2. No")

    another_transaction = get_valid_int("Enter: ", 1, 2)
    if another_transaction == 2:
        print("Thanks for using Wave Bank USSD service. Goodbye!")
        ussd_service = False
    elif another_transaction == 1:
        continue

from abc import ABC, abstractmethod  # abstraction
import random    # used for random account number generation
import account_generation  # importing mdoule

class Bank(ABC):

    def __init__(self, name, age, address,contact_number):
        self.name = name
        self.age = age
        self.address = address
        self.contact_number = contact_number
        self.generated_account_number = account_generation.generate_account_number(self)

        self.user_data = []

        self.user_dict = {
            'name': name,
            'age': age,
            'address': address,
            'account_number': self.generated_account_number,
            'contact number':0000000000,
            'original_amount': 1000,
            'updated_amount':0
        }
  
    def _registration(self, name , age, address):
        enter_name = input("Enter your name :")
        enter_age = int(input("Enter your age :"))
        enter_address = input("Enter your address: ")
        enter_contact = int(input("Enter your contact number: "))

        print("\n")
        print("*********************************************************************************************")
        print("You have been registered successfully. Your account number is :",self.generated_account_number)
        print("*********************************************************************************************")

        user_dict = {
            'name': name,
            'age': age,
            'address': address,
            'contact_number':0000000000,
            'account_number': self.generated_account_number,
            'original_amount': 1000,
            'updated_amount':0
        }

        self.user_dict['name'] = enter_name
        self.user_dict['age'] = enter_age
        self.user_dict['address'] = enter_address
        self.user_dict['contact_number'] = enter_contact

        self.user_data.append(user_dict)
       
    def _authenticate(self):
       
        entered_accountNumber = int(input("Enter your account number : "))
        if self.generated_account_number == entered_accountNumber:

            print("\n")
            print("*********************************************************************************************")
            print("Your account number is matched. You have been successfully logined...")
            print("*********************************************************************************************")
        else:
            print("wrong input....")

    @abstractmethod
    def deposit(self):
        pass

    @abstractmethod
    def withdraw(self):
        pass

    def query_submission(self):
        number = 1122445590
        print("Do you have any query?")
        query = input().lower()
        if query in ['y', 'yes']:
            message = f"You can contact on this number: {number}"
            print(message)
        elif query in ['n', 'no']:
            print("Ok, have a nice day")
        else:
            print("No issue")

    def search_account(self):
        print("Forget your account number:")
        ans = input("Please enter your answer: ")

        if ans.lower() in ['y', 'yes']:
            info = int(input("Please enter your contact number: "))

            # Assume that we have contact_number in our user_dict
            if self.user_dict.get('contact_number') == info:
                print("Your account number is:", self.user_dict.get('account_number'))
            else:
                print("Invalid contact number.")
        else:
            print("Have a nice day.")

   

class Customer(Bank):

    def __init__(self, name, age, address,contact_number):
        super().__init__(name, age, address, contact_number)
  
     
    def deposit(self):
     
        amount = int(input("Enter the amount to deposit: "))

        if amount <= 0:
            raise Exception("value must be greater than 0 and -1")

        elif amount > 0:
            self.user_dict["updated_amount"]  = self.user_dict.get('original_amount') + amount   
            print("The updated amount is: " , self.user_dict.get('updated_amount'))
            print(f"Deposited {amount} successfully. Your new balance is {self.user_dict.get('updated_amount')}.")
        else:
            print("wrong input....")

    def withdraw(self):
        try:
            amount = int(input("Enter the amount you want to withdraw: "))
        except ValueError:
            print("Please enter a valid integer....")
            return
        if amount <= int(self.user_dict.get("updated_amount")):
            self.user_dict["updated_amount"] = self.user_dict.get("updated_amount") - amount
            print(f"Withdrawn {amount} successfully. Your new balance is {self.user_dict.get('updated_amount')}.")
        else:
            print("you can't withdraw money")

    def print_info(self):

        # print(f"Name: {self.user_dict.get('name', '')}\n")
        # print(f"Age: {self.user_dict.get('age', '')}\n")
        # print(f"Address: {self.user_dict.get('address', '')}\n")
        # print(f"Account number: {self.user_dict.get('account_number', '')}\n")
        # print(f"Original Amount: {self.user_dict.get('original_amount', '')}\n")
        # print(f"Updated Amount: {self.user_dict.get('updated_amount', '')}\n")

        print("\n")
        print("*********************************************************************************************************************************")
        print("\t Name" , "\t Age", "\t Adress", "\t AccountNo." , "\t OriginalAm.", "\t\t UpdatedAm.")
        print("\n")
        print("\t", self.user_dict.get('name', ''), self.user_dict.get("age", ''), "\t", self.user_dict.get("address", ''), "\t\t", self.user_dict.get("account_number", ''), "\t", self.user_dict.get("original_amount", ''), "\t\t\t", self.user_dict.get("updated_amount", ''))
        print("*********************************************************************************************************************************")
       

        file = open("store.txt", "w")
        file.write(f"Name: {self.user_dict.get('name', '')}\n")
        file.write(f"Age: {self.user_dict.get('age', '')}\n")
        file.write(f"Address: {self.user_dict.get('address', '')}\n")
        file.write(f"Account Number: {self.user_dict.get('account_number', '')}\n")
        file.write(f"Original Amount: {self.user_dict.get('original_amount', '')}\n")
        file.write(f"Updated Amount: {self.user_dict.get('updated_amount', '')}\n")
        file.close()

    # Switch-case function
    def menu_option(self, option):
        switch = {
            0: lambda: self._registration(self.name, self.age, self.address),
            1: self._authenticate,
            2: self.deposit,
            3: self.withdraw,
            4: self.print_info,
            5: self.query_submission,
            6:self.search_account,
            7: exit
            
        }
        selected_function = switch.get(option)
        if selected_function:
            selected_function()
        else:
            print("Invalid option.")



# Example Usage
obj = Customer("ankita", 21, "delhi", 0000000000)
while True:
    print("\n\t\t\t\t\t BANK MANAGEMENT SYSTEM")
    print("\t\t\t\t\t 0: Registration")
    print("\t\t\t\t\t 1. Authentication")
    print("\t\t\t\t\t 2. Deposit")
    print("\t\t\t\t\t 3. Withdraw")
    print("\t\t\t\t\t 4. Printing Info")
    print("\t\t\t\t\t 5. Query Submission")
    print("\t\t\t\t\t 6. Search account number")
    print("\t\t\t\t\t 7. exit")


    user_option = int(input("Enter your choice (0-7): "))
    obj.menu_option(user_option)

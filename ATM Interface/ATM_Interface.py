# Project Name - ATM Interface
# Developed By - Ajay Thakur (2016kuec2026@iiitkota.ac.in)
# Branch Name - Electronics and Communication Engineering
# Institute Name - Indian Institute of Information Technology Kota (An Institute of National Importance under an Act of Parliament)
# Submitted To -  OctaNet Software Services
# Project Link (GitHub) - https://github.com/ajaythakur3369/OctaNet-Software-Services-Internship-Project/blob/main/ATM%20Interface/ATM_Interface.py
# Project Link (Drive) - https://drive.google.com/drive/u/1/folders/1Zf1Ny8Ii9dNKQ5pItqNA-H1xhtpjc5sK 

# Project Summery - The ATMs in our cities are built on Python, as we have all seen them. It is a console-based application 
# with five different classes. In order to use the system, the user must enter his or her user ID and pin when it starts. 
# Once the details are entered successfully, ATM functionality is unlocked. As a result of the project, the following operations can 
# be performed: - 1. Transactions History 2. Withdraw 3. Deposit 4. Transfer 5. Quit

# Imported datetime module. It supplies classes to work with date and time 
import datetime

# Defined the class by the user
class User:

# Defined __init__(self) method within the class. It is used to initialize the attributes of an object as soon as the object is formed. 
# A default parameter, named 'self' is always passed in its argument. This self represents the object of the class itself.
    def __init__(self, user_id, pin):
     self.user_id = user_id
     self.pin = pin
     self.balance = 0
     self.transactions_history = []

    def get_transactions_histroy(self):
        return self.transactions_history
     
    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            self.transactions_history.append((datetime.datetime.now(), "withdraw", amount))
            return True
        else:
         return False
    
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.transactions_history.append((datetime.datetime.now(), "Deposit", amount))
            return True
        else:
         return False
    
    def transfer(self, to_user, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            to_user.balance += amount
            self.transactions_history.append((datetime.datetime.now(), "Transfer to User ID: " + to_user.user_id, amount))
            to_user.transactions_history.append((datetime.datetime.now(), "Transfer from User ID: " + self.user_id, amount))
            return True
        else:
            return False 
        
# Defined the class by the user     
class ATM:
    def __init__(self):
        self.users = {}
        
    def authenticate_user(self, user_id, pin):
        if user_id in self.users and self.users[user_id].pin == pin:
            return self.users [user_id]    
        else:
            return None
        
    def add_user(self, user):
        self.users[user.user_id] = user

# Define the main function
def main():
    atm = ATM()
    # User ID and PIN 
    Neel = User("Neel", "1234")            
    Yash = User("Yash", "5678")   
    
    atm.add_user(Neel)         
    atm.add_user(Yash)      
    
    while True:
        # Display the main menu
        print("Welcome to My ATM Interface")
        # Get the User's ID
        user_id = input(("Enter the User ID "))   
        # Get the User's PIN
        pin = input(("Enter the PIN "))   
        # Check if User ID and PIN are correct
        user = atm.authenticate_user(user_id, pin)
        
        if(user):
            print("Successfully Authenticated")
            while True:
                 # Display all the Choices
                 print("1. Transactions history")
                 print("2. Withdraw")
                 print("3. Deposit")
                 print("4. Transfer")
                 print("5. Quit")

                 # Get the User's Choice
                 choice = input("Enter your Choice: ")
                 # Check the User's Choice
                 if choice == "1": 
                    print("Transactions history: ")
                    for transactions in user.get_transactions_histroy():
                        print(transactions)

                 elif choice == "2":
                    # Withdrew Amount
                    amount = float(input("Enter the Withdrawal Amount: "))
                    if user.withdraw(amount):
                        print("Successfully Withdrew. Now your Balance is: ", user.balance)
                    else:
                        print("Invalid Amount or Insufficient Balance")
                 elif choice == "3":
                    # Deposited Amount
                    amount = float(input("Enter the Deposit Amount: "))
                    if user.deposit(amount):
                        print("Successfully Deposited. Now your Balance is: ", user.balance)
                        
                    else:
                        print("Invalid Amount. Please Enter the Valid Amount")

                 elif choice == "4":
                    # Recipient's User ID 
                    recipient_id = input("Enter the Recipient's User ID: ")
                    recipient = atm.authenticate_user(recipient_id, "2323")
                    if recipient:
                        amount = float(input("Enter the Transfer Amount: "))
                        if user.transfer(recipient, amount):
                            print("Successfully Transferred")
                        else:
                            print("Invalid Amount or Insufficient Balance")
                    else:
                        print("Recipient not found")        

                 elif choice == "5":
                    # Quit
                    print("Thank you for using the ATM!")
                    exit()

                 else:
                    print("Invalid Choice. Please Select a Valid Option")

        else:
            print("Authentication Failed. Please Check your User ID and PIN")

if __name__ == "__main__":
    # Call the main function
    main()
class BankAccount:
    
    account_number = ""
    account_holder_name = ""
    initial_balance = 0
    
    def set_account_details(self, account_number, account_holder_name, initial_balance=0):
        
        self.account_number = account_number
        self.account_holder_name = account_holder_name
        self.initial_balance = initial_balance
    
    def deposit(self, amount):
        self.initial_balance += amount
    
    def withdraw(self, amount):
        if( self.initial_balance - amount > 0 ):
            self.initial_balance -= amount
            
    def display_account_info(self):
        print("Account holder : " , self.account_holder_name)
        print("Account number : " , self.account_number)
        print("Balance : " , self.initial_balance)
        

bankacc = BankAccount()
bankacc.set_account_details("1113fjfFsbs783" , "Ali Ahmed", 5000)
bankacc.deposit(1500)
bankacc.withdraw(2000)
bankacc.display_account_info()

from datetime import datetime
from abc import ABC, abstractclassmethod

class AbstractAccount(ABC):
    def __init__(self, account_id, account_no, name, balance, open_date, pin, type="") -> None:
        self.__account_id = account_id
        self.__account_no = account_no
        self.__name = name
        self.__balance = balance
        self.__open_date = open_date
        self.__pin = pin
        self.__type = type
        self.__transaction_date = datetime.now().strftime("%Y%m%d%H%M%S")
        self.__loans = []

    def get_id(self):
        return self.__account_id

    def get_account_no(self):
        return self.__account_no

    def get_name(self):
        return self.__name
    
    def get_balance(self):
        return self.__balance
    
    def get_open_date(self):
        return self.__open_date
    
    def get_pin(self):
        return self.__pin
    
    def get_type(self):
        return self.__type
    
    def get_transaction_date(self):
        return self.__transaction_date

    @abstractclassmethod
    def initial_debit(self, amount, customer, bank):
        pass

    @abstractclassmethod
    def debit(self, amount, customer, bank):
        pass

    @abstractclassmethod
    def credit(self, amount, customer, bank):
        pass

    # @abstractclassmethod
    # def transfer(self, amount, customer, bank):
    #     pass

    @abstractclassmethod
    def close(self):
        pass

    @abstractclassmethod
    def check_and_close_account(self, customer, bank):
        pass

    @abstractclassmethod
    def generate_account_id(customer):
        pass

    @abstractclassmethod
    def generate_account_number(customer):
        pass

class Savings(AbstractAccount):
    def __init__(self, account_id, account_no, name, balance, open_date, pin) -> None:
        super().__init__(account_id, account_no, name, balance, open_date, pin, "Savings Account")
        self.__pin = pin
        self.__status = "Active"
        self.__transaction_counter = 0
        self.__debit_transaction_status = ""
        self.__credit_transaction_status = ""
        self.__interest_rate = 0.04
        self.__min_initial_deposit = 500.00
        self.__maintaining_balance = 2000.00
        self.__withdrawal_limit = 20000.00

    def get_type(self):
        return super().get_type()
    
    def get_id(self):
        return super().get_id()
    
    def get_account_no(self):
        return super().get_account_no()
    
    def get_name(self):
        return super().get_name()
    
    def get_balance(self):
        return super().get_balance()
    
    def get_open_date(self):
        return super().get_open_date()
    
    def get_pin(self):
        return super().get_pin()
    
    def set_status(self, status):
        self.__status = status

    def get_status(self):
        return self.__status
    
    def get_transaction_date(self):
        return super().get_transaction_date()
    
    def get_transaction_counter(self):
        return self.__transaction_counter

    def generate_transaction_id(self):
       transaction_counter = self.get_transaction_counter()
       transaction_counter += 1

       account_number = self.get_account_no()
       timestamp = self.get_transaction_date()
       transaction_id = f"{account_number}_{timestamp}_{transaction_counter}"

       return transaction_id
    
    def get_min_initial_deposit(self):
        return self.__min_initial_deposit
    
    def get_maintaining_balance(self):
        return self.__maintaining_balance
    
    def get_withdrawal_limit(self):
        return self.__withdrawal_limit
    
    def initial_debit(self, amount, customer, bank):
        try:
            amount = float(amount)  # Attempt to convert the input to a float
        except ValueError:
            print("[Debit: Transaction Failed. Invalid amount.]")
            return
        
        if amount > self.get_withdrawal_limit():
            print("[Debit: Transaction Failed. Exceeded withdrawal limit.]")
            return
        
        if self.get_balance() == 0 and amount < self.get_min_initial_deposit():
            print("[Debit: Transaction Failed. Initial deposit not met.]")
            return

        if customer in bank.get_users() and amount > 0:
            float(self.get_balance()) + amount
            self.__record_date = datetime.now()
            self.__debit_transaction_status = "Success"
            self.__debit_transaction_id = self.generate_transaction_id()
            self.__debit_transaction_amount = amount

            print(f"[Debit: Transaction {self.__debit_transaction_status}.]")
            print(f"{self.__debit_transaction_status} {self.__record_date} {self.__debit_transaction_id} {self.__debit_transaction_amount}")
        else:
            self.__debit_transaction_status = "Failed"
            print("[Debit: Transaction Failed.]")


    def debit(self, amount, customer, bank):
        try:
            amount = float(amount)  # Attempt to convert the input to a float
        except ValueError:
            print("[Debit: Transaction Failed. Invalid amount.]")
            return
        
        if amount > self.get_withdrawal_limit():
            print("[Debit: Transaction Failed. Exceeded withdrawal limit.]")
            return

        # Check if the initial deposit condition is met
        if self.get_balance() == 0 and amount < self.get_min_initial_deposit():
            print("[Debit: Transaction Failed. Initial deposit not met.]")
            return

        if customer in bank.get_users() and amount > 0:
            new_balance = float(self.get_balance()) + amount
            self.__total_interest = (float(self.get_balance()) + amount) * self.__interest_rate
            self._AbstractAccount__balance = new_balance - self.__total_interest
            self.__record_date = datetime.now()
            self.__debit_transaction_status = "Success"
            self.__debit_transaction_id = self.generate_transaction_id()
            self.__debit_transaction_amount = amount

            # print("[Debit: Transaction Success. Interest applied.]")
        else:
            self.__debit_transaction_status = "Failed"
            # print("[Debit: Transaction Failed.]")
    
    def credit(self, amount, customer, bank):
        amount = float(amount)
        balance = float(self.get_balance())
        
        if customer in bank.get_users() and balance > 0 and amount <= balance:
            current_balance = balance
            transaction_fee = 5.0
            new_balance = current_balance - (amount + transaction_fee)
            self._AbstractAccount__balance = new_balance
            self.__record_date = datetime.now()
            self.__credit_transaction_status = "Success"
            self.__credit_transaction_id = self.generate_transaction_id()
            self.__credit_transaction_amount = amount
            self.__transaction_fee = transaction_fee
       
            print("[Credit: Transaction Success.]")

        else:
            self.__credit_transaction_status = "Failed"
            print("[Credit: Transaction Failed.]")

    # def transfer(self, amount, customer, bank):
    #     pass

    def close(self, user, bank):
        if user in bank.get_users() and self.get_status() == "Active":
            self.set_status("Closed")
            print(f"[Closed the {self.get_name()} Account.]")
            
            user_accounts = user.get_account()
            if self in user_accounts:
                user_accounts.remove(self)

        else:
            print(f"[{self.get_name()} is not active.]")

    def check_and_close_account(self, customer, bank):
        if self.get_balance() == 0:
            self.close(customer, bank)

    
    def generate_account_id(customer):
        # Create the prefix using letters
        letters = 'ABCD'
        prefix_length = len(letters)
        
        # Calculate the number of accounts for zero-padding
        initial_id = len(customer.get_account())
        
        # Equals to 9 character id
        account_id = f"{letters}{str(initial_id).zfill(5 - prefix_length)}" 

        return account_id
    
    def generate_account_number(customer):
        initial_id = len(customer.get_account())
        account_no = str(initial_id).zfill(6)

        return account_no

class Checking(AbstractAccount):
    def __init__(self, account_id, account_no, name, balance, open_date, pin) -> None:
        super().__init__(account_id, account_no, name, balance, open_date, pin, "Checking Account")
        self.__pin = pin
        self.__status = "Active"
        self.__transaction_counter = 0
        self.__transaction_date = None
        self.__debit_transaction_status = "Not Processed"
        self.__credit_transaction_status = "Not Processed"
        self.__interest_rate = 0.01
        self.__min_initial_deposit = 25000.00
        self.__maintaining_balance = 2000.00
        self.__withdrawal_limit = 0

    def get_type(self):
        return super().get_type()

    def get_id(self):
        return super().get_id()
    
    def get_account_no(self):
        return super().get_account_no()
    
    def get_name(self):
        return super().get_name()
    
    def get_balance(self):
        return super().get_balance()
    
    def get_open_date(self):
        return super().get_open_date()
    
    def get_pin(self):
        return super().get_pin()
    
    def set_status(self, status):
        self.__status = status

    def get_status(self):
        return self.__status
    
    def get_transaction_date(self):
        return super().get_transaction_date()
    
    def get_transaction_counter(self):
        return self.__transaction_counter
    
    def generate_transaction_id(self):
       transaction_counter = self.get_transaction_counter()
       transaction_counter += 1

       account_number = self.get_account_no()
       timestamp = self.get_transaction_date
       transaction_id = f"{account_number}_{timestamp}_{transaction_counter}"

       return transaction_id
    
    def get_min_initial_deposit(self):
        return self.__min_initial_deposit
    
    def get_maintaining_balance(self):
        return self.__maintaining_balance
    
    def get_withdrawal_limit(self):
        return self.__withdrawal_limit
    
    def initial_debit(self, amount, customer, bank):
        try:
            amount = float(amount)  # Attempt to convert the input to a float
        except ValueError:
            print("[Debit: Transaction Failed. Invalid amount.]")
            return
        
        if amount > self.get_withdrawal_limit():
            pass
        
        if self.get_balance() == 0 and amount < self.get_min_initial_deposit():
            print("[Debit: Transaction Failed. Initial deposit not met.]")
            return

        if customer in bank.get_users() and amount > 0:
            float(self.get_balance()) + amount
            self.__record_date = datetime.now()
            self.__debit_transaction_status = "Success"
            self.__debit_transaction_id = self.generate_transaction_id()
            self.__debit_transaction_amount = amount

            print(f"[Debit: Transaction {self.__debit_transaction_status}.]")
            print(f"{self.__debit_transaction_status} {self.__record_date} {self.__debit_transaction_id} {self.__debit_transaction_amount}")
        else:
            self.__debit_transaction_status = "Failed"
            print("[Debit: Transaction Failed.]")


    def debit(self, amount, customer, bank):
        try:
            amount = float(amount)  # Attempt to convert the input to a float
        except ValueError:
            print("[Debit: Transaction Failed. Invalid amount.]")
            return
        
        if amount > self.get_withdrawal_limit():
            pass

        # Check if the initial deposit condition is met
        if self.get_balance() == 0 and amount < self.get_min_initial_deposit():
            print("[Debit: Transaction Failed. Initial deposit not met.]")
            return

        if customer in bank.get_users() and amount > 0:
            new_balance = float(self.get_balance()) + amount
            self.__total_interest = (float(self.get_balance()) + amount) * self.__interest_rate
            self._AbstractAccount__balance = new_balance - self.__total_interest
            self.__record_date = datetime.now()
            self.__debit_transaction_status = "Success"
            self.__debit_transaction_id = self.generate_transaction_id()
            self.__debit_transaction_amount = amount

            # print("[Debit: Transaction Success. Interest applied.]")
        else:
            self.__debit_transaction_status = "Failed"
            # print("[Debit: Transaction Failed.]")
            
    def credit(self, amount, customer, bank):
        amount = float(amount)
        balance = float(self.get_balance())
        
        if customer in bank.get_users() and balance > 0 and amount <= balance:
            current_balance = balance
            transaction_fee = 5.0
            new_balance = current_balance - (amount + transaction_fee)
            self._AbstractAccount__balance = new_balance
            self.__record_date = datetime.now()
            self.__credit_transaction_status = "Success"
            self.__credit_transaction_id = self.generate_transaction_id()
            self.__credit_transaction_amount = amount
            self.__transaction_fee = transaction_fee
       
            print("[Credit: Transaction Success.]")

        else:
            self.__credit_transaction_status = "Failed"
            print("[Credit: Transaction Failed.]")

        
    # def transfer(self, amount, customer, bank):
    #     pass

    def close(self, user, bank):
        if user in bank.get_users() and self.get_status() == "Active":
            self.set_status("Closed")
            print(f"[Closed the {self.get_name()} Account.]")
            
            user_accounts = user.get_account()
            if self in user_accounts:
                user_accounts.remove(self)

        else:
            print(f"[{self.get_name()} is not active.]")

    def check_and_close_account(self, customer, bank):
        if self.get_balance() == 0:
            self.close(customer, bank)

    def generate_account_id(customer):
        # Create the prefix using letters
        letters = 'ABCD'
        prefix_length = len(letters)
        
        # Calculate the number of accounts for zero-padding
        initial_id = len(customer.get_account())
        
        # Equals to 9 character id
        account_id = f"{letters}{str(initial_id).zfill(5 - prefix_length)}" 

        return account_id

    def generate_account_number(customer):
        initial_id = len(customer.get_account())
        account_no = str(initial_id).zfill(6)

        return account_no

class Joint(AbstractAccount):
    def __init__(self, account_id, account_no, name, balance, open_date, pin) -> None:
        super().__init__(account_id, account_no, name, balance, open_date, pin, "Joint Account")
        self.__pin = pin
        self.__status = "Active"
        self.__transaction_counter = 0
        self.__transaction_date = None
        self.__debit_transaction_status = "Not Processed"
        self.__credit_transaction_status = "Not Processed"
        self.__min_initial_deposit = 50000.00
        self.__maintaining_balance = None
        self.__withdrawal_limit = 0

    def get_type(self):
        return super().get_type()
    
    def get_id(self):
        return super().get_id()
    
    def get_account_no(self):
        return super().get_account_no()
    
    def get_name(self):
        return super().get_name()
    
    def get_balance(self):
        return super().get_balance()
    
    def get_open_date(self):
        return super().get_open_date()
    
    def get_pin(self):
        return super().get_pin()
    
    def set_status(self, status):
        self.__status = status

    def get_status(self):
        return self.__status
    
    def get_transaction_counter(self):
        return self.__transaction_counter

    def get_transaction_date(self):
        return super().get_transaction_date()
    
    def generate_transaction_id(self):
       transaction_counter = self.get_transaction_counter()
       transaction_counter += 1

       account_numbesr = self.get_account_no()
       timestamp = self.get_transaction_date
       transaction_id = f"{self.get_account_no()}_{timestamp}_{transaction_counter}"

       return transaction_id
    
    def get_min_initial_deposit(self):
        return self.__min_initial_deposit
    
    def get_maintaining_balance(self):
        return self.__maintaining_balance
    
    def get_withdrawal_limit(self):
        return self.__withdrawal_limit
    
    def initial_debit(self, amount, customer, bank):
        try:
            amount = float(amount)  # Attempt to convert the input to a float
        except ValueError:
            print("[Debit: Transaction Failed. Invalid amount.]")
            return
        
        if amount > self.get_withdrawal_limit():
            pass
        
        if self.get_balance() == 0 and amount < self.get_min_initial_deposit():
            print("[Debit: Transaction Failed. Initial deposit not met.]")
            return

        if customer in bank.get_users() and amount > 0:
            float(self.get_balance()) + amount
            self.__record_date = datetime.now()
            self.__debit_transaction_status = "Success"
            self.__debit_transaction_id = self.generate_transaction_id()
            self.__debit_transaction_amount = amount

            print(f"[Debit: Transaction {self.__debit_transaction_status}.]")
            print(f"{self.__debit_transaction_status} {self.__record_date} {self.__debit_transaction_id} {self.__debit_transaction_amount}")
        else:
            self.__debit_transaction_status = "Failed"
            print("[Debit: Transaction Failed.]")


    def debit(self, amount, customer, bank):
        try:
            amount = float(amount)  # Attempt to convert the input to a float
        except ValueError:
            print("[Debit: Transaction Failed. Invalid amount.]")
            return
        
        if amount > self.get_withdrawal_limit():
            pass

        # Check if the initial deposit condition is met
        if self.get_balance() == 0 and amount < self.get_min_initial_deposit():
            print("[Debit: Transaction Failed. Initial deposit not met.]")
            return

        if customer in bank.get_users() and amount > 0:
            new_balance = float(self.get_balance()) + amount
            self.__total_interest = (float(self.get_balance()) + amount) * self.__interest_rate
            self._AbstractAccount__balance = new_balance - self.__total_interest
            self.__record_date = datetime.now()
            self.__debit_transaction_status = "Success"
            self.__debit_transaction_id = self.generate_transaction_id()
            self.__debit_transaction_amount = amount

            # print("[Debit: Transaction Success. Interest applied.]")
        else:
            self.__debit_transaction_status = "Failed"
            # print("[Debit: Transaction Failed.]")      

    def credit(self, amount, customer, bank):
        amount = float(amount)
        balance = float(self.get_balance())

        if customer in bank.get_users() and balance > 0 and amount <= balance:
            current_balance = balance
            new_balance = current_balance - amount
            self._AbstractAccount__balance = new_balance
            self.__record_date = datetime.now()
            self.__credit_transaction_status = "Success"
            self.__credit_transaction_id = self.generate_transaction_id()
            self.__credit_transaction_amount = amount
            
            print("[Credit: Transaction Success.]")

        else:
            self.__credit_transaction_status = "Failed"
            print("[Credit: Transaction Failed.]")


    # def transfer(self, amount, customer, bank):
    #     pass

    def close(self, user, bank):
        if user in bank.get_users() and self.get_status() == "Active":
            self.set_status("Closed")
            print(f"[Closed the {self.get_name()} Account.]")
            
            user_accounts = user.get_account()
            if self in user_accounts:
                user_accounts.remove(self)

        else:
            print(f"[{self.get_name()} is not active.]")

    def check_and_close_account(self, customer, bank):
        if self.get_balance() == 0:
            self.close(customer, bank)

    def generate_account_id(customer):
        # Create the prefix using letters
        letters = 'ABCD'
        prefix_length = len(letters)
        
        # Calculate the number of accounts for zero-padding
        initial_id = len(customer.get_account())
        
        # Equals to 9 character id
        account_id = f"{letters}{str(initial_id).zfill(5 - prefix_length)}" 

        return account_id
    
    def generate_account_number(customer):
        initial_id = len(customer.get_account())
        account_no = str(initial_id).zfill(6)

        return account_no

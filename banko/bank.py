from abc import ABC, abstractclassmethod

class Bank(ABC):
    __customer_count = 0
    __users_count = 0
    __online_users_count = 0

    def __init__(self, brstn, name, location, type) -> None:
        self.__brstn = brstn
        self.__name = name
        self.__location = location
        self.__type = type
        self.__customers = []
        self.__accounts = [] 
        self.__users = []
        self.__online_users = []
        self.__offline_users = []

    def get_name(self):
        return self.__name
    
    def get_location(self):
        return self.__location

    def get_customers(self):
        return self.__customers
    
    def get_account(self):
        return self.__accounts
    
    def get_users(self):
        return self.__users
    
    def get_online_users(self):
        return self.__online_users
    
    def get_offline_users(self):
        return self.__offline_users

    @abstractclassmethod
    def add_customer(self, customer):
        pass

    @abstractclassmethod
    def add_user(self, user):
        pass

    @abstractclassmethod
    def add_online_user(self, user):
        pass

    @abstractclassmethod
    def remove_online_user(self, user):
        pass

class Main(Bank):
    def __init__(self, brstn, name, location) -> None:
        super().__init__(brstn, name, location, "main")

    def get_name(self):
        return super().get_name()
    
    def get_location(self):
        return super().get_location()
    
    def get_customers(self):
        return super().get_customers()
    
    def get_user(self):
        return super().get_users()
    
    def add_customer(self, customer):
        self.get_customers().append(customer)
        Bank._Bank__customer_count += 1

    def add_user(self, user):
        self.get_users().append(user)
        Bank._Bank__users_count += 1

    def add_online_user(self, user):
        user.online()
        self.get_online_users().append(user)
        Bank._Bank__online_users_count += 1
        print(self.get_online_users())
        if user in self.get_offline_users():
            self.get_offline_users().remove(user)

    def remove_online_user(self, user):
        if user in self.get_online_users():
            user.offline()
            self.get_online_users().remove(user)
            self.get_offline_users().append(user)
            Bank._Bank__online_users_count -= 1
            print(self.get_offline_users())

    def get_customers(self):
        return super().get_customers()
    
    def get_users(self):
        return super().get_users()
    
    def generate_user_id(self):
        initial_id = len(self.get_users())
        customer_id = str(initial_id).zfill(6)
        
        return customer_id

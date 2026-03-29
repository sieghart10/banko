from abc import ABC, abstractmethod

class Person(ABC):
    def __init__(self, first_name, last_name, gender, birthdate, address, role):
        self.__first_name = first_name
        self.__last_name = last_name
        self.__gender = gender
        self.__birthdate = birthdate
        self.__address = address
        self.__role = role
    
    @abstractmethod
    def get_first_name(self):
        return self.__first_name
    
    @abstractmethod
    def get_last_name(self):
        return self.__last_name
    
    @abstractmethod
    def get_gender(self):
        return self.__gender
    
    @abstractmethod
    def get_address(self):
        return self.__address
    
    @abstractmethod
    def get_birthdate(self):
        return self.__birthdate

class User(Person):
    def __init__(self, first_name, last_name, email, password, gender, birthdate, address, user_id, phone_no, account=None):
        super().__init__(first_name, last_name, gender, birthdate, address, "customer")
        self.__first_name = first_name
        self.__last_name = last_name
        self.__email = email
        self.__password = password
        self.__user_id = user_id
        self.__phone_no = phone_no
        #self.__valid_id = valid_id
        self.__account = account if account else []
        self.__state = OfflineState(self)

    def set_age(self, age: int):
        self.__age = age
 
    def get_first_name(self):
        return self.__first_name

    def get_last_name(self):
        return self.__last_name
    
    def get_password(self):
        return self.__password
    
    def get_gender(self):
        return super().get_gender()
    
    def get_birthdate(self):
        return super().get_birthdate()
    
    def get_address(self):
        return super().get_address()
    
    def get_email(self):
        return self.__email

    def get_id(self):
        return self.__user_id

    def set_phone(self, phone_no: str):
        self.__phone_no = phone_no

    def get_phone(self):
        return self.__phone_no
    
    def get_state(self):
        return self.__state

    def changeState(self, state):
        self.__state = state

    def online(self):
        self.get_state().online()

    def offline(self):
        self.get_state().offline()

    # def set_valid_id(self, valid_id: str):
    #     self.__valid_id = valid_id

    # def get_valid_id(self):
    #     return self.__valid_id

    def get_account(self):
        return self.__account

    def add_account(self, account):
        self.get_account().append(account)


class UserState(ABC):

    @abstractmethod
    def online(self):
        pass

    @abstractmethod
    def offline(self):
        pass

class OnlineState(UserState):
    def __init__(self, user) -> None:
        super().__init__()
        self.__user = user

    def online(self):
        print("[OnlineState] Already Online!")

    def offline(self):
        self.__user.changeState(OfflineState(self.__user))
        print("[OnlineState] Going offline...")

class OfflineState(UserState):
    def __init__(self, user) -> None:
        super().__init__()
        self.__user = user

    def online(self):
        self.__user.changeState(OnlineState(self.__user))
        print("[OfflineState] Going Online...")

    def offline(self):
        print("[OfflineState] Already Offline!")

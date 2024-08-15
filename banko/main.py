import tkinter as tk
import tkinter.messagebox as messagebox
import os
from datetime import datetime
from account import Savings, Checking, Joint
from person import User
from bank import Main

class WidgetBuilder:
    def __init__(self, master):
        self.master = master
        self.frames =  []

    def create_window(self, title="", geometry="", bg="", resizable=None):
        window = tk.Toplevel(self.master, bg=bg)
        window.title(title)
        window.geometry(geometry)
        if resizable == "yes":
            window.resizable(True, True)
        elif resizable == "x":
            window.resizable(True, False)
        elif resizable == "y":
            window.resizable(False, True)
        else:
            window.resizable(False, False)
        return window
    
    def create_frame(self, parent, bg, width, height, relief):
        frame = tk.Frame(parent, width=width, height=height, relief=relief)    
        frame.config(bg=bg)
        self.frames.append(frame)
        #print(self.frames)
        return frame

    def create_label(self, parent, text, font, bg):
        label = tk.Label(parent, text=text, font=font, bg=bg)
        return label

    def create_button(self, parent, text, width, relief, bg, command):
        button = tk.Button(parent, text=text, width=width, relief=relief, bg=bg, command=command)
        return button
    
    def create_entry(self, parent, show, width):
        entry = tk.Entry(parent, show=show, width=width)
        return entry
    
    def create_radio_button(self, parent, text, variable, value, bg):
        radio = tk.Radiobutton(parent, text=text, variable=variable, value=value, bg=bg)
        return radio
    
    def show_message_box(self, type="", title="", text="", on_yes_command=None):
        result = None
        
        if type == "showinfo":
            result = messagebox.showinfo(title, text)

        elif type == "showwarning":
            result = messagebox.showwarning(title, text)

        elif type == "showerror":
            result = messagebox.showerror(title, text)

        elif type == "askquestion":
            result = messagebox.askquestion(title, text)

        elif type == "askyesno":
            result = messagebox.askyesno(title, text)

        elif type == "askokcancel":
            result = messagebox.askokcancel(title, text)

        if on_yes_command == None:
            pass
        else:
            if result:
                on_yes_command()
            else:
                pass
            
    def destroy_frame(self):
        for frame in self.frames:
            frame.destroy()

    def destroy_all_frames(self):
        for frame in self.frames:
            frame = self.frames.pop(-1)
            frame.forget()
        self.frames = []

class Command:
    def __init__(self, gui_facade):
        self.gui_facade = gui_facade

    def execute(self):
        pass

class LogInCommand(Command):
    def execute(self, email, password):
        self.gui_facade.display_log_in_menu(email, password)

class ForgotPasswordCommand(Command):
    def execute(self):
        self.gui_facade.display_forgot_menu()

class CreateMainMenuCommand(Command):
    def execute(self):
        self.gui_facade.create_main_menu()

class CreateAccountCommand(Command):
    def execute(self):
        self.gui_facade.create_new_account_menu()

class CreateAccountType(Command):
    def execute(self):
        self.gui_facade.choose_account_type()

class ChooseAccountCommand(Command):
    def execute(self, account_type):
        self.gui_facade.chosen_account_type(account_type)

class  ConfirmWindowCommand(Command):
    def execute(self):
        self.gui_facade.confirm_window()

class DisableWindowCommand(Command):
    def execute(self, window):
        self.gui_facade.disable_window(window)

class EnableWindowCommand(Command):
    def execute(self, window):
        self.gui_facade.enable_window(window)

class CreatePinCommand(Command):
    def execute(self):
        self.gui_facade.create_pin_frame()

class NavigateBackCommand(Command):
    def execute(self, command):
        self.gui_facade.navigate_back(command)

class DisplayMyAccount(Command):
    def execute(self):
        self.gui_facade.display_my_accounts()

class ShowAccountInfo(Command):
    def execute(self, account_type):
        self.gui_facade.show_account_info(account_type)

class ShowDebitFrame(Command):
    def execute(self, account_type):
        self.gui_facade.show_debit_frame(account_type)

class ShowCreditFrame(Command):
    def execute(self, account_type):
        self.gui_facade.show_credit_frame(account_type)
    
class GUIFacade:
    def __init__(self, builder, master):
        self.builder = builder
        self.master = master
        self.main_frame = None
        self.new_account_window = None
        self.bank = Main("010531064", "BanKo", "Pandi, Bulacan")

        self.log_in_command = LogInCommand(self)
        self.forgot_password_command = ForgotPasswordCommand(self)
        self.create_main_menu_command = CreateMainMenuCommand(self)
        self.create_account_command = CreateAccountCommand(self)
        self.create_account_type_command = CreateAccountType(self)
        self.choose_account_command = ChooseAccountCommand(self)
        self.confirm_window_command = ConfirmWindowCommand(self)
        self.disable_window_command = DisableWindowCommand(self)
        self.enable_window_command = EnableWindowCommand(self)
        self.create_pin_frame_command = CreatePinCommand(self)
        self.navigate_back_command = NavigateBackCommand(self)
        self.display_my_accounts_command = DisplayMyAccount(self)
        self.show_account_info_command = ShowAccountInfo(self)
        self.show_debit_frame_command = ShowDebitFrame(self)
        self.show_credit_frame_command = ShowCreditFrame(self)


    def create_main_menu(self):
        if len(self.bank.get_online_users()) == 0:
            self.clear_frame()
            self.main_frame = self.builder.create_frame(self.master, bg="#FFA500", width=0, height=0, relief=None)
            self.main_frame.pack(fill=tk.BOTH, expand=True)
            self.bank_name = self.builder.create_label(self.main_frame, f"{self.bank.get_name()}", ("Eras Demi ITC", 24), bg="#FFA500")
            self.bank_name.place(x=25, y=100, anchor= "nw")
            self.bank_tagline = self.builder.create_label(self.main_frame, "Have the best banking experience with banKo.", ("Arial", 10),bg="#FFA500")
            self.bank_tagline.place(x=25, y=150, anchor= "nw")

            self.second_frame = self.builder.create_frame(self.main_frame, bg="#F4CE14", width=320, height=370, relief=tk.RAISED)
            self.second_frame.place(x=350, y=15)

            self.email_label = self.builder.create_label(self.second_frame, "Email: ", ("Eras Demi ITC", 12), bg="#F4CE14")
            self.email_label.place(x=20, y=50)
            self.email_entry = self.builder.create_entry(self.second_frame, show="", width=30)
            self.email_entry.place(x=120, y=52)
            
            self.password_label = self.builder.create_label(self.second_frame, "Passowrd: ", ("Eras Demi ITC", 12), bg="#F4CE14")
            self.password_label.place(x=20, y=80)
            self.password_entry = self.builder.create_entry(self.second_frame, show="•", width=30)
            self.password_entry.place(x=120, y=83)

            self.login_button  = self.builder.create_button(self.second_frame, "Log In", width=39, relief=tk.GROOVE, bg="#9ADE7B", command=lambda:self.log_in_command.execute(self.email_entry.get(), self.password_entry.get()))
            self.login_button.place(x=20, y=120)
            self.forgot_button  = self.builder.create_button(self.second_frame, "Forgot password?", width=39, relief=tk.FLAT, bg="#F4CE14", command=lambda:self.forgot_password_command.execute())
            self.forgot_button.place(x=20, y=150)
            self.create_account_button  = self.builder.create_button(self.second_frame, "Create new account", width=39, relief=tk.SOLID, bg="crimson", command=lambda:self.create_account_command.execute())
            self.create_account_button.place(x=20, y=250)

        else:
            self.display_user_menu()

    def create_new_account_menu(self):
        self.clear_frame()
        self.new_account_window = self.builder.create_frame(self.master, bg="#FFA500", width=0, height=0, relief=None)
        self.new_account_window.pack(fill=tk.BOTH, expand=True)

        self.window_title = self.builder.create_label(self.new_account_window, "Sign Up", ("Eras Demi ITC", 24), bg="#FFA500")
        self.window_title.place(x=15, y=20, anchor= "nw")
        self.window_subtitle = self.builder.create_label(self.new_account_window, "Create new account quick and easy.", ("Arial", 10),bg="#FFA500")
        self.window_subtitle.place(x=15, y=60, anchor= "nw")
        
        self.first_name = self.builder.create_label(self.new_account_window, "First Name: ", ("Eras Demi ITC", 12), bg="#FFA500")
        self.first_name.place(x=15, y=110)
        self.first_name_entry = self.builder.create_entry(self.new_account_window, show="", width=30)
        self.first_name_entry.place(x=120, y=113)
        
        self.last_name = self.builder.create_label(self.new_account_window, "Last Name: ", ("Eras Demi ITC", 12), bg="#FFA500")
        self.last_name.place(x=15, y=140)
        self.last_name_entry = self.builder.create_entry(self.new_account_window, show="", width=30)
        self.last_name_entry.place(x=120, y=143)
        
        self.email_label = self.builder.create_label(self.new_account_window, "Email: ", ("Eras Demi ITC", 12), bg="#FFA500")
        self.email_label.place(x=15, y=170)
        self.email_entry = self.builder.create_entry(self.new_account_window, show="", width=30)
        self.email_entry.place(x=120, y=173)

        self.password_label = self.builder.create_label(self.new_account_window, "Passowrd: ", ("Eras Demi ITC", 12), bg="#FFA500")
        self.password_label.place(x=15, y=200)
        self.password_entry = self.builder.create_entry(self.new_account_window, show="•", width=30)
        self.password_entry.place(x=120, y=203)


        self.gender_label = self.builder.create_label(self.new_account_window, "Gender:", ("Eras Demi ITC", 12), bg="#FFA500")
        self.gender_label.place(x=15, y=230)
        genders = ["Male", "Female"]
        self.gender_var = tk.StringVar()
        self.gender_var.set("Male")
        for gender_no,  gender_type in enumerate(genders, start=1):
            self.gender_radio = self.builder.create_radio_button(self.new_account_window, text=f"{gender_type}", variable=self.gender_var, value=f"{gender_type}", bg="#FFA500")
            self.gender_radio.place(x=116 + (gender_no - 1) *90, y=233)

        self.birthdate_label = self.builder.create_label(self.new_account_window, "Birthdate (mm/dd/yyyy):", ("Eras Demi ITC", 12), bg="#FFA500")
        self.birthdate_label.place(x=15, y=260)
        self.day_entry = self.builder.create_entry(self.new_account_window, show="", width=3)
        self.day_entry.place(x=250, y=263)
        self.month_entry = self.builder.create_entry(self.new_account_window, show="", width=3)
        self.month_entry.place(x=280, y=263)
        self.year_entry = self.builder.create_entry(self.new_account_window, show="", width=5)
        self.year_entry.place(x=310, y=263)

        self.address_label = self.builder.create_label(self.new_account_window, "Address: ", ("Eras Demi ITC", 12), bg="#FFA500")
        self.address_label.place(x=15, y=290)
        self.barangay_entry = self.builder.create_entry(self.new_account_window, show="", width=12)
        self.barangay_entry.place(x=120, y=293)
        self.city_entry = self.builder.create_entry(self.new_account_window, show="", width=12)
        self.city_entry.place(x=200, y=293)
        self.province_entry = self.builder.create_entry(self.new_account_window, show="", width=12)
        self.province_entry.place(x=280, y=293)

        self.phone_no_label = self.builder.create_label(self.new_account_window, "Phone no. : ", ("Eras Demi ITC", 12), bg="#FFA500")
        self.phone_no_label.place(x=15, y=320)
        self.phone_no_entry = self.builder.create_entry(self.new_account_window, show="", width=12)
        self.phone_no_entry.place(x=120, y=323)

        def get_user_info():
            first_name = self.first_name_entry.get()
            last_name = self.last_name_entry.get()
            email = self.email_entry.get()
            password = self.password_entry.get()
            gender = self.gender_var.get()
            birthdate = f"{self.day_entry.get()} - " + f"{self.month_entry.get()} - " + f"{self.year_entry.get()}"
            address  = f"{self.barangay_entry.get()}, " + f"{self.city_entry.get()}, " + f"{self.province_entry.get()}"
            user_id = self.bank.generate_user_id()
            phone_no = self.phone_no_entry.get()

            self.new_user = User(first_name, last_name, email, password, gender, birthdate, address, user_id, phone_no, None)
            self.bank.add_user(self.new_user)
            self.bank.add_online_user(self.new_user)

        def confirm_user_info():
            birthdate = f"{self.day_entry.get()} - " + f"{self.month_entry.get()} - " + f"{self.year_entry.get()}"
            address  = f"{self.barangay_entry.get()}, " + f"{self.city_entry.get()}, " + f"{self.province_entry.get()}"
            user_info = f"First Name: {self.first_name_entry.get()}\nLast Name: {self.last_name_entry.get()}\nEmail: {self.email_entry.get()}\nGender: {self.gender_var.get()}\nBirthdate: {birthdate}\nAddress: {address}\nPhone Number: {self.phone_no_entry.get()}"
            self.builder.show_message_box("askyesno", "User Information", f"{user_info[:300]}...\n\nConfirm user information?", on_yes_command=lambda:[get_user_info(), self.create_account_type_command.execute()])

        self.submit_button = self.builder.create_button(self.new_account_window, "Sign Up", width=30, relief=tk.SOLID, bg="#9ADE7B", command=confirm_user_info)
        self.submit_button.place(x=460, y=360)

        self.back_button = self.builder.create_button(self.new_account_window, "<--", width=10, relief=tk.SOLID, bg="#FFA500", command=lambda:[self.navigate_back_command.execute(self.create_main_menu)])
        self.back_button.place(x=600, y=20)


    def choose_account_type(self):
        self.clear_frame()
        self.new_account_window = self.builder.create_frame(self.master, bg="#FFA500", width=0, height=0, relief=None)
        self.new_account_window.pack(fill=tk.BOTH, expand=True)
        self.frame_title = self.builder.create_label(self.new_account_window, "Choose Account", ("Eras Demi ITC", 24), bg="#FFA500")
        self.frame_title.place(x=210, y=20, anchor="nw")

        available_accounts = [Savings, Checking, Joint]
        customer_accounts = []
        available_account_types = []

        ### default wala pang accoount yung new_user then kapag gumawa na
        ### iaapend yung NAME ng account na nagawa ng user sa customer_accounts list ###
        for account in self.new_user.get_account():
                customer_accounts.append(account.get_name())

        ### kapag yung NAME ng account sa available_accounts is wala sa customer_accounts list iaapend nmn yung account_type sa available_account_types list ###
        for account_type in available_accounts:
                if account_type.__name__ not in customer_accounts:
                    available_account_types.append(account_type)

        for account_no, available_account in enumerate(available_account_types, start=1):
                self.account_button = self.builder.create_button(self.new_account_window, f"{available_account.__name__} Account", width=30, relief=tk.SOLID, bg="#9ADE7B", command=lambda account=available_account.__name__: self.choose_account_command.execute(account))
                self.account_button.place(x=230, y=100 + (account_no - 1) * 80, anchor="nw")
                #print(f"{account_no}")

        if len(available_account_types) == 0:
            self.builder.show_message_box("showerror", "Error", "No more available accounts left", on_yes_command=self.navigate_back_command.execute(self.create_main_menu))


    def chosen_account_type(self, account_type):
        self.clear_frame()
        self.new_account_window = self.builder.create_frame(self.master, bg="#FFA500", width=0, height=0, relief=None)
        self.new_account_window.pack(fill=tk.BOTH, expand=True)
        self.window_title = self.builder.create_label(self.new_account_window, f"{account_type} Account", ("Eras Demi ITC", 24), bg="#FFA500")
        self.window_title.place(x=15, y=20, anchor= "nw")

        self.initial_deposit = self.builder.create_label(self.new_account_window, "Initial Deposit:  ₱", ("Eras Demi ITC", 12), bg="#FFA500")
        self.initial_deposit.place(x=15, y=110)
        self.initial_deposit_entry = self.builder.create_entry(self.new_account_window, show="", width=30)
        self.initial_deposit_entry.place(x=150, y=113)
        

        self.confirm_button = self.builder.create_button(self.new_account_window, "Confirm", width=30, relief=tk.SOLID, bg="#9ADE7B", command=lambda: self.builder.show_message_box("askokcancel", "Confirmation", f"Confrim initial deposit of ₱{self.initial_deposit_entry.get()}?", on_yes_command=self.create_pin_frame_command.execute))
        self.confirm_button.place(x=460, y=360)

        self.back_button = self.builder.create_button(self.new_account_window, "<--", width=10, relief=tk.SOLID, bg="#FFA500", command=lambda:self.navigate_back_command.execute(self.choose_account_type))
        self.back_button.place(x=600, y=20)

        if account_type == "Savings":
            print("Savings Account selected")
            self.account_type = Savings

        elif account_type == "Checking":
            print("Checking Account selected")
            self.account_type = Checking

        elif account_type == "Joint":
            print("Joint Account selected")
            self.account_type = Joint

        return account_type
    
    def create_pin_frame(self):
        def get_account_info():
            pin_value = self.pin_entry.get()
            re_pin_value = self.pin_reentry.get()

            if len(pin_value) == 4 and pin_value.isdigit() and pin_value == re_pin_value:
                name = self.account_type.__name__
                open_date = datetime.now().strftime("%m-%d-%Y | %H:%M:%S")
                account_id = self.account_type.generate_account_id(self.new_user)
                account_no = self.account_type.generate_account_number(self.new_user)
                initial_deposit = self.initial_deposit_entry.get()

                self.new_account = self.account_type(account_id, account_no, name, initial_deposit, open_date, pin_value)
                self.new_account.initial_debit(initial_deposit, self.new_user, self.bank)
                self.new_user.add_account(self.new_account)

                self.pin_window.destroy()
                self.destroy_all_frames()
                self.create_main_menu()

            else:
                self.builder.show_message_box("showerror", "Confirm PIN", "PIN Does not match the requirements. Please try again.", on_yes_command=None)

        self.pin_window = self.builder.create_window(title="Setup PIN", geometry="250x250", bg="#FFA500", resizable="no")
        self.disable_window_command.execute(self.pin_window)
        self.window_label = self.builder.create_label(self.pin_window, "SETUP YOUR PIN", ("Eras Demi ITC", 12), bg="#FFA500")
        self.window_label.place(x=60, y=20, anchor="nw")

        self.pin_entry = self.builder.create_entry(self.pin_window, show="•", width=18)
        self.pin_entry.place(x=65, y=83)

        self.pin_reentry = self.builder.create_entry(self.pin_window, show="•", width=18)
        self.pin_reentry.place(x=65, y=123)

        self.confirm_button = self.builder.create_button(self.pin_window, "Confirm", width=10, relief=tk.SOLID, bg="#9ADE7B", command=get_account_info)
        self.confirm_button.place(x=80, y=200)

        self.pin_label = self.builder.create_label(self.pin_window, "re-enter PIN", ("Eras Light ITC", 10), bg="#FFA500")
        self.pin_label.place(x=85, y=150, anchor="nw")

    def display_user_menu(self):
        self.clear_frame()
        self.main_frame = self.builder.create_frame(self.master, bg="#FFA500", width=0, height=0, relief=None)
        self.main_frame.pack(fill=tk.BOTH, expand=True)
        self.bank_name = self.builder.create_label(self.main_frame, f"{self.bank.get_name()} |", ("Eras Demi ITC", 24), bg="#FFA500")
        self.bank_name.place(x=25, y=25, anchor= "nw")
        self.bank_location = self.builder.create_label(self.main_frame, f"{self.bank.get_location()}", ("Eras Light ITC", 18), bg="#FFA500")
        self.bank_location.place(x=150, y=31, anchor= "nw")
        self.open_new_account_button = self.builder.create_button(self.main_frame, "Open new account", width=30, relief=tk.SOLID, bg="#9ADE7B", command=lambda:self.create_account_type_command.execute())
        self.open_new_account_button.place(x=75, y=150)
        self.my_accounts_button = self.builder.create_button(self.main_frame, "My Accounts", width=30, relief=tk.SOLID, bg="#9ADE7B", command=lambda:self.display_my_accounts_command.execute())
        self.my_accounts_button.place(x=75, y=200)

        self.second_frame = self.builder.create_frame(self.main_frame, bg="#F4CE14", width=320, height=370, relief=tk.RAISED)
        self.second_frame.place(x=350, y=15)

        def log_out():
            if self.new_user: # check if the new_user object is not None
                self.bank.remove_online_user(self.new_user)
                self.main_frame.destroy()
                #self.second_frame.destroy()
                self.navigate_back(command=self.create_main_menu_command.execute)

        for user in self.bank.get_users():
            self.profile_label = self.builder.create_label(self.second_frame, "Profile", ("Eras Demi ITC", 24), bg="#F4CE14")
            self.profile_label.place(x=15, y=10)

            user_state = "Online" if user.get_state().__class__.__name__ == "OnlineState" else "Offline"

            self.status_label = self.builder.create_label(self.second_frame, f"Status  |", ("Eras Demi ITC", 12), bg="#F4CE14")
            self.status_label.place(x=180, y=20)
            self.state_label = self.builder.create_label(self.second_frame, f"{user_state}", ("Arial", 12), bg="#9ADE7B")
            self.state_label.place(x=250, y=20)

            self.id_label = self.builder.create_label(self.second_frame, "User ID |", ("Eras Demi ITC", 12), bg="#F4CE14")
            self.id_label.place(x=180, y=50)
            self.customer_id_label = self.builder.create_label(self.second_frame, f"{user.get_id()}", ("Arial", 12), bg="#F4CE14")
            self.customer_id_label.place(x=250, y=50)

            self.name_label = self.builder.create_label(self.second_frame, f"Name: {user.get_first_name()} {user.get_last_name()}", ("Eras Demi ITC", 12), bg="#F4CE14")
            self.name_label.place(x=20, y=80)
            self.gender_label = self.builder.create_label(self.second_frame, f"Gender: {user.get_gender()}", ("Eras Demi ITC", 12), bg="#F4CE14")
            self.gender_label.place(x=20, y=110)
            self.birthdate_label = self.builder.create_label(self.second_frame, f"Birthdate: {user.get_birthdate()}", ("Eras Demi ITC", 12), bg="#F4CE14")
            self.birthdate_label.place(x=20, y=140)
            self.address_label = self.builder.create_label(self.second_frame, f"Address: {user.get_address()}", ("Eras Demi ITC", 12), bg="#F4CE14")
            self.address_label.place(x=20, y=170)
            self.phone_label = self.builder.create_label(self.second_frame, f"Phone Number: {user.get_phone()}", ("Eras Demi ITC", 12), bg="#F4CE14")
            self.phone_label.place(x=20, y=200)

            self.log_out_button = self.builder.create_button(self.second_frame, "Log Out", width=8, relief=tk.SOLID, bg="crimson", command=log_out)
            self.log_out_button.place(x=240, y=330)

    def display_my_accounts(self):
        self.clear_frame()
        self.new_account_window = self.builder.create_frame(self.master, bg="#FFA500", width=0, height=0, relief=None)
        self.new_account_window.pack(fill=tk.BOTH, expand=True)
        self.frame_title = self.builder.create_label(self.new_account_window, "My Accounts", ("Eras Demi ITC", 24), bg="#FFA500")
        self.frame_title.place(x=25, y=25, anchor= "nw")

        user_accounts = self.new_user.get_account()

        if not user_accounts:
            self.no_accounts_label = self.builder.create_label(self.new_account_window, "No accounts found.", ("Eras Demi ITC", 16), bg="#FFA500")
            self.no_accounts_label.place(x=30, y=80, anchor="nw")
        
        else:
            for account_no, account_type in enumerate(user_accounts, start=1):
                self.account_no_label = self.builder.create_label(self.new_account_window, f"{account_no}.", ("Eras Demi ITC", 16), bg="#FFA500")
                self.account_no_label.place(x=30, y=120 + (account_no - 1) * 60, anchor="nw")
                self.account_type_button = self.builder.create_button(self.new_account_window, f"{account_type.get_name()} Account", width=30, relief=tk.SOLID, bg="#9ADE7B", command=lambda account=account_type: self.show_account_info_command.execute(account))
                self.account_type_button.place(x=75, y=120 + (account_no - 1) * 60, anchor="nw")

        self.back_button = self.builder.create_button(self.new_account_window, "<--", width=10, relief=tk.SOLID, bg="#FFA500", command=lambda:[self.navigate_back_command.execute(self.create_main_menu)])
        self.back_button.place(x=600, y=20)

    def show_account_info(self, account_type):
        self.clear_frame()
        self.new_account_window = self.builder.create_frame(self.master, bg="#FFA500", width=0, height=0, relief=None)
        self.new_account_window.pack(fill=tk.BOTH, expand=True)
        self.frame_title = self.builder.create_label(self.new_account_window, f"{account_type.get_name()} Account", ("Eras Demi ITC", 24), bg="#FFA500")
        self.frame_title.place(x=25, y=25, anchor= "nw")
        self.back_button = self.builder.create_button(self.new_account_window, "<--", width=10, relief=tk.SOLID, bg="#FFA500", command=lambda:self.navigate_back_command.execute(self.display_my_accounts))
        self.back_button.place(x=600, y=20)

        self.account_no_label = self.builder.create_label(self.new_account_window, f"Account No. :  {account_type.get_account_no()}", ("Eras Demi ITC", 12), bg="#FFA500")
        self.account_no_label.place(x=25, y=110)
        self.account_id_label = self.builder.create_label(self.new_account_window, f"Account ID: {account_type.get_id()}", ("Eras Demi ITC", 12), bg="#FFA500")
        self.account_id_label.place(x=25, y=140)
        self.open_date_label = self.builder.create_label(self.new_account_window, f"Open Date:  {account_type.get_open_date()}", ("Eras Demi ITC", 12), bg="#FFA500")
        self.open_date_label.place(x=25, y=170)
        self.balance_label = self.builder.create_label(self.new_account_window, f"Balance:  {account_type.get_balance()}", ("Eras Demi ITC", 18), bg="#FFA500")
        self.balance_label.place(x=25, y=220)

        def close_account():
            account_type.close(self.new_user, self.bank)
            self.create_main_menu_command.execute()

        self.second_frame = self.builder.create_frame(self.new_account_window, bg="#F4CE14", width=320, height=250, relief=tk.RAISED)
        self.second_frame.place(x=350, y=80)
        self.debit_button = self.builder.create_button(self.second_frame, "Debit", width=30, relief=tk.SOLID, bg="#9ADE7B", command=lambda account=account_type: self.show_debit_frame_command.execute(account))
        self.debit_button.place(x=50, y=50)
        self.credit_button = self.builder.create_button(self.second_frame, "Credit", width=30, relief=tk.SOLID, bg="#9ADE7B", command=lambda account=account_type: self.show_credit_frame_command.execute(account))
        self.credit_button.place(x=50, y=100)
        self.close_button = self.builder.create_button(self.second_frame, "Close Account", width=30, relief=tk.SOLID, bg="#9ADE7B", command=close_account)
        self.close_button.place(x=50, y=150)

    def show_debit_frame(self, account_type):
        self.clear_frame()
        self.new_account_window = self.builder.create_frame(self.master, bg="#FFA500", width=0, height=0, relief=None)
        self.new_account_window.pack(fill=tk.BOTH, expand=True)
        self.window_title = self.builder.create_label(self.new_account_window, "Debit", ("Eras Demi ITC", 24), bg="#FFA500")
        self.window_title.place(x=15, y=20, anchor= "nw")
        self.account_title = self.builder.create_label(self.new_account_window, f"{account_type.get_name()} Account", ("Eras Demi ITC", 24), bg="#FFA500")
        self.account_title.place(x=220, y=20, anchor= "nw")
        self.balance_label = self.builder.create_label(self.new_account_window, f"Balance: ₱{account_type.get_balance()}", ("Arial", 16), bg="#FFA500")
        self.balance_label.place(x=270, y=60, anchor= "nw")
        self.deposit_label = self.builder.create_label(self.new_account_window, f"Deposit:    ₱", ("Eras Demi ITC", 12), bg="#FFA500")
        self.deposit_label.place(x=180, y=200)
        self.deposit_entry = self.builder.create_entry(self.new_account_window, show="", width=30)
        self.deposit_entry.place(x=280, y=203)
        self.pin_label = self.builder.create_label(self.new_account_window, f"PIN: ", ("Eras Demi ITC", 12), bg="#FFA500")
        self.pin_label.place(x=250, y=250)
        self.pin_entry = self.builder.create_entry(self.new_account_window, show="", width=16)
        self.pin_entry.place(x=320, y=253)

        def do_transaction():
            pin_value = self.pin_entry.get()

            if pin_value == self.new_account.get_pin():
                deposit = self.deposit_entry.get()
                self.new_account.debit(deposit, self.new_user, self.bank)
                print(f"{self.new_account.get_balance()}")
                self.create_main_menu_command.execute()

            else:
                self.builder.show_message_box("showerror", "Transaction Failed", "Wrong PIN. Please try again.", on_yes_command=None)
        
        self.confirm_button = self.builder.create_button(self.new_account_window, "Confirm", width=30, relief=tk.SOLID, bg="#9ADE7B", command=lambda: self.builder.show_message_box("askokcancel", "Confirmation", f"Confrim deposit amount of ₱{self.deposit_entry.get()}?", on_yes_command=do_transaction))
        self.confirm_button.place(x=460, y=360)

        self.back_button = self.builder.create_button(self.new_account_window, "<--", width=10, relief=tk.SOLID, bg="#FFA500", command=lambda:self.navigate_back_command.execute(command=lambda account=account_type: self.show_account_info(account)))
        self.back_button.place(x=600, y=20)

    def show_credit_frame(self, account_type):
        self.clear_frame()
        self.new_account_window = self.builder.create_frame(self.master, bg="#FFA500", width=0, height=0, relief=None)
        self.new_account_window.pack(fill=tk.BOTH, expand=True)
        self.window_title = self.builder.create_label(self.new_account_window, "Credit", ("Eras Demi ITC", 24), bg="#FFA500")
        self.window_title.place(x=15, y=20, anchor= "nw")
        self.account_title = self.builder.create_label(self.new_account_window, f"{account_type.get_name()} Account", ("Eras Demi ITC", 24), bg="#FFA500")
        self.account_title.place(x=220, y=20, anchor= "nw")
        self.balance_label = self.builder.create_label(self.new_account_window, f"Balance: ₱{account_type.get_balance()}", ("Arial", 16), bg="#FFA500")
        self.balance_label.place(x=270, y=60, anchor= "nw")
        self.withdraw_label = self.builder.create_label(self.new_account_window, f"Withdraw:  ₱", ("Eras Demi ITC", 12), bg="#FFA500")
        self.withdraw_label.place(x=180, y=200)
        self.withdraw_entry = self.builder.create_entry(self.new_account_window, show="", width=30)
        self.withdraw_entry.place(x=300, y=203)
        self.pin_label = self.builder.create_label(self.new_account_window, f"PIN: ", ("Eras Demi ITC", 12), bg="#FFA500")
        self.pin_label.place(x=250, y=250)
        self.pin_entry = self.builder.create_entry(self.new_account_window, show="", width=16)
        self.pin_entry.place(x=320, y=253)

        def do_transaction():
            pin_value = self.pin_entry.get()

            if pin_value == self.new_account.get_pin():
                withdraw = self.withdraw_entry.get()
                self.new_account.credit(withdraw, self.new_user, self.bank)
                print(f"{self.new_account.get_balance()}")
                self.create_main_menu_command.execute()

            else:
                self.builder.show_message_box("showerror", "Transaction Failed", "Wrong PIN. Please try again.", on_yes_command=None)
        
        self.confirm_button = self.builder.create_button(self.new_account_window, "Confirm", width=30, relief=tk.SOLID, bg="#9ADE7B", command=lambda: self.builder.show_message_box("askokcancel", "Confirmation", f"Confrim withdrawal amount of ₱{self.withdraw_entry.get()}?", on_yes_command=do_transaction))
        self.confirm_button.place(x=460, y=360)

        self.back_button = self.builder.create_button(self.new_account_window, "<--", width=10, relief=tk.SOLID, bg="#FFA500", command=lambda:self.navigate_back_command.execute(command=lambda account=account_type: self.show_account_info(account)))
        self.back_button.place(x=600, y=20) 

    def disable_window(self, window):
        window.grab_set()

    def enable_window(self, window):
        window.grab_release()
    
    def display_log_in_menu(self, email, password):
        users = self.bank.get_offline_users()

        if not users:
            messagebox.showerror("Error", "Create an account first.")
        else:
            login_successful = False
            for user in users:
                if email == user.get_email() and password == user.get_password():
                    self.bank.add_online_user(user)
                    self.create_main_menu_command.execute()
                    login_successful = True
                    break
                else:
                    continue

            if not login_successful:
                self.builder.show_message_box("showerror", "Login Failed", "Invalid email or password. Please try again.")
                    

    def display_forgot_menu(self):
        if not self.bank.get_users():
            messagebox.showerror("Error", "Create an account first.")

    def navigate_back(self, command=None):
        self.clear_frame()
        self.destroy_all_frames()
        command()

    def clear_frame(self):
        self.builder.destroy_frame()

    def destroy_all_frames(self):
        self.builder.destroy_all_frames()
        
class BankApplication(tk.Tk):
    def __init__(self) -> None:
        super().__init__()
        self.builder = WidgetBuilder(self)
        self.gui_facade = GUIFacade(self.builder, self)
        self.title("Bank Application")
        self.geometry("700x400")
        self.resizable(False, False)
        self.gui_facade.create_main_menu()
        self.run()

    def run(self):
        self.mainloop()

if __name__ == '__main__':
    os.system("cls")
    BankApplication()

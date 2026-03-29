# BanKo

A banking simulation desktop application built with Python and Tkinter.

## Features

- **User registration** with personal details (name, email, gender, birthdate, address, phone)
- **Login / Logout** with email and password authentication
- **Multiple account types** — Savings, Checking, and Joint accounts
- **Debit (deposit)** and **Credit (withdraw)** transactions with PIN verification
- **Interest rates** and **transaction fees** applied per account type
- **Close accounts** when no longer needed
- **User profile** display with online/offline status

## Account Types

| Type | Min. Initial Deposit | Interest Rate | Withdrawal Limit | Transaction Fee |
|------|---------------------|---------------|-------------------|-----------------|
| Savings | 500 | 4% | 20,000 | 5 |
| Checking | 25,000 | 1% | None | 5 |
| Joint | 50,000 | — | None | None |

## Design Patterns

- **Builder Pattern** — `WidgetBuilder` for constructing UI widgets
- **Facade Pattern** — `GUIFacade` for orchestrating screens and navigation
- **Command Pattern** — encapsulated actions (`LogInCommand`, `CreateAccountCommand`, etc.)
- **State Pattern** — `OnlineState` / `OfflineState` for user session state
- **Abstract Base Classes** — `Bank`, `AbstractAccount`, `Person`, `UserState`

## Project Structure

- `main.py` — Application entry point, UI builder, command classes, and GUI facade
- `bank.py` — Bank ABC and `Main` bank implementation
- `account.py` — Account ABC with `Savings`, `Checking`, and `Joint` subclasses
- `person.py` — Person ABC, `User` class, and state classes

## User Interface
<img width="888" height="549" alt="image" src="https://github.com/user-attachments/assets/3435d490-f722-409d-964a-904906ab660d" />
<img width="894" height="545" alt="image" src="https://github.com/user-attachments/assets/fe6bf8d9-72d4-4d8a-b688-13db04317d01" />
<img width="886" height="547" alt="image" src="https://github.com/user-attachments/assets/d6724bb2-85b4-4c17-854d-b069be5d369d" />
<img width="894" height="553" alt="image" src="https://github.com/user-attachments/assets/ceca955a-621a-4f89-b5ae-a7777b4f5195" />
<img width="881" height="551" alt="image" src="https://github.com/user-attachments/assets/19fd0817-96f1-4866-803f-08a32002342c" />
<img width="888" height="551" alt="image" src="https://github.com/user-attachments/assets/0987c378-83cd-4351-ac13-9ee4fc831206" />


## How to Run

```bash
python main.py
```

## Requirements

- Python 3
- Tkinter (included with standard Python installations)

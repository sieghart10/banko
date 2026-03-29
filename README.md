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

## How to Run

```bash
python main.py
```

## Requirements

- Python 3
- Tkinter (included with standard Python installations)

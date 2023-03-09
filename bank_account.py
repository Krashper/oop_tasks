class BankAccount:
    def __init__(self, balance: float, account_number: int, account_holder: str):
        self.balance = balance
        self.account_number = account_number
        self.account_holder = account_holder
        
    def deposit(self, amount: float) -> None:
        self.balance += amount
        
    def withdraw(self, amount: float) -> None:
        if amount > self.balance:
            raise ValueError('Insufficient funds')
        self.balance -= amount

    def get_balance(self) -> float:
        return self.balance
        
    def get_account_number(self) -> int:
        return self.account_number
        
    def get_account_holder(self) -> str:
        return self.account_holder
        
    def __str__(self) -> str:
        return f'Account Holder: {self.account_holder}, Account Number: {self.account_number}, Balance: ${self.balance}'

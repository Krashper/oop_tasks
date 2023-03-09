from bank_account import BankAccount


def test_class_bank_account():
    # create a BankAccount object
    acct = BankAccount(1000.0, 123456789, "John Smith")

    # test deposit method
    acct.deposit(500.0)
    assert acct.get_balance() == 1500.0

    # test withdraw method with sufficient funds
    acct.withdraw(200.0)
    assert acct.get_balance() == 1300.0

    # test withdraw method with insufficient funds
    try:
        acct.withdraw(1500.0)
    except ValueError as e:
        assert str(e) == 'Insufficient funds'

    # test get_account_number method
    assert acct.get_account_number() == 123456789

    # test get_account_holder method
    assert acct.get_account_holder() == "John Smith"

    # test __str__ method
    assert str(acct) == "Account Holder: John Smith, Account Number: 123456789, Balance: $1300.0"

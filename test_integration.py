import pytest
from bank_app import transfer, calculate_interest

def test_transfer_success():
    from_balance, to_balance = transfer(5000, 2000, 1000)
    assert from_balance == 4000
    assert to_balance == 3000


def test_transfer_insufficient_balance():
    with pytest.raises(ValueError):
        transfer(500, 2000, 1000)


def test_transfer_then_interest():
    from_balance, to_balance = transfer(10000, 1000, 2000)
    updated_balance = calculate_interest(to_balance, 10, 1)
    assert updated_balance == pytest.approx(3300)


def test_transfer_invalid_amount():
    with pytest.raises(ValueError):
        transfer(5000, 2000, -500)

from soda import Soda

def test_class():
    my_drink = Soda()
    assert my_drink.show_my_drink() == 'Обычная газировка'
    my_fresh = Soda('лайм')
    assert my_fresh.show_my_drink() == 'Газировка и лайм'
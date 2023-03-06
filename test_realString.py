from realString import RealString


def test_class():
    str1 = RealString('Молоко')
    str2 = RealString('Абрикосы растут')
    str3 = 'Золото'
    str4 = [1, 2, 3]
    assert str1 < str4 == True
    assert str1 >= str2 == False
    assert str1 == str3 == True
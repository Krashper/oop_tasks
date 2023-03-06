from Nikola import Nikola


def test_class():
    person1 = Nikola('Иван', 31)
    person2 = Nikola('Николай', 14)
    assert person1.name == 'Я не Иван, а Николай'
    assert person2.name == 'Николай'
    assert person1.age == 31
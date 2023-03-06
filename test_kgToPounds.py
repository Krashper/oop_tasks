from kgToPounds import KgToPounds


def test_class():
    weight = KgToPounds(12)
    assert weight.to_pounds() == 26.46
    assert weight.kg == 12
    weight.kg = 41
    assert weight.kg == 41
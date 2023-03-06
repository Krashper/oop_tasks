from multiple_inheritance.multiple_inheritance import PetToy

def test_class(capfd):
    pet_toy = PetToy()
    pet_toy.interact()
    captured = capfd.readouterr()
    assert captured.out == "Pet is playing\nToy is moving\n"
    
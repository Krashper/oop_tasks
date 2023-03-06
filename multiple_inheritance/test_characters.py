from characters import Player, Enemy, Boss

def test_class_player(capfd):
    player1 = Player("Alice", 100, 10, 1)
    player1.get_info()  # output: Alice: Health = 100, Attack = 10
    player1.take_damage(20)  # output: Alice takes 20 damage.
    player1.get_info()  # output: Alice: Health = 80, Attack = 10
    player1.level_up()
    player1.get_info()
    captured = capfd.readouterr()
    assert captured.out == "Alice: Health = 100, Attack = 10\nAlice takes 20 damage.\nAlice: Health = 80, Attack = 10\nAlice gets level 2\nAlice: Health = 96.0, Attack = 12.0\n"

def test_class_enemy(capfd):
    enemy1 = Enemy("Goblin", 50, 5, 10)
    enemy1.get_info()
    enemy1.take_damage(15)  # output: Goblin takes 15 damage.
    enemy1.get_info()  # output: Goblin: Health = 35, Attack = 5
    enemy1_reward = enemy1.give_reward()
    assert enemy1_reward == 10
    captured = capfd.readouterr()
    assert captured.out == "Goblin: Health = 50, Attack = 5\nGoblin takes 15 damage.\nGoblin: Health = 35, Attack = 5\nThis player is getting 10 xp\n"

def test_class_boss(capfd):
    boss1 = Boss("Dragon", 500, 50, 10, 100, "Ice")
    boss1.get_info()  # output: Dragon: Health = 500, Attack = 50, Level = 10
    boss1.take_damage(100)  # output: Dragon takes 100 damage.
    boss1.get_info()  # output: Dragon: Health = 400, Attack = 50, Level = 10
    boss1.get_weakness()  # output: This boss has a weakness: Ice
    captured = capfd.readouterr()
    assert captured.out == "Dragon: Health = 500, Attack = 50\nDragon takes 100 damage.\nDragon: Health = 400, Attack = 50\nThis boss has a weakness: Ice\n"
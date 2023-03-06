class Soda:
    def __init__(self, ingredient=None):
        if isinstance(ingredient, str):
            self.ingredient = ingredient
        else:
            self.ingredient = None
    def show_my_drink(self):
        if self.ingredient:
            answer = f'Газировка и {self.ingredient}'
            print(answer)
        else:
            answer = 'Обычная газировка'
            print(answer)

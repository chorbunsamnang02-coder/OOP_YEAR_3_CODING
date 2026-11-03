class LucktNuymberGame:
    def __init__(self , number):
        self.number = number
    def get_next_number(self):
        return self.number+1
    def display(self):
        return f" The next number :{self.get_next_number()}"
num = int(input(" Please enter number : "))
game = LucktNuymberGame(num)
print(game.display())

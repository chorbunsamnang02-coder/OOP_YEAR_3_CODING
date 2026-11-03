#Hundread counter
class HundreadCounter:
    def __init__(self , number):
        self.number=number
    def count_hundread(self):
        if self.number < 0:
            return "Error: Please enter a positive number."
        else:
            count = self.number // 100
            return count
number = int(input("Enter a number: "))
counter = HundreadCounter(number)
print("The number of hundreds in", number, "is:", counter.count_hundread())
            

        
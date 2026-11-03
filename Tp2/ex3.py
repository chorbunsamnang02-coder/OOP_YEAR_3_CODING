#equation calculator
class Equation_Calulator:
    def __init__(self , y , z):
        self.y = y
        self.z=z
    def calculate_x(self):
        x=(self.y*self.z)/(self.y+self.z)
        return x

    def display_result(self):
        if self.y ==0 or self.z ==0 or self.y + self.z==0:
            return "Error: Division by zero"
        else:
            x=self.calculate_x()
            return "The value of x is: ", self.calculate_x()    
y = float(input("Enter the value of y: "))
z = float(input("Enter the value of z: "))
calculator = Equation_Calulator(y, z)
print(calculator.display_result())
class Greeting:
    def __init__(self , name):
        self.name=name

    def say_hello(self):
        print("hello" , self.name)

input_name=str(input("Please enter your name :"))
greeting = Greeting(input_name)
greeting.say_hello()
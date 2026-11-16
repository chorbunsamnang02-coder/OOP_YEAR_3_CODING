class Book :
    def __init__(self , title , author , price):
        self.title = title
        self.author = author
        self.__price = price
    def get_price(self):
        return self.__price
    def set_price(self , new_price):
        if new_price < 0:
            print("Price cannot be negative.")
        else:
            self.__price = new_price
    def display_info(self):
        print(f"Title: {self.title}, Author: {self.author}, Price: ${self.__price:.2f}")
class EBook(Book):
    def __init__(self , title , author , price , file_size):
        super().__init__(title , author , price)
        self.file_size = file_size
    def display_info(self):
        super().display_info()
        print(f"File Size: {self.file_size} MB")
book1 = Book(" Good vibe good life ", "F. Scott Fitzgerald", 10.99)
ebook1 = EBook("Engineering book ", "F. Scott Fitzgerald", 10.99, 2.5)

book1.display_info()
ebook1.display_info()

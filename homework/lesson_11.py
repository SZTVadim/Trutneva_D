class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def get_info(self):
        return f"'{self.title}' автор {self.author}, {self.pages} стр."

    def is_long(self):
        if self.pages > 300:
            return True
        else:
            return False


book1 = Book("Война и мир", "Лев Толстой", 1225)
book2 = Book("Мастер и Маргарита", "Михаил Булгаков", 480)
book3 = Book("Маленький принц", "Антуан де Сент-Экзюпери", 96)

print(book1.get_info())
print(book2.get_info())
print(book3.get_info())


class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Снято {amount}. Текущий баланс: {self.balance}")
            return True
        else:
            print("Недостаточно средств")
            return False

    def get_balance(self):
        return self.balance


account = BankAccount("Дарья", 1000)
account.deposit(500)
account.withdraw(300)
account.withdraw(2000)
print(account.get_balance())

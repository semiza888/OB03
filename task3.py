# Создайте класс Author и класс Book. Класс Book должен использовать композицию
# для включения автора в качестве объекта.

class Author():
    def __init__(self, name, surname, nationality):
        self.name = name
        self.surname = surname
        self.nationality = nationality

class Book():
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def get_info_book(self):
        print(f'{self.title} - {self.author.name}, {self.author.surname}, {self.author.nationality}')

author = Author('Лев', 'Толстой', 'русский')
book = Book('После бала', author)

book.get_info_book()





class Publisher:
    def __init__(self, name, loccation):
        self.name = name
        self.location = loccation

    def get_info(self):
        return(f'{self.name} ({self.location})')
    
    def publish(self, message):
        print(f'Готовим "{message}" к публикации в {self.get_info()}')


class BookPublisher(Publisher):
    def __init__(self, name, location, num_authors):
        super().__init__(name, location)
        self.num_authors = num_authors

    def publish(self, title, author):
        print(f'Передаем рукопись "{title}", написанную автором {author} в издательство {self.get_info()}')


class NewspaperPublisher(Publisher):
    def __init__(self, name, location, num_pages):
        super().__init__(name, location)
        self.num_pages = num_pages

    def publish(self, article):
        print(f'Печатаем свежий номер со статьей "{article}" на главной странице в издательстве {self.get_info()}')

    

publisher = Publisher("АБВГД Пресс", "Москва")
publisher.publish("Справочник писателя")

book_publisher = BookPublisher("Важные Книги", "Самара", 52)
book_publisher.publish("Приключения Чебурашки", "В.И. Пупкин")

newspaper_publisher = NewspaperPublisher("Московские вести", "Москва", 12)
newspaper_publisher.publish("Новая версия Midjourney будет платной")


################################################

# Готовим "Справочник писателя" к публикации в АБВГД Пресс (Москва)
# Передаем рукопись "Приключения Чебурашки", написанную автором В.И. Пупкин в издательство Важные Книги (Самара)
# Печатаем свежий номер со статьей "Новая версия Midjourney будет платной" на главной странице в издательстве Московские вести (Москва)
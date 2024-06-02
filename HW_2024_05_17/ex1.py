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


# Комментарий преподавателя:

# Код читабельный и хорошо структурирован
# Имена переменных и методов соответствуют конвенциям Python
# Используется наследование и метод super() для вызова методов родительского класса
# Результат работы кода соответствует примеру использования


# В строке 4 опечатка в названии переменной (location вместо loccation)

# Что можно улучшить:
#     Добавить документацию к классам и методам в виде докстрингс
#     Добавить аннотацию типов в методах


# Этого не было в условии задания, но если бы это была настоящая задача на разработку, то я бы дал ещё такие комментарии:
# В методе publish подклассов можно было бы добавить проверку на пустую строку для параметров title, author и article.
# Если строка пустая, то можно выводить сообщение об ошибке и прерывать выполнение метода.

# В методе __init__ подклассов можно было бы добавить проверку на положительное значение для параметров num_authors и num_pages.
# Если значение отрицательное, то можно выводить сообщение об ошибке и прерывать выполнение метода.
